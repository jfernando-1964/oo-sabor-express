from fastapi import FastAPI,Query
import requests

app = FastAPI()

@app.get('/api/Hello')
def ola_mundo():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    
    '''
    return {'Hello':'World'}
@app.post('/api/description/')
def get_description(description: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes  
    
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
   

    if response.status_code == 200:
        dados_json = response.json()
        if description is None:
            return {'Dados':dados_json}
        dados_restaurante = []
        for i in dados_json:
            if i['description'] == description:
                dados_restaurante.append({
            "restaurnte": i['Company'],
            "item": i['Item'],
            "price": i['price'],
            "description": i['description']
        })
        return {'Restaurante':description,'Cardapio':dados_restaurante}

    else: 
        return {'Erro':f'{response.status_code} - {response.text}'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes  
    
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
   

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}
        dados_restaurante = []
        for i in dados_json:
            if i['Company'] == restaurante:
                dados_restaurante.append({
            "restaurnte": i['Company'],
            "item": i['Item'],
            "price": i['price'],
            "description": i['description']
        })
        return {'Restaurante':restaurante,'Cardapio':dados_restaurante}

    else: 
        return {'Erro':f'{response.status_code} - {response.text}'}