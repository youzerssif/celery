import requests
from requests import get
from bs4 import BeautifulSoup
import json

url = 'https://www.zalando.fr/accueil-femme/'

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
response = get(url,headers=headers)

html_soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:
    
    print('okkokokookoko')
    # print(html_soup.prettify())
    
    div_module = html_soup.find('script', attrs = {'class':'re-data-el-hydrate'}, type='application/json').text
    # data = json.loads(div_module.text)
    data = div_module.lstrip('<![CDATA').rstrip(']>')
    desired_data = dict(data['model']['featureToggles'])
    print(desired_data)
    # source = requests.get("https://en.zalando.de/carhartt-wip-hooded-chase-sweatshirt-c1422s02x-g13.html?_rfl=de").text
    # soup = BeautifulSoup(source, "lxml")
    # scr = soup.find("script", id = "z-vegas-pdp-props").text

    # data = json.loads(scr.lstrip('<![CDATA').rstrip(']>'))
    # desired_data = dict(data['model']['articleInfo'])
    # print(desired_data)
   
    # module = div_module.find_all('div', attrs = {'class':'col-sm-6 col-p10'})
            
    # for item in div_module:
    #     #------------RECUPERATION---------------#  
    #     print(item)      
        # div = item.find('div', attrs = {'class':'col-sm-8 col-8 col-per'})
        # img = item.find('div', attrs = {'class':'col-sm-4 col-4'})
        # #------------AFFECTATION---------------# 
        # a = div.find('a')
        # serv = div.find('span').get_text()
        # imag = img.find('img')
        # image = imag['src']
        # lien = a['href']
        # #------------AFFICHAGE---------------#
        # print(lien)
        # print(image)
        # print(serv)
else:
    print('erreur statut',status_code)