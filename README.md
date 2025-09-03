# 🤖 Script de Instalação e Configuração de Bots de Telegram
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Sumário

* [1. Introdução ao Script](#1-introdução-ao-script)
  * [1.1 Visão Geral](#11-visão-geral)
  * [1.2 Como Funciona](#12-como-funciona)
* [2. Script `install.py`](#2-script-installpy)
  * [2.1 Objetivo do Script](#21-objetivo-do-script)
  * [2.2 Como Utilizar](#22-como-utilizar)
  * [2.3 Importante](#23-importante)
* [3. Estrutura do Projeto](#3-estrutura-do-projeto)
  * [3.1 Pastas e Arquivos](#31-pastas-e-arquivos)
* [4. Extras](#4-extras)
  * [4.1 Licença](#41-licença)
  * [4.2 Referências](#42-referencias)
* [5. Contato](#5-contato)
* [6. Nota](#6-nota)

## 1. Introdução ao Script

### 1.1 Visão Geral

Este repositório contém scripts úteis para a criação e configuração de bots no Telegram e outras interações com APIs externas. O principal script é o `install.py`, que realiza o download e a execução de código a partir de uma URL externa.

### 1.2 Como Funciona

O script `install.py` realiza uma solicitação HTTP para uma URL externa (codificada em base64) e executa o código obtido dessa URL. É necessário ter o Python instalado e a biblioteca `requests` configurada para que o script funcione corretamente.

## 2. Script `install.py`

### 2.1 Objetivo do Script

O objetivo principal deste script é buscar um código Python a partir de uma URL codificada, processá-lo e executá-lo em seu ambiente. Esse processo pode ser útil em automações ou configurações rápidas, mas deve ser feito com cuidado devido aos riscos envolvidos.

### 2.2 Como Utilizar

1. **Copie o script fornecido** para um arquivo `.py` no seu projeto.
2. **Instale a biblioteca `requests`**: Se ainda não tiver a biblioteca `requests` instalada, use o seguinte comando no terminal:
   ```bash
   pip install requests
   ```

3. **Execute o script**: Após realizar os passos anteriores, basta rodar o script e ele fará uma solicitação HTTP para obter um código de uma URL e executá-lo.

### 2.3 Importante

**Este script executa código de uma fonte externa**, o que pode ser perigoso. **Nunca utilize este script com URLs desconhecidas ou não confiáveis**, pois isso pode expor seu sistema a riscos de segurança. Sempre verifique a origem do código e entenda o que está sendo executado.

Se você não tem certeza da URL ou do código que está sendo baixado, **não utilize este script.**

## 3. Estrutura do Projeto

### 3.1 Pastas e Arquivos

O repositório possui a seguinte estrutura:

* **`install/`**: Contém o script de instalação e outros arquivos relacionados à criação e configuração do bot.
* **`bot_telegram/`**: Contém o código responsável pela criação dos bots de Telegram.
* **`canalqb/`**: Pasta relacionada ao canal e ao repositório.
* **Arquivos como `criandobots.py`, `criandopasta.py`, `criasessions.py`**: Scripts auxiliares para configurar bots e sessões.

## 4. Extras

### 4.1 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

### 4.2 Referências

* [Documentação da API do Telegram](https://core.telegram.org/bots/api)
* [Python Requests](https://docs.python-requests.org/en/latest/)

## 5. Contato

* Feito por **CanalQb/Rodrigo Moraes** no GitHub.
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: **13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava**
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)


*Readme.md corrigido por ChatGPT*

## 6. Nota

* {**requests**}: *Biblioteca Python para fazer requisições HTTP facilmente. Usada aqui para baixar o código de uma URL externa.*
* {**base64**}: *Codificação usada para transformar dados binários em texto. A URL de onde o código será baixado está codificada em base64.*
* {**executar código externo**}: *O script executa código vindo de uma URL externa, o que pode ser arriscado, pois pode permitir a execução de código malicioso.* 
