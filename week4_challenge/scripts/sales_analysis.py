import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import logging

# 1. Logging Setup
logging.basicConfig(filename='store_sales_analysis.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Loading the dataset...')

# 2. Load Data
store_data = pd.read_csv('store.csv')
sales_data = pd.read_csv('sales.csv')  # Assuming sales data is in a separate CSV

# 3. Data Cleaning
logging.info('Handling missing data...')

# Check for missing values
missing_values = store_data.isnull().sum()
logging.info(f"Missing values in dataset:\n{missing_values}")

# Handling missing values - Example for 'CompetitionDistance'
store_data['CompetitionDistance'].fillna(store_data['CompetitionDistance'].median(), inplace=True)

# Handling missing values for competition open dates
store_data['CompetitionOpenSinceMonth'].fillna(0, inplace=True)
store_data['CompetitionOpenSinceYear'].fillna(0, inplace=True)

# Handling Promo2 columns
store_data['Promo2SinceWeek'].fillna(0, inplace=True)
store_data['Promo2SinceYear'].fillna(0, inplace=True)
store_data['PromoInterval'].fillna('None', inplace=True)

# 4. Merge store and sales data (assuming they share a common column)
merged_data = pd.merge(sales_data, store_data, on='Store')

# 5. Check for outliers in sales
logging.info('Checking for outliers in sales data...')
sns.boxplot(x=merged_data['Sales'])
plt.title('Outliers in Sales')
plt.show()

# Handling outliers: Remove sales = 0 (if needed)
merged_data = merged_data[merged_data['Sales'] > 0]

# 6. Check for distribution in promotions
logging.info('Checking promotion distribution between training and test sets...')
sns.countplot(x='Promo', data=merged_data)
plt.title('Promo Distribution in Dataset')
plt.show()

# 7. Sales behavior before, during, and after holidays
logging.info('Analyzing sales behavior during holidays...')
plt.figure(figsize=(12, 6))
sns.boxplot(x='StateHoliday', y='Sales', data=merged
