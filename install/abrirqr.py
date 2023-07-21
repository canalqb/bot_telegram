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
print('telefone', telefone)

diretorio_atual = os.getcwd()
diretorio_pai = os.path.dirname(diretorio_atual)

print("O diretorio_atual é:", diretorio_atual)
print("O diretório do nível anterior é:", diretorio_pai)
