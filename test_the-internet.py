from selenium.webdriver.common.by import By
from selenium import webdriver
from automation.common import CommonOps

def test_ab_two_variations(driver):
    text_list = []
    expected_list = ['A/B Test Control', 'A/B Test Variation 1']
    count = 0

    ops = CommonOps(driver)
    ops.click_link_by_text("A/B Testing")
    while len(text_list) < 2 and count < 10:
        h3 = driver.find_element(by=By.TAG_NAME, value="h3")
        if len(text_list) > 0 and text_list[0] != h3.text:
            text_list.append(h3.text)
            driver.quit()
            break
        elif len(text_list) == 0: 
            text_list.append(h3.text)
        driver.delete_all_cookies()
        driver.refresh()
        count += 1

    difference = set(text_list) ^ set(expected_list)
    assert not difference