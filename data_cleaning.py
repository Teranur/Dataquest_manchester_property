import polars as pl


def read_and_rename_files():
    df = pl.read_parquet("data/pp_data_man.parquet")
    df2 = pl.read_parquet("data/pc_man.parquet")
    df.columns = [
        "id", "price", "date", "postcode", "property_type", "new", "duration",
        "paon", "saon", "street", "locality", "town_city", "district", "county"
    ]
    df2 = df2.rename({"pcds": "postcode", "lat": "latitude", "long": "longitude"})
    return df, df2


def normalize_postcode(df):
    return df.with_columns(
        pl.col("postcode")
          .cast(pl.Utf8)
          .str.strip_chars()
          .str.to_uppercase()
          .str.replace_all(r"\s+", " ")
          .alias("postcode")
    )


def parse_date_column(df):
    return df.with_columns(
        pl.col("date")
        .str.slice(0, 10)
        .str.strptime(pl.Date, format="%Y-%m-%d", strict=True)
        .alias("date")
    )


def join_lat_long(df, df2):
    df2_norm = normalize_postcode(df2)
    return df.join(
        df2_norm.select("postcode", "latitude", "longitude"),
        on="postcode",
        how="left"
    )


def clean_strings(df):
    string_cols = [c for c, t in df.schema.items() if t == pl.Utf8]
    return df.with_columns([
        pl.when(pl.col(c) == "").then(None).otherwise(pl.col(c)).alias(c) for c in string_cols
    ])


def combine_paon_saon(df):
    return df.with_columns(
        pl.when(pl.col("saon").is_not_null() & (pl.col("saon") != ""))
          .then(pl.concat_str([pl.col("paon"), pl.col("saon")], separator=", "))
          .otherwise(pl.col("paon"))
          .alias("paon")
    ).drop("saon")


def drop_and_format(df):
    df = df.drop_nulls(subset=["postcode"])
    df = df.drop("locality")
    df = normalize_postcode(df)
    df = df.with_columns(
        pl.col("price")
          .str.replace_all(",", "")
          .cast(pl.Float64)
          .alias("price")
    )
    df = df.with_columns([
        pl.col("date").dt.year().alias("sale_year"),
        pl.col("date").dt.month().alias("sale_month"),
        pl.col("date").dt.quarter().alias("sale_quarter")
    ])
    df = normalize_postcode(df)
    return df


def impute_street(df):
    df_non_null_street = df.filter(pl.col("street").is_not_null())
    postcode_mode_list = (
        df_non_null_street
        .group_by("postcode")
        .agg(pl.col("street").mode().alias("street_modes"))
    )
    postcode_fill = postcode_mode_list.with_columns(
        pl.col("street_modes").list.first().alias("imputed_street")
    ).drop("street_modes")
    df_joined = df.join(postcode_fill, on="postcode", how="left")
    return df_joined.with_columns(
        pl.when(pl.col("street").is_null())
          .then(pl.col("imputed_street"))
          .otherwise(pl.col("street"))
          .alias("street")
    ).drop("imputed_street")


def fill_nulls(df):
    return df.with_columns([
        pl.col("paon").fill_null("N/A"),
        pl.col("street").fill_null("N/A")
    ])


def convert_to_categorical(df, categorical_cols):
    for col in categorical_cols:
        if col in df.columns:
            df = df.with_columns(
                pl.col(col)
                .str.strip_chars()
                .str.to_lowercase()
                .cast(pl.Categorical)
                .alias(col)
            )
    return df


def create_pipeline_and_save():
    categorical_cols = ["property_type", "duration", "new"]
    df, df2 = read_and_rename_files()
    df = normalize_postcode(df)
    df = parse_date_column(df)
    df = join_lat_long(df, df2)
    df = clean_strings(df)
    df = combine_paon_saon(df)
    df = drop_and_format(df)
    df = impute_street(df)
    df = fill_nulls(df)
    df = convert_to_categorical(df, categorical_cols)
    df.write_parquet("data/pp_data_cleaned.parquet")
    print("Pipeline complete and saved as data/pp_data_cleaned.parquet")


create_pipeline_and_save()