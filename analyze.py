from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "mwg_financials.csv"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)


def pct(x):
    return round(x * 100, 1)


df = pd.read_csv(DATA).set_index("year")

# Basic ratios I would look at first for a working-capital borrower.
df["revenue_growth"] = df["revenue_bn_vnd"].pct_change()
df["net_margin"] = df["npat_bn_vnd"] / df["revenue_bn_vnd"]
df["current_ratio"] = df["current_assets_bn_vnd"] / df["current_liabilities_bn_vnd"]
df["quick_ratio"] = (
    df["cash_bn_vnd"] + df["short_term_investments_bn_vnd"] + df["receivables_bn_vnd"]
) / df["current_liabilities_bn_vnd"]
df["total_debt_bn_vnd"] = df["short_term_debt_bn_vnd"] + df["long_term_debt_bn_vnd"]
df["debt_to_equity"] = df["total_debt_bn_vnd"] / df["equity_bn_vnd"]
df["net_debt_bn_vnd"] = (
    df["total_debt_bn_vnd"]
    - df["cash_bn_vnd"]
    - df["short_term_investments_bn_vnd"]
)
df["cfo_to_debt"] = df["cfo_bn_vnd"] / df["total_debt_bn_vnd"]
df["cash_interest_cover"] = df["cfo_bn_vnd"] / df["interest_expense_bn_vnd"]
df["inventory_to_revenue"] = df["inventory_bn_vnd"] / df["revenue_bn_vnd"]

ratio_cols = [
    "revenue_growth",
    "net_margin",
    "current_ratio",
    "quick_ratio",
    "debt_to_equity",
    "net_debt_bn_vnd",
    "cfo_to_debt",
    "cash_interest_cover",
    "inventory_to_revenue",
]
df[ratio_cols].to_csv(OUT / "credit_ratios.csv")

latest = df.loc[2025]
print("MWG - simplified credit review")
print(f"Revenue growth: {pct(latest['revenue_growth'])}%")
print(f"Net margin: {pct(latest['net_margin'])}%")
print(f"Current ratio: {latest['current_ratio']:.2f}x")
print(f"Quick ratio: {latest['quick_ratio']:.2f}x")
print(f"Debt / equity: {latest['debt_to_equity']:.2f}x")
print(f"Net debt: {latest['net_debt_bn_vnd']:,.0f} bn VND")
print(f"CFO / debt: {latest['cfo_to_debt']:.2f}x")
print(f"CFO / interest: {latest['cash_interest_cover']:.2f}x")
