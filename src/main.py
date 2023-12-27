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

def redirector_function(driver, url_tuple):
    bookie = url_tuple[0]
    match bookie:
        case "LADBROKES":
            print('running for ladbrokes')
        case "SPORTSBET":
            print('running for sportsbet')
        case "BLUEBET":
            print('running for bluebet')
        case "PLAYUP":
            print('running for playup')
        case "BET365":
            print('running for bet365')
        case "TAB":
            print('running for tab')
        case "POINTSBET":
            print('running for pointsbet')
        case "UNIBET":
            print('running for unibet')
        case _:
            print('?????')

def main():
    driver = webdriver.Chrome()
    for url_tuple in nba_urls:
        redirector_function(driver, url_tuple)
        
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