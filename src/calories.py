# calories.py
# Estimate calories from food label + relative portion score

import pandas as pd


class CalorieEstimator:
    def __init__(self):
        # Base calorie reference per food item
        self.calorie_reference = {
            "rice": 206,
            "bread": 80,
            "tomato": 22,
            "carrot": 25,
            "broccoli": 55,
            "potato": 130,
            "cucumber": 16,
            "lettuce": 10,
            "onion": 44,
            "pepper": 24,
            "corn": 96,
            "sauce": 60,
            "fish": 180,
            "shrimp": 99,
            "steak": 250,
            "pork": 242,
            "chicken duck": 239,
            "fried meat": 280,
            "sausage": 301,
            "egg": 78,
            "pasta": 221,
            "noodles": 220,
            "pizza": 285,
            "pie": 320,
            "tofu": 144,
            "apple": 95,
            "banana": 105,
            "orange": 62,
            "grape": 62,
            "strawberry": 33,
            "blueberry": 57,
            "lemon": 17,
            "mango": 99,
            "avocado": 240,
            "watermelon": 46,
            "milk": 103,
            "coffee": 5,
            "juice": 110,
            "tea": 2,
            "ice cream": 137,
            "cake": 257,
            "chocolate": 230,
            "biscuit": 150,
            "french fries": 312,
            "hamburg": 295,
            "salad": 80,
            "soup": 90,
        }
        self.default_calories = 100

    def estimate(self, df_portion: pd.DataFrame) -> tuple[pd.DataFrame, float]:
        """
        Estimate calories from relative portion output.

        Parameters
        ----------
        df_portion : pd.DataFrame
            DataFrame produced by the portion analysis stage.

        Returns
        -------
        tuple[pd.DataFrame, float]
            Final calorie table and total estimated calories.
        """
        if df_portion.empty:
            return pd.DataFrame(), 0.0

        df_calories = df_portion.copy()

        # Map base calories by label
        df_calories["base_calories"] = df_calories["label"].map(self.calorie_reference)
        df_calories["base_calories"] = df_calories["base_calories"].fillna(self.default_calories)

        # Convert relative portion size into a calorie scaling factor
        # small -> lower calories, large -> higher calories
        df_calories["portion_scale"] = 0.5 + df_calories["size_score_norm"]

        # Final estimated calories
        df_calories["estimated_calories"] = (
            df_calories["base_calories"] * df_calories["portion_scale"]
        )

        # Round for readability
        df_calories["base_calories"] = df_calories["base_calories"].round(1)
        df_calories["portion_scale"] = df_calories["portion_scale"].round(2)
        df_calories["estimated_calories"] = df_calories["estimated_calories"].round(1)

        # Final output table
        df_calorie_table = df_calories[
            [
                "label",
                "confidence",
                "pixel_area",
                "depth_median",
                "size_score_norm",
                "portion_estimate",
                "base_calories",
                "portion_scale",
                "estimated_calories",
            ]
        ].copy()

        df_calorie_table = df_calorie_table.sort_values(
            "estimated_calories", ascending=False
        ).reset_index(drop=True)

        total_calories = round(df_calorie_table["estimated_calories"].sum(), 1)

        return df_calorie_table, total_calories