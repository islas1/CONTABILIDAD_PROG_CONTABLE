import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk
import time
import functools
from time import sleep

# --------BASE DE DATOS Y FUNCIONES DE ESTA---------

conexion = sqlite3.connect("conta.db")
conexion.execute(
    "CREATE TABLE IF NOT EXISTS login (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), contra VARCHAR(225), corr VARCHAR (255))")

def create_tables():
    db = sqlite3.connect("conta.db")

    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE asientos (id INT(255), cargos VARCHAR(255), abonos VARCHAR(225), debe VARCHAR(255), haber VARCHAR(255))")
        cursor.execute("CREATE TABLE auxiliar (id INT(255), concepto VARCHAR(255), entradas VARCHAR(255), salidas VARCHAR(255), existencias VARCHAR(255), unitario VARCHAR(255), promedio VARCHAR(255), debe VARCHAR(255), haber VARCHAR(255), saldo VARCHAR(255))")
        print("TABLAS CREADAS CORRECTAMENTE")
    except:
        print("LAS TABLAS NO SE CREARON O YA EXISTEN")
        return

create_tables()

# **************--------FUNCIONES PARA EL DISEÑO DEL PROGRAMA-------***********

def centrar(a, wt, ht):
    wtotal = a.winfo_screenwidth()
    htotal = a.winfo_screenheight()
    wventana = wt
    hventana = ht
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)

    a.geometry(str(wventana)+"x"+str(hventana) +
               "+"+str(pwidth)+"+"+str(pheight))
    
#-----DISEÑO DE LOS ENTRY DE LA VENTANA DE LOGIN-----

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

#-----DISEÑO DE LOS ENTRY DE LA VENTANA DE REGISTRO-----

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
        messagebox.showinfo(message="Algún campo sigue vacío, vuelva a intentar", title="Aviso")
    else:
        sign_user()

def validacion_de_login():
    if user_log.get()=="Usuario" or contra_log.get()=="Contraseña" or corr_log.get()=="Correo electronico" or corr_log2.get()=="":
        error()
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
    des1()
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

#*****------------------FUNCIONES DE LA BASE DE DATOS PARA LOS ASIENTOS------------------*****************

def actualizar_as():
    conexion = sqlite3.connect("conta.db")
    fcursor = conexion.cursor()
    no_asiento.config(state="normal")
    sql="SELECT id FROM asientos ORDER BY id desc LIMIT 1"
    try:
        fcursor.execute(sql)
        conexion.commit()
        dat=fcursor.fetchall()
        no_asiento.delete(0, END)
        no_asiento.insert(0, dat)
    except:
        conexion.rollback()
        messagebox.showerror(
            message="dou! No se pudo realizar el registro", title="AVISO DE REGISTRO")

        print("aqui")
        return

    no_asiento.config(state="readonly")

def siguiente_as():
    conexion = sqlite3.connect("conta.db")
    fcursor = conexion.cursor()
    no_asiento.config(state="normal")
    sql="SELECT id FROM asientos ORDER BY id desc LIMIT 1"
    try:
        fcursor.execute(sql)
        conexion.commit()
        dat=fcursor.fetchall()
    except:
        conexion.rollback()
        messagebox.showerror(
            message="dou! No se pudo realizar el registro", title="AVISO DE REGISTRO")
        return
    
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, dat)
    act2=str(res).replace(",","")
    act2=str(act2).replace("(", "")
    act2=str(act2).replace(")", "")
    print(act2)

    global act_
    global act3

    act3=int(act2)
    act_=int(no_asiento.get())
    act=int(no_asiento.get())+1

    no_asiento.delete(0, END)
    no_asiento.insert(0, act)

    if act_>act3:
        no_asiento.delete(0, END)
        no_asiento.insert(0, act_)

    a= TRUE
    debetemp = "500"
    habertemp = "600"
    if a== TRUE :
        messagebox.showinfo(message="El total de haber es de:"+habertemp+" y el total de debe es de: "+debetemp, title="Sumas")


    no_asiento.config(state="readonly")
        
def no_as():
    no_asiento.config(state="normal")
    if no_asiento.get()=="":
        no_asiento.delete(0, END)
        no_asiento.insert(0, "1")
    no_asiento.config(state="readonly")

def actualizacion_as ():
    conexion = sqlite3.connect("conta.db")
    fcursor = conexion.cursor()
    consulta = "SELECT * FROM asientos ORDER BY id desc"
    fcursor.execute(consulta)
    datos = fcursor.fetchall()
    for i in datos:
        lista_asientos.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4],))

