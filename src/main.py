from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import timedelta
from tabulate import tabulate

def get_teams_playing(driver):
    # Note that a game played on the 30th of Dec (Sydney time) is listed as a game
    # on the 29th of December (US time)
    yesterday = datetime.now() - timedelta(days=1)

    # Format the date for yesterday
    formatted_date_yesterday = yesterday.strftime("%A, %B %d").upper()

    driver.get("https://www.nba.com/schedule")
    
    dates_elements = driver.find_elements(By.CLASS_NAME, "ScheduleDay_sdDay__3s2Xt")
    num_games_elements = driver.find_elements(By.CLASS_NAME, "ScheduleDay_sdWeek__iiTmo")

    index = 0
    for date in dates_elements:
        # Done to ensure the correct set of games are selected
        if date.text == formatted_date_yesterday:
            break
        index += 1

    # tokenised_string should be in the format ['X', 'Games']
    tokenised_string = num_games_elements[index].text.split()
    num_games = int(tokenised_string[0])

    # Necessary to ensure that the correct teams playing for the day are selected
    ignore_num_games = 0
    for i in range(index):
        tokenised_string_ignore = num_games_elements[i].text.split()
        ignore_num_games += int(tokenised_string_ignore[0])

    name_elements = driver.find_elements(By.CSS_SELECTOR, "a[data-id*='team']")

    # Create list of team names
    names = []
    ignored_counter = 0
    for element in name_elements:
        if not element.text == '':
            if ignored_counter < ignore_num_games * 2:
                ignored_counter += 1
                continue
            names.append(element.text)
        if len(names) == num_games * 2:
            break
    
    # Create dictionary with team names and betting odds as key-value pairs
    team_dict = {}
    for name in names:
        team_dict[name] = 0.00

    return names, team_dict

def find_sportsbet_odds(driver, team_dict, bookie_url):
    driver.get(bookie_url)

    filter = driver.find_element(By.CSS_SELECTOR, "[data-automation-id='market-filter-select']")
    select = Select(filter)
    select.select_by_visible_text("Match Betting")

    odds_elements = driver.find_elements(By.CSS_SELECTOR, "[data-automation-id='price-text']")
    name_elements = driver.find_elements(By.CLASS_NAME, "size12_fq5j3k2.normal_fgzdi7m.caption_f4zed5e")

    # Odds and team at same index correspond to each other
    odds = [element.text for element in odds_elements]
    teams = [name.text for name in name_elements]

    print(odds)
    print(teams)

def redirector_function(driver, bookie_info, team_dict):
    bookie_name = bookie_info[0]
    bookie_url = bookie_info[1]

    match bookie_name:
        case "LADBROKES":
            print("Running for Ladbrokes")
        case "SPORTSBET":
            print("Running for Sportsbet")
            find_sportsbet_odds(driver, team_dict, bookie_url)
        case "BLUEBET":
            print("Running for Bluebet")
        case "PLAYUP":
            print("Running for Playup")
        case "BET365":
            print("Running for Bet365")
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
    team_names, team_dict = get_teams_playing(driver)
    for bookie_info in nba_urls:
        redirector_function(driver, bookie_info, team_dict)

    driver.quit()

if __name__ == "__main__":
    main()