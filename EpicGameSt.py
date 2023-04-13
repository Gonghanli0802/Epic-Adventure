# Gonghan Li

# This program scrapes all the weekly free games that EPIC Games send out. 
# Stores the relavent infomation and sends it to user's phone

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import pickle
from twilio.rest import Client
import keys
import time
import pandas as pd


# find_price(driver) locates the price tag of each game. 
def find_price(driver):
    try:
        display_list = driver.find_elements(By.CLASS_NAME, "css-u4p24i")
        price_str = display_list[2].text
        begin = 0
        while (begin < len(price_str) and price_str[begin] != "C"):
            begin += 1
        return price_str[begin:begin+8]
    except:
        return "Price not found"

# find_genres(driver) locates the genres of each free game.
def find_genres(driver):
    try:
        limit = 0
        gen_str = ""
        genres_class = driver.find_elements(By.CLASS_NAME, "css-t8k7")
        for sub_class in genres_class:
            second = sub_class.find_element(By.CLASS_NAME, "css-19v36wf")
            third = second.find_element(By.CLASS_NAME, "css-119zqif")

            if limit == 2:
                gen_str += third.text
                return gen_str
            
            gen_str += third.text + ", "
            limit += 1
        
        return gen_str
    except:
        return "Genres not found"

# print_rating(driver, temp_game) locates the metacritic score for each free weekly game.
def find_rating(driver, temp_game):
    text_box = driver.find_element(
        By.ID, "primary_search_box")
    text_box.clear()
    time.sleep(1)
    text_box.send_keys(temp_game)
    driver.find_element(By.ID, "primary_search_box").send_keys(Keys.RETURN)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div:nth-child(3) > a > input"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(7) > a > input[type=radio]"))
    )
    element.click()
    result_list = []

    try:
        driver.find_element(
            By.CSS_SELECTOR, "#main_content > div > div.module.search_results.fxdcol.gu6 > div > ul > li.result.first_result > div > div.basic_stats.has_thumbnail > div > h3 > a").click()
        time.sleep(3)

        result_list.append(driver.find_elements(
            By.CLASS_NAME, "metascore_anchor")[0].text)
        result_list.append(driver.find_elements(
            By.CLASS_NAME, "metascore_anchor")[1].text)
        return result_list
    except:
        result_list.append("Unavailable")
        result_list.append("Unavailable")
        return result_list

# send_message(str) sends the weekly free games information to user's phone
def send_message(str):
    cl = Client(keys.account_sid, keys.auth_token)
    message = cl.messages.create(
        body = str,
        from_= keys.twilio_number,
        to = keys.my_phone
    )
    print(message.body)


def __main__():

    #Load user profile to avoid having to login
    chrome_options = Options()
    chrome_options.add_argument(
        r"--user-data-dir=C:\Users\Kevin\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument(r'--profile-directory=Default')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument(
        '--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--remote-allow-origins=*")
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    try:
        # Navigate to Epic Games and load the cookies
        time.sleep(3)
        driver.get("https://store.epicgames.com/en-US/")
        WAIT = WebDriverWait(driver, 10)
        game_list = []
        date_list = []
        genres_list = []
        price_list = []
        length = 0
        game_num = 0
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
           driver.add_cookie(cookie)

        # Locate the weekly free games and parse relavant info
        name_class = WAIT.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "css-1h2ruwl")
            )
        )
        date_class = driver.find_elements(By.CLASS_NAME, "css-nf3v9d")

        for temp in date_class:
            tex = temp.text
            if (len(tex) != 0 and tex[0] == "F"):
                date_list.append(temp.text)
                game_list.append(name_class[length].text)
                length = length + 1

        while game_num < len(name_class):
            temp_game = name_class[game_num]
            temp_game.click()
            time.sleep(5)
            price_list.append(find_price(driver))
            genres_list.append(find_genres(driver))
            driver.back()
            name_class = WAIT.until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "css-1h2ruwl"))
                )
            game_num = game_num + 1

        pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))


        # Navigate to Metacritic to parse the rating of each game
        driver.get("https://www.metacritic.com/game")
        length = 0
        excel_list = []

        for temp_game in game_list:
            rating_list = []
            rating_list = find_rating(driver, temp_game)
            excel_item = {
                'title': temp_game,
                'price': price_list[length],
                'genres': genres_list[length],
                'time': date_list[length],
                'critic': rating_list[0],
                'user': rating_list[1]
            }
            length = length + 1
            excel_list.append(excel_item)

        # Saves data to excel and send to user's phone
        df = pd.DataFrame(excel_list)
        df.to_excel("Games.xlsx")
        result_string = "The weekly free games of EPIC Games are\n"
        result_string += df.to_string()
        send_message(result_string)

    finally:
        driver.close()
        driver.quit()


__main__()