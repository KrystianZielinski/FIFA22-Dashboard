from dash import html, dcc

nested_pie_plot_section = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id="nested-pie-plot")  # Scatter plot
            ],
            style={"marginTop": "20px"},
        )
    ]
)
