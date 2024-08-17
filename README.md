<div>
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_clara.png" alt="logo clara" width="300" style="display: inline-block; vertical-align: top; margin-right: 10px;">
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_dark.png" alt="logo dark" width="300" style="display: inline-block; vertical-align: top;">
</div>

# Daily Variation Average

## Description

This script generates a histogram that displays the average daily variation of an asset, represented either as value changes or points. It retrieves the necessary data from MetaTrader 5 (MT5), a popular trading platform.

## Features

- **Data Retrieval**: Connects to MT5 and retrieves historical price data for a specified asset.
- **Daily Variation Calculation**: Computes the daily variation as the difference between the closing and opening prices.
- **Histogram Plotting**: Plots a histogram of the daily variations, illustrating how often different ranges of variations occur.

## Libraries Used

- `matplotlib`: For plotting histograms and visualizing data.
- `MetaTrader5`: For fetching historical price data from MT5.
- `pandas`: For data manipulation and analysis.
