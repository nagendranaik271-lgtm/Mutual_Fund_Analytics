-- Bluestock Mutual Fund Analytics
-- SQL Analysis Queries

-- Query 1: Top 5 Fund Houses by AUM
SELECT
    fund_house,
    aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;


-- Query 2: Average NAV by Month
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date)
ORDER BY month;


-- Query 3: Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- Query 4: Funds with Expense Ratio Below 1%
SELECT
    amfi_code,
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- Query 5: SIP YoY Growth
SELECT
    month,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- Query 6: Highest NAV
SELECT
    amfi_code,
    date,
    nav
FROM fact_nav
ORDER BY nav DESC
LIMIT 1;


-- Query 7: Transactions by Type
SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;


-- Query 8: Total Investment Amount
SELECT
    SUM(amount_inr) AS total_investment_inr
FROM fact_transactions;


-- Query 9: Number of Funds by Category
SELECT
    category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category
ORDER BY total_funds DESC;


-- Query 10: Total Number of Funds
SELECT
    COUNT(*) AS total_funds
FROM dim_fund;


-- Query 11: Top 5 Funds by Sharpe Ratio
SELECT
    scheme_name,
    fund_house,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- Query 12: Top 5 Funds by 3-Year Return
SELECT
    scheme_name,
    fund_house,
    return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;


-- Query 13: Average Expense Ratio by Fund House
SELECT
    fund_house,
    AVG(expense_ratio_pct) AS avg_expense_ratio_pct
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_expense_ratio_pct;


-- Query 14: Transaction Amount by Transaction Type
SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount_inr
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount_inr DESC;


-- Query 15: Funds by Risk Grade
SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;