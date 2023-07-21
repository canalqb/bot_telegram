import re
import os
import telethon
from telethon import TelegramClient
from qrcode import QRCode
import platform

sistema_operacional = platform.system()
if sistema_operacional == "Windows":
    idsystem = 'w'
elif sistema_operacional == "Linux":
    if "android" in platform.uname().release.lower():
        idsystem = 'a'
    else:
        idsystem = 'l'
else:
    idsystem = 'o'
    
#idsystem Pode retornar w para Windows), (a para Android), (l para Linux), )o para outros sistemas)
print('ddd',DDIDDDTELEFONE)

diretorio_atual = os.getcwd()
caminho_arquivo = os.path.join(diretorio_atual, DDIDDDTELEFONE, "dados", "meutelefone.txt")

# Inicializar as variáveis para armazenar os valores
tel = None
id_ = None
hash_ = None

# Ler o arquivo e extrair as variáveis
with open(caminho_arquivo, 'r') as arquivo:
    for linha in arquivo:
        if linha.startswith("TEL"):
            tel = linha.split()[1]
        elif linha.startswith("ID"):
            id_ = linha.split()[1]
        elif linha.startswith("HASH"):
            hash_ = linha.split()[1]

# Imprimir as variáveis extraídas
#print("TEL:", tel)
#print("ID:", id_)
#print("HASH:", hash_)

session_file = os.path.join(idsystem + tel) 
print(session_file)
client = TelegramClient(session_file, int(id_), str(hash_), device_model= 'bot', timeout=2, connection_retries=1, auto_reconnect=True)
#client.loop.run_until_complete(main(client))
#client.disconnect()
