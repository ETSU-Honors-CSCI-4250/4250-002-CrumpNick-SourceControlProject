from selenium import webdriver
from selenium.webdriver.common.by import By


def test_two_buttons():
    driver = setup()

    title = driver.title
    assert title == "4250 Honors Project"

    driver.implicitly_wait(0.5)

    s1_button = driver.find_element(by=By.ID, value="s1")
    s2_button = driver.find_element(by=By.ID, value="s2")
    
    s1_button.click()
    bg_color_s1 = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor;")
    s2_button.click()
    tx_color_s2 = driver.execute_script("return window.return window.getComputedStyle(arguments[0]).color;", h1_element)
    #rgb(144, 238, 144)
    print(bg_color_s1)
    print(tx_color_s2)
    assert bg_color_s1 == "rgb(0, 0, 0)", f"S1 background color mismatch! Found: {bg_color_s1}"
    assert tx_color_s2 == "rgb(0, 0, 0)", f"S2 text color mismatch! Found: {bg_color_s2}"

    teardown(driver)

def setup():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000")
    return driver

def teardown(driver):
    driver.quit()
