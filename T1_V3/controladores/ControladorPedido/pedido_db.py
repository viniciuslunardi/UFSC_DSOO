import sqlite3
class PedidoDB:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute(
			"CREATE TABLE IF NOT EXISTS pedidos (codigo INTEGER PRIMARY KEY, nome TEXT, cpf INTEGER,telefone TEXT, rua TEXT, numero INTEGER, complemento TEXT, pedido TEXT, data TEXT, status TEXT)"
			)
		self.conn.commit()

	def fetch(self):
		self.cur.execute("SELECT * FROM pedidos \n")
		rows = self.cur.fetchall()
		return rows

	def insert(self, codigo, nome, cpf, telefone, rua, numero, complemento, pedido, status, data):
		self.cur.execute("INSERT INTO pedidos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
		(codigo, nome, cpf, telefone, rua, numero, complemento, pedido, status, data)
		)
		self.conn.commit()

	def remove(self, codigo):
	    self.cur.execute("DELETE FROM pedidos WHERE codigo=?", (codigo,))
	    self.conn.commit()	

	def update(self, codigo, nome, cpf, telefone, rua, numero, complemento, pedido, status, data):
		self.cur.execute("UPDATE pedidos SET nome = ?, cpf = ?, telefone = ?, rua = ?, numero = ?, complemento = ?, pedido = ?, status = ? WHERE codigo = ?", 
		(nome, cpf, telefone, rua, numero, complemento, pedido, status, codigo))
		self.conn.commit()

	def __del__(self):
		self.conn.close()