def add_as():
    global conteo_ascar
    global conteo_asabon

    conteo_asabon=int()
    conteo_ascar=int()
    conexion = sqlite3.connect("conta.db")
    fcursor = conexion.cursor()

    no_asiento.config(state="normal")

    imp1=importe.get()
    print(imp1)

    importe2 = (format(int(imp1), ',d'))
    no_asiento2=int(no_asiento.get())

    print(no_asiento2, asiento_entry.get(), 0,  importe2, 0)

    if aboncar_box.get()=="CARGOS":
        sql = "INSERT INTO asientos (id, cargos, abonos, debe, haber) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(no_asiento2, asiento_entry.get(), "",  importe2, "")
    elif aboncar_box.get()=="ABONOS":
        sql="INSERT INTO asientos (id, cargos, abonos, debe, haber) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(no_asiento2, "",  asiento_entry.get(), "", importe2)
    
    try:
        fcursor.execute(sql)
        conexion.commit()
    except:
        conexion.rollback()
        messagebox.showerror(
            message="dou! No se pudo realizar el registro", title="AVISO DE REGISTRO")
        return
    
    consulta = "SELECT * FROM asientos ORDER BY id desc"

    filacrud = lista_asientos.get_children()
    for item in filacrud:
        lista_asientos.delete(item)

    fcursor.execute(consulta)
    datos = fcursor.fetchall()
    for i in datos:
        lista_asientos.insert("", 0, text=i[0], values=(
            i[1], i[2], i[3], i[4],))
        
    conexion.close()
    actualizar_as()
    no_asiento.config(state="readonly")

    
#****************--------------------VENTANA DE ERROR--------------------------------------*********************************

def error ():

    try:
        ven1.withdraw()
        ven2.withdraw()
        ven2.withdraw()
    except Exception:
        pass

    global vene
    vene = Toplevel(ven1)
    vene.title ("Ups...error")
    vene.resizable(width=False, height=False)
    vene.geometry('400x450')
    centrar(vene, 400, 450)
    img = Image.open("CONTABILIDAD_PROG_CONTABLE/Mono1.png")
    new_img = img.resize ((300,256))
    render = ImageTk.PhotoImage(new_img)
    img1 = Label(vene, image= render)
    img1.image = render
    img1.place(x=45, y=38)
    miEtiqueta1 = Label(vene, text="Datos incorrectos \n Algun campo sigue vacio, completelo antes de continuar", font=("Times New Roman", 13), fg="gray1")
    miEtiqueta1.pack()

    #se crean los botones
    boton = tk.Button(vene,command=des3, text='Ok entiendo', height=2, width=10)
    boton.place(x=160, y=350)

    vene.protocol("WM_DELETE_WINDOW", des3)

    vene.mainloop()

def error2 ():

    try:
        ven3.withdraw()
    except Exception:
        pass

    global vene2
    vene2 = Toplevel(ven1)
    vene2.title ("Ups...error")
    vene2.resizable(width=False, height=False)
    vene2.geometry('400x450')
    centrar(vene2, 400, 450)
    img = Image.open("CONTABILIDAD_PROG_CONTABLE/Mono1.png")
    new_img = img.resize ((300,256))
    render = ImageTk.PhotoImage(new_img)
    img1 = Label(vene2, image= render)
    img1.image = render
    img1.place(x=45, y=38)
    miEtiqueta1 = Label(vene2, text="Datos incorrectos \n Algun campo sigue vacio, completelo antes de continuar", font=("Times New Roman", 13), fg="gray1")
    miEtiqueta1.pack()

    #se crean los botones
    boton = tk.Button(vene2,command=des4, text='Ok entiendo', height=2, width=10)
    boton.place(x=160, y=350)

    vene2.protocol("WM_DELETE_WINDOW", des4)

    vene2.mainloop()


#****************--------------FUNCIONES PARA LOS ASIENTOS----------------************************

def validar_asientos ():
    if cuenta_cod.get()=="" or asiento_entry.get()=="" or aboncar_box.get()=="" or importe.get()=="":
        error2()
    else:
        add_as()

def validacion_entradas():
    if cuenta_cod.get()=="":
        error2()
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

#****************-------------------ESPACIO DEDICADO A LA DESTRUCCION DE VENTANAS----------------***************************

def des1 ():
    try:
       ven2.destroy()
       ven1.deiconify()
    except Exception:
        pass

def des2 ():
    try:
       ven3.destroy()
       ven1.deiconify()
       siguiente_as()
    except Exception:
        pass

def des3 ():
    try:
       vene.destroy()
       ven1.deiconify()

    except Exception:
        pass

