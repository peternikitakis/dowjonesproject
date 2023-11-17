import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the start and end dates for the data
start_date = '2022-01-01'
end_date = '2023-01-01'

# Download data for Dow and S&P 500
dow_data = yf.download('^DJI', start=start_date, end=end_date)
sp500_data = yf.download('^GSPC', start=start_date, end=end_date)

# Select the 'Close' prices
dow_close = dow_data['Close']
sp500_close = sp500_data['Close']

# Calculate the percentage change from the initial value for each index
dow_percentage = (dow_close / dow_close.iloc[0] * 100) - 100
sp500_percentage = (sp500_close / sp500_close.iloc[0] * 100) - 100

# Combine into a DataFrame
df_percentage = pd.DataFrame({'Dow': dow_percentage, 'S&P 500': sp500_percentage})

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df_percentage.index, df_percentage['Dow'], label='Dow')
plt.plot(df_percentage.index, df_percentage['S&P 500'], label='S&P 500')
plt.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.7)  # Add a horizontal line at 0%
plt.title('Dow vs S&P 500 Comparison (Percentage Change)')
plt.xlabel('Date')
plt.ylabel('Percentage Change from Initial Value')
plt.legend()
plt.grid(True)
plt.show()
