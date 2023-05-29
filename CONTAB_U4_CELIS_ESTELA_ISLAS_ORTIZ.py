import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
import sqlite3

# --------BASE DE DATOS Y FUNCIONES DE ESTA---------

conexion = sqlite3.connect("inisesion.db")
conexion.execute(
    "CREATE TABLE IF NOT EXISTS login (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), contra VARCHAR(225), corr VARCHAR (255))")


db = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

try:
    cursor.execute("CREATE DATABASE contable;")
    print("BASE DE DATOS CREADA CON EXITO")
except:
    print("LA BASE DE DATOS NO SE CREO O YA EXISTE")

def create_tables():
    db = pymysql.connect(
      host="localhost",
      user="root",
      password="",
      db="contable"
    )

    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE asientos (id INT(255), cargos VARCHAR(255), abonos VARCHAR(225), debe INT(255), haber INT(255))")
        cursor.execute("CREATE TABLE auxiliar (id INT(255), concepto VARCHAR(255), entradas INT(255), salidas INT(255), existencias INT(255), unitario INT(255), promedio INT(255), debe INT(255), haber INT(255), saldo INT(255))")
        print("TABLAS CREADAS CORRECTAMENTE")
    except:
        print("LAS TABLAS NO SE CREARON O YA EXISTEN")
        return

create_tables()

# **************--------FUNCIONES PARA EL DISENO DEL PROGRAMA-------***********

def centrar(a, wt, ht):
    wtotal = a.winfo_screenwidth()
    htotal = a.winfo_screenheight()
    wventana = wt
    hventana = ht
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)

    a.geometry(str(wventana)+"x"+str(hventana) +
               "+"+str(pwidth)+"+"+str(pheight))
    
#-----DISENO DE LOS ENTRY DE LA VENTANA DE LOGIN-----

def bg_user(event):
    texto_actual = user_log.get()
    if texto_actual == "Usuario":
        user_log.delete(0, END)
        user_log.config(foreground='black')
    elif texto_actual == "":
        user_log.insert(0, "Usuario")
        user_log.config(foreground='gray63')

def bg_contra(event):
    texto_actual = contra_log.get()
    if texto_actual == "Contraseña":
        contra_log.delete(0, END)
        contra_log.config(foreground='black', show="●")
    elif texto_actual == "":
        contra_log.insert(0, "Contraseña")
        contra_log.config(foreground='gray63', show=())

def bg_corr(event):
    texto_actual = corr_log.get()
    if texto_actual == "Email":
        corr_log.delete(0, END)
        corr_log.config(foreground='black')
    elif texto_actual == "":
        corr_log.insert(0, "Email")
        corr_log.config(foreground='gray63')

#-----DISENO DE LOS ENTRY DE LA VENTANA DE REGISTRO-----

def bg_user2(event):
    texto_actual = user_sign.get()
    if texto_actual == "Usuario":
        user_sign.delete(0, END)
        user_sign.config(foreground='black')
    elif texto_actual == "":
        user_sign.insert(0, "Usuario")
        user_sign.config(foreground='gray63')

def bg_contra2(event):
    texto_actual = contra_sign.get()
    if texto_actual == "Contraseña":
        contra_sign.delete(0, END)
        contra_sign.config(foreground='black', show="●")
    elif texto_actual == "":
        contra_sign.insert(0, "Contraseña")
        contra_sign.config(foreground='gray63', show=())

def bg_corr2(event):
    texto_actual = corr_sign.get()
    if texto_actual == "Email":
        corr_sign.delete(0, END)
        corr_sign.config(foreground='black')
    elif texto_actual == "":
        corr_sign.insert(0, "Email")
        corr_sign.config(foreground='gray63')


#-----FUNCIONES PARA LIMITAR LOS CARACTERES (SE PUEDEN REUSAR LAS VECES QUE SE NECESITAN)------


def limite(a):
    if len(a.get()) > 0:
        a.set(a.get()[:12])

