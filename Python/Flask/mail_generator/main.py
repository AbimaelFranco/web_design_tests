from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/form')
def form():
    return render_template('formulario.html')

@app.route('/confirmacion', methods=['POST'])
def confirmacion():
    if request.method == 'POST':
        nombre= request.form['nombre']
        email= request.form['email']
        telefono= request.form.get('telefono')
        empresa= request.form['empresa']
        plaza= request.form['plaza']
        
        datos = {
        'nombre': nombre,
        'correo': email,
        'telefono': telefono,
        'empresa': empresa,
        'plaza': plaza
        }

        return render_template('correo.html', **datos)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)