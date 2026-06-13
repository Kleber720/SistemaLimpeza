# SistemaLimpeza

Sistema de gerenciamento para controle de estoque de produtos e de funcionários. Foi desenvolvido em Python e utiliza o framework [Flet](https://flet.dev/) para a interface gráfica, armazenando os dados localmente em arquivos JSON.

## Funcionalidades

* **Gerenciamento de Funcionários:** Adicionar, listar e remover funcionários.
* **Gerenciamento de Produtos:** Adicionar, buscar por ID, listar e excluir produtos do estoque.
* **Geração Automática de IDs:** Um serviço de infraestrutura que gera automaticamente IDs únicos e incrementais para novos registros de dados.
* **Interface Gráfica (GUI):** Interface fácil e moderna construída com Flet.

## Estrutura do Projeto

* `app.py`: Arquivo raiz e ponto de entrada principal da aplicação.
* `src/main/`: Contém os processos principais da aplicação e as rotinas de interface de usuário.
* `src/model/DAO/`: Classes de acesso aos dados (Data Access Objects) como `Produtos_DAO` e `Funcionario_DAO` responsáveis pelas operações de CRUD nos arquivos JSON.
* `src/infrastructure/services/`: Serviços auxiliares (ex: `geradorID.py` para criar chaves primárias).
* `src/database/`: Diretório onde os arquivos JSON (`funcionarios.json`, `produto.json`, `estoque.json`) ficam armazenados para simular um banco de dados.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface:** Flet
* **Banco de Dados:** Arquivos JSON locais

## Como Executar

1. Certifique-se de ter o Python instalado na sua máquina (versão 3.x recomendada).
2. Abra o terminal e navegue até o diretório raiz do projeto.
3. Instale a biblioteca do Flet (e outras possíveis dependências do projeto):

   ```bash
   pip install flet
   ```

4. Execute o arquivo principal da aplicação:

   ```bash
   python app.py
   ```

*Desenvolvido como um projeto prático para a gestão de recursos.*
