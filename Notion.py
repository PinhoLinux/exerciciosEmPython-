import requests

NOTION_API_KEY = 'SuaChaveDeIntegracao'
NOTION_DATABASE_ID = 'IDDoSeuBancoDeDados'

headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
}

# Exemplo: Criar uma nova página
data = {
    'parent': {
        'database_id': NOTION_DATABASE_ID
    },
    'properties': {
        'title': {
            'title': [{
                'text': {
                    'content': 'Nova Página'
                }
            }]
        }
    }
}

response = requests.post('https://api.notion.com/v1/pages',
                         headers=headers,
                         json=data)
