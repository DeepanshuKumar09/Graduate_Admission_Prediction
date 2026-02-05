<div align="center">

# 🎓 Graduate Admission Chance Predictor

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)

**A deep learning-powered tool to estimate graduate admission probability.**

[View Demo](#) · [Report Bug](#) · [Request Feature](#)

</div>

---

## 📖 Project Overview

This project implements a machine learning model to predict the "Chance of Admit" for prospective graduate students based on various academic and personal factors. The prediction model is built using a Keras deep learning neural network and is exposed through an interactive Streamlit web application.

The application serves as a bridge between complex machine learning models and end-users, offering a simple, interactive interface for real-time predictions.

---

## 🚀 Key Components

| Component | Description |
| :--- | :--- |
| **🧠 Neural Network** | A sequential Keras model (`keras_model.keras`) optimized for regression to predict admission chance. |
| **⚖️ Data Scaler** | A `MinMaxScaler` (`minmax_scaler.pkl`) ensuring input data matches training distribution. |
| **💻 Streamlit UI** | An interactive web dashboard (`app.py`) for real-time user input and visualization. |

---

## 🛠️ Features & Inputs

The model analyzes **7 key indicators** to generate a prediction about the chance of admission. These features are categorized below:

<div align="center">

| 📚 Academic Performance | 💡 Experience & Qualifications | 🏫 Institutional Factors |
| :--- | :--- | :--- |
| `GRE Score` | `SOP` (Statement of Purpose Score) | `University Rating` |
| `TOEFL Score` | `LOR` (Letter of Recommendation Score) | `Research` (0/1) |
| `CGPA` | | |

</div>

The Streamlit application allows users to input values for the following features:

-   **GRE Score**: Graduate Record Examinations score.
-   **TOEFL Score**: Test of English as a Foreign Language score.
-   **University Rating**: Rating of the university (e.g., from 1 to 5).
-   **SOP (Statement of Purpose) Score**: Rating of the Statement of Purpose.
-   **LOR (Letter of Recommendation) Score**: Rating of the Letter of Recommendation.
-   **CGPA (Cumulative Grade Point Average)**: Undergraduate CGPA.
-   **Research**: Binary indicator (1 for having research experience, 0 for no research experience).

---

## Prediction Output

The application will display the "Predicted Chance of Admit" as a numerical value between 0.00 and 1.00, representing the probability of admission.


