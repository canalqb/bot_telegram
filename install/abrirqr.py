import telethon
from qrcode import QRCode
import os
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
print("TEL:", tel)
print("ID:", id_)
print("HASH:", hash_)
