from dash import html, dcc


horizontal_bar_plot_section = html.Div(
    [
        dcc.Graph(id="horizontal-bar-plot")  # Scatter plot
    ],
    style={"width": "50%", "margin-top": "15px"},
)  # Plot takes up most of the space
