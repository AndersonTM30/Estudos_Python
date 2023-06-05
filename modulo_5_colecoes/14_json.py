
import json
from pathlib import Path

carros = [
    {"Marca": "Nissan", "Preço": 45.000, "Cor": "Azul"},
    {"Marca": "Ford", "Preço": 75.000, "Cor": "Verde"},
    {"Marca": "BMW", "Preço": 117.000, "Cor": "Amarelo"}
]

# Converte a lista para o formato json
carros_json = json.dumps(carros)
# Cria um arquivo no formato json
Path('14_1_carros.json').write_text(carros_json)

arquivo_carros_json = Path('14_1_carros.json').read_text()
arquivo_json = json.loads(arquivo_carros_json)
print(f'Marca: {arquivo_json[0]["Marca"]} - Preço: {arquivo_json[0]["Preço"]}')