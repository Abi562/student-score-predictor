# -------------------------------
# Student Score Predictor (Multi-Feature)
# -------------------------------

# Step 0: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Step 1: Create Dataset with Multiple Features
# Features: Hours, Attendance (%), Sleep Hours
data = {
    'Hours': [2, 4, 6, 8, 5, 7],
    'Attendance': [60, 80, 70, 90, 85, 95],  # in %
    'Sleep': [6, 7, 5, 8, 6.5, 7.5],         # hours per day
    'Scores': [45, 60, 75, 85, 70, 88]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Step 2: Visualize Data (optional)
plt.scatter(df['Hours'], df['Scores'], color='blue', label='Hours vs Score')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.title('Study Hours vs Scores')
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend()
plt.show()

# Step 3: Prepare Data
X = df[['Hours', 'Attendance', 'Sleep']]  # Multiple features
y = df['Scores']

# Step 4: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 5: Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate Model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"\nMean Absolute Error on Test Data: {mae:.2f}")

# Step 7: Interactive Prediction
print("\n--- Multi-Feature Student Score Predictor ---")
print("Enter study details in format: Hours,Attendance,Sleep (e.g., 5,90,7)")
print("Type 'exit' to quit.")

while True:
    user_input = input("\nEnter study details: ")
    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
    try:
        values = [float(x.strip()) for x in user_input.split(',')]
        if len(values) != 3:
            print("Please enter exactly 3 values: Hours, Attendance, Sleep")
            continue
        predicted_score = model.predict([values])
        print(f"Predicted Score: {predicted_score[0]:.2f} 🎯")
    except ValueError:
        print("Invalid input! Please enter numbers separated by commas.")