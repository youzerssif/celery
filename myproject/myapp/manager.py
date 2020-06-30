from django.shortcuts import render
import requests
from requests import get
from bs4 import BeautifulSoup
import json
from django.http import JsonResponse
# Create your views here.

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
    
    