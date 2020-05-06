"""
1. PEGAR TODOS OS LINKS DE AULAS
    -   {'nome da aula': 'link da aula'}
2. NAVEGAR ATÉ O EXERCÍCIO 3
    -   achar a url do exercício 3 e ir até lá
"""

from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

url = 'https://selenium.dunossauro.live/aula_04.html'

browser = Firefox()
browser.get(url)

sleep(10)

def get_links(browser, elemento):
    """
    PEGA TODOS OS LINKS DENTRO DE UM ELEMENTO 
        - browser = instância do navegador
        - elemento = webelement [aside, main, body, ul, ol]
    """
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado

"""
PARTE 1

########################

aside = browser.find_element_by_tag_name('aside')
aside_acoras= aside.find_elements_by_tag_name('a')

resultado_1 = {}

for acora in aside_acoras:
    resultado_1[acora.text] = acora.get_attribute('href')

pprint(resultado_1)

## --> browser.get(resultado_1['Aula 3'])  iria para a pagina da aula 3

########################

PARTE 2

########################

main = browser.find_element_by_tag_name('main')
main_links = main.find_elements_by_tag_name('a')

resultado_2 = {}

for acora in main_links:
    resultado_2[acora.text] = acora.get_attribute('href')

pprint(resultado_2)

######################
"""

pprint(get_links(browser, 'aside'))  # PARTE 1

exercicios = get_links(browser, 'main')  # PARTE 2
browser.get(exercicios['Exercício 3'])  # PARTE 2