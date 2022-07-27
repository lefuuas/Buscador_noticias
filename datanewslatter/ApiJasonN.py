
from email.headerregistry import Address
from bs4 import BeautifulSoup
from matplotlib.pyplot import setp
from Componets.textcorection import corrigirtxt
import requests
import os
from Componets.resumidor import resumidor


def Api(addrs, classnamed, atribut):
    resp = 0
    step = []
    links = []
    vfcode = []
    while True:
        os.system('clear')
        print('restarful')

        response = requests.get(addrs)
        print('teste de requisiçao')
        soup = BeautifulSoup(response.content, 'html.parser')
        noticia = soup.find_all(f'{atribut}', attrs={'class': f'{classnamed}'})
        for notcies in noticia:
            print('teste de buscar noticias')
            for link in notcies.find_all('a'):
                verificate = link.get('href')
                print('Teste de encontra links')
                if verificate in vfcode:
                    os.system('clear')
                    print('Buscando Novas Noticias')
                    return step


                else:

                        links.append(link.get('href'))
                        vfcode.append(link.get('href'))
                        cont = 0
                        for paragrafos in links:
                            tt = requests.get(paragrafos)
                            site = BeautifulSoup(tt.content, 'html.parser')
                            finalytext =''
                            cont+= 1
                            for texto in site.find_all('p'):
                                formattext = texto.get_text()
                                resumer = formattext.strip()
                                ok = str(resumer)
                                finalytext += ok.replace('None', '') + '\n'
                            
                        finalytext = resumidor(finalytext) + '\n'
                        al=corrigirtxt(finalytext)
                        step.append(al)
                        print(f'resp atual {resp}')
                        resp += 1
                    
                                



                    
                        



                           