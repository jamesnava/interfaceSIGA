from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox


class Ventana(object):
	
	def __init__(self):
		font2=("Comic Sans MS",18,"bold")
		self.Windows_Main=ThemedTk(theme="arc")
		self.Windows_Main.geometry("800x500")
		self.Windows_Main.title("Interface SIGA")
		self.add_menu()

		etiqueta=Label(self.Windows_Main,text="Ingrese el Script: ",font=font2)
		etiqueta.grid(row=1,column=1)

		self.Scripts =Text(self.Windows_Main, width=40, height=10)
		self.Scripts.grid(row=2,column=2)
		btn_Aceptar=ttk.Button(self.Windows_Main,text="Ejecutar")
		btn_Aceptar.grid(row=3,column=1,columnspan=2,pady=10)
		self.Windows_Main.mainloop()

	def add_menu(self):
		menubar=Menu(self.Windows_Main)
		archivo=Menu(menubar,tearoff=0)
		menubar.add_cascade(label='Configuracion',menu=archivo)
		archivo.add_command(label="Base de datos",command=self.Top_Configuration)

		Operaciones=Menu(menubar,tearoff=0)
		menubar.add_cascade(label='Acciones',menu=Operaciones)
		Operaciones.add_command(label="Ejecutar",command=None)

		self.Windows_Main.config(menu=menubar)

	def Top_Configuration(self):
		font1=("Comic Sans MS",14,"bold")
		self.modulo_config=Toplevel(self.Windows_Main)
		self.modulo_config.geometry("400x300")
		self.modulo_config.resizable(0,0)
		self.modulo_config.grab_set()
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
			server=f"SERVIDOR={self.entry_ServerIp.get()}\n"
			bd=f"DATABASE={self.entry_DataBase.get()}\n"
			user=f"USUARIO={self.entry_Usuario.get()}\n"
			password=f"PASS={self.entry_Pasword.get()}\n"
			archivo.write(server)
			archivo.write(bd)
			archivo.write(user)
			archivo.write(password)
		self.modulo_config.destroy()
		


if __name__=="__main__":
	Ventana()
		
