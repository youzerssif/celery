from django.shortcuts import render
import requests
from requests import get
from bs4 import BeautifulSoup
import json
from django.http import JsonResponse
# Create your views here.


# Récuperation des categories sur le site
def cat_api(request):

    url = 'https://www.zalando.fr/accueil-homme/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        
        div_module = html_soup.find('script', attrs = {'id':'z-navicat-header-props'}, type='application/json')
        data_to_python_json = div_module.contents[0].replaceWith("")
        
        d = data_to_python_json.strip('<![CDATA[').strip(']>')
        datas = json.loads(d)
        
        # print()
        # print(de)
        c = datas['model']['topnavi']['children'][2]['children']
        
        mydata = []
        mydata.append(c)
    else:
        print('erreur statut',status_code)
    return JsonResponse(mydata, safe=False)

# Fonction pour récuperer le lien des collections
def collection_api(request):
    url = 'https://www.zalando.fr/accueil-homme/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        div_module = html_soup.find('script', attrs = {'class':'re-data-el-hydrate'}, type='application/json')
        data_to_python_json = div_module.contents[0].replaceWith("")
        
        datas =json.loads(data_to_python_json)
        datas = datas['graphqlCache']
        mydata = []
        mydatas = []
        for key in datas.keys(): 
            if "ern:collection" in key:
                try:
                    contdata = datas[key]['data']['collection']
                    urlCollection = contdata['uri']
                    titre = contdata['title']
                    
                    # print(titre)
                    mydata.append(urlCollection)
                    print(urlCollection)
                        
                        # urldata = m
                        # # print(urldata)
                        # header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
                        # responses = get(urldata,headers=header)

                        # html_soups = BeautifulSoup(responses.text, 'html.parser')

                        # if responses.status_code == 200:
                            
                        #     div_module = html_soups.find('script', attrs = {'class':'re-data-el-hydrate'}, type='application/json')
                        #     data_to_python_json = div_module.contents[0].replaceWith("")
                        #     datas =json.loads(data_to_python_json)
                        #     datas = datas['graphqlCache']
                            
                        #     for key in datas.keys(): 
                        #         if "ern:product" in key:
                        #             try:
                        #                 contdata = datas[key]['data']['product']
                        #                 mydatas.append(contdata)
                        #             except:
                        #                 pass
                        # else:
                        #     print('erreur statut',status_code)
                        # return JsonResponse(mydatas, safe=False)
                except Exception as e:
                    print(str(e))
    else:
        print('erreur statut',response.status_code)
    return JsonResponse(mydatas, safe=False)

## Fonctions pour récuperer les données d'une collection
def data_collection(request):
    
    url = 'https://www.zalando.fr/collections/cIjAWB_QQ6q/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        
        div_module = html_soup.find('script', attrs = {'class':'re-data-el-hydrate'}, type='application/json')
        data_to_python_json = div_module.contents[0].replaceWith("")
        datas =json.loads(data_to_python_json)
        datas = datas['graphqlCache']
        mydata = []
        for key in datas.keys(): 
            if "ern:product" in key:
                try:
                    contdata = datas[key]['data']['product']
                    mydata.append(contdata)
                except:
                    pass
    else:
        print('erreur statut',status_code)
    return JsonResponse(mydata, safe=False)