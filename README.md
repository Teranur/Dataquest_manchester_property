# The Manchester Sales Challenge
This repository provides the data and brief for the Manchester House Sales Challenge. Your task is to explore, clean, and analyse the dataset to answer the questions below and present your findings.

## What you need to deliver
- Use the data provided in this repository.
- Perform your own data cleaning and wrangling.
- Answer all challenge questions (explaining your approach and assumptions).
- Build and share a dashboard that communicates your findings.
- Host your code (at minimum the data-wrangling pipeline) in a public GitHub repository.
- Present your process, insights, and dashboard.

## Background
This challenge focuses on residential and non-residential property sale prices (Prices Paid) within Greater Manchester, UK. 
The dataset is a modified, falsified version of the UK Prices Paid data and includes falsified risk information. Do not use it for real-world decisions or analysis.

Scope and timeframe:
- Geographic focus: Greater Manchester only.
- Time period: 01/1996 to 12/2024.

The data is provided in the [data](data) folder as parquet files. This is real world data, there may be missing values and/or errors.

## The Challenge Questions
Some questions are intentionally ambiguous; justify your choices and methodology.

1. What are the top 10 most expensive detached homes sold as Freehold in Manchester City after 2010?
2. What are the top 5 most expensive postal sectors (postal sectors are the section of the postal code after the area sector: examples include `M1 3`, `M1 4`) in the Salford district between March 2012 and September 2015?
3. Where do you think in Greater Manchester are the most residential homes being built over the past 10 years?
4. What was the most expensive non-residential property sold in Greater Manchester in 2017? Find and share context about this sale.
5. Which residential building types are seeing the biggest proportional rise in prices?
6. Historically, what property sale(s) in Trafford was the furthest south‑east?
7. Were there any other interesting trends, patterns, or issues you found?

## The Data
Descriptions of the supplied datasets are below.

### Prices Paid
You may need to sanitise this dataset. Columns include:

| Column             | Description                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| `id`               | Unique identifier for each transaction                                                          |
| `price`            | Price paid for the transaction                                                                  |
| `postcode`         | Postcode of the transaction                                                                     |
| `date`             | Date of the sale completion                                                                     |
| `property_type`    | F - Flat <br/>S - Semi Detached <br/>D - Detached <br/>T - Terraced <br/>O - Other (Non Residential) |
| `new`              | Y - New Build<br/> N - Old Build                                                                     |
| `duration`         | F - Freehold<br/> L - Leasehold                                                                      |
| `paon`             | Primary Addressable Object Name                                                                  |
| `saon`             | Secondary Addressable Object Name                                                                |
| `street`           | Street name                                                                                      |
| `locality`         | Locality of the transaction                                                                      |
| `town_city`        | Town or city name                                                                                |
| `district`         | District name                                                                                    |
| `county`           | County name                                                                                      |

#### Postcodes
Provides latitude and longitude for each postcode. Columns include:

| Column | Description                                                                                  |
|--------|----------------------------------------------------------------------------------------------|
| `pcds` | Postcode                                                                                      |
| `lat`  | Latitude                                                                                      |
| `long` | Longitude                                                                                     |

## Rules and constraints
- You may use any programming language and any visualisation tools (e.g. Power BI, Tableau).
- For data manipulation, you must use `polars`. `pandas` is not permitted for wrangling.
- You may use any additional libraries or resources; cite any external sources used.

## Submission
Submit a link to your GitHub repository containing your code and share your dashboard. You will be asked to present your approach and findings.
This is an opportunity to demonstrate data analysis, visualisation, and communication skills. Feel free to be creative and go beyond the minimum requirements.

## Contact
If you have any questions, please contact us via GitHub.