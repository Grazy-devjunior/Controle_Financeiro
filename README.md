Finance CLI - Controle Financeiro no Terminal

Um sistema simples, eficiente e direto ao ponto para gerenciamento de gastos via linha de comando (CLI), utilizando Python e SQLite.

Visão Geral

O Finance CLI é uma aplicação que permite registrar, listar e futuramente analisar gastos pessoais diretamente pelo terminal. Ideal para quem quer controle financeiro sem depender de interfaces gráficas pesadas.


-Funcionalidades

Adicionar gastos com descrição, valor e categoria

Armazenamento persistente com SQLite

Listar todos os gastos cadastrados

(Em evolução) Relatório mensal


Arquitetura do Projeto

O projeto segue uma estrutura modular :

Finance_CLI/
│
├── CLI.py              # Interface de linha de comando
├── DataBase.py         # Conexão e criação do banco
├── organizacao.py      # Classe Gasto (modelo)
├── servicos.py         # Regras de negócio
└── Finance.db          # Banco de dados SQLite



-Explicação dos Componentes

🔹 organizacao.py

Define a entidade principal do sistema:

class Gasto:
    def __init__(self, descricao, valor, categoria, data):

Aqui você modela o dado. Isso é padrão de mercado: separar dados da lógica.



🔹 DataBase.py

Responsável pela conexão e criação da tabela:

sqlite3

Cria a tabela transactions com:

id

data

descrição

valor

categoria



Uso de context manager (with) → evita dor de cabeça com conexão aberta.



🔹 servicos.py

Camada de regras de negócio:

adicionar_gasto() → insere no banco

listar_gastos() → retorna todos os registros


Aqui você separa lógica da interface. Isso é mentalidade de dev profissional.



🔹CLI.py

Interface via terminal usando argparse.

Comandos disponíveis:

Adicionar gasto

python CLI.py add --descricao "Almoço" --valor 25 --categoria "Comida"

Listar gastos

python CLI.py list



-Tecnologias Utilizadas
 Python 3
 SQLite (banco leve e embutido)
 argparse (CLI)



-Onde esse projeto pode ser aplicado?

1. Controle financeiro pessoal

Perfeito pra quem quer sair do caos financeiro sem depender de app cheio de anúncio.

 2. Base para sistemas maiores

Pode evoluir isso para:

API (com Flask ou FastAPI)

Dashboard web

App mobile



-Como Rodar o Projeto

1. Clone o repositório

git clone https://github.com/seu-usuario/finance-cli.git
cd finance-cli

2. Execute o sistema

python CLI.py add --descricao "Café" --valor 5 --categoria "Lanche"
python CLI.py list

