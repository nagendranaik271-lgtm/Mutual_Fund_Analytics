# Data Dictionary

This document describes all cleaned datasets used in the Mutual Fund Analytics project.

---

# 1. 01_fund_master.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| fund_house | TEXT | Mutual fund company name |
| scheme_name | TEXT | Name of the mutual fund scheme |
| category | TEXT | Fund category (Equity, Debt, Hybrid, etc.) |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Direct or Regular plan |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Expense ratio (%) |
| exit_load_pct | REAL | Exit load (%) |
| min_sip_amount | INTEGER | Minimum SIP amount |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk category |
| sebi_category_code | TEXT | SEBI category code |

Source: 01_fund_master.csv

---

# 2. 02_nav_history_cleaned.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| amfi_code | INTEGER | AMFI scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

Source: 02_nav_history.csv

---

# 3. 03_aum_by_fund_house.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| date | DATE | Reporting date |
| fund_house | TEXT | Mutual fund company |
| aum_lakh_crore | REAL | AUM in lakh crore |
| aum_crore | REAL | Assets Under Management (Crore INR) |
| num_schemes | INTEGER | Number of schemes |

Source: 03_aum_by_fund_house.csv

---

# 4. 04_monthly_sip_inflows.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| month | TEXT | Month |
| sip_inflow_crore | REAL | SIP inflows (Crore INR) |
| active_sip_accounts_crore | REAL | Active SIP accounts |
| new_sip_accounts_lakh | REAL | Newly opened SIP accounts |
| sip_aum_lakh_crore | REAL | SIP Assets Under Management |
| yoy_growth_pct | REAL | Year-over-Year growth percentage |

Source: 04_monthly_sip_inflows.csv

---

# 5. 05_category_inflows.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| month | TEXT | Month |
| category | TEXT | Mutual fund category |
| net_inflow_crore | REAL | Net inflow in Crore INR |

Source: 05_category_inflows.csv

---

# 6. 06_industry_folio_count.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| month | TEXT | Month |
| total_folios_crore | REAL | Total folios |
| equity_folios_crore | REAL | Equity folios |
| debt_folios_crore | REAL | Debt folios |
| hybrid_folios_crore | REAL | Hybrid folios |
| others_folios_crore | REAL | Other folios |

Source: 06_industry_folio_count.csv

---

# 7. 07_scheme_performance_cleaned.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| amfi_code | INTEGER | AMFI scheme code |
| scheme_name | TEXT | Mutual fund name |
| fund_house | TEXT | Mutual fund company |
| category | TEXT | Fund category |
| plan | TEXT | Direct or Regular |
| return_1yr_pct | REAL | One-year return (%) |
| return_3yr_pct | REAL | Three-year return (%) |
| return_5yr_pct | REAL | Five-year return (%) |
| benchmark_3yr_pct | REAL | Benchmark return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annual Standard Deviation |
| max_drawdown_pct | REAL | Maximum Drawdown |
| aum_crore | REAL | Assets Under Management |
| expense_ratio_pct | REAL | Expense Ratio |
| morningstar_rating | INTEGER | Morningstar Rating |
| risk_grade | TEXT | Risk Grade |

Source: 07_scheme_performance.csv

---

# 8. 08_investor_transactions_cleaned.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Mutual fund code |
| transaction_type | TEXT | SIP, Lumpsum or Redemption |
| amount_inr | REAL | Investment amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier of city |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income |
| payment_mode | TEXT | Payment mode |
| kyc_status | TEXT | KYC verification status |

Source: 08_investor_transactions.csv

---

# 9. 09_portfolio_holdings.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| amfi_code | INTEGER | Mutual fund code |
| stock_symbol | TEXT | Stock symbol |
| stock_name | TEXT | Company name |
| sector | TEXT | Industry sector |
| weight_pct | REAL | Portfolio weight (%) |
| market_value_cr | REAL | Market value (Crore INR) |
| current_price_inr | REAL | Current stock price |
| portfolio_date | DATE | Portfolio reporting date |

Source: 09_portfolio_holdings.csv

---

# 10. 10_benchmark_indices.csv

| Column | Data Type | Business Definition |
|--------|-----------|---------------------|
| date | DATE | Trading date |
| index_name | TEXT | Benchmark index |
| close_value | REAL | Closing index value |

Source: 10_benchmark_indices.csv