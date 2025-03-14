'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("../simple.html")

title = driver.title

driver.implicitly_wait(1)


s1_button = driver.find_element(by=By.ID, value="s1")
s1_button.click()

bg_color_s1 = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor;")
assert bg_color_s1 == "rgb(144, 238, 144)", f"S1 background mismatch! Found: {bg_color_s1}"

s2_button = driver.find_element(by=By.ID, value="s2")
s2_button.click()

bg_color_s2 = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor;")
assert bg_color_s2 == "rgb(255, 0, 0)", f"S2 background mismatch! Found: {bg_color_s2}"

print("All tests passed successfully!")
driver.quit()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    driver = setup()

    title = driver.title
    assert title == "Web form"
    # assert title == "4250 Honors Project"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    # s1_button = driver.find_element(by=By.ID, value="s1")
    # s2_button = driver.find_element(by=By.ID, value="s2")
    
    '''
    s1_button.click()
    
    bg_color_s1 = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor;")
    assert bg_color_s1 == "rgb(144, 238, 144)", f"S1 background mismatch! Found: {bg_color_s1}"
    
    s2_button.click()
    '''
    
    text_box.send_keys("Selenium")
    submit_button.click()
    # s1_button.click()
    # bg_color_s1 = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor;")
    # s2_button.click()
    #bg_color_s2 = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor;")
    
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
    # assert bg_color_s1 == "rgb(144, 238, 144)", f"S1 background mismatch! Found: {bg_color_s1}"
    # assert bg_color_s2 == "rgb(255, 0, 0)", f"S2 background mismatch! Found: {bg_color_s2}"

    teardown(driver)

def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    # driver.get("http://localhost:8000")
    return driver

def teardown(driver):
    driver.quit()
