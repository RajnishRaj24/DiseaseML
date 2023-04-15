from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__)

model1 = pickle.load(open('Diabetes_Model.pkl', 'rb'))
model2 = pickle.load(open('Heart_Model.pkl', 'rb'))
model3 = pickle.load(open('Parkinson_Model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

#  ------------- For diabetes page to open --------------------

@app.route('/diabetes-prediction-page')
def diabetes_page():
    return render_template('Diabetes.html')


@app.route('/handle-click')
def handle_click():
    return redirect('/diabetes-prediction-page')

#  ------------- For Heart page to open --------------------

@app.route('/heart-disease-prediction-page')
def heart_page():
    return render_template('Heart.html')


@app.route('/handle-click1')
def handle_click1():
    return redirect('/heart-disease-prediction-page')

#  --------------------- For Parkinson page to open ------------------------

@app.route('/parkinson-disease-prediction-page')
def parkinson_page():
    return render_template('Parkinson.html')


@app.route('/handle-click2')
def handle_click2():
    return redirect('/parkinson-disease-prediction-page')

# ------------------ For BMI Page to open --------------------------

@app.route('/body-mass-index-calculator-page')
def bmi_page():
    return render_template('BMI.html')


@app.route('/handle-click3')
def handle_click3():
    return redirect('/body-mass-index-calculator-page')

@app.route('/contact-us-page')
def contact():
    return render_template('contactus.html')

# ---------------------- Diabetes Predictions ---------------------------


@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    Glucose = int(request.form['Glucose'])
    Blood = int(request.form['Blood'])
    Insulin = int(request.form['Insulin'])
    bmi = int(request.form['BMI'])
    age = int(request.form['Age'])

    output = model1.predict([[Glucose, Blood, Insulin, bmi, age]])

    if output[0] == 0:
        return render_template('Diabetes.html', pred="The Person is not diabetic.")
    else:
        return render_template('Diabetes.html', pred="The person is diabetic.")

# ---------------------- Heart Predictions ---------------------------


@app.route('/prediction1', methods=['POST', 'GET'])
def prediction1():
    age1 = int(request.form['age'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['tbps'])
    cholestrol = int(request.form['chol'])
    thal = int(request.form['thal'])
    slope = int(request.form['slope'])

    output1 = model2.predict([[age1, cp, trestbps, cholestrol, thal, slope]])

    if output1[0] == 0:
        return render_template('Heart.html', predi="The Person has no heart disease.")
    else:
        return render_template('Heart.html', predi="The person has heart disease.")

# ---------------------- Parkinson Predictions ---------------------------


@app.route('/prediction2', methods=['POST', 'GET'])
def prediction2():
    mdvpfhi = float(request.form['mdvpfhi'])
    mdvpflo = float(request.form['mdvpflo'])
    mdvpjitter = float(request.form['mdvpjitter'])
    mdvpshi = float(request.form['mdvpshi'])
    mdvpshidb = float(request.form['mdvpshidb'])
    shiq3 = float(request.form['shiq3'])
    shiq5 = float(request.form['shiq5'])
    mdvpapq = float(request.form['mdvpapq'])
    shidda = float(request.form['shidda'])
    rpde = float(request.form['rpde'])
    spread1 = float(request.form['spread1'])
    spread2 = float(request.form['spread2'])
    d2 = float(request.form['d2'])
    ppe = float(request.form['ppe'])

    output2 = model3.predict([[mdvpfhi, mdvpflo, mdvpjitter, mdvpshi, mdvpshidb,
                             shiq3, shiq5, mdvpapq, shidda, rpde, spread1, spread2, d2, ppe]])

    if output2[0] == 0:
        return render_template('Parkinson.html', predic="The Person has no parkinson.")
    else:
        return render_template('Parkinson.html', predic="The person has parkinson.")

# ---------------------- Main Class ---------------------------


if __name__ == '__main__':
    app.run(debug=True)