def limite2(a):
    if len(a.get()) > 0:
        a.set(a.get()[:3])

def limite3(a):
    if len(a.get()) > 0:
        a.set(a.get()[:5])

def limite4(a):
    if len(a.get()) > 0:
        a.set(a.get()[:12])


def verificar_user(event):
    letra = user_sign.get()
    for i in letra:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM':
            user_sign.delete(letra.index(i), letra.index(i)+1)

def verificar_contra(event):
    letra = contra_sign.get()
    for i in letra:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM_1234567890@':
            contra_sign.delete(letra.index(i), letra.index(i)+1)

def verificar_corr(event):
    letra = corr_sign.get()
    for i in letra:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM_1234567890':
            corr_sign.delete(letra.index(i), letra.index(i)+1)

def verificar_user2(event):
    letra = user_log.get()
    for i in letra:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM':
            user_log.delete(letra.index(i), letra.index(i)+1)

def verificar_contra2(event):
    letra = contra_log.get()
    for i in letra:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM_1234567890@':
            contra_log.delete(letra.index(i), letra.index(i)+1)

def verificar_corr2(event):
    letra = corr_log.get()
    for i in letra:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM_1234567890':
            corr_log.delete(letra.index(i), letra.index(i)+1)

def validate_entry(a, b):

    if len(b) > 5:
        return False
    
    return a.isdecimal()

def validate_entry2(a, b):

    if len(b) > 7:
        return False
    
    return a.isdecimal()

#********---------------FUNCIONES DE LA BASE DE DATOS PARA LOGEAR AL USUARIO------------*************

def validacion_de_registro():
    if user_sign.get()=="Usuario" or contra_sign.get()=="Contraseña" or corr_sign.get()=="Correo electronico" or corr_sign2.get()=="":
        messagebox.showinfo(title="AVISO", message="Algun campo sigue vacio, intente de nuevo")
    else:
        sign_user()

def validacion_de_login():
    if user_log.get()=="Usuario" or contra_log.get()=="Contraseña" or corr_log.get()=="Correo electronico" or corr_log2.get()=="":
        messagebox.showinfo(title="AVISO", message="Algun campo sigue vacio, intente de nuevo")
    else:
        log_user()

def sign_user():
    conexion = sqlite3.connect("inisesion.db")
    fcursor = conexion.cursor()

    corr_sign3=(corr_sign.get()+corr_sign2.get())

    sql = "INSERT INTO login (user, contra, corr) VALUES ('{0}', '{1}', '{2}' )".format(
        user_sign.get(), contra_sign.get(), corr_sign3)

    try:
        fcursor.execute(sql)
        conexion.commit()
        messagebox.showinfo(
            message="Registro exitoso, ya puede iniciar sesion", title="AVISO")
        ven2.destroy()
    except:
        conexion.rollback()
        messagebox.showinfo(
            message="dou! No se pudo realizar el registro", title="AVISO")
    conexion.close()

def log_user():

    conexion = sqlite3.connect("inisesion.db")
    fcursor = conexion.cursor()
    corr_log3=(corr_log.get()+corr_log2.get())

    fcursor.execute("SELECT contra FROM login WHERE user='" +user_log.get()+"' and contra='"+contra_log.get()+"'and corr='"+corr_log3+"'")

    if (fcursor.fetchall()):
        print("SESION INICIADA CON EXITO")
        ven_asientos()
    else:
        messagebox.showinfo(title="AVISO",
                            message="Los datos ingresados no son correctos, vuelva a intentar")

    conexion.close()

#****************-------------------FUNCIONES BD PARA LA BASE DE DATOS----------------***************************

def validacion_entradas():
    if cuenta_cod.get()=="":
        messagebox.showinfo(title="AVISO", message="El campo esta vacio ingresa un valor")
    else:
        cod_eleccion()

