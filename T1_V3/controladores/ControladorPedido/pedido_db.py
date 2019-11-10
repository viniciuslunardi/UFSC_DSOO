import sqlite3
class PedidoDB:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute(
			"CREATE TABLE IF NOT EXISTS pedidos (cpf INTEGER PRIMARY KEY, nome, telefone, endereco)"
			)
		self.conn.commit()

	

	def __del__(self):
		self.conn.close()
