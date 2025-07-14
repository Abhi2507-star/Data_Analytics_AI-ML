📊 Customer Churn Prediction – Telecom Case Study
This project explores customer churn behavior using exploratory data analysis (EDA) techniques on a telecom dataset. Churn, the tendency of customers to leave a service, is a critical business metric. This analysis uncovers the most influential factors that contribute to customer attrition and provides actionable insights for retention strategies.

📌 Project Objectives
Analyze the churn distribution among telecom customers.

Identify key features correlated with customer churn.

Visualize patterns through univariate and bivariate plots.

Derive data-driven recommendations for reducing churn.

📂 Dataset Information
📄 Source: Telco Customer Churn dataset

📊 Rows: 7,032 entries

🔑 Target: Churn (Yes/No)

Key features include:

Customer demographics (gender, senior citizen, dependents)

Services subscribed (InternetService, OnlineSecurity, etc.)

Account information (Contract type, MonthlyCharges, PaymentMethod)

Tenure and TotalCharges

🛠️ Technologies Used
Python (pandas, numpy)

Visualization (matplotlib, seaborn)

Jupyter Notebook (Google Colab)

CSV data handling

🔍 Exploratory Data Analysis (EDA)
✅ Data Cleaning
Removed unnecessary columns like customerID and unnamed columns

Converted TotalCharges to numeric and handled missing values

Encoded SeniorCitizen as "Yes"/"No"

📈 Univariate & Bivariate Visualizations
Count plots, pie charts, histograms, boxplots

Grouped analysis by Contract type, SeniorCitizen status, Payment method, etc.

Heatmap for correlation analysis

📊 Key Insights
📉 Churn Rate: ~26.6% of customers have churned.

⏳ Tenure: Short-tenure customers are more likely to churn.

📜 Contract: Month-to-month plans have the highest churn.

💳 Payment Method: Customers using Electronic Check churn the most.

📶 Services: Lack of OnlineSecurity and TechSupport strongly correlates with higher churn.

💰 MonthlyCharges: High charges combined with short tenure increase churn risk.

⚧ Gender: No significant effect on churn.

📎 Visual Examples
Churn vs Tenure Distribution (Histogram)

Churn by Contract Type (Stacked Countplot)

Correlation Heatmap

Churn by Services (Multiple subplots)

🧠 Conclusion
This analysis highlights actionable areas for improving customer retention:

Encourage long-term contracts

Provide better onboarding and early engagement

Promote value-added services like OnlineSecurity and TechSupport

Offer discounts for users with higher MonthlyCharges

Target new users (short-tenure) with personalized retention offers
