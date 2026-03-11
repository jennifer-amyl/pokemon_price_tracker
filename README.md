# Pokemon Price Tracker

A Python project for tracking Pokémon card purchase prices, current values, and profit/loss from a CSV file.

## Features

- Reads Pokémon card data from CSV
- Calculates total paid and current value
- Calculates profit/loss per card
- Calculates percentage change
- Identifies best and worst performing cards
- Exports a CSV report
- Generates a text summary report

## How to Run

```bash
py tracker.py

## Using eBay CSV Export

This tool can also work with CSV exports from eBay purchase history.

To use eBay data:

1. Export your purchase history from eBay as a CSV file.
2. Keep the columns for:
   - Item title
   - Price paid
   - Quantity
3. Rename the columns to match the format used by this project:

| eBay Column | Project Column |
|-------------|---------------|
| Item title  | Card |
| Price paid  | PurchasePrice |
| Quantity    | Quantity |

You can then add a `CurrentPrice` column manually using current market prices.

Once formatted, the CSV can be used as input for the tracker.
