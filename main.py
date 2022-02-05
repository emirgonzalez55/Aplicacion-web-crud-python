from flask import Flask,render_template, request, redirect, url_for, flash, session
import mysql.connector
import bcrypt
encriptado = bcrypt.gensalt()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="bd"
)

app = Flask(__name__)
app.secret_key = '$2b$12$39LtIdywYUQLY9VPU4ArteoI6T0cPJsHZKvyWuw2LOEvh8UGwvAq2'

@app.route("/", methods = ["POST", "GET"])
def login():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        password = request.form["password"].encode("utf-8")
        mycursor = mydb.cursor()
        resultados = mycursor.execute("SELECT * FROM usuarios WHERE nombre=%s ",(nombre,))
        datos = mycursor.fetchone()
        print(datos)
    
        if datos != None:
            if bcrypt.checkpw(password, datos[2].encode("utf-8")):
                session['nombre'] = datos[1]
                print(session)
                print(datos[2])
                return redirect(url_for("inicio"))
            else:
                flash('¡El usuario y/o contraseña son incorrectos!')
                return redirect(url_for('login'))
        else:
            flash('¡El usuario y/o contraseña son incorrectos!')
            return redirect(url_for('login'))        

    return render_template('index.html')  

@app.route("/logout")
def logout():
    session.pop('nombre', None)
    return redirect(url_for('login'))
  
@app.route("/registrar", methods = ["POST", "GET"])
def registrar():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        password = request.form["password"]
        password_encode = password.encode("utf-8")
        password_encriptado = bcrypt.hashpw(password_encode ,encriptado)
        mycursor = mydb.cursor()
        sql = "INSERT INTO usuarios (nombre, password) VALUES (%s, %s)"
        mycursor.execute(sql,(nombre, password_encriptado))
        mydb.commit()
        flash('Usuario creado con exito')
        return redirect(url_for('registrar'))
        
    return render_template('registrar.html')

@app.route("/inicio")
def inicio():
    if "nombre" in session:
        return render_template('inicio.html') 
    else:
        return redirect(url_for("login"))

@app.route("/consultas", methods = ["POST", "GET"])
def search():
    if "nombre" in session:
        if request.method == 'POST':
            consulta = request.form["consulta"]
            mycursor = mydb.cursor()
            mycursor.execute ("""SELECT * FROM procesadores WHERE marca LIKE %s OR modelo LIKE %s 
                                UNION SELECT * FROM graficas WHERE marca LIKE %s OR modelo LIKE %s 
                                UNION SELECT * FROM chipsets WHERE marca LIKE %s OR modelo LIKE %s """,("%" + consulta + "%","%" + consulta + "%","%" + consulta + "%","%" + consulta + "%" ,"%" + consulta + "%","%" + consulta + "%")) 
            datos = mycursor.fetchall()
            print(datos)
            if datos != []:
                flash('Resultados de la busqueda.')
                return render_template('consultas.html', resultados = datos)
            else:
                flash('No hay resultados que coincidan con la busqueda.')
                return render_template('consultas.html', resultados = datos)

    else:
        return redirect(url_for("login"))
        
    return render_template('consultas.html') 

@app.route("/procesadores")
def procesadores():
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("SELECT * FROM procesadores") 
        datos = mycursor.fetchall()
        return render_template('procesadores.html', procesadores = datos) 
    else:
        return redirect(url_for("login"))

@app.route("/graficas")
def graficas():
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("SELECT * FROM graficas") 
        datos = mycursor.fetchall()
        return render_template('graficas.html', graficas = datos) 
    else:
        return redirect(url_for("login"))

@app.route("/chipsets")
def chipsets():
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("SELECT * FROM chipsets") 
        datos = mycursor.fetchall()
        return render_template('chipsets.html', chipsets = datos) 
    else:
        return redirect(url_for("login")) 
                        
@app.route("/addcpu", methods = ["POST", "GET"])
def addcpu():
    if "nombre" in session:
        if request.method == 'POST':
            marca = request.form["marca"]
            modelo = request.form["modelo"]
            rendimiento = request.form["rendimiento"]
            mycursor = mydb.cursor()
            sql = "INSERT INTO procesadores (marca, modelo, rendimiento) VALUES (%s, %s, %s)"
            mycursor.execute(sql,(marca, modelo, rendimiento))
            mydb.commit()
            flash('Procesador añadido correctamente')
            return redirect(url_for('addcpu'))
    else:
        return redirect(url_for("login"))   

    return render_template('addcpu.html')  

