from src.portion import PortionEstimator
from src.calories import CalorieEstimator

portion_estimator = PortionEstimator()
calorie_estimator = CalorieEstimator()

df_portion = portion_estimator.estimate(food_items)
df_calorie_table, total_calories = calorie_estimator.estimate(df_portion)