import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from timehelper import get_today_date


def retrieve_youtube_link(team: str):
    today_date = get_today_date()
    options = Options()
    options.add_argument("-headless")
    logging.basicConfig(level=logging.ERROR)

    with webdriver.Firefox(options=options) as driver:
        yt_url = f"https://www.youtube.com/results?search_query={team}+highlights"
        driver.get(yt_url)
        print("Youtube URL retrieved...")

        wait = WebDriverWait(driver, 2)
        wait.until(presence_of_element_located((By.ID, "contents")))

        video_contents = driver.find_elements(By.XPATH, "//a[@id='video-title']")[:3]

        try:
            for element in video_contents:
                title_attr = element.get_attribute("aria-label")
                href_attr = element.get_attribute("href")

                if f"{today_date} by NBA" and team.upper() in title_attr:
                    return f"[Game Highlights]({href_attr})"
            return "Highlights not found"

        except Exception as e:
            logging.error(f"Unexpected error retrieving YT URL: {str(e)}")
        finally:
            driver.quit()
