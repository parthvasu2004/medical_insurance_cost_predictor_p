**Medical Insurance Cost Predictor**


🔗 Repository: [parthvasu2004/medical_insurance_cost_predictor_p](https://github.com/parthvasu2004/medical_insurance_cost_predictor_p)


🚀 **Overview**


The Medical Insurance Cost Predictor is a machine learning-powered web application designed to estimate the cost of medical insurance based on various factors such as age, BMI, smoking habits, and region. The application utilizes a regression model for prediction and is deployed using Flask.


🛠️ **Features**


✔️ Predicts medical insurance costs based on key health and demographic factors.  

✔️ Machine Learning Model trained using Regression techniques.  

✔️ Flask Web Application with a user-friendly interface.  

✔️ Provides insights into how different factors influence insurance costs.  

✔️ Live Deployment on Render for real-time predictions.  


📂 **Project Structure**


medical_insurance_cost_predictor_p/
│── templates/              # HTML templates for the web app  
│── static/                 # Static files (CSS, images, JS)  
│── app.py                  # Flask web application  
│── insurance.csv           # Preprocessed dataset  
│── regressor.pkl           # Trained ML model  
│── .gitignore              # Ignored files  
│── README.md               # Project documentation  
│── CollabNotebookMCP.ipynb # Jupyter Notebook for training  


⚙️ **Installation & Setup**


1️⃣ Clone the Repository


git clone https://github.com/parthvasu2004/medical_insurance_cost_predictor_p.git
cd medical_insurance_cost_predictor_p


2️⃣ Create & Activate Virtual Environment (Optional but Recommended)


python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows


3️⃣ Install Dependencies


pip install -r requirements.txt


4️⃣ Run the Application


python app.py

Visit `http://127.0.0.1:5000/` in your browser to access the web app.


🎯 **How It Works**


1️⃣ Enter User Details – Input parameters like age, BMI, number of children, smoking habits, and region.

2️⃣ Predict Insurance Cost – The model estimates the expected medical insurance cost.

3️⃣ Data-Driven Insights – Helps individuals and insurance providers understand pricing trends.


🔍 **Machine Learning Model**

- **Algorithm Used:** Regression Model

- **Dataset:** Preprocessed medical insurance dataset (`insurance.csv`).

- **Pretrained Model:** Stored as `regressor.pkl`.


🔗 **Live Deployment**


The application is deployed on Render. https://medical-insurance-cost-predictor-mhp.onrender.com


⚠️ **Important Note:**


🚀 This project is deployed on Render's free-tier hosting, so the website may take **1 to 50 seconds** to load.

📊 The model is trained on a limited dataset, so accuracy may vary based on new data and real-world conditions.  


🤝 **Contribution**


Contributions are welcome! Feel free to fork this repository, create feature branches, and submit pull requests.


📜 **License**


This project is licensed under the MIT License – free to use and modify.

📬 **Contact**

👤 **Parth Vasu**  
📧 parthvasu2004@gmail.com  
🔗 https://www.linkedin.com/in/parth-pandey-3442a9256/

