# Arbitrage Betting Bot

## Overview

**Arbitrage Betting Bot** is a Python-based automation tool that scrapes and compares betting odds across multiple bookmaker websites to identify profitable arbitrage opportunities. Designed initially for **NBA games** and optimized for **Australian betting platforms**, the bot helps users quickly compare odds, calculate potential returns, and receive instant alerts when guaranteed-profit scenarios arise.

>  **Note:** This tool is intended **for educational and informational use only**. It does not promote or encourage gambling.

---

## Features

* **Automated Odds Scraping** – Collects live betting odds from multiple bookmakers using Selenium.
* **Cross-Bookmaker Comparison** – Identifies the best odds for each team across supported platforms.
* **Arbitrage Detection** – Calculates combined probabilities to detect risk-free profit opportunities.
* **Bet Sizing & ROI Estimation** – Computes the optimal stake distribution and expected ROI for each arbitrage event.
* **Email Alerts** – Sends automatic notifications when new arbitrage opportunities are found.

---

## Planned Enhancements

* **Multi-Sport Support:** Extend functionality to additional sports beyond NBA.
* **Expanded Bookmaker Coverage:** Integrate more platforms (e.g., BlueBet, Bet365, TAB).
* **Live Betting Module:** Implement support for real-time betting markets, which often yield higher arbitrage margins.

---

## Known Issues

* **Live Odds Variability:** Bookmakers format live odds differently; live game suspensions may trigger float conversion errors.
* **Unibet Game “Features”:** Occasionally misaligns odds display. Will be resolved once more data is collected on their featured-game formatting.

---

## Understanding Arbitrage Betting

### What Is Arbitrage Betting?

Arbitrage betting (or “arbing”) involves placing bets on **all possible outcomes** of an event with **different bookmakers** to lock in a profit regardless of the result. It exploits inconsistencies in odds between platforms.

### The Mathematics Behind It

Bookmakers set odds based on implied probabilities. For instance:

* Sportsbet offers **2.00** on the Knicks → 50% implied probability
* Sportsbet offers **1.85** on the Magic → 54.05% implied probability
* Combined total: **104.05%**, ensuring the bookmaker’s margin.

An arbitrage occurs when the **combined probability** is **below 100%**.
If another bookmaker offers **2.10** for the Magic, the combined probability becomes:

```
1/2.00 + 1/2.10 = 0.9762 → 97.62%
```

That implies a **2.38% ROI** opportunity.

#### Bet Sizing Example

To guarantee equal profit, distribute your $100 stake proportionally:

* Expected return: $102.38
* Bet on Knicks: 102.38 / 2.00 = **$51.19**
* Bet on Magic: 102.38 / 2.10 = **$48.75**

Result: A **guaranteed profit** regardless of outcome.

---

## Email Alerts

Each arbitrage alert includes:

* Teams and bookmakers involved
* Current odds for both outcomes
* Recommended stake per outcome (based on a $100 base bet)
* Expected return and ROI percentage

🔗 [Sample Email Screenshot](https://imgur.com/a/6oP44W7)

---

## Secure Email Credentials with `.env`

### Setting Up

Create a `.env` file in your project root:

```bash
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_app_specific_password
RECIPIENT_EMAIL=recipient@example.com
```

>  Use **app-specific passwords** (with 2FA enabled) instead of your main account password.

Ensure `.env` is listed in `.gitignore` to protect credentials.

### Accessing in Code

```python
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')
recipient = os.getenv('RECIPIENT_EMAIL')
```

This setup is automatically handled in `src/email_alert.py`.

---

## Disclaimer

This software is intended **solely for educational and informational purposes**. Betting involves financial risk and may be restricted by law in some regions.
The author does **not guarantee accuracy** of scraped odds or promote gambling activity. Always verify odds directly with bookmakers and ensure compliance with local laws before use.

---

## Prerequisites

* **Python 3.x**
* **Selenium**
* **Google Chrome** (or modify WebDriver for another browser)

---

## Installation

```bash
# Clone the repository
git clone git@github.com:mxl1503/arbitrage-betting-bot.git

# Navigate to the project directory
cd arbitrage-betting-bot

# Install dependencies
pip install selenium tabulate python-dotenv
```

---

## Usage

To start the scraper:

```bash
python3 src/main.py
```

---

## Supported Bookmakers

Currently integrated platforms:

* Ladbrokes
* Sportsbet
* PlayUp
* PointsBet
* Unibet

*More integrations coming soon.*

---

## Acknowledgements

Inspired by:

* [How Web Scraping is Transforming the World with its Applications – Hiren Patel](https://towardsdatascience.com/https-medium-com-hiren787-patel-web-scraping-applications-a6f370d316f4)
* [How I Got Banned from Sports Betting... Arbitrage Betting Explained – New Money](https://www.youtube.com/watch?v=TGinzvSDayU)
* [I Used Arbitrage Betting Strategy for 30 Days – Caan Berry Pro Trader](https://www.youtube.com/watch?v=gsXcOpmf75U)
* [How I Built a Sports Betting Bot | Arbitrage Betting Explained – Victor Fang](https://www.youtube.com/watch?v=q-NKvlGHJD4)

---
