# importando o SQLite
import sqlite3 as lite

# Criando conexão
con = lite.connect('form.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Formulario(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, email TEXT, telefone TEXT,  dia_em DATE, estado TEXT, assunto TEXT)")
