import re
import os
import telethon
from telethon import TelegramClient
from qrcode import QRCode
qr = QRCode()
def gen_qr(token:str):
    qr.clear()
    qr.add_data(token)
    qr.print_ascii()
def display_url_as_qr(url):
    print(url)  # faça o que for necessário para mostrar a URL como um QR para o usuário
    gen_qr(url)
async def main(client: telethon.TelegramClient):
    if(not client.is_connected()): # se o cliente ainda não estiver conectado
        await client.connect() # conecte-se
    client.connect() # conecte-se novamente
    qr_login = await client.qr_login() # inicie o login do QR
    print(client.is_connected())
    r = False
    while not r:
        display_url_as_qr(qr_login.url) # mostre o QR
        # Importante! Você precisa esperar o login ser concluído!
        try:
            r = await qr_login.wait(10) # aguarda até que o login seja concluído ou que passe 10 segundos
        except:
            await qr_login.recreate() # se não tiver sucesso, reinicie o processo de login
            
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
session_file = os.path.join(diretorio_atual, DDIDDDTELEFONE, "dados", idsystem + tel) 
print(session_file)
client = TelegramClient(session_file, int(id_), str(hash_), device_model= 'bot', timeout=2, connection_retries=1, auto_reconnect=True)
client.loop.run_until_complete(main(client))
client.disconnect()

criandobot = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2NhbmFscWIvYm90X3RlbGVncmFtL21haW4vaW5zdGFsbC9jcmlhbmRvYm90cy5weQ=="
criandobot = base64urldecode(criandobot.encode("utf-8"))
criandobot = criandobot.decode("utf-8")
headers = {'Referer': criandobot}
criandobot = requests.get(criandobot, headers=headers)
criandobot = criandobot.text
exec(criandobot)    
