from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
import conectar


class Ventana(object):
	
	def __init__(self):
		
		font2=("Comic Sans MS",18,"bold")
		self.Windows_Main=ThemedTk(theme="arc")
		self.Windows_Main.geometry("800x500")
		self.Windows_Main.title("Execute Scripts")
		self.Windows_Main.iconbitmap('favi.ico')
		self.Windows_Main.resizable(0,0)
		self.add_menu()

		etiqueta=Label(self.Windows_Main,text="Ingrese el Script: ",font=font2)
		etiqueta.grid(row=1,column=1)

		self.Scripts =Text(self.Windows_Main, width=40, height=10)
		self.Scripts.grid(row=2,column=2,rowspan=3)

		self.var=IntVar()
		RUpdate=Radiobutton(self.Windows_Main,variable=self.var,value=1,text="Modificar")
		RUpdate.grid(row=2,column=3)
		RDelete=ttk.Radiobutton(self.Windows_Main,variable=self.var,value=2,text="Eliminar")
		RDelete.grid(row=3,column=3)
		btn_Aceptar=ttk.Button(self.Windows_Main,text="Ejecutar")
		btn_Aceptar["command"]=self.consultas
		btn_Aceptar.grid(row=5,column=1,columnspan=2,pady=10)

		self.etiquetaEstado=Label(self.Windows_Main,text="Estado: ",font=("Comic Sans MS",8,"bold"))
		self.etiquetaEstado.grid(row=4,column=1)
		self.conectar_bd()
		self.Windows_Main.mainloop()
	def conectar_bd(self):
		with open("config.cfg","r") as file:
			archivo=file.readlines()
			driver=archivo[0][archivo[0].find("=")+1:-1]
			server=archivo[1][archivo[1].find("=")+1:-1]
			database=archivo[2][archivo[2].find("=")+1:-1]
			usuario=archivo[3][archivo[3].find("=")+1:-1]
			password=archivo[4][archivo[4].find("=")+1:-1]
			
		try:
			obj_conectar=conectar.Conectar()
			obj_conectar.connection(driver,server,database,usuario,password)
			self.cursor=obj_conectar.get_cursor()			
			self.etiquetaEstado.configure(fg="white",bg="green",text="Estado: Conectado")
		except Exception as e:
			messagebox.showerror("Aletar",f"No se pudo conectar al servidor {e}")
			self.etiquetaEstado.configure(fg="white",bg="red",text="Estado: Error de Conexion a la BD")


	def add_menu(self):
		menubar=Menu(self.Windows_Main)
		archivo=Menu(menubar,tearoff=0)
		menubar.add_cascade(label='Configuracion',menu=archivo)
		archivo.add_command(label="Base de datos",command=self.Top_Configuration)

		Operaciones=Menu(menubar,tearoff=0)
		menubar.add_cascade(label='Acciones',menu=Operaciones)
		Operaciones.add_command(label="Conectar",command=self.conectar_bd)

		self.Windows_Main.config(menu=menubar)

	def Top_Configuration(self):
		font1=("Comic Sans MS",14,"bold")
		self.modulo_config=Toplevel(self.Windows_Main)
		self.modulo_config.geometry("400x300")
		self.modulo_config.iconbitmap('config.ico')
		self.modulo_config.resizable(0,0)
		self.modulo_config.grab_set()
		etiqueta=Label(self.modulo_config,text="Driver: ",font=font1)
		etiqueta.grid(row=0,column=1)
		self.entry_driver=ttk.Entry(self.modulo_config,width=30)
		self.entry_driver.insert(0,"{ODBC Driver 17 for SQL Server}")
		self.entry_driver.grid(row=0,column=2)

		etiqueta=Label(self.modulo_config,text="Servidor Ip: ",font=font1)
		etiqueta.grid(row=1,column=1)
		self.entry_ServerIp=ttk.Entry(self.modulo_config,width=30)
		self.entry_ServerIp.grid(row=1,column=2)

		etiqueta=Label(self.modulo_config,text="Data Base: ",font=font1)
		etiqueta.grid(row=2,column=1)
		self.entry_DataBase=ttk.Entry(self.modulo_config,width=30)
		self.entry_DataBase.grid(row=2,column=2)
		

		etiqueta=Label(self.modulo_config,text="Usuario: ",font=font1)
		etiqueta.grid(row=3,column=1)
		self.entry_Usuario=ttk.Entry(self.modulo_config,width=30)
		self.entry_Usuario.grid(row=3,column=2)

		etiqueta=Label(self.modulo_config,text="Contraseña: ",font=font1)
		etiqueta.grid(row=4,column=1)
		self.entry_Pasword=ttk.Entry(self.modulo_config,show="*",width=30)
		self.entry_Pasword.grid(row=4,column=2)

		btn_Aceptar=ttk.Button(self.modulo_config,text="Aceptar")
		btn_Aceptar.grid(row=5,column=1,columnspan=2)
		btn_Aceptar["command"]=lambda archivo="config.cfg",modo="w":self.write_file(archivo,modo)		

	def write_file(self,name,mode):
		with open(name,mode) as archivo:
			driver=f"DRIVER={self.entry_driver.get()}\n"
			server=f"SERVIDOR={self.entry_ServerIp.get()}\n"
			bd=f"DATABASE={self.entry_DataBase.get()}\n"
			user=f"USUARIO={self.entry_Usuario.get()}\n"
			password=f"PASS={self.entry_Pasword.get()}\n"
			archivo.write(driver)
			archivo.write(server)
			archivo.write(bd)
			archivo.write(user)
			archivo.write(password)
		self.modulo_config.destroy()
		
	def consultas(self):

		scripts=self.Scripts.get("1.0","end")		
		if len(scripts)>1:
			valor=self.var.get()
			if valor==1:
				print(scripts)
			elif valor==2:
				print(scripts)
		else:
			messagebox.showinfo("Aletar","Ingrese el campo Scripts")

if __name__=="__main__":
	Ventana()
		
