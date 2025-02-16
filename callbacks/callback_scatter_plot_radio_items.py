from dash import Input, Output
from utils import get_attributes


def register_scatter_radio_items_callbacks(app):
    # Callback 1: Update 'x' options and value based on category selection
    @app.callback(
        [
            Output("scatter-plot-radio_x", "options"),
            Output("scatter-plot-radio_x", "value"),
        ],
        [Input("category-dropdown", "value")],  # Listen for category change
    )
    def update_x_options(selected_category):
        attributes = get_attributes()  # Get the dictionary of categories and attributes

        # Get the list of options for the selected category
        options = [
            {"label": attr, "value": attr} for attr in attributes[selected_category]
        ]

        # Set default value for x to the first option
        default_value_x = options[0]["value"] if options else None

        return options, default_value_x

    # Callback 2: Update 'y' options based on 'x' value and category selection
    @app.callback(
        [
            Output("scatter-plot-radio_y", "options"),
            Output("scatter-plot-radio_y", "value"),
        ],
        [
            Input("scatter-plot-radio_x", "value"),
            Input("category-dropdown", "value"),
        ],  # Track category change as well
    )
    def update_y_options(selected_x_value, selected_category):
        attributes = get_attributes()  # Get the dictionary of categories and attributes

        # Get the list of options for the selected category
        options = [
            {"label": attr, "value": attr} for attr in attributes[selected_category]
        ]

        # Filter out the selected x value from the y options
        y_options = [opt for opt in options if opt["value"] != selected_x_value]

        # Set the default value for y to the first available option from the filtered y options
        default_value_y = y_options[0]["value"] if y_options else None

        return y_options, default_value_y
