from selenium.webdriver import Firefox
from time import sleep 

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Firefox()
browser.get(url)
sleep(3)

# MODO 1:

# ---------------------------------------------------------
h1 = browser.find_element_by_tag_name('h1').text
ps = browser.find_elements_by_tag_name('p')
dct = {}

for p in ps:
    dct.update({p.get_attribute('atributo'): p.text})

print({h1: dct})


browser.quit()

# ---------------------------------------------------------
'''
MODO 2:

# ---------------------------------------------------------

h1 = browser.find_element_by_tag_name('h1').text
ps = browser.find_elements_by_tag_name('p')
dct = {}

for p in ps:
    dct[p.get_attribute('atributo')] = p.text

print({h1: dct})

browser.quit()

# -------------------------------------------------------

MODO 3

# ---------------------------------------------------------

h1 = browser.find_element_by_tag_name('h1').text
ps = browser.find_elements_by_tag_name('p')
attrs = []
texts = []

for p in ps:
    attrs.append(p.get_attribute('atributo'))

for p in ps:
    texts.append(p.text)


print({h1: dict(zip(attrs, texts))})

browser.quit()

'''