import argparse
from datetime import datetime
from DataBase import DataBase
from organizacao import Gasto
from servicos import adicionar_gasto, listar_gastos

db = DataBase()
db.create_table()

parser = argparse.ArgumentParser(description="Controle financeiro CLI")
subparsers = parser.add_subparsers(dest="comando")

# comando add
parser_add = subparsers.add_parser("add")
parser_add.add_argument("--descricao", required=True)
parser_add.add_argument("--valor", type=float, required=True)
parser_add.add_argument("--categoria", required=True)

# comando list
subparsers.add_parser("list")

args = parser.parse_args()

if args.comando == "add":
    gasto = Gasto(
        descricao=args.descricao,
        valor=args.valor,
        categoria=args.categoria,
        data=datetime.now().strftime("%Y-%m-%d")
    )
    adicionar_gasto(gasto)
    print("Gasto adicionado com sucesso!")

elif args.comando == "list":
    gastos = listar_gastos()
    for g in  gastos:
         print(g)

elif args.comando == "relatorio":
    from servicos import relatorio_mensal
    relatorio_mensal()