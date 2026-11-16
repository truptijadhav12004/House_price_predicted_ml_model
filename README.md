
# 🏡 House Price Prediction Using Machine Learning

## 📌 Project Overview
This project is a Machine Learning-based web application that predicts house prices using the California Housing Dataset.

It uses Linear Regression to estimate house values based on different housing features. An interactive web interface is developed using Streamlit.

## 🎯 Project Objectives
- Predict house prices using Machine Learning.
- Perform Exploratory Data Analysis (EDA).
- Apply data preprocessing and feature scaling.
- Train and evaluate a Linear Regression model.
- Build an interactive web application for predictions.

## 📊 Dataset Information
- **Dataset:** California Housing Dataset
- **Source:** Scikit-learn
- **Total Records:** 20,640
- **Total Features:** 8
- **Target Variable:** MedHouseVal

The dataset is loaded using `fetch_california_housing` from Scikit-learn. No separate CSV file is required.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Linear Regression
- MinMaxScaler
- Streamlit
- Pickle

## 🤖 Machine Learning Algorithm
**Linear Regression**

Linear Regression is used to predict house values based on input housing features.

## ⚙️ Project Workflow
1. Load the California Housing Dataset.
2. Perform data cleaning and preprocessing.
3. Conduct Exploratory Data Analysis (EDA).
4. Apply feature scaling.
5. Split data into training and testing sets.
6. Train the Linear Regression model.
7. Evaluate model performance.
8. Save the trained model using Pickle.
9. Develop an interactive application using Streamlit.

## 📁 Project Structure

```text
House_price_predicted_ml_model/
│
├── Housing Price Prediction Using Machine Learning.ipynb
├── app.py
├── chatgpt_for_house.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

## 🚀 How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/truptijadhav12004/House_price_predicted_ml_model.git
```

### Step 2: Open Project Folder

```bash
cd House_price_predicted_ml_model
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run Streamlit Application

```bash
streamlit run app.py
```

## 🌐 Live Application

[Click Here to View House Price Prediction App](https://housepricepredictedmlmodel-l3erqt4z9qvznhia4dgwlm.streamlit.app/)

## 📌 Model Evaluation

The model is evaluated using regression performance metrics such as:
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## 👩‍💻 Author

**Trupti Jadhav**

GitHub: [truptijadhav12004](https://github.com/truptijadhav12004)

---

⭐ If you find this project useful, feel free to explore the repository!
