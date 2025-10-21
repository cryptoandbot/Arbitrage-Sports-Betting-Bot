# Web scraping functions to find betting odds from various bookmakers
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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
        # Slightly diffrent as sometimes Ladbrokes doesn't offer odds on all games
        # but Sportsbet does, so update team dictionary if odds are offered
        if not team_name in team_dict or team_dict[team_name][0] < betting_odds:
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