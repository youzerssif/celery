from django.shortcuts import render
import requests
from requests import get
from bs4 import BeautifulSoup
import json, demjson
from django.http import JsonResponse
# Create your views here.


# Récuperation des categories sur le site
def cat_api():

    url = 'https://www.zalando.fr/accueil-homme/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    mydata = []
    
    if response.status_code == 200:
        div_module = html_soup.find('script', attrs = {'id':'z-navicat-header-props'}, type='application/json')
        data_to_python_json = div_module.contents[0].replaceWith("")
        
        d = data_to_python_json.strip('<![CDATA[').strip(']>')
        datas = json.loads(d)
        
        # print()
        # print(de)
        c = datas['model']['topnavi']['children'][2]['children']
        # print(c)
        
        mydata.append(c)
        # print(mydata)
    else:
        print('erreur statut',status_code)
    return mydata

# class SrcpCollection:
#     def __init__(self):
#         super().__init__()
        
#     def getUrl(self):
#         url = 'https://www.zalando.fr/accueil-homme/'
#         headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
        
#         req = requests.get(url,headers=headers)
#         print("redirect",req.url, req.is_redirect)
#         status = False
#         soup = ""
#         if req.status_code == 200:
#             html_doc = req.text
#             soup = BeautifulSoup(html_doc, 'html.parser')
#             status = True
#         return status, soup

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
        
        for key in datas.keys(): 
            if "ern:collection" in key:
                try:
                    contdata = datas[key]['data']['collection']
                    titre = contdata['title']
                    
                    if "https://www.zalando.fr/collections/" in contdata['uri']:
                        # print("ok")
                        url_valide =  contdata['uri']
                        # mydata.append(url_valide)
                        print(url_valide)
                        url = url_valide
                        # print(url)

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
                                        # print(contdata)
                                        mydata.append(contdata)
                                    except:
                                        pass
                        else:
                            print('erreur statut',status_code)
                        return JsonResponse(data=mydata, safe=False)
                    elif not "https://www.zalando.fr/collections/" in contdata['uri']:
                        print('les autres liens')
                        other = contdata['uri']
                    else:
                        pass
                    # urlCollections = urlCollection
                except Exception as e:
                    print(str(e))
    else:
        print('erreur statut',response.status_code)
    return url_valide

## Fonctions pour récuperer les données d'une collection
def data_collection(request):
    
    url = collection_api()
    print(url)

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
                    # print(contdata)
                    mydata.append(contdata)
                except:
                    pass
    else:
        print('erreur statut',status_code)
    return JsonResponse(data=mydata, safe=False)