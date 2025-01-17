"""
This is a boilerplate pipeline 'reporting'
generated using Kedro 0.17.5
"""
import pandas as pd
import PIL

from modular_spaceflights.pipelines.reporting.image_utils import DrawTable


def make_price_histogram(model_input_data: pd.DataFrame) -> pd.DataFrame:
    """[summary]

    Returns:
        [type]: [description]
    """
    price_data_df = model_input_data[["price", "engine_type"]]
    return price_data_df


def make_cancel_policy_chart(
    model_input_data: pd.DataFrame, top_counties: int = 20
) -> pd.DataFrame:
    """[summary]

    Args:
        model_input_data (pd.DataFrame): [description]
        top_counties (int, optional): [description]. Defaults to 20.

    Returns:
        pd.DataFrame: [description]
    """
    country_policy_df = (
        model_input_data.groupby(["company_location", "cancellation_policy"])["price"]
        .sum()
        .reset_index()
    )

    high_value_countries = (
        model_input_data.groupby("company_location")
        .price.sum()
        .sort_values()
        .head(top_counties)
        .index
    )

    high_value_filter = country_policy_df.company_location.isin(high_value_countries)
    return country_policy_df[high_value_filter]


def make_price_analysis_image(model_input_table: pd.DataFrame) -> PIL.Image:

    analysis_df = (
        model_input_table.groupby("cancellation_policy")[
            ["price", "review_scores_rating"]
        ]
        .mean()
        .reset_index()
    )

    pil_table = DrawTable(analysis_df)
    return pil_table.image