@app.route("/addgpu", methods = ["POST", "GET"])
def addgpu():
    if "nombre" in session:
        if request.method == 'POST':
            marca = request.form["marca"]
            modelo = request.form["modelo"]
            rendimiento = request.form["rendimiento"]
            mycursor = mydb.cursor()
            sql = "INSERT INTO graficas (marca, modelo, rendimiento) VALUES (%s, %s, %s)"
            mycursor.execute(sql,(marca, modelo, rendimiento))
            mydb.commit()
            flash('Grafica añadida correctamente')
            return redirect(url_for('addgpu'))
    else:
        return redirect(url_for("login"))   

    return render_template('addgpu.html')  

@app.route("/addchipset", methods = ["POST", "GET"])
def addchipset():
    if "nombre" in session:
        if request.method == 'POST':
            marca = request.form["marca"]
            modelo = request.form["modelo"]
            rendimiento = request.form["rendimiento"]
            mycursor = mydb.cursor()
            sql = "INSERT INTO chipsets (marca, modelo, rendimiento) VALUES (%s, %s, %s)"
            mycursor.execute(sql,(marca, modelo, rendimiento))
            mydb.commit()
            flash('Chipset añadido correctamente')
            return redirect(url_for('addchipset'))
    else:
        return redirect(url_for("login"))   

    return render_template('addchipset.html')  

@app.route("/eliminarcpu/<string:id>")
def eliminarcpu(id):
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("DELETE FROM procesadores WHERE id={0}".format(id))
        mydb.commit()
        return redirect(url_for('procesadores'))  
    else:
        return redirect(url_for("login")) 
        
@app.route("/eliminargpu/<string:id>")
def eliminargpu(id):
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("DELETE FROM graficas WHERE id={0}".format(id))
        mydb.commit()
        return redirect(url_for('graficas')) 
    else:
        return redirect(url_for("login")) 

@app.route("/eliminarchipset/<string:id>")
def eliminarchipsets(id):
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("DELETE FROM chipsets WHERE id={0}".format(id))
        mydb.commit()
        return redirect(url_for('chipsets'))         
    else:
        return redirect(url_for("login")) 

@app.route("/editarcpu/<string:id>", methods = ["POST", "GET"])
def editarcpu(id):
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("SELECT * FROM procesadores WHERE id= {0}".format(id))
        datos = mycursor.fetchall()
        print(datos)
        if request.method == 'POST':
            marca = request.form["marca"]
            modelo = request.form["modelo"]
            rendimiento = request.form["rendimiento"]
            mycursor = mydb.cursor()
            mycursor.execute ("UPDATE procesadores SET marca = %s, modelo = %s, rendimiento = %s WHERE id= %s",(marca, modelo, rendimiento, id))
            mydb.commit()
            return redirect(url_for('procesadores'))         
    else:
        return redirect(url_for("login"))  

    return render_template('editarcpu.html', procesador = datos[0])       

@app.route("/editargpu/<string:id>", methods = ["POST", "GET"])
def editargpu(id):
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("SELECT * FROM graficas WHERE id= {0}".format(id))
        datos = mycursor.fetchall()
        print(datos)
        if request.method == 'POST':
            marca = request.form["marca"]
            modelo = request.form["modelo"]
            rendimiento = request.form["rendimiento"]
            mycursor = mydb.cursor()
            mycursor.execute ("UPDATE graficas SET marca = %s, modelo = %s, rendimiento = %s WHERE id= %s",(marca, modelo, rendimiento, id))
            mydb.commit()
            return redirect(url_for('graficas'))     
    else:
        return redirect(url_for("login"))  

    return render_template('editargpu.html', grafica = datos[0]) 

@app.route("/editarchipset/<string:id>", methods = ["POST", "GET"])
def editarchipset(id):
    if "nombre" in session:
        mycursor = mydb.cursor()
        mycursor.execute ("SELECT * FROM chipsets WHERE id= {0}".format(id))
        datos = mycursor.fetchall()
        print(datos)
        if request.method == 'POST':
            marca = request.form["marca"]
            modelo = request.form["modelo"]
            rendimiento = request.form["rendimiento"]
            mycursor = mydb.cursor()
            mycursor.execute ("UPDATE chipsets SET marca = %s, modelo = %s, rendimiento = %s WHERE id= %s",(marca, modelo, rendimiento, id))
            mydb.commit()
            return redirect(url_for('chipsets'))       
    else:
        return redirect(url_for("login"))  

    return render_template('editarchipset.html', chipset = datos[0]) 

if __name__ == "__main__":
	app.run(debug=True)   