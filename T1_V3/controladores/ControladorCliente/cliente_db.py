import sqlite3
class ClienteDB:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute(
			"CREATE TABLE IF NOT EXISTS clientes (cpf INTEGER PRIMARY KEY, nome TEXT, telefone TEXT, rua TEXT, numero INTEGER, complemento TEXT, senha INTEGER)"
			)
		self.conn.commit()

	def fetch(self):
		self.cur.execute("SELECT * FROM clientes \n")
		rows = self.cur.fetchall()
		return rows

	def insert(self, cpf, nome, telefone, rua, numero, complemento, senha):
		self.cur.execute("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?, ?)",
		(cpf, nome, telefone, rua, numero, complemento, senha)
		)
		self.conn.commit()

	def remove(self, cpf):
	    self.cur.execute("DELETE FROM clientes WHERE cpf=?", (cpf,))
	    self.conn.commit()	

	def update(self, cpf, nome, telefone, rua, numero, complemento, senha):
		self.cur.execute("UPDATE clientes SET nome = ?, telefone = ?, rua = ?, numero = ?, complemento = ?, senha = ? WHERE cpf = ?", 
		(nome, telefone, rua, numero, complemento, senha, cpf))
		self.conn.commit()

	def __del__(self):
		self.conn.close()