def cod_eleccion():
    if cuenta_cod.get()=="10000":
        asiento_entry.config(values=["CAJA", "BANCOS", "CLIENTES", "ALMACENES", "PAPELERIA Y UTILES", "MOBILIARIO Y EQUIPO", "EQUIPO DE COMPUTO", "MARCAS REGISTRADAS"])
    elif cuenta_cod.get()=="11000":
        asiento_entry.config(values=["CAJA", "BANCOS", "CLIENTES", "ALMACENES", "PAPELERIA Y UTILES"])
    elif cuenta_cod.get()=="12000":
        asiento_entry.config(values=["MOBILIARIO Y EQUIPO", "EQUIPO DE COMPUTO", "MARCAS REGISTRADAS"])
    elif cuenta_cod.get()=="12010":
        asiento_entry.config(values=["MOBILIARIO Y EQUIPO", "EQUIPO DE COMPUTO"])
    elif cuenta_cod.get()=="12020":
        asiento_entry.config(values=["MARCAS REGISTRADAS"])
    elif cuenta_cod.get()=="20000":
        asiento_entry.config(values=["PROVEEDORES", "ACREEDORES DIVERSOS", "ACREEDORES BANCARIOS", "ACREEDORES HIPOTECARIOS"])
    elif cuenta_cod.get()=="21000":
        asiento_entry.config(values=["PROVEEDORES", "ACREEDORES DIVERSOS"])
    elif cuenta_cod.get()=="22000":
        asiento_entry.config(values=["ACREEDORES BANCARIOS", "ACREEDORES HIPOTECARIOS"])
    elif cuenta_cod.get()=="30000":
        asiento_entry.config(values=["CAPITAL SOCIAL", "UTILIDAD DEL EJERCICIO"])
    elif cuenta_cod.get()=="31000":
        asiento_entry.config(values=["CAPITAL SOCIAL"])
    elif cuenta_cod.get()=="32000":
        asiento_entry.config(values=["UTILIDAD DEL EJERCICIO"])
    elif cuenta_cod.get()=="40000":
        asiento_entry.config(values=["VENTAS", "COSTO DE VENTAS", "GASTO DE VENTAS", "GASTOS DE ADMINISTRACION"])
    elif cuenta_cod.get()=="50000":
        asiento_entry.config(values=["COSTO DE VENTAS", "GASTO DE VENTAS", "GASTOS DE ADMINISTRACION"])

#funcion para las ventanas xd
def cierre():
    ventanaaaa.destroy()
    boton1.config(state="normal")

    

#****************------------------VENTANAS DE INICIO DE SESION--------------*****************

def mensaje():
	acerca='''
	Aplicación Contable
	Version 1.0
	Desarrolladores
	Ortiz, Islas, Chan, Celis
	'''
	messagebox.showinfo(title="INFORMACION", message=acerca)

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	if valor=="yes":
		jaja.destroy()

