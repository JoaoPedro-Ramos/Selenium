from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser = Firefox()
browser.get(url)

sleep(3)

lista_nao_ordenada = browser.find_element_by_tag_name('ul')
item = lista_nao_ordenada.find_elements_by_tag_name('li')

browser.quit()