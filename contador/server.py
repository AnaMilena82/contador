from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# nuestra ruta de índice manejará la representación de nuestro formulari
app.secret_key = 'clavesecretaaqui' # establece una clave secreta

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if 'key_name' in session:
        session['key_name'] +=  1
    else:
        session['key_name'] =  0

    if request.method == 'POST':
        incremento = int(request.form['incremento'])
        session['key_name'] += incremento -1

    return render_template('index.html', counter=session['key_name'])

@app.route('/destroy_session')
def destroy_session():
    session.pop('key_name')		# borra una clave específica
    return redirect("/")	 

@app.route('/incremento_2')
def incremento_2():
    session['key_name'] +=  1
    return redirect("/")       
   

@app.route('/<path:path>') #Asegúrate de que si el usuario escribe cualquier ruta distinta a las especificadas, reciba un mensaje de error que diga "¡Lo siento! No hay respuesta. Inténtalo otra vez.”.
def error(path):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'

    






if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