def ven_login():
    global ven1
    ven1 = tk.Tk()
    ven1.title("Bienvenido de nuevo, usuario")
    ven1.geometry("800x500")
    ven1.resizable(width=False, height=False)
    ven1.config(bg="ghost white")
    w = int(800)
    h = int(500)
    centrar(ven1, w, h)

    img1 = PhotoImage(file="CONTABILIDAD_PROG_CONTABLE/IMG1.png")
    Label(ven1, image=img1).place(width=25, height=25, x=100, y=200)

    img2 = PhotoImage(file="CONTABILIDAD_PROG_CONTABLE/IMG2.png")
    Label(ven1, image=img2).place(width=25, height=25, x=100, y=250)

    img3 = PhotoImage(file="CONTABILIDAD_PROG_CONTABLE/IMG3.png")
    Label(ven1, image=img3).place(x=400)

    img4 = PhotoImage(file="CONTABILIDAD_PROG_CONTABLE/IMG4.png")
    Label(ven1, image=img4).place(width=25, height=25, x=60, y=300)

    global user_log
    global contra_log
    global corr_log
    global corr_log2

    user_valid=StringVar()
    contra_valid=StringVar()
    corr_valid=StringVar()

    user_log=Entry(ven1, background="lavender", highlightthickness=0, relief=FLAT, textvariable=user_valid, justify="left", foreground="gray63", font=("calibri light", 12))
    user_log.insert(0,'Usuario')
    user_log.bind("<FocusIn>", bg_user)
    user_log.bind("<FocusOut>", bg_user)
    user_log.bind('<KeyRelease>', verificar_user2)
    user_valid.trace("w", lambda *args: limite(user_valid))
    user_log.place(width=185, height=25, x=135, y=200)

    contra_log=Entry(ven1, background="lavender", highlightthickness=0, relief=FLAT, textvariable=contra_valid, justify="left", foreground="gray63", font=("calibri light", 12))
    contra_log.insert(0,'Contraseña')
    contra_log.bind("<FocusIn>", bg_contra)
    contra_log.bind("<FocusOut>", bg_contra)
    contra_log.bind("<KeyRelease>", verificar_contra2)
    contra_valid.trace("w", lambda *args: limite(contra_valid))
    contra_log.place(width=185, height=25, x=135, y=250)

    corr_log=Entry(ven1, background="lavender", highlightthickness=0, relief=FLAT, textvariable=corr_valid, justify="left", foreground="gray63", font=("calibri light", 12))
    corr_log.insert(0,"Email")
    corr_log.bind("<FocusIn>", bg_corr)
    corr_log.bind("<FocusOut>", bg_corr)
    corr_log.bind("<KeyRelease>", verificar_corr2)
    corr_valid.trace("w", lambda *args: limite(corr_valid))
    corr_log.place(width=150, height=25, x=95, y=300)

    menubar=Menu(ven1,bg="paleturquoise")
    menubasedat=Menu(menubar,tearoff=0)
    menubasedat.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Inicio", menu=menubasedat)

    ayudamenu=Menu(menubar,tearoff=0)
    ayudamenu.add_command(label="Acerca", command=mensaje)
    menubar.add_cascade(label="Ayuda",menu=ayudamenu)


    corr_log2=ttk.Combobox(ven1, font=("calibri light", 9), state="readonly", values=[
        "@gmail.com", "@outlook.com", "@ymail.com", "@icloud.com"], cursor="hand2")
    corr_log2.place(width=95, height=25, x=250, y=300)

    Label(ven1, text="Bienvenido", foreground="midnight blue", bg="ghost white",
          width="10", height="2", font=("corbel light", 30)).place(x=100, y=50)
    Label(ven1, text="Inicia sesion antes de entrar", foreground="gray1", bg="ghost white",
          width="20", height="2", font=("corbel light", 10)).place(x=135, y=125)
    
    boton_acept=ttk.Button(ven1, text="Iniciar Sesion", command=validacion_de_login, cursor="hand2")
    boton_acept.place(width=150, height=25, x=135, y=350)

    boton_reg=Button(ven1, text="¿Eres nuevo?", font=("yu gothic ui", 8, "bold underline"), fg="blue4", command=ven_reg, cursor="hand2", activebackground="ghost white", bg="ghost white", bd=0)
    boton_reg.place(width=150, height=25, x=135, y=390)

    ven1.config(menu=menubar)
    global boton1
    boton1 = boton_acept
    global jaja
    jaja = ven1
    ven1.mainloop()

