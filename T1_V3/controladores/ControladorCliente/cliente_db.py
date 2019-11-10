import sqlite3
class ClienteDB:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute(
			"CREATE TABLE IF NOT EXISTS clientes (cpf INTEGER PRIMARY KEY, nome text, telefone text, endereco text, senha INTEGER)"
			)
		self.conn.commit()

	def insert(self, cpf, nome, telefone, endereco, senha):
		self.cur.execute("INSERT INTO clientes VALUES (?, ?, ?, ?, ?)",
		(cpf, nome, telefone, endereco, senha))
		self.conn.commit()

	def remove(self, cpf):
	    self.cur.execute("DELETE FROM parts WHERE cpf=?", (cpf,))
	    self.conn.commit()	

	def update(self, cpf, nome, telefone, endereco, senha):
		self.cur.execute("UPDATE parts SET nome = ?, telefone = ?, endereco = ?, senha = ? WHERE cpf = ?", 
		(nome, telefone, endereco, senha, cpf))
		self.conn.commit()

	def __del__(self):
		self.conn.close()
