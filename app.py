from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')
@app.route('/respuesta', methods= ['POST'])
def respuesta():
    if request.method == 'POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2']) 
        suma = n1+n2
        return render_template('formulario.html', res=suma)           

@app.route('/nombres', methods= ['POST'])
def nombres():
    if request.method == 'POST':
        nombre = request.form['name']
        rol = request.form['rol']
        tel = request.form['tel']
        mail = request.form['mail']
        usu= nombre,rol,tel,mail,
        return render_template('index.html', usu=usu) 

 

if __name__ == '__main__':
    app.run(debug=True)