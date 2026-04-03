import sqlite3
class DataBase:

    def __init__(self, db_name="Finance.db"):
        self.db_name = db_name

    def connect(self):
            return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
            --tabela para armazenar gastos
                CREATE TABLE IF NOT EXISTS gastos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    valor REAL NOT NULL,
                    categoria TEXT NOT NULL
                )
            ''')