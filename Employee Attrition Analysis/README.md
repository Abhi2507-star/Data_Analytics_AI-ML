🧠 Employee Attrition Analysis
This project focuses on analyzing employee attrition using a dataset from a fictional company. Attrition refers to whether employees leave the company (Yes) or stay (No). Through exploratory data analysis, feature engineering, and machine learning, this project identifies the key factors influencing employee attrition and builds a predictive model.

📁 Dataset
The dataset used: WA_Fn-UseC_-HR-Employee-Attrition.csv

Records: 1,470

Features: 35 (such as Age, JobRole, MonthlyIncome, Attrition, etc.)

Target Variable: Attrition (Yes/No)

🔍 Key Steps
1. Exploratory Data Analysis (EDA)
Checked data types, missing values, and unique values

Visualized:

Attrition by department

Age distribution by attrition

Monthly income across job roles

Correlation heatmap

2. Data Cleaning
Removed columns with no predictive power: EmployeeCount, Over18, StandardHours, EmployeeNumber

Label encoded categorical variables

Checked class imbalance (severe imbalance: 237 Yes vs. 1233 No)

3. Feature Engineering & Selection
Selected 25 relevant features based on correlation with attrition and domain understanding

Applied SMOTE to balance the dataset

4. Data Preprocessing
Train-test split (70-30)

Scaled numerical features using StandardScaler

5. Model Building
Used Random Forest Classifier

Achieved 89.3% accuracy

Evaluated using:

Confusion Matrix

Classification Report

Feature Importance

🔑 Top Influential Features
Feature	Impact on Attrition
OverTime	High (working overtime ↑ attrition)
MonthlyIncome	Low income ↑ attrition
StockOptionLevel	Fewer options ↑ attrition
JobSatisfaction	Lower satisfaction ↑ attrition
Age	Younger employees ↑ attrition
WorkLifeBalance	Poor balance ↑ attrition

📊 Visualizations
Count plots, boxplots, and heatmaps used for better insights

Feature importance plotted to highlight most predictive attributes

🛠 Technologies Used
Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)

Jupyter/Google Colab

imbalanced-learn (SMOTE)

📌 How to Run
Clone the repository or open the notebook in Google Colab

Install required libraries (if running locally):

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
Load the dataset

Run each cell in order from top to bottom

📈 Future Improvements
Hyperparameter tuning (e.g., GridSearchCV)

Try other models (XGBoost, SVM)

Add SHAP or LIME for model interpretability
