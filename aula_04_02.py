from selenium.webdriver import Firefox

def find_by_text(browser, tag, text):
    '''
        ENCONTRAR O ELEMENTO COM O TEXTO: TEXT

        Argumentos: 
            - browser = Instância do browser [Firefox, Chrome...]
            - texto = Conteúdo que deve estar na tag
            - tag = Tag onde o texto será procurado
    '''

    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento

    
def find_by_href(browser, link):
    '''
        ENCONTRAR O ELEMENTO COM A COM O LINK: LINK

        Argumentos: 
            - browser = Instância do browser [Firefox, Chrome...]
            - link = Link que será procurado em todas as tags 'a'
    '''
    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser = Firefox()
browser.get(url) 


# elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')

elemento_ddg = find_by_href(browser, 'ddg')

print(elemento_ddg.text)
print(elemento_ddg.get_attribute('href'))
browser.quit()