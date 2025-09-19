# Manchester Property Sales Challenge — Submission

This repository contains the data, code, and analysis for the Manchester Property Sales Challenge. The project focuses on exploring, cleaning, and analyzing property sales data for Greater Manchester, using `polars` for data processingm, documented in a Jupyter notebook and data wrangler for an initial visual analysis.

---

## Repository Structure

/data

├── pp_data_man.parquet # Raw property sales data

├── pc_man.parquet # Raw postcode latitude & longitude data

└── pp_data_man_cleaned.parquet # Cleaned dataset output by the pipeline

data_cleaning.jup.ipynb     # Jupyter notebook documenting exploration, cleaning, and analysis

data_cleaning.py            # Python pipeline script implementing cleaning with polars

README.md                   # This file: project overview, instructions, and answers


---

## Background

- Dataset covers Greater Manchester property sales from January 1996 to December 2024.
- Contains residential and non-residential transactions.
- Data is synthetic and requires cleaning due to missing or inconsistent values.

---

## Data Cleaning and Pipeline

- Raw data loaded and cleaned with `polars` in `data_cleaning.py`.
- Cleaning steps include filtering incomplete records, parsing dates, and joining postcode coordinates.
- Cleaned data saved as `pp_data_man_cleaned.parquet`.
- Detailed analysis and rationale are documented in the Jupyter notebook `data_cleaning.jup.ipynb`.

---

## Challenge Answers

1. **Top 10 Most Expensive Detached Freehold Homes Sold in Manchester City After 2010**  
  The most expensive detached freehold homes sold in Manchester were in range of £5.5 and £2.2 million pounds, topping them of course the Manchester district with 5 sold
  4 in the district of Salford and a home sold in Bury. those were:
  - {919FEC06-206B-9A90-E053-6C04A8C0A300} Manchester District
  - {EED73E76-92B1-6AF3-E053-6C04A8C08ABA} Manchester District
  - {404A5AF4-5B8E-CD2B-E050-A8C063055C7B} Manchester District
  - {2FD36066-57B8-4BF8-E050-A8C0620562B1} Manchester District
  - {1775CCF7-2793-38BA-E063-4704A8C05A7C} Manchester District
  - {CFC9085C-95B5-9A70-E053-6B04A8C09D6A} Salford District
  - {F87E72F9-DE63-176C-E053-6B04A8C0D2BE} Salford District
  - {DBA933F9-5C72-669D-E053-6B04A8C0AD56} Bury District
  - {D22473F5-8A93-7B40-E053-6C04A8C0A630} Salford District
  - {E7B085FC-292F-7E31-E053-6C04A8C0E67F} Salford District

2. **Top 5 Most Expensive Postal Sectors in Salford (Mar 2012 - Sep 2015)**  
   The top 5 sectors were `M28 2`, `M30 9`, `M28 1`, `M7 4`, `M50 2` 
   But its important to note that the total amount of money spend for homes were slightly different
   with the ranking being `M28 2`, `M28 3`, `M30 9`, `M28 1`and `M5 4`
   we can see that the most expensive sectors are the most desireable as well and that the Manchester District is king.


3. **Most Residential New Builds in the Past 10 Years**  
   From the previous task we can see the highest demand is in Manchester District, and where there is demand there is supply with:
    - 75359 new builds in Manchester District
    - 55284 new builds in Wigan District
    - 52514 new builds in Salford District
    - 51305 new builds in Stockport District
    - 43050 new builds in Bolton District
    - 38667 new builds in Trafford District
    - 35357 new builds in Tameside District
    - 31551 new builds in Rochdale District
    - 30694 new builds in Bury District
    - 30544 new builds in OldHam District

4. **Most Expensive Non-Residential Property Sold in 2017**  
   The Printworks, Manchester’s premier entertainment complex, spans approximately 368,770 sq ft over four floors. It was acquired by DZT Investors from Land Securities for £107,086,856. Previously, Land Securities purchased it from Resolution Property for £93.9 million, who had bought it for £100 million. Originally a printing plant until 2012, The Printworks has since transformed into a vibrant centre with bars, restaurants, shops, and leisure facilities.

5. **Residential Building Types with Largest Proportional Price Increase Since 1996**  
  The largest proportional price increase occurred in terraced properties, which rose by 431.3% from a median price of £32,000 to £170,000.
    This was followed by semi-detached homes, which increased by 396.5% from £49,350 to £245,000.
    Detached properties saw a 347.9% rise from £83,500 to £373,997.50, while flats increased by 341.9%, from £39,600 to £175,000.

6. **Furthest South-East Sale in Trafford Since 1996**  
   The sale happened in 2009 close to the Manchester Airport, it was sold for £350,000
    - {022C7567-EBCC-4038-8DE0-F0796357154B}
    the next furthest were sold in 2002 and 2000 for £250,000 and £200,000 respectively
    All 3 properties were sold in Rivershill Gardens

7. **Additional Trends and Insights**  

   - Data Cleaning and Preparation
    The dataset originally contained missing values represented as empty strings (""), which interfered with automated null detection because these were not recognized as nulls by default. After identifying this issue, empty strings were effectively converted to proper null values. Where applicable, these nulls were filled using appropriate methods depending on the column’s context, while columns or records with excessive missing data—such as those missing postcodes—were removed to maintain dataset integrity. This careful cleaning ensured a reliable and consistent dataset suitable for rigorous analysis.
   - Price Growth Patterns
    The analysis reveals that terraced properties experienced the largest proportional increase, followed by semi-detached, then detached homes, with flats showing the smallest relative growth. This suggests a market preference shifting towards traditional house types over flats within Greater Manchester. Such trends likely reflect broader regional development patterns and regeneration efforts focusing on family homes and suburban areas. These dynamics indicate evolving demand and investment priorities in the local property market.

   - Despite terraced houses being the most popular in terms of sales volume, the highest total revenue is generated from semi-detached houses, reflecting their significantly higher average sale  prices. Semi-detached properties in Greater Manchester consistently command higher market values compared to terraced homes, which attracts greater investment returns despite lower transaction counts. This pattern highlights how market preference and price premiums influence overall value generation across property types.

   - The majority of property sales turnover is from old buildings, which account for 88.73% of all properties sold. In contrast, new builds represent only 11.27% of the total sales, highlighting that established properties dominate the market in terms of transaction volume.


---

## How to Run

1. Clone the repository:  
    git clone <[url](https://github.com/Teranur/Dataquest_manchester_property.git)>

2. Install dependencies (e.g., via pip) best done in a venv:  
pip install polars etc.

3. Run the data cleaning pipeline:  
python data_cleaning.py

4. Open the Jupyter notebook to explore the analysis and cleaning choices:
jupyter notebook data_cleaning.jup.ipynb

5. Visualizations and analysis done in PowerBI:
import the cleaned parquet file into PowerBI

## Contact

Questions or suggestions? Please open an issue in this repository or contact email ch.sobczak97@gmail.com.