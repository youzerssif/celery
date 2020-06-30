from django.shortcuts import render

# Create your views here.


def home(request):
    
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
        
        div_module = html_soup.find('script', attrs = {'class':'re-data-el-hydrate'}, type='application/json')
        # data = json.loads(div_module.text)
        data_to_python_json = div_module.contents[0].replaceWith("")
        # print(data,"zjncldncze")
        
        datas =json.loads(data_to_python_json)
        # print(datas)
       

        
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
    print(div_module)
    data={
        'datas':datas,
    }
    return render(request, 'home.html',data)


def json_api(request):
    import requests
    from requests import get
    from bs4 import BeautifulSoup
    import json
    from django.http import JsonResponse

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
        datas = datas['graphqlCache']
        
        # print()
        # print(datas)
        for key in datas.keys(): 
            if "ern:product" in key:
                print(key)
       

        
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
    return JsonResponse(datas, safe=False)
    
    