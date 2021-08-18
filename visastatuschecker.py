import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pushsafer import init, Client
import dateutil.parser as dparser
import datetime
import os
import re

def login():
    driver = webdriver.Chrome(r'C:\Users\lpenatre\Downloads\chromedriver.exe')
    driver.minimize_window()
    driver.get("https://pastel.diplomatie.gouv.fr/VisaNET-Consultation-Internet/html/frameset/frameset.html")
    driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "BODY_WIN"))))
    sleep(5)
    driver.execute_script("parent.parent.ComposantMenuFrameset.SelectItem2Menu1(0,0,false)")
    driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "CONTENU_WIN"))))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "numero_quittance"))).send_keys("MEX202121600032")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nele1"))).send_keys("1998")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nele2"))).send_keys("06")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nele3"))).send_keys("30")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bouton_valider_link"))).click()
    return driver


def check_for_appts():
    init("kWHKzMacTKjIUKLinMJ1")
    try:
        driver = login()
        while True:
            try:
                sleep(4)
                if ("Your visa application is still being processed." in driver.find_element_by_id("description_fiche").text):
                    print("Aun no :/")
                else:
                    raise TimeoutException
            except TimeoutException:
                Client("41943").send_message("Ya se actualizo!", "Abreme", "41943", "1", "0", "3", "https://pastel.diplomatie.gouv.fr/VisaNET-Consultation-Internet/html/frameset/frameset.html", "Abremex2", "0", "2", "60", "600", "1", "", "", "")
                input("Press ENTER to continue.")
            sleep(600)
            driver.refresh()
            driver.minimize_window()
            driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "BODY_WIN"))))
            driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "CONTENU_WIN"))))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "numero_quittance"))).send_keys("MEX202121600032")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nele1"))).send_keys("1998")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nele2"))).send_keys("06")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nele3"))).send_keys("30")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bouton_valider_link"))).click()
    except TimeoutException:
        driver.quit()
        check_for_appts()

check_for_appts()