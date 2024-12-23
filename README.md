# Customer Behavior Analysis

This repository contains a Python script for analyzing customer behavior using a dataset. The analysis explores purchasing patterns, spending habits, and customer segmentation. The dataset includes information such as customer age, product categories, purchase frequency, and more.

## Libraries Used
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib`: For creating visualizations.
- `seaborn`: For statistical data visualization.
- `google.colab`: For file management in Google Colab.

## Data Overview
The dataset consists of the following columns:
- `Customer_ID`: Unique identifier for each customer.
- `Name`: Customer's name.
- `Age`: Customer's age.
- `Gender`: Customer's gender.
- `Location`: Location of the customer.
- `Product_Category`: Category of the product purchased.
- `Product_Name`: Name of the product purchased.
- `Price`: Price of the purchased product.
- `Purchase_Frequency`: How often the customer makes a purchase.
- `Total_Spent`: Total money spent by the customer.
- `Date`: Date of purchase.
- `Purchased_Next`: Whether the customer made a repeat purchase (1 = Yes, 0 = No).

## Analysis Steps
1. **Data Loading and Cleaning**:
   - Data is loaded from a CSV file.
   - Missing values are identified and handled (dropped in this case).

2. **Descriptive Statistics**:
   - Average values of customer age, total spending, and purchase frequency are calculated.

3. **Customer Segmentation**:
   - Customers are segmented by age (18-25, 26-35, 36-45, 46+).
   - Spending analysis by product categories is performed.
   - Purchase frequency comparison across categories is done.

4. **Date Processing**:
   - Dates are converted to datetime objects.
   - Total spending and purchase frequency are calculated monthly.

5. **Repeat vs. Non-Repeat Buyers**:
   - Analysis of spending differences between repeat buyers and non-repeat buyers.

6. **Visualization**:
   - Bar plot showing average spending by product category.
   - Box plot showing expenditure distribution by age segments.

7. **Exporting Results**:
   - Final analysis results are saved to a CSV file.

## Requirements
- Python 3.x
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Google Colab (for file management)

## How to Use
1. Clone the repository to your local machine or use it in a Google Colab environment.
2. Upload your `customer_data.csv` file or specify the path in the script.
3. Run the Python script to generate the analysis and visualizations.
4. Check the saved CSV file (`customer_analysis_results.csv`) for results.
