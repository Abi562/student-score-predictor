Student Score Predictor using Machine Learning (Python)


Project Overview

Students often wonder:
"If I study more hours, how much can I score in exams?"

This project predicts a student’s exam score using Machine Learning (Linear Regression) based on study hours, attendance, and sleep hours. It also allows interactive predictions and includes visualizations to show the relationship between study habits and exam performance.



Objective

Demonstrate the relationship between study habits and exam scores.

Build a model to predict future scores based on study patterns.

Make the project interactive, allowing users to input study details and get predicted scores instantly.



Tools & Libraries Used

Python – Programming language

Pandas & NumPy – Data handling and manipulation

Matplotlib – Data visualization

Scikit-learn – Machine Learning library


Dataset

A sample dataset is used with the following columns:

Hours	Attendance (%)	Sleep (hrs)	Scores

2	60	6	45
4	80	7	60
6	70	5	75
8	90	8	85
5	85	6.5	70
7	95	7.5	88


Workflow / Steps

1. Data Preparation

Collected data on study hours, attendance, sleep, and scores.

Handled dataset using Pandas.



2. Data Visualization

Plotted scatter plot of study hours vs scores.

Observed linear trend → suitable for Linear Regression.



3. Model Training

Split data into training (80%) and testing (20%) sets.

Trained Linear Regression model using scikit-learn.



4. Prediction & Evaluation

Predicted scores for new inputs.

Calculated Mean Absolute Error (MAE) for model accuracy.

Example: Predicted Score for 9.5 hours, 95% attendance, 7.5 hrs sleep ≈ 92.5 marks.



5. Interactive Prediction

User can enter study hours, attendance, and sleep hours to get instant predictions.



6. Visualization of Regression Line

Scatter plot with regression line shows the trend between study habits and scores.



Python Code Highlights

# Example: Multi-Feature Prediction
X = df[['Hours', 'Attendance', 'Sleep']]
y = df['Scores']
model = LinearRegression()
model.fit(X_train, y_train)

# Interactive prediction
hours = 7
attendance = 95
sleep = 7.5
predicted_score = model.predict([[hours, attendance, sleep]])
print(f"Predicted Score: {predicted_score[0]:.2f}")

> Full code is included in the interactive_score_predictor.py file.





Results & Learning

✅ More study hours, higher attendance, and proper sleep → higher predicted scores.
✅ Learned to handle datasets with Pandas.
✅ Learned data visualization using Matplotlib.
✅ Applied Linear Regression for multi-feature prediction.
✅ Built interactive prediction program for users.


Real-Life Use Case

Predict student performance based on study habits.

Can be extended with more features like revision hours, assignment scores, or extra-curricular activities.

Useful for teachers and students to understand study patterns and plan accordingly.


Future Enhancements

Include more features such as revision hours, assignment completion, and participation.

Use a larger real dataset for better accuracy.

Deploy as a web app using Streamlit or Flask for interactive user access.



Skills & Tools Demonstrated

Python Programming

Machine Learning – Linear Regression

Data Handling – Pandas & NumPy

Data Visualization – Matplotlib

Model Evaluation – Mean Absolute Error
