from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
#url = 'https://www.facilitron.com/searchfacility/u:facilitron/lat:37.8271784/lng:-122.2913078/dist:20/activities:-1/types:-1/namelike:grass%20field'
url = 'https://www.facilitron.com/'
driver = webdriver.Chrome(PATH)

driver.get(url)
# title = driver.find_elements_by_class_name("facility-header search-link")

search_facility = driver.find_element_by_id("facilityActivitySearchBox")
search_facility.send_keys("grass field")
search_city = driver.find_element_by_id("searchLocationField")
search_city.send_keys("San Francisco CA, USA")
time.sleep(1)
search_city.send_keys(Keys.ARROW_DOWN)
search_city.send_keys(Keys.ENTER)

time.sleep(2)

location = driver.find_elements_by_class_name("search-link")

# for i in title:
#     print(i.text)


for i in location:
    print(i.text)

text = [x.text for x in location]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'location'])
    writer.writerow(text)

time.sleep(10000)

driver.quit()