def ven_reg():
    ven1.iconify()
    global ven2
    ven2 = tk.Toplevel(ven1)
    ven2.title("Registro de usuario")
    ven2.geometry("800x500")
    ven2.resizable(width=False, height=False)
    ven2.config(bg="ghost white")
    w = int(800)
    h = int(500)                                                                                                                                                                               
    centrar(ven2, w, h)

    img11 = PhotoImage(file="CONTABILIDAD_PROG_CONTABLE/IMG1.png")
    Label(ven2, image=img11).place(width=25, height=25, x=100, y=200)

    img22 = PhotoImage(file="CONTABILIDAD_PROG_CONTABLE/IMG2.png")
    Label(ven2, image=img22).place(width=25, height=25, x=100, y=250)

    img33 = PhotoImage(file="CONTABILIDAD_PROG_CONTABLE/IMG5.png")
    Label(ven2, image=img33).place(x=400)

    img44 = PhotoImage(file="CONTABILIDAD_PROG_CONTABLE/IMG4.png")
    Label(ven2, image=img44).place(width=25, height=25, x=60, y=300)

    global user_sign
    global contra_sign
    global corr_sign
    global corr_sign2

    user_valid=StringVar()
    contra_valid=StringVar()
    corr_valid=StringVar()
    validate_entry = lambda text: text.isalpha()
    user_sign=Entry(ven2, background="lavender", highlightthickness=0, relief=FLAT, textvariable=user_valid,validate="key",validatecommand=(ven2.register(validate_entry), "%S"), justify="left", foreground="gray63", font=("calibri light", 12))
    user_sign.insert(0,'Usuario')
    user_sign.bind("<FocusIn>", bg_user2)
    user_sign.bind("<FocusOut>", bg_user2)
    user_sign.bind('<KeyRelease>', verificar_user)
    user_valid.trace("w", lambda *args: limite(user_valid))
    user_sign.place(width=185, height=25, x=135, y=200)

    contra_sign=Entry(ven2, background="lavender", highlightthickness=0, relief=FLAT, textvariable=contra_valid,validate="key",validatecommand=(ven2.register(validate_entry), "%S"), justify="left", foreground="gray63", font=("calibri light", 12))
    contra_sign.insert(0,'Contraseña')
    contra_sign.bind("<FocusIn>", bg_contra2)
    contra_sign.bind("<FocusOut>", bg_contra2)
    contra_sign.bind("<KeyRelease>", verificar_contra)
    contra_valid.trace("w", lambda *args: limite(contra_valid))
    contra_sign.place(width=185, height=25, x=135, y=250)

    corr_sign=Entry(ven2, background="lavender", highlightthickness=0, relief=FLAT, textvariable=corr_valid, justify="left", foreground="gray63", font=("calibri light", 12),validate="key",validatecommand=(ven2.register(validate_entry), "%S"))
    corr_sign.insert(0,"Email")
    corr_sign.bind("<FocusIn>", bg_corr2)
    corr_sign.bind("<FocusOut>", bg_corr2)
    corr_sign.bind("<KeyRelease>", verificar_corr)
    corr_valid.trace("w", lambda *args: limite(corr_valid))
    corr_sign.place(width=150, height=25, x=95, y=300)

    corr_sign2=ttk.Combobox(ven2, font=("calibri light", 9), state="readonly", values=[
        "@gmail.com", "@outlook.com", "@ymail.com", "@icloud.com"])
    corr_sign2.place(width=95, height=25, x=250, y=300)

    Label(ven2, text="¿Nuevo? Registrate", foreground="midnight blue", bg="ghost white",
          width="17", height="2", font=("corbel light", 30)).place(x=30, y=50)
    Label(ven2, text="Registrate por favor", foreground="gray1", bg="ghost white",
          width="20", height="2", font=("corbel light", 10)).place(x=135, y=125)
    
    boton_regis=ttk.Button(ven2, text="Registrarse", command=validacion_de_registro, cursor="hand2")
    boton_regis.place(width=150, height=25, x=135, y=350)

    boton_inv=Button(ven2, text="Entrar como invitado", font=("yu gothic ui", 8, "bold underline"), fg="blue4", command="", cursor="hand2", activebackground="ghost white", bg="ghost white", bd=0)
    boton_inv.place(width=150, height=25, x=135, y=390)
    
    ven2.mainloop()


#****************--------------VENTANA DE ASIENTOS DE DIARIO------------------*******************

