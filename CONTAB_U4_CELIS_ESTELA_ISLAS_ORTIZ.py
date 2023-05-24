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
        a.set(a.get()[:8])

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
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM_1234567890':
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
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM_1234567890':
            contra_log.delete(letra.index(i), letra.index(i)+1)

def verificar_corr2(event):
    letra = corr_log.get()
    for i in letra:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNM_1234567890':
            corr_log.delete(letra.index(i), letra.index(i)+1)

def verificar_codigo(event):
    letra = cod.get()
    for i in letra:
        if i not in '1234567890':
            cod.delete(letra.index(i), letra.index(i)+1)

def verificar_codigo2(event):
    letra = cod2.get()
    for i in letra:
        if i not in '1234567890':
            cod2.delete(letra.index(i), letra.index(i)+1)

def verificar_codigo3(event):
    letra = cod3.get()
    for i in letra:
        if i not in '1234567890':
            cod3.delete(letra.index(i), letra.index(i)+1)

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

    cuenta_valid = StringVar()
    cuenta_valid2 = StringVar()

    asiento_entry=ttk.Combobox(ven3, font=("calibri light", 9), state="readonly", values=[
        "Agregar las cuentas"])
    asiento_entry.place(x=10, y=90,width=220)

    combo_2=ttk.Combobox(ven3, font=("calibri light", 9), state="readonly", values=[
        "Agregar las cuentas"])
    combo_2.place(x=10, y=145,width=220)

    num_valid = StringVar()
    cuenta_cod=Entry(ven3, background="ghostwhite", justify="left", textvariable=cuenta_valid, foreground="black", font=("calibri light", 12))   #8
    cuenta_cod.place(x=10, y=30,width=130, height=30)
    cuenta_cod.bind('<KeyRelease>', verificar_codigo)
    cuenta_valid.trace("w", lambda *args: limite3(cuenta_valid))
    boton_acept=ttk.Button(ven3, text="Boton",cursor="hand2")  # command pendiente
    boton_acept.place(x=150, y=30,height=30)
    cuenta_cod2=Entry(ven3, background="ghostwhite", justify="left", textvariable=cuenta_valid2, foreground="black", font=("calibri light", 12))   # 12
    cuenta_cod2.place(x=10, y=200,width=220, height=30)
    cuenta_cod2.bind('<KeyRelease>', verificar_codigo2)
    cuenta_valid2.trace("w", lambda *args: limite4(cuenta_valid2))
    boton_reg=ttk.Button(ven3, text="Regresar", cursor="hand2", command=ven3.destroy)  # command pendiente
    boton_reg.place(x=10, y=400, width=220)
    boton_añadir=ttk.Button(ven3, text="Añadir", cursor="hand2")  # command pendiente
    boton_añadir.place(x=67, y=260,height=30,width=120)
    boton_sig_as=ttk.Button(ven3, text="Siguiente asiento", cursor="hand2")  # command pendiente
    boton_sig_as.place(x=67, y=300, height=30,width=120)
    No_asiento=Entry(ven3, background="ghostwhite", justify="left", textvariable=num_valid, foreground="black", font=("calibri light", 12))   #numeros del siguiente asiento
    No_asiento.place(x=10, y=360, width=30, height=30)
    No_asiento.bind('<KeyRelease>', verificar_codigo3)
    num_valid.trace("w", lambda *args: limite2(num_valid))
    mi_label3 = Label(ven3,
                        text="No. de asiento",
                        bg="azure") 
    mi_label3.place(x=50, y=360,width=80,height=30)

    global cod
    cod = cuenta_cod
    global cod2 
    cod2 = cuenta_cod2
    global cod3 
    cod3 = No_asiento
    
    ven3.mainloop()


ven_login()