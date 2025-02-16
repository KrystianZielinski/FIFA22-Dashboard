# layouts/radar_layout.py
from dash import html, dcc

avg_median_radio_items = html.Div(
    [
        dcc.RadioItems(
            options=[  # List of options should be dictionaries
                {"label": "Average", "value": "Average"},  # Correct format
                {"label": "Median", "value": "Median"},
            ],
            value="Average",  # Default selected value
            id="avg-median-radio",  # ID for the widget
            labelStyle={
                "display": "inline-block",
                "margin-right": "10px",
                "font-size": "20px",
            },  # Optional styling
        ),
    ],
    style={
        "position": "relative",  # Position relative to its container
        "top": "-560px",  # Move it up
        "left": "380px",
        "text-align": "left",  # Center the radio items horizontally
        "margin-bottom": "5px",  # Add some space below the radio items
    },
)

radar_plot_section = html.Div(
    [dcc.Graph(id="radar-chart"), avg_median_radio_items],
    style={"width": "30%", "padding": "0px", "margin-top": "-120px"},
)
