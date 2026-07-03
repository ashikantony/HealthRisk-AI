from datetime import datetime


class ModelCardGenerator:

    def __init__(
        self,
        model_name,
        version
    ):

        self.model_name = model_name
        self.version = version

    def generate(
        self,
        purpose,
        dataset,
        metrics
    ):

        return {

            "model_name":
                self.model_name,

            "version":
                self.version,

            "created":
                str(
                    datetime.now()
                ),

            "purpose":
                purpose,

            "dataset":
                dataset,

            "metrics":
                metrics,

            "limitations": [
                "Potential data drift",
                "Population bias",
                "Temporal shifts"
            ],

            "ethical_considerations": [
                "Healthcare fairness",
                "Privacy compliance",
                "Responsible AI usage"
            ]
        }

    def export_markdown(
        self,
        card
    ):

        markdown = f"""
# {card['model_name']}

Version: {card['version']}

Created: {card['created']}

## Purpose
{card['purpose']}

## Dataset
{card['dataset']}

## Metrics
{card['metrics']}

## Limitations
{card['limitations']}

## Ethical Considerations
{card['ethical_considerations']}
"""

        return markdown