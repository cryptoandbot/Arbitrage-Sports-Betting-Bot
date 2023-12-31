# Arbitrage Betting Bot

## Overview
This project is a Python-based tool that scrapes betting odds from various bookmaker websites. It aims to identify the best odds for each team playing on a given day, allowing users to quickly compare odds,
helping make more informed decisions as well as be alerted when an arbitrage betting opportunity arises. Currently, the script is designed for NBA games only.

## Features
- **Automated Scraping:** Collects odds from multiple bookmaker websites.
- **Team Odds Comparison:** Compares odds across different platforms to find the best available odds for each team.
- **Arbitrage Opportunity Calculator:** Finds arbitrage opportunities when present.
- **Custom Alert System:** Alert users via email when arbitrage betting opportunities arise.

## Planned Future Features
- **Works With Multiple Sports:** Functional for multiple sports to find more arbitrage opportunities. 
- **Adding More Bookies:** Add functionality for Bluebet, Bet365, TAB and more.

## Arbitrage Betting Explained

### What is Arbitrage Betting?
Arbitrage betting is a betting strategy where you place bets on all possible outcomes of an event with different bookmakers, taking advantage of differing odds to guarantee a profit regardless of the event's result.

### The Maths Explained
We can exploit the variation in odds offered by different bookmakers to ensure a profit. A bookmaker sets odds based on the expected probability of a particular outcome. Let's consider the odds offered
by Sportsbet on a NY Knicks vs Orlando Magic game on 30/12/23. The odds of 2.00 and 1.85 respectively suggest that the bookmaker believes that the Knicks have a 50% chance of winning, and that the
Magic has a 54.05% chance of winning. This is calculated by taking 1 divided by the odds offered (1/odds). 

You'll notice that the probability adds up to over 100%. This essentially means that if you bet on both outcomes, you'll lose a little bit of money each time, ensuring the bookie makes money.
However, in rare cases, you'll find odds that result in a probability that sums to under 100%, representing an arbitrage betting opportunity. Taking the same scenario, suppose I found a bookmaker who offered odds of 2.10 for the Magic to win. Summing the inverses of the odds, we get 1/2.00 + 1/2.10 = 97.62%. This represents an arbitrage opportunity (as it's below 100%) and we can place wagers proportional to the betting odds to guarantee profit.

## Secure Email Credentials with a `.env` File

### Setting Up The `.env` File
To securely handle your email credentials for alert notifications:
1. Create a `.env` file in your project root directory.
2. Add your email and password to this file:
```
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_password
```
3. Ensure that `.env` is listed in your `.gitignore` to keep your credentials secure.

### Accessing Credentials in Python
Use the `dotenv` package to load and access these variables in your Python scripts:
```python
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')
```
This is done in `src/email_alert.py` so adding to the `.env` file is sufficient

### Setting the Recipient's Email
Similarly, use the `.env` file to set the recipient's email. Add to the file 
your recipient email in the format:
```
RECIPIENT_EMAIL=your_email@example.com
```
This will automatically change your recipient email in the script.

Here's what the email alert looks like: https://imgur.com/a/gj2k9Y6

## Disclaimer
This tool is provided for educational and informational purposes only. It is important to note that gambling involves significant financial risk and may not be suitable for everyone. I do not promote or endorse gambling. Users are advised to exercise caution and bet within their means. Additionally, the accuracy of the betting odds data extracted by this tool cannot be guaranteed, as bookmakers frequently update odds. Users are responsible for verifying the odds with the bookmaker before placing any bets. This tool is intended for personal use, and the user must ensure compliance with all local laws and regulations regarding online betting in their jurisdiction.

## Prerequisites
- Python3
- Selenium
- Chrome (can change to any modern browser with small code modifications)

## Installation
1. Ensure Python is installed on your system.
2. Install Selenium, Tabulate and Python-Dotenv: `pip install selenium`, `pip install tabulate` and `pip install python-dotenv`
3. Install Google Chrome (or change WebDriver to a browser of your choice)
4. Clone this repository: `git clone git@github.com:mxl1503/arbitrage-betting-bot.git`.

## Usage
To run the scraper:
```bash
python3 src/main.py
```

## Supported Bookmakers
Currently the script uses the following bookmakers to find arbitrage opportunities:
- Ladbrokes
- Sportsbet
- Playup
- Pointsbet
- Unibet

## Acknowledgements
Project inspired by the following sources:
- **How Web Scraping is Transforming the World with its Applications** by Hiren Patel (https://towardsdatascience.com/https-medium-com-hiren787-patel-web-scraping-applications-a6f370d316f4)
- **How I got banned from sports betting... - Arbitrage Betting Explained** by New Money (https://www.youtube.com/watch?v=TGinzvSDayU)
- **I Used Arbitrage Betting Strategy for 30 Days – Results & Explanation** by Caan Berry Pro Trader (https://www.youtube.com/watch?v=gsXcOpmf75U)
- **How I built a sports betting bot | Arbitrage Betting Explained** by Victor Fang (https://www.youtube.com/watch?v=q-NKvlGHJD4)