def des4 ():
    try:
       vene2.withdraw()
       ven3.deiconify()
    except Exception:
        pass

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

    try:
        ven3.withdraw()
        ven2.withdraw()
    except Exception:
        pass


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
    Label(ven1, text="Inicia sesión antes de entrar", foreground="gray1", bg="ghost white",
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

    try:
        ven1.withdraw()
        ven3.withdraw()
    except Exception:
        pass


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

    boton_inv=Button(ven2, text="Entrar como invitado", font=("yu gothic ui", 8, "bold underline"), fg="blue4", command=des1, cursor="hand2", activebackground="ghost white", bg="ghost white", bd=0)
    boton_inv.place(width=150, height=25, x=135, y=390)
    
    ven2.protocol("WM_DELETE_WINDOW", des1)
    ven2.mainloop()


#****************--------------VENTANA DE PROMEDIOS------------------*******************

def ven_promedios():
    ventana = Tk()
    ventana.configure(bg="azure")
    ventana.resizable(width=False, height=False)


#****************--------------VENTANA DE ASIENTOS DE DIARIO------------------*******************

def ven_asientos():

    try:
        ven1.withdraw()
        ven2.withdraw()
        vene2.withdraw
    except Exception:
        pass

    global ven3
    ven3 = Tk()
    ven3.title("Programa contable")
    ven3.geometry("1280x720")
    ven3.resizable(width=False, height=False)
    ven3.config(bg="azure")
    w = int(850)
    h = int(450)
    centrar(ven3, w, h)

    global lista_asientos
    global num 

    tabla_asientos = LabelFrame(
        ven3, text=" ASIENTO DE DIARIO ",background="ghostwhite")
    tabla_asientos.grid(row=6, column=20, padx=20, pady=80)
    tabla_asientos.place(x=250, y=0)

    lista_asientos = ttk.Treeview(
        tabla_asientos, height=10, columns=("#1", "#2", "#3", "#4"))
    lista_asientos.grid(row=6, column=0, padx=20, pady=75)

    lista_asientos.heading("#0", text="ID", anchor=CENTER)
    lista_asientos.heading("#1", text="Cargos", anchor=CENTER)
    lista_asientos.heading("#2", text="Abonos", anchor=CENTER)
    lista_asientos.heading("#3", text="Debe", anchor=CENTER)
    lista_asientos.heading("#4", text="Haber", anchor=CENTER)

    lista_asientos.column("#0",  width=50)
    lista_asientos.column("#1",  width=150)
    lista_asientos.column("#2", width=150)
    lista_asientos.column("#3",  width=100)
    lista_asientos.column("#4",  width=100)

    menubar=Menu(ven3,bg="paleturquoise")
    menubasedat=Menu(menubar,tearoff=0)
    menubasedat.add_command(label="Ventana de edicion", command=ven_promedios)
    menubar.add_cascade(label="Editar asientos", menu=menubasedat)



    global cuenta_cod
    global asiento_entry
    global aboncar_box
    global importe
    global no_asiento

    num = 1
    cuenta_valid = StringVar()
    import_valid = StringVar()

    cuenta_cod=Entry(ven3, validate="key", validatecommand=(ven3.register(validate_entry), "%S", "%P"), background="ghostwhite", justify="left", textvariable=cuenta_valid, foreground="black", font=("calibri light", 12))   #codigo
    cuenta_cod.place(x=10, y=30,width=130, height=30)

    asiento_entry=ttk.Combobox(ven3, font=("calibri light", 9), state="readonly", values=[])
    asiento_entry.place(x=10, y=90,width=220)

    aboncar_box=ttk.Combobox(ven3, font=("calibri light", 9), state="readonly", values=[
        "CARGOS", "ABONOS"])
    aboncar_box.place(x=10, y=145,width=220)

    importe=Entry(ven3, validate="key", validatecommand=(ven3.register(validate_entry2), "%S", "%P"), background="ghostwhite", justify="left", textvariable=import_valid, foreground="black", font=("calibri light", 12))   # 12
    importe.place(x=10, y=200,width=220, height=30)

    no_asiento=Entry(ven3, background="ghostwhite", state="readonly", justify="left", foreground="black", font=("calibri light", 12))   #numeros del siguiente asiento
    no_asiento.place(x=10, y=360, width=30, height=30)

    boton_acept=ttk.Button(ven3, text="Agregar",cursor="hand2", command=validacion_entradas)  
    boton_acept.place(x=150, y=30,height=30)

    boton_reg=ttk.Button(ven3, text="Regresar", cursor="hand2", command=des2)  
    boton_reg.place(x=10, y=400, width=220)

    boton_añadir=ttk.Button(ven3, text="Añadir", cursor="hand2", command=validar_asientos) 
    boton_añadir.place(x=67, y=260,height=30,width=120)

    boton_sig_as=ttk.Button(ven3, text="Siguiente asiento", cursor="hand2", command=siguiente_as)  
    boton_sig_as.place(x=67, y=300, height=30,width=120)

    mi_label3 = Label(ven3, text="No. de asiento", bg="azure") 
    mi_label3.place(x=50, y=360,width=80,height=30)

    no_as()
    actualizacion_as()

    ven3.protocol("WM_DELETE_WINDOW", des2)
    ven3.config(menu=menubar)
    ven3.mainloop()

#****************-------------Temporizador------------------*******************

#****************--------------VENTANA PROGRESS BAR--------------******************

ven_login()