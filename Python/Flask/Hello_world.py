from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is a simple Flask application.'

@app.route('/user/<username>')
def show_user_(username):
    return f'User: {username}'

@app.route('/mail/<nombre>/<correo>')
@app.route('/mail/<nombre>/<correo>/<telefono>')
def show_email(nombre, correo, telefono=None):
    datos ={
        'nombre': nombre,
        'correo': correo,
        'telefono': telefono
    }
    return render_template('email.html', **datos)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/confirmacion', methods=['POST'])
def confirmacion():
    if request.method == 'POST':
        usuario = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form.get('telefono', 'No proporcionado')
        datos = {
            'nombre': usuario,
            'correo': correo,
            'telefono': telefono
        }
        return render_template('confirmacion.html', **datos)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)