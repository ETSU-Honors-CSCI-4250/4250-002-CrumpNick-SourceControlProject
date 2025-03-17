from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get("http://localhost:3000")
    # assert "4250 Honors Project" in driver.title

    s1_button = driver.find_element(by=By.ID, value="s1")
    s2_button = driver.find_element(by=By.ID, value="s2")
    h1_element = driver.find_element(by=By.TAG_NAME, value="h1")
    
    s1_button.click()
    bg_color_s1 = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor;")
    s2_button.click()
    tx_color_s2 = driver.execute_script("return window.getComputedStyle(arguments[0]).color;", h1_element)
    # rgb(144, 238, 144)
    # rgb(255, 0, 0)
    assert bg_color_s1 == "rgb(144, 238, 144)"
    assert tx_color_s2 == "rgb(255, 0, 0)"
    # rgb(0, 0, 0)

finally:
    driver.quit()

