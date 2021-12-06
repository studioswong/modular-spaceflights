"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.17.5
"""

from functools import reduce
from operator import add
from typing import Iterable, List

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from modular_spaceflights.pipelines.feature_engineering.nodes import (
    create_static_features,
    create_derived_features,
    joiner,
)


def new_feature_pipeline() -> Pipeline:
    """This function will return a namespaced instance of 
    a pipeline that creates a set of features defined within the 
    `conf/**/*parameters.yml`.

    'Static' features are those plucked directly from the primary layer
    'Derived' features are those constructed by combining two existing columns

    Returns:
        Pipeline: A namespaced instance of a feature engineering pipeline
    """
    static_pipe = Pipeline(
        [
            node(
                func=create_static_features,
                inputs=["prm_shuttle_company_reviews", "params:feature.static"],
                outputs="feat_static_features",
            ),
            node(
                func=create_derived_features,
                inputs=[
                    "prm_spine_table",
                    "prm_shuttle_company_reviews",
                    "params:feature.derived",
                ],
                outputs="feat_derived_features",
            ),
            node(
                func=joiner,
                inputs=[
                    "prm_spine_table",
                    "feat_static_features",
                    "feat_derived_features",
                ],
                outputs="model_input_table",
            ),
        ]
    )
    modular_instance = pipeline(
        pipe=static_pipe,
        inputs=["prm_shuttle_company_reviews", "prm_spine_table"],
        outputs="model_input_table",
        namespace="feature_engineering",
    )
    return modular_instance
