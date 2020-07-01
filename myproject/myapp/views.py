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
        print('erreur statut',response.status_code)
    print(div_module)
    data={
        'datas':datas,
    }
    return render(request, 'home.html',data)

######## elle recupere les datas de la premiere pages ##############  

def json_api(request):


    url = 'https://www.zalando.fr/accueil-homme/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        
        
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
       
    else:
        print('erreur statut',response.status_code)
    return JsonResponse(mydata, safe=False)
    
######## elle recupere les datas des pages categories ##############  
def json_mode_homme(request):

    url = 'https://www.zalando.fr/accueil-luxe-homme/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
            
        try:
                
            div_module = html_soup.find('script', id ="app-props", type='application/json')
            # data = json.loads(div_module.text)
            data_to_python_json = div_module.contents[0].replaceWith("")
            # print(data_to_python_json.replace('<![CDATA[','').replace(']>',''),"zjncldncze")

            data = json.loads(data_to_python_json.replace('<![CDATA[','').replace(']]>',''))
            mydata = []
            # print(data)
            for item in data['content']['brands']['brands']:
                mydata.append(item)
                # print(item)
            # data = data['articles']

                    
        except Exception as e:
            print(str(e))

    else:
        print('erreur statut',response.status_code)
    return JsonResponse(mydata, safe=False)


def json_detail_article(request):
    
    url = 'https://www.zalando.fr/lindbergh-plain-mens-suit-slim-fit-costume-lg522a002-o13.html'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        
        try:
            div_module = html_soup.find('script', attrs = {'class':'re-data-el-hydrate'}, type='application/json')
            data_to_python_json = div_module.contents[0].replaceWith("")
            datas =json.loads(data_to_python_json)
            datas = datas['graphqlCache']
        except Exception as e:
            print(str(e))
        
        try:
            div_module = html_soup.find('script', id ="z-vegas-shipping-props", type='application/json')
            # data = json.loads(div_module.text)
            data_to_python_json = div_module.contents[0].replaceWith("")

            
            
            
            articleInfo = json.loads(data_to_python_json.strip('<![CDATA[').strip(']>'))
            

            mydata = []
            for key in datas.keys(): 
                if "ern:product" in key:
                    try:
                        contdata = datas[key]['data']['product']
                        # print(contdata)
                        mydata.append(contdata)
                        
                    except:
                        pass
                        
        except Exception as e:
            print(str(e)) 
        
        
    else:
        print('erreur statut',response.status_code)
    return JsonResponse(articleInfo, safe=False)