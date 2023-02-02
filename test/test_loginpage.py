import time

import pytest
from selenium import webdriver


@pytest.fixture()
def test_setup():
    global driver
    url = "http://uat-iqrashopingdemo.ml/"
    driver_path = "C:\\Users\\takia\\Desktop\\workspace_python\\ui_iqrashopping\\chromedriver.exe"
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    driver.implicitly_wait(10)

    yield
    driver.close()
    driver.quit()


def test_login(test_setup):
    username = "//*[@id='username-9']"
    password = "//*[@id='user_password-9']"
    login = "//*[@id='um-submit-btn']"
    time.sleep(3)
    driver.find_element_by_xpath(username).send_keys("Test_user2023")
    time.sleep(3)
    driver.find_element_by_xpath(password).send_keys("Test_user2023")
    time.sleep(3)
    driver.find_element_by_xpath(login).click()
    title = driver.title
    actual_title = "Test User | Iqra shoping Demo"
    assert title == actual_title
    driver.save_screenshot("image.png")


def test_login2(test_setup):
    username = "//*[@id='username-9']"
    password = "//*[@id='user_password-9']"
    login = "//*[@id='um-submit-btn']"
    time.sleep(3)
    driver.find_element_by_xpath(username).send_keys("Test_user2023")
    time.sleep(3)
    driver.find_element_by_xpath(password).send_keys("Test_user2023")
    time.sleep(3)
    driver.find_element_by_xpath(login).click()
    title = driver.title
    actual_title = "Test User | Iqra shoping Demo"
    assert title == actual_title
    driver.save_screenshot("image.png")

# def test_closebrowser():
#     driver.close()
#     driver.quit()
