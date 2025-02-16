from dash import html, dcc
from utils import get_attributes

scatter_plot_radio_items_x = html.Div(
    [
        html.H4("X axis", style={"textAlign": "center"}),  # Title above the radio items
        dcc.RadioItems(
            options=[
                {"label": attr, "value": attr}
                for attr in get_attributes()["Physical Condition"]
            ],
            value=get_attributes()["Physical Condition"][0],
            id="scatter-plot-radio_x",
            labelStyle={
                "display": "flex",
                "flexDirection": "row",
                "align-items": "center",
                "margin-bottom": "5px",
            },  # Align text next to radio dot
        ),
    ]
)

scatter_plot_radio_items_y = html.Div(
    [
        html.H4("Y axis", style={"textAlign": "center"}),  # Title above the radio items
        dcc.RadioItems(
            options=[
                {"label": attr, "value": attr}
                for attr in get_attributes()["Physical Condition"]
            ],
            value=get_attributes()["Physical Condition"][1],
            id="scatter-plot-radio_y",
            labelStyle={
                "display": "flex",
                "flexDirection": "row",
                "align-items": "center",
                "margin-bottom": "5px",
            },  # Align text next to radio dot
        ),
    ],
    style={
        "marginTop": "10px"  # Move the container up (adjust as needed)
    },
)


# Radio items container (X and Y close together)
# Radio items container (X and Y stacked vertically)
radio_items_container = html.Div(
    [scatter_plot_radio_items_x, scatter_plot_radio_items_y],
    style={
        "display": "flex",
        "flexDirection": "column",  # Stack items vertically
        "marginTop": "-125px",  # Move the container up (adjust as needed)
    },
)

# Scatter plot section
scatter_plot_section = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id="scatter-plot")  # Scatter plot
            ],
            style={"width": "70%"},
        ),  # Plot takes up most of the space
        html.Div(
            [
                radio_items_container  # Radio items next to the plot
            ],
            style={
                "flex": "0 1 auto",  # Let radio items take only the space they need
                "display": "flex",
                "justify-content": "flex-start",  # Align to the left
                "align-items": "center",  # Align vertically
                "margin-left": "285px",
                "margin-top": "125px",
                "z-index": "10",
            },
        ),  # Optional: Move it slightly more to the left
    ],
    style={"display": "flex", "align-items": "center", "padding": "10px"},
)  # Align plot and radio items horizontally
