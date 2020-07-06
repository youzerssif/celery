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
        print('erreur statut',response.status_code)
    return JsonResponse(data=mydata, safe=False) 

def catLook(request):
    url = 'https://www.zalando.fr/get-the-look-homme/'
    # https://www.zalando.fr/get-the-look-homme/?styleFilter=style_classic
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    
    req = requests.get(url,headers=headers)
    # print("redirect",req.url, req.is_redirect)
    status = False
    soup = ""
    cnt = 0
    data = []
    if req.status_code == 200:
        html_doc = req.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        try:
            for x in soup.find_all('div'):
                myattrs = x.attrs
                # print(x)
                if 'onclick' in myattrs.keys():
                    data = x
                    cnt += 1
                    datas = myattrs['onclick'].strip('return')
                    d = json.loads(datas)
                    menuLook = d["props"]["filters"][0]['options']
                    for m in menuLook:
                        # Recuperation des liens de categorie de look
                        allStyle = m['label']
                        # print(allStyle)
                        urlda = "https://www.zalando.fr/get-the-look-homme/?styleFilter={}".format(allStyle)
                        print(urlda)
                        
                    

                    break
        except:
            data = None
        status = True
    return JsonResponse(data=d, safe=False)

def look(request):
    url = 'https://www.zalando.fr/get-the-look-homme/?styleFilter=style_classic'
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    
    req = requests.get(url,headers=headers)
    # https://www.zalando.fr/outfits/DQ5B3SZeRDm/
    status = False
    soup = ""
    cnt = 0
    data = []
    if req.status_code == 200:
        html_doc = req.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        try:
            for x in soup.find_all('div'):
                myattrs = x.attrs
                if 'onclick' in myattrs.keys():
                    cnt += 1
                    datas = myattrs['onclick'].strip('return')
                    d = json.loads(datas)
                    keyLook = d["props"]["outfitsById"]
                    for k in keyLook.values():
                        # print(k)
                        titre = k["creator"]["name"]
                        # print(titre)
                        imageauteur = k["creator"]["media"]
                        for i in imageauteur:
                            img = i["images"]
                            # print(type(img))
                            for im in img.values():
                                auteurimage = im["url"]
                        
                        photo = k["media"]
                        for p in photo:
                            ph = p["images"]
                            # print(type(ph))
                            for item in ph.values():
                                photolook = item["url"]
                                # print(photolook)
                    data.append(keyLook)
                    break
        except:
            data = None
        status = True
    return JsonResponse(data=data, safe=False)

def articlelook(request):
    url = 'https://www.zalando.fr/outfits/DQ5B3SZeRDm/'
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    
    req = requests.get(url,headers=headers)
    status = False
    soup = ""
    cnt = 0
    dataarticle = []
    if req.status_code == 200:
        html_doc = req.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        status = True
        div_module = soup.find('script',  attrs={'class':'re-data-el-hydrate'}, type='application/json')
        data_to_python_json = div_module.contents[0].replaceWith("")
        datasjson = json.loads(data_to_python_json)
        datas = datasjson['graphqlCache']

        for key in datas.keys(): 
            if "ern:product" in key:
                try:
                    contdata = datas[key]['data']['product']
                    
                    dataarticle.append(contdata)
                except:
                    pass
            
            if "ern:collection" in key:
                outfilt = datas[key]['data']
                dataarticle.append(outfilt)
        
    else:
        print('erreur statut',req.status_code)
    return JsonResponse(data=dataarticle, safe=False)

def article(request):
    
    url = 'https://www.zalando.fr/massimo-dutti-chemise-blue-m3i22d05r-k12.html'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = get(url,headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    mydata = []
    
    if response.status_code == 200:
        div_module = html_soup.find('script', attrs = {'id':'z-vegas-pdp-props'}, type='application/json')
        data_to_python_json = div_module.contents[0].replaceWith("")
        
        d = data_to_python_json.strip('<![CDATA[').strip(']>')
        datas = json.loads(d)
        article = datas["model"]["articleInfo"]
        
        nom = article['name']
        prix = article['displayPrice']['price']['formatted']
        marque = article['brand']['name']
        couleur = article['color']
        description = article['attributes'][0:1]
        for item in description:
            print(item['data'])
        # print(description)
        # prix_reduit = article['displayPrice']['price']
        image = article['media']['images']
        # print(nom, prix, image)
        for item in image:
            images = item['sources']
            # print(images)
        mydata.append(article)
    else:
        print('erreur statut',response.status_code)
    return JsonResponse(data=mydata, safe=False) 

# Fonction pour récuperer le lien des collections
def allCollection(request):
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
                    # print(titre)
                    url_valide =  contdata['uri']
                    mydata.append(url_valide)
                        
                except Exception as e:
                    print(str(e))
    else:
        print('erreur statut',response.status_code)
    return JsonResponse(data=mydata, safe=False) 

## Fonctions pour récuperer les données d'une collection
def singleCollection(request):
    
    url = "https://www.zalando.fr/collections/YUgpTMN3TYu/"

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
        print('erreur statut',response.status_code)
    return JsonResponse(data=mydata, safe=False)