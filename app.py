from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
with open('regressor.pkl', 'rb') as file:
    regressor = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    age = int(request.form['age'])
    gender = int(request.form['gender'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker'])
    region = int(request.form['region'])

    # Create input array
    input_data = np.array([[age, gender, bmi, children, smoker, region]])
    prediction = regressor.predict(input_data)
    output = prediction[0] * 82.91  # Assuming 1 USD = 82.91 INR, update the conversion rate as needed
    output = round(output, 2)

    return str(output)

if __name__ == '__main__':
    app.run(debug=True)
