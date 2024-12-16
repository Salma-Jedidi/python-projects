# python-projects
# House Price Prediction Model

This notebook explores a house price prediction model using a dataset that includes features such as square footage, number of bedrooms and bathrooms, and additional details like the grade and condition of the house. Below is an outline of the steps taken:

### 1. Data Loading and Initial Exploration
The dataset is loaded from a CSV file containing information about house prices.
Initial exploration includes:
Checking the dataset’s shape.
Reviewing data types, null values, and basic statistics.
### 2. Data Visualization and Insights
Various visualizations were used to analyze key features:
Bedrooms: Most houses have 3 bedrooms, with some outliers having more than 7.
Bathrooms: Includes classifications such as full, half, three-quarter, and quarter bathrooms.
Floors: Column includes floating-point values, indicating partial floors.
Waterfront & View: Mostly constant, suggesting they can be dropped from the model.
Grade: Strongly affects house pricing, as shown in bivariate analysis.
### 3. Multivariable Analysis
Relationships between price and features like sqft_living and sqft_living15 were analyzed.
Renovations were found to increase house prices, with 88% of houses being renovated.
### 4. Correlation and Feature Importance
The correlation matrix revealed:
Features like sqft_living, grade, and sqft_above have the highest positive correlation with price.
### 5. Outlier Detection
Boxplots identified outliers in numerical features such as sqft_living and price.
### 6. Data Preprocessing
Unnecessary columns (e.g., id, date, zipcode) were dropped.
Dataset prepared for training:
StandardScaler was applied to standardize features.
### 7. Model Building and Evaluation
The following models were trained and evaluated:

Linear Regression (LR):
- MAE: 127,896.60
- MSE: 44,093,475,276.57
- RMSE: 209,984.46
- R²: 0.695

Random Forest Regressor (RF):
- MAE: 89,563.64
- MSE: 27,520,251,406.68
- RMSE: 165,892.29
- R²: 0.809

Support Vector Regression (SVR):
- MAE: 226,085.77
- MSE: 153,056,862,412.38
- RMSE: 391,224.82
- R²: -0.060

XGBoost Regressor (XGB):
- MAE: 88,843.66
- MSE: 27,316,613,030.36
- RMSE: 165,277.38
- R²: 0.811


### 8. Final Model Ranking
Label	RSME	R²	Rank
RF_tune	160,202.09	0.822	1st
xgb	165,277.38	0.811	2nd
rf	165,892.29	0.809	3rd
lr	209,984.46	0.695	4th
lr1	214,494.28	0.681	5th
svr	391,224.82	-0.060	6th
### Best Model: RF_tune

# Why?
Lowest RSME: 160,202, indicating the smallest prediction error.
Highest R²: 0.822, meaning it explains the most variance in the data.
# Next Steps
Experiment with other regression models (e.g., Random Forest, XGBoost) and hyperparameter tuning to improve accuracy.
Explore feature engineering techniques, such as:
Handling outliers.
Adding new features to enhance model performance.
