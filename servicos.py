from DataBase import DataBase
from organizacao import Gasto

db = DataBase()

def adicionar_gasto(gasto: Gasto):
    with db.connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO gastos (descricao, valor, categoria, data)
            VALUES (?, ?, ?, ?)
        ''', (gasto.descricao, gasto.valor, gasto.categoria, gasto.data))

def listar_gastos():
    with db.connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM gastos')
        gastos = cursor.fetchall()
    return gastos