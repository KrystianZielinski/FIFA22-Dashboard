from dash import Input, Output
from utils import get_attributes


def register_violin_radio_items_callbacks(app):
    @app.callback(
        [
            Output("violin-plot-radio", "options"),
            Output("violin-plot-radio", "value"),
        ],  # Update both options and default value
        [Input("category-dropdown", "value")],  # Input from the dropdown selection
    )
    def update_violin_radio_items(selected_category):
        attributes = get_attributes()  # Get the dictionary of categories and attributes
        # Get the list of options for the selected category
        options = [
            {"label": attr, "value": attr} for attr in attributes[selected_category]
        ]

        # Set the default value to the first attribute in the selected category
        default_value = options[0]["value"] if options else None

        return options, default_value
