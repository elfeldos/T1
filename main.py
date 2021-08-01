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

    time.sleep(2)

    search_input = browser.find_element_by_name('q')            # Suchfeld anwählen und eingeben 
    search_input.send_keys(first_search)

    time.sleep(2)

    search_enter = browser.find_element_by_css_selector('input[type="submit"]')        # submit drücken
    search_enter.send_keys(Keys.RETURN)


    try:          # get url 
      url = WebDriverWait(browser, 10).until(              # Browser wartet bis Css Selektor angewendet werden kann 
        EC.presence_of_element_located((By.CSS_SELECTOR, "cite.iUh30.Zu0yb.qLRx3b.tjvcx"))             # Css Selektor für class in der der Text steht -> wie kann ich aus dem Element den Text extrahieren ?
    )
    except:
      browser.quit

    try:          # get title
      title = WebDriverWait(browser, 10).until(               # browser wartet bis css selektor angewendet werden kann 
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3.LC20lb.DKV0Md"))                # Css Selektor für class in der der text steht -> wie kann ich aus dem Element den Text extrahieren ?
    )
    except:                   # finally = no matter what, quit // except = if it doesn't work, quit
      browser.quit            # Browser wird nach der Suche jedes einzelnen Begriffs beendet (und danach wieder gestartet)


    Data.append([first_search , url , title])                  # erweitere Data Liste um Suchergebnisse

with open('/Users/freddy/Desktop/Monetcard Python/src/NewTabelleMonet.csv', 'w') as new_file:             # wenn fertig, wird neue csv erstellt   
  csv_writer = csv.writer(new_file, delimiter=',')                     # erstelle writerobjekt (ich schreibe jetzt)
  for line in Data:                         # Iteration über neue Zeilen (= neue Zeilen entsprechen Anzahl alten Zeilen)
    csv_writer.writerow(line)               # schreibe für jede Zeile in neue csv Datei



   # im Optimalfall stehen die gegoogelten Begriffe neben den dazugehörenden Ergebnissen und URL's in einer Liste


