from django.shortcuts import render

# Create your views here.
import requests
from requests import get
from bs4 import BeautifulSoup
import json
from django.http import JsonResponse


def home(request):
    


    url = 'https://www.zalando.fr/accueil-femme/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        
        print('okkokokookoko')
        # print(html_soup.prettify())
        
        div_module = html_soup.find('script', attrs = {'class':'re-data-el-hydrate'}, type='application/json')
        # data = json.loads(div_module.text)
        data_to_python_json = div_module.contents[0].replaceWith("")
        # print(data,"zjncldncze")
        
        datas =json.loads(data_to_python_json)
        # print(datas)
       


    else:
        print('erreur statut',status_code)
    print(div_module)
    data={
        'datas':datas,
    }
    return render(request, 'home.html',data)


def json_api(request):


    url = 'https://www.zalando.fr/accueil-homme/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        
        # print('okkokokookoko')
        # print(html_soup.prettify())
        
        div_module = html_soup.find('script', attrs = {'class':'re-data-el-hydrate'}, type='application/json')
        # data = json.loads(div_module.text)
        data_to_python_json = div_module.contents[0].replaceWith("")
        # print(data,"zjncldncze")
        
        datas =json.loads(data_to_python_json)
        datas = datas['graphqlCache']
        
        # print()
        # print(datas)
        mydata = []
        for key in datas.keys(): 
            if "ern:product" in key:
                try:
                    contdata = datas[key]['data']['product']
                    # print(contdata)
                    mydata.append(contdata)
                    
                except:
                    pass
       

        
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
    return JsonResponse(mydata, safe=False)
    
    
def json_mode_homme(request):


    url = 'https://www.zalando.fr/mode-homme/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        
        # print('okkokokookoko')
        # print(html_soup.prettify())
        
        div_module = html_soup.find('script', id ="z-nvg-cognac-props", type='application/json')
        # data = json.loads(div_module.text)
        data_to_python_json = div_module.contents[0].replaceWith("")
        # print(data,"zjncldncze")

        data = json.loads(data_to_python_json.strip('<![CDATA[').strip(']>'))
        print(data)
        # data = datas['graphqlCache']
            
        # # print()
        # # print(datas)
        # mydata = []
        # for key in data.keys(): 
        #     print(key)
            # if "ern:product" in key:
            #     try:
            #         contdata = datas[key]['data']['product']
            #         # print(contdata)
            #         mydata.append(contdata)
                    
            #     except:
        #         pass

    else:
        print('erreur statut',status_code)
    return JsonResponse(data, safe=False)
    