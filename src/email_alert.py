import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import os

load_dotenv()

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
        if arb < float(100):
            subject = "Arbitrage Opportunity Alert"
            message = f"An arbitrage opportunity exists in the game: {home_team[i]} vs {away_team[i]}\n"\
                      f"Home Team Odds: {home_odds[i]} by {home_bookie[i]}\n"\
                      f"Away Team Odds: {away_odds[i]} by {away_bookie[i]}\n"\
                      f"Arbitrage Percentage: {arb}%"
            recipient_email = os.getenv("RECIPIENT_EMAIL")
            send_email(subject, message, recipient_email)