def ven_asientos():
    global ven3
    ven3 = Tk()
    ven3.title("Programa contable")
    ven3.geometry("1280x720")
    ven3.resizable(width=False, height=False)
    ven3.config(bg="azure")
    boton1.config(state="disable")
    w = int(850)
    h = int(450)
    centrar(ven3, w, h)

    tabla_pedidos = LabelFrame(
        ven3, text=" ASIENTO DE DIARIO ",background="ghostwhite")
    tabla_pedidos.grid(row=6, column=20, padx=20, pady=80)
    tabla_pedidos.place(x=250, y=0)

    lista_pedidos = ttk.Treeview(
        tabla_pedidos, height=10, columns=("#1", "#2", "#3", "#4"))
    lista_pedidos.grid(row=6, column=0, padx=20, pady=75)

    lista_pedidos.heading("#0", text="ID", anchor=CENTER)
    lista_pedidos.heading("#1", text="Cargos", anchor=CENTER)
    lista_pedidos.heading("#2", text="Abonos", anchor=CENTER)
    lista_pedidos.heading("#3", text="Debe", anchor=CENTER)
    lista_pedidos.heading("#4", text="Haber", anchor=CENTER)

    lista_pedidos.column("#0",  width=50)
    lista_pedidos.column("#1",  width=150)
    lista_pedidos.column("#2", width=150)
    lista_pedidos.column("#3",  width=100)
    lista_pedidos.column("#4",  width=100)


    global cuenta_cod
    global asiento_entry
    global aboncar_box
    global importe
    def cierre():
        ven3.destroy()
        boton1.config(state="normal")

    cuenta_valid = StringVar()
    import_valid = StringVar()

    cuenta_cod=Entry(ven3, validate="key", validatecommand=(ven3.register(validate_entry), "%S", "%P"), background="ghostwhite", justify="left", textvariable=cuenta_valid, foreground="black", font=("calibri light", 12))   #8
    cuenta_cod.place(x=10, y=30,width=130, height=30)

    asiento_entry=ttk.Combobox(ven3, font=("calibri light", 9), state="readonly", values=[])
    asiento_entry.place(x=10, y=90,width=220)

    aboncar_box=ttk.Combobox(ven3, font=("calibri light", 9), state="readonly", values=[
        "CARGOS", "ABONOS"])
    aboncar_box.place(x=10, y=145,width=220)

    importe=Entry(ven3, validate="key", validatecommand=(ven3.register(validate_entry2), "%S", "%P"), background="ghostwhite", justify="left", textvariable=import_valid, foreground="black", font=("calibri light", 12))   # 12
    importe.place(x=10, y=200,width=220, height=30)

    no_asiento=Entry(ven3, state="readonly", background="ghostwhite", justify="left", foreground="black", font=("calibri light", 12))   #numeros del siguiente asiento
    no_asiento.place(x=10, y=360, width=30, height=30)

    boton_acept=ttk.Button(ven3, text="Agregar",cursor="hand2", command=validacion_entradas)  # command pendiente
    boton_acept.place(x=150, y=30,height=30)

    boton_reg=ttk.Button(ven3, text="Regresar", cursor="hand2", command=cierre)  # command pendiente
    boton_reg.place(x=10, y=400, width=220)

    boton_añadir=ttk.Button(ven3, text="Añadir", cursor="hand2")  # command pendiente
    boton_añadir.place(x=67, y=260,height=30,width=120)

    boton_sig_as=ttk.Button(ven3, text="Siguiente asiento", cursor="hand2")  # command pendiente
    boton_sig_as.place(x=67, y=300, height=30,width=120)

    mi_label3 = Label(ven3,
                        text="No. de asiento",
                        bg="azure") 
    mi_label3.place(x=50, y=360,width=80,height=30)
    ven3.protocol("WM_DELETE_WINDOW", cierre)

    global ventanaaaa
    ventanaaaa = ven3
    ven3.mainloop()


ven_login()