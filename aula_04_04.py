from selenium.webdriver import Firefox
from urllib.parse import urlparse

url = 'https://selenium.dunossauro.live/aula_04_b.html'

browser = Firefox()
browser.get(url)


urlparseada = urlparse(browser.current_url)
print(urlparseada)
