from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tabulate import tabulate

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

def get_teams_playing(driver):
    driver.get("https://www.nba.com/schedule")

    # num_games_element.text should be in the format "x Games"
    num_games_element = driver.find_element(By.CLASS_NAME, "ScheduleDay_sdWeek__iiTmo")
    num_games = int(num_games_element.text[0])

    name_elements = driver.find_elements(By.CSS_SELECTOR, "a[data-id*='team']")

    names = []
    for element in name_elements:
        if not element.text == '':
            names.append(element.text)
        if len(names) == num_games * 2:
            break
    
    team_dict = {}
    for name in names:
        team_dict[name] = 0.00

    return names, team_dict

def redirector_function(driver, bookie_info, team_dict):
    bookie_name = bookie_info[0]
    bookie_url = bookie_info[1]

    match bookie_name:
        case "LADBROKES":
            print("Running for Ladbrokes")
        case "SPORTSBET":
            print("Running for Sportsbet")
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
    driver = webdriver.Chrome()
    team_names, team_dict = get_teams_playing(driver)
    for bookie_info in nba_urls:
        redirector_function(driver, bookie_info, team_dict)

    # driver.get("https://www.sportsbet.com.au/betting/basketball-us/nba")

    # filter = driver.find_element(By.CSS_SELECTOR, "[data-automation-id='market-filter-select']")
    # select = Select(filter)
    # select.select_by_visible_text("Match Betting")

    # odds_elements = driver.find_elements(By.CSS_SELECTOR, "[data-automation-id='price-text']")
    # name_elements = driver.find_elements(By.CLASS_NAME, "size12_fq5j3k2.normal_fgzdi7m.caption_f4zed5e")

    # odds = [element.text for element in odds_elements]
    # teams = [name.text for name in name_elements]

    driver.quit()

if __name__ == "__main__":
    main()