from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


import csv  # imnportiere csv Liste

Data = [] # neue Liste

with open('/Users/freddy/Desktop/Monetcard Python/src/TabelleMonet.csv', 'r') as csv_file: # alte Liste einlesen
  reader = csv.reader(csv_file)
  list1 = list(reader)    # liste anders konfigurieren dass ich leichter bzw sinnvoll auf indizes zugreifen kann ! (liste anstatt reader)
    
  for i in list1: # iterationen über jede zeile 
    first_search = i[0] # werte aus der liste in first_search abspeichern 



  # first_search = list1[0]


#list1 = ['Amazon Sofortbezahlung','Amazon Ratenkauf', 'Asos Ratenkauf']
#first_search = list1[0]


    browser = webdriver.Chrome('/Users/freddy/Desktop/Chromedriver/chromedriver 3')

    browser.get('https://www.google.com')                      # Browser festgelegt

    time.sleep(1)

    consent_agb = browser.find_element_by_id('L2AGLb')         # Datenschutz zustimmen, wenn dies nicht angezeigt wird kann dies auskommentiert werden
    consent_agb.send_keys(Keys.RETURN)

    time.sleep(2)

    search_input = browser.find_element_by_name('q')            # Suchfeld anwählen und eingeben 
    search_input.send_keys(first_search)

    time.sleep(2)

    search_enter = browser.find_element_by_css_selector('input[type="submit"]')     # submit drücken
    search_enter.send_keys(Keys.RETURN)

    #time.sleep(2)

    #heading3 = browser.find_element_by_class_name('LC20lb DKV0Md')
    #heading3.send_keys(Keys.RETURN)

    # try:
      #  main = WebDriverWait(browser, 10).until(                # webdriver = chrome, wait maximum 10 sek for ID:... till loaded
      #     EC.presence_of_element_located((By.XPATH, "//div[@class='yuRUbf']/h3))
        #    )
        #print(main.text)

        #divs = main.find_elements_by_tag_name('div')
        #for div in divs:
        #   header = divs.find_elements_by_class_name('LC20lb DKV0Md')
          #  print(header.text) # ERROR siehe Stack Overflow


    #finally:             # finally = no matter what, quit // except = if it doesn't work, quit
    time.sleep(2)
    browser.quit()


    Data.append([first_search , 'url' , 'h3']) # variable des google ergebnisses eifügen für url  # erweitere Data Liste um ergebnisse

with open('/Users/freddy/Desktop/Monetcard Python/src/NewTabelleMonet.csv', 'w') as new_file: # wenn fertig, neue csv wird erstellt   
  csv_writer = csv.writer(new_file, delimiter=',') # erstelle writerobjekt (ich schreibe jetzt)
  for line in Data:     # iteration über neue zeilen (= neue zeilen entsprechen anzahl alten zeilen)
    csv_writer.writerow(line) # schreibe für jede zeile in neue csv datei

    print(line)





# <input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Suche" value="" aria-label="Suche" data-ved="0ahUKEwiWl_zMxIjyAhWiWhUIHdZLClgQ39UDCAc">
# <input class="gNO89b" value="Google Suche" aria-label="Google Suche" name="btnK" type="submit" data-ved="0ahUKEwiWl_zMxIjyAhWiWhUIHdZLClgQ4dUDCA4">

# <cite class="iUh30 Zu0yb qLRx3b tjvcx">https://www.amazon.de<span class="dyjrff qzEoUe"> › Finanzierung</span></cite> // URL bei Suchergebnis 
# <h3 class="LC20lb DKV0Md">Finanzierung : Amazon.de</h3> // Titel bei Suchergebnis
