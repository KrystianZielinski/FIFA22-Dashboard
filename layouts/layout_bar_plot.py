# layouts/radar_layout.py
from dash import html, dcc

bar_plot_section = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id="bar-plot")  # Scatter plot
            ],
            style={"width": "30%", "margin-top": "-10px"},
        )
    ]
)
