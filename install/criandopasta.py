import os

# Variável global para armazenar o DDIDDDTELEFONE
DDIDDDTELEFONE = ""

def verificar_arquivo_existe(dados_path, telefone):
    arquivo_telefone = os.path.join(dados_path, f'meutelefone.txt')
    if os.path.exists(arquivo_telefone):
        with open(arquivo_telefone, 'r') as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) == 3 and linhas[0].startswith('TEL') and linhas[1].startswith(f'{telefone}ID') and linhas[2].startswith(f'{telefone}HASH'):
                return True
    return False

def criar_pasta_telefone(telefone):
    dados_path = os.path.join('..', DDIDDDTELEFONE, 'dados')  # Navegar um nível acima para a pasta "DDIDDDTELEFONE"
    if not os.path.exists(dados_path):
        os.makedirs(dados_path)
    return dados_path

def salvar_dados_telefone(dados_path, telefone, id_telegram, hash_telegram):
    arquivo_telefone = os.path.join(dados_path, f'meutelefone.txt')
    with open(arquivo_telefone, 'w') as arquivo:
        arquivo.write(f'TEL {telefone}\n')
        arquivo.write(f'{telefone}ID {id_telegram}\n')
        arquivo.write(f'{telefone}HASH {hash_telegram}\n')

def main():
    global DDIDDDTELEFONE

    ddi = input('Digite o DDI (código do país): ')
    ddd = input('Digite o DDD (código da região): ')
    telefone = input('Digite o número de telefone (sem DDI e DDD): ')
    telefone_completo = f'{ddi}{ddd}{telefone}'
    
    # Salvar o valor na variável global
    DDIDDDTELEFONE = telefone_completo

    dados_path = criar_pasta_telefone(telefone_completo)

    if not verificar_arquivo_existe(dados_path, telefone_completo):
        id_telegram = input('Digite o ID do Telegram: ')
        hash_telegram = input('Digite o HASH do Telegram: ')

        salvar_dados_telefone(dados_path, telefone_completo, id_telegram, hash_telegram)
        print('Dados salvos com sucesso!')
    else:
        print('Os dados já foram salvos anteriormente. Ignorando a próxima etapa.')

if __name__ == "__main__":
    main()
