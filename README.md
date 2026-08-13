\# Bluestock Mutual Fund Analytics Capstone



\## Project Overview



This project analyzes Indian mutual fund data to understand fund performance, NAV trends, investor transactions, AUM, SIP inflows, risk, and market trends.



The project covers the complete analytics workflow:



\- Data ingestion

\- Data cleaning and validation

\- SQLite database creation and loading

\- Exploratory Data Analysis (EDA)

\- Fund performance analysis

\- Advanced risk analytics

\- Fund recommendation logic

\- Interactive Power BI dashboard

\- Final report and presentation



\---



\## Objectives



The main objectives of this project are:



1\. Build a reliable ETL pipeline for mutual fund datasets.

2\. Clean and validate the available mutual fund data.

3\. Store structured data in a SQLite database.

4\. Analyze NAV, AUM, SIP inflows, transactions, and fund performance.

5\. Calculate performance and risk metrics such as Sharpe Ratio, VaR and CVaR.

6\. Develop a fund scorecard and recommendation logic.

7\. Build an interactive four-page Power BI dashboard.

8\. Present key findings through a final report and presentation.



\---



\## Tools and Technologies



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Plotly

\- SQLite

\- SQL

\- Power BI

\- Jupyter Notebook

\- Git and GitHub



\---



\## Data Pipeline



The project follows this workflow:



Raw Data

↓

Data Ingestion

↓

Data Cleaning \& Validation

↓

Processed Data

↓

SQLite Database

↓

EDA \& Performance Analytics

↓

Advanced Analytics

↓

Power BI Dashboard

↓

Final Report \& Presentation



\---



\## Database



The project uses SQLite for structured data storage.



Main tables include:



\- `dim\\\_fund`

\- `fact\\\_nav`

\- `fact\\\_transactions`

\- `fact\\\_performance`

\- `fact\\\_aum`

\- `monthly\\\_sip\\\_inflows`



The database contains:



\- 64,320 NAV records

\- 32,778 transaction records

\- 40 fund performance records

\- 40 fund master records

\- 90 AUM records

\- 48 monthly SIP inflow records



The SQLite database file is excluded from Git tracking using `.gitignore`.



\---



\## Exploratory Data Analysis



EDA was performed to understand:



\- NAV trends

\- AUM growth

\- Fund-house comparison

\- Category distribution

\- SIP inflow trends

\- Transaction distribution

\- Investor demographics

\- Sector allocation

\- Benchmark comparison

\- NAV correlations



Charts and analysis outputs are stored in the `reports/` directory.



\---



\## Performance Analytics



Fund performance was analyzed using metrics including:



\- 1-year return

\- 3-year return

\- 5-year return

\- Expense ratio

\- Sharpe ratio

\- Risk/volatility

\- Benchmark comparison



A fund scorecard was also created to compare funds based on performance and risk-related metrics.



\---



\## Advanced Analytics



Advanced analysis includes:



\- Rolling Sharpe Ratio

\- Value at Risk (VaR)

\- Conditional Value at Risk (CVaR)

\- Risk comparison across funds

\- Fund recommendation logic



The VaR/CVaR analysis is available in:



`reports/var\\\_cvar\\\_report.csv`



The rolling Sharpe visualization is available in:



`reports/rolling\\\_sharpe\\\_chart.png`



\---



\## Power BI Dashboard



The interactive Power BI dashboard contains four main pages:



\### Page 1 — Industry Overview



Includes:



\- Total AUM

\- SIP inflows

\- Total folios

\- Total schemes

\- Industry AUM trend

\- AUM by AMC



\### Page 2 — Fund Performance



Includes:



\- Fund performance comparison

\- Risk/return analysis

\- Fund scorecard

\- NAV versus benchmark

\- Fund house/category/plan slicers



\### Page 3 — Investor Analytics



Includes:



\- Transactions by state

\- Transaction type distribution

\- Investor analysis

\- Monthly transaction trends

\- Investor-related slicers



\### Page 4 — SIP \& Market Trends



Includes:



\- SIP inflow trend

\- Nifty 50 comparison

\- Category inflow analysis

\- Top categories by net inflow



The dashboard also includes interactive filters, tooltips, and drill-through functionality.



\---



\## Project Structure



```text

Mutual\\\_Fund\\\_Analytics/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── notebooks/

│   ├── EDA\\\_Analysis.ipynb

│   ├── Performance\\\_Analytics.ipynb

│   └── Advanced\\\_Analytics.ipynb

│

├── dashboard/

│   ├── bluestock\\\_mf\\\_dashboard.pbix

│   ├── bluestock\\\_mf\\\_dashboard.pdf

│   └── 4 page PNG screenshots/

│       ├── 01\\\_Industry\\\_Overview.png

│       ├── 02\\\_Fund\\\_Performance.png

│       ├── 03\\\_Investor\\\_Analytics.png

│       └── 04\\\_SIP\\\_Market\\\_Trends.png

│

├── sql/

│   ├── schema.sql

│   └── queries.sql

│

├── reports/

│   ├── Final\\\_Report.pdf

│   ├── Bluestock\\\_MF\\\_Presentation.pptx

│   ├── var\\\_cvar\\\_report.csv

│   └── analytical charts

│

├── data\\\_cleaning.py

├── data\\\_ingestion.py

├── database\\\_load.py

├── live\\\_nav\\\_fetch.py

├── recommender.py

├── requirements.txt

├── data\\\_dictionary.md

├── .gitignore

└── README.md
