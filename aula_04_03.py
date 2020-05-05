from selenium.webdriver import Firefox
from time import sleep

def find_by_text(browser, tag, text):
    elements = browser.find_elements_by_tag_name(tag)
    for element in elements:
        if element.text == text:
            return element

url = 'https://selenium.dunossauro.live/aula_04_b.html'

browser = Firefox()
browser.get(url)

box_names = ['um', 'dois', 'tres', 'quatro']

for name in box_names:
    find_by_text(browser, 'div', name).click()

for name in box_names:
    sleep(0.2)
    browser.back()

for name in box_names:
    sleep(0.2)
    browser.forward()

sleep(3)