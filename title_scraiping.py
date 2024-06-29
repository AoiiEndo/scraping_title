from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

options = webdriver.ChromeOptions() #webdriverの起動
# options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options = options)
url = '---'
driver.get(url)

driver.implicitly_wait(10)

titles =[]

try:
    for i in range(1, 100):
        if(i >= 2):
            click_area = driver.find_element(By.XPATH, '//main/div[2]/div/div[2]/div/button[2]')
            click_area.click()
        for j in range(1,10):
            title_position = driver.find_element(By.XPATH, '//main/div[2]/div/article['+str(j)+']/h2/a').text
            titles.append(title_position)
    data = np.vstack(titles)
    df = pd.DataFrame(data, columns=[1])
    df['titles'] = titles
    csv_filename = "---.csv"
    df.to_csv(csv_filename, index=False)
except Exception as e:
    print(e)