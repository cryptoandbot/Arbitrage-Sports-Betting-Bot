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

# def find_bet365_odds(driver, team_dict, bookie_url):
#     driver.get(bookie_url)

#     # Wait for website to load properly
#     wait = WebDriverWait(driver, 15)
#     wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sac-ParticipantOddsOnly50OTB_Odds")))

#     odds_elements = driver.find_elements(By.CLASS_NAME, "sac-ParticipantOddsOnly50OTB_Odds")
#     odds = [odd.text for odd in odds_elements]
#     print(odds)

# def find_tab_odds(driver, team_dict, bookie_url):
#     driver.get(bookie_url)
#     time.sleep(1)
#     elements = driver.find_elements(By.CSS_SELECTOR, "animate-odd")

#     for element in elements:
#         print(element.text)

def find_pointsbet_odds(driver, team_dict, bookie_url):
    driver.get(bookie_url)
    time.sleep(1)

    odds_elements = driver.find_elements(By.CLASS_NAME, "fheif50")
    name_elements = driver.find_elements(By.CLASS_NAME, "f193t5zp.f1r0ggt8.f1wtz5iq.f1rokedd")
    
    # Odds are in order of H2H, Line and Total, and therefore I only want the 1st,
    # 4th, 7th and so on numbers
    counter = 0
    odds = []
    for odd_element in odds_elements:
        if counter % 3 == 0:
            odds.append(odd_element.text)
        counter += 1

    names = [name.text for name in name_elements]

    for i in range(len(odds)):
        team_name = names[i]

        # Check if any odds are better at Pointsbet and update accordingly
        betting_odds = float(odds[i])
        if team_dict[team_name][0] < betting_odds:
            team_dict[team_name] = (betting_odds, "POINTSBET") 

def find_unibet_odds(driver, team_dict, bookie_url):
    driver.get(bookie_url)
    time.sleep(1)

    odds_elements = driver.find_elements(By.CLASS_NAME, "_8e013")
    name_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-test-name='teamName']")

    # Odds are in order of Team 1 Win, Team 2 Win, Team 1 Moneyline, Team 2 Moneyline
    counter = 0
    odds = []
    for odd_element in odds_elements:
        if counter % 4 == 0 or counter % 4 == 1:
            odds.append(odd_element.text)
        counter += 1

    names = [name.text for name in name_elements]

    for i in range(len(odds)):
        try:        
            team_name = names[i]

            # Check if any odds are better at Unibet and update accordingly
            betting_odds = float(odds[i])
            if team_dict[team_name][0] < betting_odds:
                team_dict[team_name] = (betting_odds, "UNIBET") 
        except KeyError:
            # Sometimes teams playing will break the odds mapping so just break
            # and ignore this case
            break
      
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
        opp = (1/home_odds[i] + 1/away_odds[i]) * 100
        arb_opps.append(opp)
    
    matches_data = zip(home_team, away_team, arb_opps, home_bookie, home_odds, away_bookie, away_odds)
    print(tabulate(matches_data, headers=["Home Team", "Away Team", 'Arb (%)', 'Bookie', 'Odds', 'Bookie', 'Odds']))

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