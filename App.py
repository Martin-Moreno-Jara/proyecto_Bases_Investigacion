from flask import Flask, render_template, request,redirect,url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rraxxerr420'
app.config['MYSQL_DB'] = 'prueba'
mysql=MySQL(app)

app.secret_key='mysecretkey'

@app.route('/')
def index():
    return "Index de la pagina"
@app.route('/login')
def page_login():
    cur= mysql.connection.cursor()
    cur.execute("select * from usuario")
    data =cur.fetchall()
    print(data)
    return render_template("index.html",usuarios=data)

@app.route('/register', methods=['POST'])
def page_register():
    if request.method =='POST':
        usuario =request.form['usuario']
        contra =request.form['contraseña']
        rol =request.form['rol']
        cur =mysql.connection.cursor()
        cur.execute('INSERT INTO usuario values (%s,%s,%s)',(usuario,contra,rol))
        mysql.connection.commit()
        flash('Usuario registrado')
        return redirect(url_for('page_login'))

@app.route('/estudiante/<string:id>')
def page_estudiante(id):
        cur =mysql.connection.cursor()
        cur.execute("DELETE FROM usuario WHERE nombre LIKE '{0}'".format(id))
        mysql.connection.commit()
        print(id)
        flash("Persona removida de la existencia")
        return redirect(url_for("page_login"))
    
@app.route('/profesor')
def page_profesor():
    return "Pagina de profesores"
@app.route('/empleado')
def page_empleado():

    return "pagina de empleados"
@app.route('/grupo')
def page_grupo():
    return "pagina del grupo de investigación"

if __name__=="__main__":
    app.run(port=3000,debug=True)