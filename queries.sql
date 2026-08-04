-- Query 1: Top 5 Funds by AUM
SELECT fund_house,aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV per Month
SELECT strftime('%Y-%m', full_date) AS month,
       AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- Query 3: Transactions by State
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 4: Funds with Expense Ratio < 1%
SELECT amfi_code,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Query 5: SIP YoY Growth
SELECT month,
       yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

-- Query 6: Highest NAV
SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 1;

-- Query 7: Number of Transactions by Type
SELECT transaction_type,
       COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- Query 8: Total Investment Amount
SELECT SUM(amount_inr) AS total_investment
FROM fact_transactions;

-- Query 9: Number of Funds in Each Category
SELECT category,
       COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

-- Query 10: Total Number of Funds
SELECT COUNT(*) AS total_funds
FROM dim_fund;
