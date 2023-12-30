from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tabulate import tabulate
import time

def find_ladbrokes_odds(driver, team_dict, bookie_url):
    driver.get(bookie_url)
    time.sleep(1)

    odds_elements = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='price-button-odds']")
    name_elements = driver.find_elements(By.CLASS_NAME, "displayTitle")

    # Odds and team at same index correspond to each other
    odds = [odd.text for odd in odds_elements]
    teams = [name.text for name in name_elements]
    
    for i in range(len(odds)):
        team_name = teams[i]
        betting_odds = float(odds[i])

        # Construct dictionary using infomation from Ladbrokes
        team_dict[team_name] = (betting_odds, "LADBROKES") 

def find_sportsbet_odds(driver, team_dict, bookie_url):
    driver.get(bookie_url)
    time.sleep(1)

    filter = driver.find_element(By.CSS_SELECTOR, "[data-automation-id='market-filter-select']")
    select = Select(filter)
    select.select_by_visible_text("Match Betting")

    odds_elements = driver.find_elements(By.CSS_SELECTOR, "[data-automation-id='price-text']")
    name_elements = driver.find_elements(By.CLASS_NAME, "size12_fq5j3k2.normal_fgzdi7m.caption_f4zed5e")

    # Odds and team at same index correspond to each other
    odds = [odd.text for odd in odds_elements]
    teams = [name.text for name in name_elements]

    for i in range(len(odds)):
        team_name = teams[i]

        # Check if any odds are better at Sportsbet and update accordingly
        betting_odds = float(odds[i])
        if team_dict[team_name][0] < betting_odds:
            team_dict[team_name] = (betting_odds, "SPORTSBET") 

def find_playup_odds(driver, team_dict, bookie_url):
    driver.get(bookie_url)
    time.sleep(1)

    elements = driver.find_elements(By.CLASS_NAME, "py-1")
    assorted_team_odds = [element.text for element in elements]

    for team in team_dict:
        try:
            team_index = assorted_team_odds.index(team)
            # Ensure the next item in the list is a number (odds)
            if team_index + 1 < len(assorted_team_odds) and assorted_team_odds[team_index + 1].replace('.', '', 1).isdigit():
                team_odds = float(assorted_team_odds[team_index + 1])
                if team_dict[team][0] < team_odds:
                    team_dict[team] = (team_odds, "PLAYUP")
        except ValueError:
            print(f"Team {team} not found in odds list")


            
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
        case "BLUEBET":
            print("Running for Bluebet")
            # find_bluebet_odds(driver, team_dict, bookie_url)
        case "PLAYUP":
            print("Running for Playup")
            find_playup_odds(driver, team_dict, bookie_url)
        case "BET365":
            print("Running for Bet365")
            find_bet365_odds(driver, team_dict, bookie_url)
        case "TAB":
            print("Running for TAB")
        case "POINTSBET":
            print("Running for Pointsbet")
        case "UNIBET":
            print("Running for Unibet")
        case _:
            print(f"Invalid url: {bookie_url}")

def main():
    nba_urls = [
        ("LADBROKES", "https://www.ladbrokes.com.au/sports/basketball/usa/nba"), 
        ("SPORTSBET", "https://www.sportsbet.com.au/betting/basketball-us/nba"),
        ("BLUEBET", "https://www.bluebet.com.au/sports/Basketball/107/United-States-of-America/NBA-Matches/39251"),
        ("PLAYUP", "https://www.playup.com.au/betting/sports/basketball/nba"),
        ("BET365", "https://www.bet365.com.au/#/AS/B18/"),
        ("TAB", "https://www.tab.com.au/sports/betting/Basketball/competitions/NBA"),
        ("POINTSBET", "https://pointsbet.com.au/sports/basketball/NBA"),
        ("UNIBET", "https://www.unibet.com.au/betting/sports/filter/basketball/nba/all/matches"),
    ]

    driver = webdriver.Chrome()

    team_dict = {}
    for bookie_info in nba_urls:
        redirector_function(driver, bookie_info, team_dict)

    driver.quit()

    print(team_dict)

if __name__ == "__main__":
    main()