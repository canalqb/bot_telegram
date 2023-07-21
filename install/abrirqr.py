import telethon
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

def display_url_as_qr(url):
    qr = QRCode()
    qr.add_data(url)
    qr.print_ascii()

async def main():
    api_id = int(id_telegram)  # Substitua pelo seu API ID
    api_hash = str(hash_telegram)  # Substitua pelo seu API Hash
    telefone = str(DDIDDDTELEFONE)
    session_file = os.path.join(idsystem + telefone)
    
    async with telethon.TelegramClient(session_file, api_id, api_hash, device_model= 'bot', timeout=2, connection_retries=1, auto_reconnect=True) as client:
        qr_login = await client.qr_login()
        display_url_as_qr(qr_login.url)

        try:
            await qr_login.wait()
        except telethon.errors.TimeoutError:
            print("Tempo limite excedido. Tente novamente.")

if __name__ == "__main__":
    main_loop = telethon.events.asyncio_loop.AsyncioLoop()
    main_loop.run_until_complete(main())
