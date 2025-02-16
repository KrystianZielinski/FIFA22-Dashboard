from dash import html, dcc
from utils import get_attributes

violin_plot_radio_items = html.Div(
    [
        # Title above the radio items (X axis)
        html.H4(
            "Skill", style={"textAlign": "center"}
        ),  # You can adjust style as needed
        dcc.RadioItems(
            options=[
                {"label": attr, "value": attr}
                for attr in get_attributes()["Physical Condition"]
            ],  # Default options
            value=get_attributes()["Physical Condition"][0],  # Default selected value
            id="violin-plot-radio",  # ID for the widget
            labelStyle={
                "display": "flex",
                "flexDirection": "row",
                "align-items": "center",
                "margin-bottom": "5px",
            },  # Optional styling
        ),
    ],
    style={
        "marginTop": "-100px"  # Move the container up (adjust as needed)
    },
)

# Scatter plot section
violin_plot_section = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id="violin-plot")  # Scatter plot
            ],
            style={"width": "70%"},
        ),  # Plot takes up most of the space
        html.Div(
            [
                violin_plot_radio_items  # Radio items next to the plot
            ],
            style={
                "flex": "0 1 auto",  # Let radio items take only the space they need
                "display": "flex",
                "justify-content": "flex-start",  # Align to the left
                "align-items": "center",  # Align vertically
                "margin-left": "285px",
                "margin-top": "75px",
                "z-index": "10",
            },
        ),
    ],
    style={"display": "flex", "align-items": "center", "padding": "10px"},
)  # Align plot and radio items horizontally
