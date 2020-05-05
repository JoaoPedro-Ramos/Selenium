from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_02.html'

browser = Firefox()
browser.get(url)

sleep(4)

a = browser.find_element_by_tag_name('a')
msg = ''

while 'Você ganhou' not in msg:
    a.click()
    msg = browser.find_elements_by_tag_name('p')[-1].text

browser.quit()
