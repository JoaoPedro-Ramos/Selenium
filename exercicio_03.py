from selenium.webdriver import Firefox
from time import sleep 
from urllib.parse import urlparse

browser = Firefox()

browser.get('https://selenium.dunossauro.live/exercicio_03.html')
sleep(5)

def get_links(browser, elemento):

    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado

sleep(5)
main = get_links(browser, 'main')
sleep(3)
print(main)
browser.get(main['Começar por aqui'])

sleep(3)

ps = browser.find_elements_by_tag_name('p')
conta = (ps[1].text).split()
resultado = int(conta[0]) * int(conta[2])

sleep(3)

lis = get_links(browser, 'main')
for l in lis:
    if int(l) != resultado:
        browser.get(lis[l])

sleep(60)

titulo = browser.title
main_ = get_links(browser, 'main')
browser.get(main_[titulo])

sleep(5)

urlparseada = urlparse(browser.current_url)
path = urlparseada.path
MAIN = get_links(browser, 'main')
for m in MAIN:
    if m in path:
            browser.get(MAIN[m])

sleep(5)

browser.refresh()
