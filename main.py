from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


import csv      # importiere csv Liste

Data = []       # neue Liste

with open('/Users/freddy/Desktop/Monetcard Python/src/TabelleMonet.csv', 'r') as csv_file:       # alte Liste einlesen
  reader = csv.reader(csv_file)
  list1 = list(reader)               # Liste anders konfigurieren sodass ich leichter bzw sinnvoll auf Indizes zugreifen kann (Liste anstatt reader)
    
  for i in list1:          # Iterationen über jede Zeile 
    first_search = i[0]          # Werte aus der liste in first_search abspeichern 



    browser = webdriver.Chrome('/Users/freddy/Desktop/Chromedriver/chromedriver 3')

    browser.get('https://www.google.com')                         # Browser festgelegt

    time.sleep(1)

    consent_agb = browser.find_element_by_id('L2AGLb')         # Datenschutz zustimmen, wenn dies nicht angezeigt wird kann es auskommentiert werden
    consent_agb.send_keys(Keys.RETURN)

    time.sleep(2)                             # time.sleep = warten bis Seite vollständig geladen

    search_input = browser.find_element_by_name('q')            # Suchfeld anwählen und eingeben 
    search_input.send_keys(first_search)

    time.sleep(2)

    search_enter = browser.find_element_by_css_selector('input[type="submit"]')        # submit drücken
    search_enter.send_keys(Keys.RETURN)

    time.sleep(3)

    h3_headings = browser.find_elements_by_xpath('//h3')      #  h3 Element aufrufen 
    title =  h3_headings[0].text                            # Text des ersten Elementes aus der Ergebnisseite als Variable definieren

    url_first_element = browser.find_element_by_xpath('//cite')   #  cite Element aufrufen 
    url = url_first_element.text                              # Text des Ersten Elementes aus der Ergebnisseite als Variable definieren


    Data.append([first_search , url , title])                  # erweitere Data Liste um Suchergebnisse

with open('/Users/freddy/Desktop/Monetcard Python/src/NewTabelleMonet.csv', 'w') as new_file:             # wenn fertig, wird neue csv erstellt   
  csv_writer = csv.writer(new_file, delimiter=',')                     # erstelle writerobjekt (ich schreibe jetzt)
  for line in Data:                         # Iteration über neue Zeilen (= neue Zeilen entsprechen Anzahl alten Zeilen)
    csv_writer.writerow(line)               # schreibe für jede Zeile in neue csv Datei



   # im Optimalfall stehen die gegoogelten Begriffe neben den dazugehörenden Ergebnissen und URL's in einer Liste


