from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_two_buttons():
    driver = setup()

    title = driver.title
    assert title == "4250 Honors Project"
        
    driver.implicitly_wait(0.5)

    s1_button = driver.find_element(by=By.ID, value="s1")
    s2_button = driver.find_element(by=By.ID, value="s2")
    h1_element = driver.find_element(by=By.TAG_NAME, value="h1")
    
    s1_button.click()
    bg_color_s1 = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor;")
    s2_button.click()
    tx_color_s2 = driver.execute_script("return window.getComputedStyle(arguments[0]).color;", h1_element)
    # rgb(144, 238, 144)
    # rgb(255, 0, 0)
    assert bg_color_s1 == "rgb(0, 0, 0)"
    assert tx_color_s2 == "rgb(0, 0, 0)"
    # rgb(0, 0, 0)

    teardown(driver)

def setup():
    options = Options()
    options.add_argument("--user-data-dir=/tmp/chrome_user_data")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000")
    return driver

def teardown(driver):
    driver.quit()

if __name__ == "__main__":
    test_two_buttons()
