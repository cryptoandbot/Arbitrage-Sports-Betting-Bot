import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import os

load_dotenv()

def calculate_bet_size(arb, home_odds, away_odds):
    bet_stake = 100 

    # If you change the default bet stake, you'll need to update the math on
    # the ROI and expected return
    ROI = round(100 - arb, 2)
    expected_return = round(bet_stake + ROI, 2)

    home_bet = round(expected_return/home_odds, 2)
    away_bet = round(expected_return/away_odds, 2)
    return home_bet, away_bet, expected_return, ROI
     

def send_email(subject, message, recipient_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, recipient_email, text)
    server.quit()


def alert_if_arb_opp(home_team, away_team, arb_opps, home_bookie, home_odds, away_bookie, away_odds):
    for i, arb in enumerate(arb_opps):
        if not arb < float(100):
            home_bet, away_bet, expected_return, ROI = calculate_bet_size(arb, home_odds[i], away_odds[i])
            subject = "Arbitrage Opportunity Alert"
            message = f"An arbitrage opportunity exists in the game: {home_team[i]} vs {away_team[i]}.\n"\
                      f"Home Team Odds: {home_odds[i]} by {home_bookie[i]}.\n"\
                      f"Away Team Odds: {away_odds[i]} by {away_bookie[i]}.\n"\
                      f"Arbitrage Percentage: {arb}%.\n\n"\
                      f"For a bet of size $100, put ${home_bet} on {home_team[i]} and ${away_bet} on {away_team[i]}.\n"\
                      f"This results in a return of ${expected_return} and a {ROI}% ROI.\n"
            recipient_email = os.getenv("RECIPIENT_EMAIL")
            send_email(subject, message, recipient_email)

