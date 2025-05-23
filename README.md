# Crypto Market CLI

A simple command-line Python tool that fetches and displays cryptocurrency market data using the [CoinGecko API](https://www.coingecko.com/en/api).

## Features

- 📈 Retrieves top cryptocurrencies by market capitalization.
- 💵 Shows current price, market cap, and price changes over 1 hour, 24 hours, and 7 days.
- 🎨 Colorized CLI output using `colorama`.
- ❌ Handles connection and response errors gracefully.

## Usage

```bash
python main.py
```

You will see a formatted list of the top 10 cryptocurrencies with the following details:

- ID
- Symbol
- Name
- Price in USD
- Market Cap
- Price Change (1h, 24h, 7d)

## Project Structure

```
.
├── main.py       # Entry point for CLI
├── utils.py      # API logic and data processing
├── README.md     # Project description
└── requirements.txt  # Required packages (optional)
```

## Requirements

- Python 3.8+
- `requests`
- `colorama`

Install dependencies:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.