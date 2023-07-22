import os
import shutil

diretorio_atual = os.getcwd() 
dados_dir = os.path.join(diretorio_atual, DDIDDDTELEFONE, "dados")
sessions_dir = os.path.join(diretorio_atual, DDIDDDTELEFONE,  "sessions")
bots_dir = os.path.join(diretorio_atual, DDIDDDTELEFONE, "bots")

# Lista todas as pastas dentro de "raiz/bots"
subpastas = [subpasta for subpasta in os.listdir(bots_dir) if os.path.isdir(bots_dir)]

for subpasta in subpastas:
    # Cria a pasta correspondente em "raiz/sessions" caso ainda não exista
    sessions_subpasta = os.path.join(sessions_dir)
    if not os.path.exists(sessions_subpasta):
        os.makedirs(sessions_subpasta)

    # Encontra o arquivo w{DDIDDDTELEFONE}.session dentro de "DDIDDDTELEFONE/dados"
    nome_pasta_raiz = os.path.basename(os.path.normpath(diretorio_atual))
    session_file = f"w{DDIDDDTELEFONE}.session"
    origem = os.path.join(dados_dir, session_file)
    
    # Copia o arquivo para "raiz/sessions" com o nome de cada arquivo .py
    subpasta_dir = os.path.join(diretorio_atual, DDIDDDTELEFONE, "bots", subpasta)
    print(subpasta_dir)
    for arquivo_py in os.listdir(subpasta_dir):
        print(arquivo_py)
        if arquivo_py.endswith(".py"):
            destino = os.path.join(sessions_subpasta, os.path.splitext(arquivo_py)[0] + ".session")
            shutil.copy(origem, destino)
            print(f"Arquivo '{session_file}' copiado como '{os.path.splitext(arquivo_py)[0] + '.session'}' em '{sessions_subpasta}'")
