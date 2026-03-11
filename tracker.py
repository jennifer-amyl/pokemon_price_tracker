import pandas as pd

input_file = "cards.csv"
output_file = "card_report.csv"
text_report = "report.txt"

print(f"Reading file: {input_file}")

try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"Error: '{input_file}' was not found.")
    raise SystemExit

# work out totals
df["TotalPaid"] = df["PurchasePrice"] * df["Quantity"]
df["TotalCurrentValue"] = df["CurrentPrice"] * df["Quantity"]
df["ProfitLoss"] = df["TotalCurrentValue"] - df["TotalPaid"]
df["PercentChange"] = ((df["CurrentPrice"] - df["PurchasePrice"]) / df["PurchasePrice"]) * 100

print("\nCard Profit/Loss Summary:")
print(df[["Card", "Set", "PurchasePrice", "CurrentPrice", "Quantity", "ProfitLoss", "PercentChange"]])

total_paid = df["TotalPaid"].sum()
total_value = df["TotalCurrentValue"].sum()
total_profit = df["ProfitLoss"].sum()

best_card = df.loc[df["ProfitLoss"].idxmax()]
worst_card = df.loc[df["ProfitLoss"].idxmin()]

df.rename(columns={
    "TotalPaid": "Total Paid (£)",
    "TotalCurrentValue": "Total Current Value (£)",
    "ProfitLoss": "Profit / Loss (£)",
    "PercentChange": "Percent Change (%)"
}, inplace=True)

df.to_csv(output_file, index=False)

with open(text_report, "w", encoding="utf-8") as file:
    file.write("Pokemon Card Price Tracker Report\n")
    file.write("================================\n\n")

    file.write(f"Total paid: £{total_paid:.2f}\n")
    file.write(f"Current value: £{total_value:.2f}\n")
    file.write(f"Total profit/loss: £{total_profit:.2f}\n\n")

    file.write("Best performing card:\n")
    file.write(f"{best_card['Card']} ({best_card['Set']}) - £{best_card['ProfitLoss']:.2f}\n\n")

    file.write("Worst performing card:\n")
    file.write(f"{worst_card['Card']} ({worst_card['Set']}) - £{worst_card['ProfitLoss']:.2f}\n\n")

    file.write("Full card breakdown:\n")
    file.write(df.to_string(index=False))

print(f"\nSaved CSV report to {output_file}")
print(f"Saved TXT report to {text_report}")

print(f"\nTotal paid: £{total_paid:.2f}")
print(f"Current value: £{total_value:.2f}")
print(f"Total profit/loss: £{total_profit:.2f}")
print(f"Best card: {best_card['Card']} ({best_card['Set']})")
print(f"Worst card: {worst_card['Card']} ({worst_card['Set']})")