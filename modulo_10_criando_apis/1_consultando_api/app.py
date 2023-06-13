import requests
from pprint import pprint

#GET
endpoint = 'https://jsonplaceholder.typicode.com/todos'
def consultar_todo(endpoint):
    resultado_get = requests.get(endpoint)
    pprint(resultado_get.json())

# consultar_todo(endpoint)

# GET com Id
id = '2'
def consulta_todo_por_id(endpoint, id):
    resultado_get_id = requests.get(f'{endpoint}/{id}')
    pprint(resultado_get_id.json())
    
# consulta_todo_por_id(endpoint, id)

# POST - Criar um novo registro
payload = {
    'completed': False,
    'title': 'Teste de envio de todo',
    'userId': 1
}
def criar_um_todo(endpoint, payload):
    resultado_post = requests.post(endpoint, payload)
    pprint(resultado_post.json())

# criar_um_todo(endpoint, payload)

# PUT - Alterar um recurso existente
payload = {
    'completed': False,
    'title': 'Teste de atualização de todo',
    'userId': 1
}
def atualizar_todo(endpoint, id, payload):
    resultado_put = requests.put(f'{endpoint}/{id}', payload)
    pprint(resultado_put.json())

# atualizar_todo(endpoint, id, payload)

# DELETE
def deletar_todo(endpoint, id):
    resultado_delete = requests.delete(f'{endpoint}/{id}')
    pprint(resultado_delete.json())

# deletar_todo(endpoint, id)