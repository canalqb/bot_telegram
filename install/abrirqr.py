import telethon
from qrcode import QRCode
import platform
print("rodrigo")
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

print(id_telegram)
print(hash_telegram)
print(telefone)
