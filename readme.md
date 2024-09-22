📊 Food Price Analysis and Inflation Forecasting
This project focuses on analyzing food prices over time and predicting future prices. The analysis includes understanding price trends, detecting inflation rates, and suggesting policies based on food price inflation in different regions.

🚀 Project Overview
We have a dataset that contains information about food items, their prices in different regions, and over time. Using this data, we:

Calculate inflation rates for each item.
Visualize the trends and relationships in the data through graphs.
Build a predictive model to forecast future prices.
Suggest policies for food security based on high inflation items.
📂 Dataset
The dataset contains:

Item: Name of the food item (e.g., Rice, Beans, etc.).
Current_Price: The latest price of the food item.
Past_Price: The previous price of the food item.
Month/Year: The time when the prices were recorded.
Region: The region where the data was collected.

🛠️ How to Use
1. Clone the Repository
First, clone this project repository to your local machine:
git clone https://github.com/Bax-dev/Food-Analysis-in-Nigeria-2024-.git
cd food-price-analysis

Install Dependencies
Make sure you have the required Python libraries installed. You can install them using:
pip install pandas matplotlib seaborn numpy scikit-learn statsmodels

.

📈 Key Steps in the Analysis
Descriptive Statistics: Understand the main characteristics of the data, such as average prices and inflation rates.

Missing Value Check: Identifies if there are any missing values in the dataset.

Correlation Heatmap: Visualizes how different numerical columns (like current prices, past prices, inflation) are related.

Price Distribution Plot: Shows how food prices are spread out and identifies common price ranges.

Boxplot: Detects price outliers for each food item to identify any unusual spikes or drops.

Time Series Analysis: Plots price trends over time for different food items in specific regions, such as Lagos.

Predictive Modeling: Uses a linear regression model to predict the average price for the next year (2025).

Policy Suggestions: Highlights items with high inflation rates and suggests policies to control rising prices.

🖼️ Graphs Generated
Correlation Heatmap: Shows how the prices and inflation rates are related.
Price Distribution: Shows how common or rare certain prices are.
Boxplot of Prices: Shows price ranges for each food item and detects any price outliers.
Price Trends Over Time: Shows how food prices change month by month in a specific region (e.g., Lagos).
Inflation Rate Plot: Shows which items have the highest inflation rates by region.
📊 Prediction Model
We use Linear Regression to forecast the future prices. The predicted average price for the year 2025 is shown in the output.

🎯 Policy Suggestions
Items with high inflation rates (above 10%) are flagged, and the project suggests that these items should be subsidized to improve food security.

📥 Contributing
Contributions are welcome! If you find any bugs or want to improve the project, feel free to open an issue or submit a pull request.