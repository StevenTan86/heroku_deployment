from types import MethodType
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('dib_79.pkl')

@app.route('/')
def HelloWorld():
    return render_template('home.html')

@app.route('/predict', methods=['post'])
def predict():
    preg  = request.form.get('preg')
    plas = request.form.get('plas')
    pres  = request.form.get('pres')
    skin = request.form.get('skin')
    test  = request.form.get('test')
    mass = request.form.get('mass')
    pedi  = request.form.get('pedi')
    age = request.form.get('age')

    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if output[0] == 0:
        ans = 'No Diabetis'
    else:
        ans = 'Diabetis'
    
    return render_template('home.html', pred=ans)

@app.route('/welcome')
def Welcome():
    return render_template('welcome.html')

@app.route('/contact')
def Contact():
    return render_template('contact.html')

@app.route('/blog')
def Blog():
    return render_template('blog.html')

@app.route('/gallery')
def Gallery():
    return render_template('gallery.html')

app.run(debug=True)
