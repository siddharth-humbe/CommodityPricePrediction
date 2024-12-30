# **Time Series Analysis and Forecasting of Sugar Prices**

This repository focuses on analyzing and forecasting sugar prices using time series methodologies like ARMA, ARIMA, and SARIMA. It includes modules for scraping, preprocessing, visualizing, and forecasting data with detailed steps and outputs.

## **Features**

1. **Data Collection:**
   - Web scraping sugar price data from [IndexMundi](https://www.indexmundi.com/commodities/?commodity=sugar&months=360) using `BeautifulSoup`.

2. **Exploratory Data Analysis (EDA):**
   - Understand trends, seasonality, and patterns in the data.
   - Generate visualizations for better insights.

3. **Time Series Modeling:**
   - Train ARMA, ARIMA, and SARIMA models for forecasting.
   - Evaluate models using statistical and machine learning metrics.

4. **Forecasting:**
   - Use the best-performing model for future price predictions.
   - Visualize and analyze the accuracy of predictions.

---

## **Installation and Usage**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/siddharth-humbe/CommodityPricePrediction.git
2.	Install Dependencies:
  Install Python libraries from requirements.txt:
  pip install -r requirements.txt
3.	Run the Project:
  Execute the main script:
    python main.py
4.	Pre-trained Models:
  Load pre-trained SARIMA models from the models/ folder for instant forecasting.

Dependencies

Required Python libraries:
	•	pandas
	•	numpy
	•	matplotlib
	•	statsmodels
	•	scikit-learn
	•	BeautifulSoup
	•	requests
	•	nltk

Install all dependencies via:
  pip install -r requirements.txt


Visualizations

  1.	Seasonality Decomposition:
Shows patterns of seasonality and trends over time.
	2.	Forecasting Results:
Predicted prices over time with SARIMA and actual data comparison.

Insights

1.	Trends and Patterns:
  •	Significant price increases between 2009-2011, likely driven by market factors.
  •	Prices are relatively higher in the last 15 years compared to the first 15 years.
2.	Seasonality:
  •	Repeating patterns of price fluctuations, indicating predictable seasonal behaviors.
3.	Model Performance:
  •	SARIMA was the most accurate model, capturing seasonality effectively.

Future Enhancements

•	Integrate external factors (e.g., weather conditions, economic indicators).
•	Apply deep learning approaches for advanced forecasting.

  
