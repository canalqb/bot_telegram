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
#______Resgatando Variaveis ______
api_id = id_telegram  # Substitua pelo seu API ID
api_hash = hash_telegram  # Substitua pelo seu API Hash
telefone = str(DDIDDDTELEFONE)
session_file = os.path.join(idsystem + telefone)

nomedevice = idsystem + telefone
client = TelegramClient(session_file, int(api_id), str(api_hash), device_model= 'bot', timeout=2, connection_retries=1, auto_reconnect=True)
client.loop.run_until_complete(main(client))
client.disconnect()

# Obtendo o nome da sessão
#session_name = os.path.splitext(session_file)[0]

client = locals().get('client')
print("Arquivo de saída gerado com sucesso!")
