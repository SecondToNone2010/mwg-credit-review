# MWG credit review case

I made this as a small corporate-credit exercise after my internship exposure to corporate loan files. The goal was not to reproduce a bank's internal rating model. I wanted a simple case where I could start from published financial statements, calculate a few ratios myself, and write down what I would care about before looking at collateral or a proposed facility.

## Company

Mobile World Investment Corporation (HOSE: MWG), a large Vietnamese retailer. I used consolidated figures for 2023-2025 and kept everything in VND billion.

## What I looked at

- revenue and profit recovery
- short-term liquidity
- debt relative to equity
- operating cash flow relative to debt and interest
- inventory as a share of sales
- cash plus short-term investments versus borrowings

I deliberately kept the model simple. There is no internal bank data, no credit-rating override, and no claim that the facility structure below is how a bank would actually approve MWG.

## Main takeaways

The business recovered strongly after a weak 2023. Revenue increased in both 2024 and 2025, while net profit recovered much faster. Liquidity is reasonable for a retailer: the current ratio stayed above 1.5x and cash plus short-term investments were larger than interest-bearing debt by the end of 2025. Operating cash flow remained positive, although it fell from the unusually strong 2024 level.

The main things I would still watch are inventory, thin retail margins, the amount of short-term borrowing, and execution risk from expansion. The balance sheet looks more comfortable than in 2023, but this is still a working-capital-heavy retail business rather than a low-leverage industrial company.

## Illustrative facility

For practice, I assumed a 12-month revolving working-capital line of VND 1,500bn. Primary repayment would be operating cash flow and cash conversion from inventory sales. I would monitor at least:

- current ratio above 1.2x
- total debt / equity below 1.5x
- positive operating cash flow
- no material deterioration in inventory relative to sales

These are case-study assumptions, not MWG's actual borrowing terms or a bank recommendation.

## Files

- `data/mwg_financials.csv`: public figures used in the analysis
- `analyze.py`: the ratio calculations
- `output/credit_ratios.csv`: calculated ratios
- `credit_memo.md`: short written credit view
- `MWG_Credit_Case.xlsx`: Excel version of the review

## Run

```bash
pip install -r requirements.txt
python analyze.py
```

## Sources

- MWG Investor Relations, Annual Report 2025: https://cdnv2.tgdd.vn/mwgvn/investorrelations/files/news/2026/3/2353/99/4b/994bc4902d35965c5e4013897d4f78f4.pdf
- MWG Investor Relations, Annual Report 2024: https://cdnv2.tgdd.vn/mwgvn/investorrelations/files/posts/2025/4/0/bd/b4/bdb4909af7f69858abb538dac47b2e76.pdf
- MWG Investor Relations homepage: https://mwg.vn/
- Historical balance-sheet cross-check: https://ishareinvest.com/vi/insights/stocks/mwg/bao-cao-tai-chinh/

Some historical figures are rounded to the nearest VND billion, so the project is for analysis practice rather than audit-level reconciliation.
