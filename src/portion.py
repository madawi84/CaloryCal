# portion.py
# Turn per-item depth summary into a relative portion estimate

import pandas as pd


class PortionEstimator:
    @staticmethod
    def portion_label(x: float) -> str:
        """Convert a normalised size score into a portion class."""
        if x < 0.33:
            return "small"
        elif x < 0.66:
            return "medium"
        return "large"

    def estimate(self, food_items: list[dict]) -> pd.DataFrame:
        """
        Build a portion summary table from detected food items.

        Parameters
        ----------
        food_items : list[dict]
            List of per-item dictionaries containing area and depth statistics.

        Returns
        -------
        pd.DataFrame
            Portion summary sorted from largest to smallest estimated portion.
        """
        df_food_items = pd.DataFrame(food_items)

        if df_food_items.empty:
            return pd.DataFrame()

        # Relative thickness proxy from depth spread
        df_food_items["depth_range"] = (
            df_food_items["depth_max"] - df_food_items["depth_min"]
        )

        # Relative size score using median depth
        df_food_items["size_score"] = (
            df_food_items["pixel_area"] * df_food_items["depth_median"]
        )

        # Optional alternative using mean depth
        df_food_items["size_score_mean"] = (
            df_food_items["pixel_area"] * df_food_items["depth_mean"]
        )

        # Normalise for easier comparison
        max_size = df_food_items["size_score"].max()
        if max_size > 0:
            df_food_items["size_score_norm"] = df_food_items["size_score"] / max_size
        else:
            df_food_items["size_score_norm"] = 0.0

        # Portion label
        df_food_items["portion_estimate"] = df_food_items["size_score_norm"].apply(
            self.portion_label
        )

        # Select and format final columns
        df_portion = df_food_items[
            [
                "item_index",
                "label",
                "confidence",
                "pixel_area",
                "depth_mean",
                "depth_median",
                "depth_range",
                "size_score",
                "size_score_norm",
                "portion_estimate",
            ]
        ].copy()

        round_cols = [
            "confidence",
            "depth_mean",
            "depth_median",
            "depth_range",
            "size_score",
            "size_score_norm",
        ]
        df_portion[round_cols] = df_portion[round_cols].round(4)

        df_portion = df_portion.sort_values(
            "size_score", ascending=False
        ).reset_index(drop=True)

        return df_portion