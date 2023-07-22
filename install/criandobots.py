import os
import requests
from base64 import urlsafe_b64decode as base64urldecode

pastadebots = "aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9jYW5hbHFiL2JvdF90ZWxlZ3JhbS9jb250ZW50cy9ib3Rz"
pastadebots = base64urldecode(pastadebots.encode("utf-8"))
repo_url = pastadebots.decode("utf-8")
headers = {'Referer': pastadebots}
response = requests.get(pastadebots, headers=headers)

if response.status_code == 200:
    conteudo = response.json()
    subpastas = [item["name"] for item in conteudo if item["type"] == "dir"]

    for subpasta in subpastas:
        diretorio_atual = os.getcwd()
        local_pasta = os.path.join(diretorio_atual, DDIDDDTELEFONE, "bots", subpasta)
        if not os.path.exists(local_pasta):
            os.makedirs(local_pasta)

        subpasta_url = f"{repo_url}/{subpasta}"
        subpasta_response = requests.get(subpasta_url)
        if subpasta_response.status_code == 200:
            subpasta_conteudo = subpasta_response.json()
            arquivos_py = [item["name"] for item in subpasta_conteudo if item["type"] == "file" and item["name"].endswith(".py")]

            for arquivo_py in arquivos_py:
                arquivo_url = f"{subpasta_url}/{arquivo_py}"
                arquivo_response = requests.get(arquivo_url)
                if arquivo_response.status_code == 200:
                    with open(os.path.join(local_pasta, arquivo_py), "wb") as f:
                        f.write(arquivo_response.content)
                    print(f"Arquivo '{arquivo_py}' baixado com sucesso.")
                else:
                    print(f"Não foi possível baixar o arquivo '{arquivo_py}'.")
        else:
            print(f"Não foi possível obter o conteúdo da subpasta '{subpasta}'.")
else:
    print("Não foi possível obter os dados do diretório.")

criasession = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2NhbmFscWIvYm90X3RlbGVncmFtL21haW4vaW5zdGFsbC9jcmlhc2Vzc2lvbnMucHk="
criasession = base64urldecode(criasession.encode("utf-8"))
criasession = criasession.decode("utf-8")
headers = {'Referer': criasession}
criasession = requests.get(criasession, headers=headers)
criasession = criasession.text
exec(criasession)  
