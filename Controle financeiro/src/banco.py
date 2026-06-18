import sqlite3

connect = sqlite3.connect("financeiro.db")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL
)
''')

connect.commit()


def adicionar_transacao(tipo, descricao, valor):
    cursor.execute(
        "INSERT INTO transacoes (tipo, descricao, valor) VALUES (?, ?, ?)",
        (tipo, descricao, valor)
    )
    connect.commit()


def listar_transacoes():
    cursor.execute("SELECT * FROM transacoes")
    return cursor.fetchall()


def calcular_saldo():
    cursor.execute(
        "SELECT SUM(valor) FROM transacoes WHERE tipo = 'receita'"
    )
    receitas = cursor.fetchone()[0] or 0

    cursor.execute(
        "SELECT SUM(valor) FROM transacoes WHERE tipo = 'despesa'"
    )
    despesas = cursor.fetchone()[0] or 0

    return receitas - despesas