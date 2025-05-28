import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

COIN_ID = 'bitcoin'
CURRENCY = 'usd'
DAYS = '7'
URL = f'https://api.coingecko.com/api/v3/coins/{COIN_ID}/market_chart?vs_currency={CURRENCY}&days={DAYS}'

response = requests.get(URL)
data = response.json()

timestamps = [datetime.fromtimestamp(item[0] / 1000) for item in data['prices']]
prices = [item[1] for item in data['prices']]
market_caps = [item[1] for item in data['market_caps']]

# Downsample data
timestamps_ds = timestamps[::6]
prices_ds = prices[::6]
market_caps_ds = market_caps[::6]

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
sns.lineplot(x=timestamps_ds, y=prices_ds, color='green')
plt.title('Bitcoin Price (USD) - Last 7 Days')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.tight_layout(pad=2)

plt.subplot(2, 1, 2)
sns.lineplot(x=timestamps_ds, y=market_caps_ds, color='purple')
plt.title('Bitcoin Market Cap (USD) - Last 7 Days')
plt.ylabel('Market Cap (USD)')
plt.xticks(rotation=45)
plt.tight_layout(pad=2)

plt.show()
