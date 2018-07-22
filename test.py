import os
import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome()
    driver.get("https://serbia.levi9.jobs/open-positions/?location_id=29&role_id=7")
    driver.find_element_by_xpath('//*[@id="junior-test-developer"]/div/div/div[3]/div[1]/a').click()
    try:
        fillingTheName = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="apply-form"]/form/div[2]/div[1]/input'))
        )
    except:
        driver.quit()
    # write user name
    fillingTheName.send_keys('Andjela')
    # write surname
    driver.find_element_by_xpath('//*[@id="apply-form"]/form/div[2]/div[2]/input').send_keys('Pajic')
    # write email
    driver.find_element_by_xpath('//*[@id="apply-form"]/form/div[3]/div[1]/input').send_keys('andjela.pajic90@gmail.com')
    # write phone number
    driver.find_element_by_xpath('//*[@id="apply-form"]/form/div[3]/div[2]/input').send_keys('0638879132')
    # upload cover letter
    driver.find_element_by_xpath('//*[@id="apply-form"]/form/div[4]/div[2]/div/input').send_keys(os.getcwd() + "\Cover Letter Levi9.doc")
    # upload CV
    driver.find_element_by_xpath('//*[@id="apply-form"]/form/div[4]/div[3]/div/input').send_keys(os.getcwd() + "\Andjela Pajic CV.pdf")
    # choosing the option
    driver.find_element_by_xpath('//*[@id="howdidyoufindthisjobposition"]').click()
    driver.find_element_by_xpath('//*[@id="howdidyoufindthisjobposition"]/option[3]').click()
    # write comment in Text Area
    driver.find_element_by_xpath('//*[@id="apply-form"]/form/div[4]/div[6]/textarea').send_keys('Automatizacija procesa apliciranja za poziciju Junior Test Developer')
    # wait until popup iframe is present
    try:
        popupIframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="dialog_iframe"]'))
        )
    except:
        driver.quit()
    driver.switch_to_frame(popupIframe)
    #closing popup
    driver.find_element_by_xpath('//*[@id="u_0_0"]/div/div/span/div/div[1]/div[3]/div').click()
    driver.switch_to_default_content()
  
    driver.save_screenshot('applicationForm.png')




except:
    traceback.print_exception(*exc_info)
    del exc_info
