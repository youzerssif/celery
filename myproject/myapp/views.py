from django.shortcuts import render

# Create your views here.
import requests
from requests import get
from bs4 import BeautifulSoup
import json
from django.http import JsonResponse


def home(request):
    


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
        # print(datas)
        datas = datas['graphqlCache']
        
        mydata = []
        for key in datas.keys(): 
            if "ern:product" in key:
                try:
                    contdata = datas[key]['data']['context']
                    # print(contdata)
                    mydata.append(contdata)
                    
                except:
                    pass
        return JsonResponse(datas, safe=False)


    else:
        print('erreur statut',response.status_code)
   

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


    url = 'https://www.zalando.fr/homme/?camp=mu_sneaker_releases'

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
            try:
                next_page = html_soup.find_all('li', attrs={'class':'cat_item-25ZBj'})[2]
                next_page = url + next_page.find('a', {'class': 'cat_link-8qswi'}).get('href')
                # c = json_mode_homme(next_page)
                # print(next_page)
            except Exception as e:
                print(str(e))
                
            # print(data)
            for item in data['content']['brands']['brands']:
                mydata.append(item)
                # print(item)
            # data = data['articles']
            return JsonResponse(mydata, safe=False)
            
                    
        except Exception as e:
            print(str(e))
            
        try:
            div_module = html_soup.find('script', id ="z-nvg-cognac-props", type='application/json')
            # data = json.loads(div_module.text)
            data_to_python_json = div_module.contents[0].replaceWith("")
            # print(data_to_python_json.replace('<![CDATA[','').replace(']>',''),"zjncldncze") z-nvg-cognac-props"

            mydata = json.loads(data_to_python_json.replace('<![CDATA[','').replace(']]>',''))

            mydata = mydata['articles']
            # print(mydata)
            try:
                next_page = html_soup.find_all('li', attrs={'class':'cat_item-25ZBj'})[2]
                next_page = url + next_page.find('a', {'class': 'cat_link-8qswi'}).get('href')
                # print(next_page)
                # c = json_mode_homme(next_page)
                # print(c)
            except Exception as e:
                print(str(e))
            

            return JsonResponse(mydata, safe=False)

        except Exception as e:
            print(str(e))

    else:
        print('erreur statut',response.status_code)
    

def json_detail_article(request):
    
    url = 'https://www.zalando.fr/outfits/nFbqYN8fRCK/'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        
        try:
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
                        # break
                        mydata.append(contdata)
                        # print(mydata)
                        # break
                        
                    except:
                        pass
                    
            return JsonResponse(datas, safe=False)
        except Exception as e:
            print(str(e))
        
        try:
            div_module = html_soup.find('script', id ="z-vegas-shipping-props", type='application/json')
            # data = json.loads(div_module.text)
            data_to_python_json = div_module.contents[0].replaceWith("")

            articleInfo = json.loads(data_to_python_json.strip('<![CDATA[').strip(']>'))
            

            mydata = []
            for key in articleInfo.keys(): 
                if "ern:product" in key:
                    try:
                        contdata = articleInfo[key]['data']['product']
                        # print(contdata)
                        mydata.append(contdata)
                        
                    except:
                        pass
            return JsonResponse(mydata, safe=False)
                        
        except Exception as e:
            print(str(e)) 
        
        
    else:
        print('erreur statut',response.status_code)
    
