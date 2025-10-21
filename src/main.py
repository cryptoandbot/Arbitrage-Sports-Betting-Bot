# Main arbitrage betting bot - scrapes odds and identifies opportunities
from selenium import webdriver
from selenium.webdriver.common.by import By
from tabulate import tabulate

from find_odds import *
from email_alert import *
      
def redirector_function(driver, bookie_info, team_dict):
    bookie_name = bookie_info[0]
    bookie_url = bookie_info[1]

    match bookie_name:
        case "LADBROKES":
            print("Running for Ladbrokes")
            find_ladbrokes_odds(driver, team_dict, bookie_url)
        case "SPORTSBET":
            print("Running for Sportsbet")
            find_sportsbet_odds(driver, team_dict, bookie_url)
        case "PLAYUP":
            print("Running for Playup")
            find_playup_odds(driver, team_dict, bookie_url)
        case "POINTSBET":
            print("Running for Pointsbet")
            find_pointsbet_odds(driver, team_dict, bookie_url)
        case "UNIBET":
            print("Running for Unibet")
            find_unibet_odds(driver, team_dict, bookie_url)
        case _:
            print(f"Invalid url: {bookie_url}")

def tabulate_data(team_dict):
    home_team = [team for i, team in enumerate(team_dict) if i % 2 == 0]
    away_team = [team for i, team in enumerate(team_dict) if i % 2 != 0]

    home_odds = [team_dict[team][0] for team in home_team]
    away_odds = [team_dict[team][0] for team in away_team]

    home_bookie = [team_dict[team][1] for team in home_team]
    away_bookie = [team_dict[team][1] for team in away_team]

    arb_opps = []
    for i in range(len(home_odds)):
        opp = round((1/home_odds[i] + 1/away_odds[i]) * 100, 3)
        arb_opps.append(opp)
    
    matches_data = zip(home_team, away_team, arb_opps, home_bookie, home_odds, away_bookie, away_odds)
 
    print('')
    print(tabulate(matches_data, headers=["Home Team", "Away Team", 'Arb (%)', 'Bookie', 'Odds', 'Bookie', 'Odds']))
    print('')

    alert_if_arb_opp(home_team, away_team, arb_opps, home_bookie, home_odds, away_bookie, away_odds)

def main():
    nba_urls = [
        ("LADBROKES", "https://www.ladbrokes.com.au/sports/basketball/usa/nba"), 
        ("SPORTSBET", "https://www.sportsbet.com.au/betting/basketball-us/nba"),
        ("PLAYUP", "https://www.playup.com.au/betting/sports/basketball/nba"),
        ("POINTSBET", "https://pointsbet.com.au/sports/basketball/NBA"),
        ("UNIBET", "https://www.unibet.com.au/betting/sports/filter/basketball/nba/all/matches"),
    ]

    driver = webdriver.Chrome()

    team_dict = {}
    for bookie_info in nba_urls:
        redirector_function(driver, bookie_info, team_dict)

    driver.quit()

    tabulate_data(team_dict)

if __name__ == "__main__":
    main()