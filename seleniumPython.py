from selenium import webdriver
url = 'http://uat-iqrashopingdemo.ml/'
driver_path = "C:\\Users\\takia\Desktop\\workspace_python\\ui_iqrashopping\\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get(url)
print(driver.title)
expected_title="Iqra shoping Demo"
actual_title=driver.title
assert expected_title==actual_title, "title is not maching"