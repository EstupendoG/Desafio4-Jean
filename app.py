from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask('__name__')

# Configurações Banco de Ddos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'yl_fanpage'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

# Adiciona Comentários
@app.route('/add_coment' , methods=['POST'])
def add_coment():
    if request.method == 'POST':
        user_coment = request.form['user_coment']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tb_comentarios (com_texto) VALUES (%s)' , (user_coment,))
        mysql.connection.commit()

        cur.close()
        return redirect(url_for('home'))

# Exibe Comentários
@app.route('/Comentarios')
def coments():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tb_comentarios')
    comentarios = cur.fetchall()
    cur.close()
    return render_template('comentarios.html' , comentarios=comentarios)