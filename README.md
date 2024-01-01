# Arbitrage Betting Bot

## Overview
This project is a Python-based tool that scrapes betting odds from various bookmaker websites. It aims to identify the best odds for each team playing on a given day, allowing users to quickly compare odds,
helping make more informed decisions as well as be alerted when an arbitrage betting opportunity arises. Currently, the script is designed for NBA games only.

## Features
- **Automated Scraping:** Collects odds from multiple bookmaker websites.
- **Team Odds Comparison:** Compares odds across different platforms to find the best available odds for each team.
- **Arbitrage Opportunity Calculator:** Finds arbitrage opportunities when present.
- **Bet Sizing and ROI Calculation:** Calculates the optimal bet size for each outcome and the expected return on investment (ROI) for arbitrage opportunities.
- **Custom Alert System:** Alert users via email when arbitrage betting opportunities arise.

## Planned Future Features
- **Works With Multiple Sports:** Functional for multiple sports to find more arbitrage opportunities. 
- **Adding More Bookies:** Add functionality for Bluebet, Bet365, TAB and more.

## Arbitrage Betting Explained

### What is Arbitrage Betting?
Arbitrage betting is a betting strategy where you place bets on all possible outcomes of an event with different bookmakers, taking advantage of differing odds to guarantee a profit regardless of the event's result.

### The Maths Explained
We can take advantage of the differences in odds offered by various bookmakers to secure a guaranteed profit. This strategy, known as arbitrage betting, is based on the principle that bookmakers set odds to 
reflect the expected probabilities of the outcomes of an event. For example, consider a basketball game between the NY Knicks and Orlando Magic, where Sportsbet offers odds of 2.00 for the Knicks and 1.85 
for the Magic. These odds imply that Sportsbet estimates a 50% chance of the Knicks winning (calculated as 1 divided by the odds, or 1/2.00) and a 54.05% chance for the Magic (1/1.85).

The combined probability exceeds 100% (50% + 54.05% = 104.05%), which is typical in betting markets. This overround ensures that the bookmaker profits regardless of the outcome if bets are evenly 
distributed. However, arbitrage opportunities arise when the combined implied probabilities of all possible outcomes are less than 100%. For instance, if another bookmaker offers odds of 2.10 for the Magic, 
the combined probability becomes 1/2.00 + 1/2.10, which equals 97.62%. This under 100% total indicates an arbitrage opportunity, with an ROI of 2.38% (calculated by 100% - combined probability).

We also need to calculate how much to bet on each outcome to ensure we make the same return regardless of the game's actual outcome. To determine the bet sizing, we take the expected return and divide
through by the odds offered on each outcome. In this example, let's suppose I'm betting with $100. Since I know my ROI is 2.38%, I can expect a return of $102.38. This means that I'll bet $51.19 on the Knicks and $38.75 on the Magic to ensure a profit is made. These bets were calculated by taking my expected return of $102.38, and dividing it by each team's odds to find the bet sizing. In this case, 
$102.38/2.00 = $51.19 and $102.38/2.10 = $38.75 giving me the amount to bet on the Knicks and Magic respectively. 

## Email Alert Content

The email alert includes the following information:

- The teams playing and their respective odds from different bookies.
- The calculated bet size to place on each team.
- The expected return and ROI for a given bet stake (default $100).
- Arbitrage percentage indicating the profitability of the opportunity.

A sample email alert can be seen here: https://imgur.com/a/6oP44W7

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
This is done in `src/email_alert.py` so adding to the `.env` file is sufficient.

### Authentication Error
This is a common issue even if you've inputted the correct email and password. Instead,
create an app specific password (requires you to have 2FA turned on) and instead use the
app specific password you've created. This will fix this issue

### Setting the Recipient's Email
Similarly, use the `.env` file to set the recipient's email. Add to the file 
your recipient email in the format:
```
RECIPIENT_EMAIL=your_email@example.com
```
This will automatically change your recipient email in the script.

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

More to be added soon!

## Acknowledgements
Project inspired by the following sources:
- **How Web Scraping is Transforming the World with its Applications** by Hiren Patel (https://towardsdatascience.com/https-medium-com-hiren787-patel-web-scraping-applications-a6f370d316f4)
- **How I got banned from sports betting... - Arbitrage Betting Explained** by New Money (https://www.youtube.com/watch?v=TGinzvSDayU)
- **I Used Arbitrage Betting Strategy for 30 Days – Results & Explanation** by Caan Berry Pro Trader (https://www.youtube.com/watch?v=gsXcOpmf75U)
- **How I built a sports betting bot | Arbitrage Betting Explained** by Victor Fang (https://www.youtube.com/watch?v=q-NKvlGHJD4)
