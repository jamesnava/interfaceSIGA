import pyodbc
from tkinter import messagebox

class Conectar(object):
	def __init__(self):
		self.cursor=None
		self.conn=None
	def connection(self,driver,server,bd,user,password):		
		constr=(f"DRIVER={driver};SERVER="+server+";DATABASE="+bd+";UID="+user+";PWD="+password)		
		try:
			self.conn=pyodbc.connect(constr)
			
		except pyodbc.Error as e:
			messagebox.showerror("Alerta",f"error de conexion {e}")
	def get_cursor(self):
		self.cursor=self.conn.cursor()
		return self.cursor
