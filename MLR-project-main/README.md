# Car Fuel Efficiency Prediction

## Overview

This project develops a **Multiple Linear Regression (MLR) model** to predict **Fuel Information.City MPG (Miles Per Gallon)** using key numerical features from the `cars.csv` dataset. The primary objective is to analyze how different car specifications impact fuel efficiency. The model is implemented in **Python** using Jupyter Notebook, following a structured workflow of data preprocessing, feature selection, and model evaluation.

## Dataset: cars.csv

The dataset contains a variety of car specifications, including **engine performance metrics, dimensions, and fuel efficiency data**. The target variable in this analysis is:

- **Fuel Information.City MPG** (City Miles Per Gallon), which represents the car’s fuel efficiency in urban driving conditions.

### Selected Features

Feature selection was performed using **correlation analysis** and **Variance Inflation Factor (VIF) scores** to ensure meaningful predictors without multicollinearity. The final selected features include:

- **Engine Information.Engine Statistics.Horsepower** – Affects engine power and fuel consumption.
- **Engine Information.Engine Statistics.Torque** – Influences acceleration and efficiency.
- **Dimensions.Height** – Impacts air resistance and vehicle weight.
- **Dimensions.Length** – Contributes to overall aerodynamics.
- **Dimensions.Width** – Affects stability and efficiency.
- **Engine Information.Number of Forward Gears** – Impacts gear ratio and fuel efficiency.
- **Fuel Information.Highway MPG** – Strongly correlated with city MPG.
- **Identification.Year** – Accounts for technological advancements in fuel efficiency.

## Model Development

The workflow for this project includes:

### 1. Data Preprocessing

- Handled missing values and removed duplicate records.
- Identified categorical and numerical variables.
- Scaled numerical features for consistency in model performance.
- Removed outliers using **the IQR method**.

### 2. Feature Selection

- Applied **correlation analysis** to determine relationships between variables.
- Used **VIF scores** to eliminate multicollinearity among predictors.
- Selected optimal features to improve model interpretability and accuracy.

### 3. Model Training & Evaluation

- Implemented **Multiple Linear Regression** using selected features.
- Assessed model performance using key regression metrics:

## Performance Results

| Model Version | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) | R-squared (R²) |
| ------------- | ------------------------- | ------------------------------ | -------------- |
| Final Model   | 0.2093                    | 0.2765                         | 0.9244         |

### Insights from Results

- The model explains **92.44%** of the variance in City MPG, indicating a strong fit.
- **Engine power, dimensions, and the number of forward gears significantly affect fuel efficiency.**
- Outlier removal and feature selection enhanced the model’s reliability and predictive power.
- The final model offers accurate and interpretable predictions for fuel efficiency.

## Files Included

- `cars.csv` – Dataset containing car specifications.
- `Multiple_Linear_Regression_Analysis.ipynb` – Jupyter Notebook with complete preprocessing, feature selection, model training, and evaluation.
- `README.md` – This documentation file.

## Conclusion

This project demonstrates how **feature selection, outlier removal, and proper preprocessing improve regression model accuracy**. The final **MLR model provides reliable predictions** of City MPG based on key vehicle characteristics. Future enhancements could involve **advanced regression techniques** or **additional feature engineering**.

## Author

**Raha Billa**

