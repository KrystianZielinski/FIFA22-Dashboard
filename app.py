# app.py
from dash import Dash, html

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash
from callbacks.callback_radar_plot import register_radar_callbacks
from callbacks.callback_scatter_plot import register_scatter_callbacks
from callbacks.callback_scatter_plot_radio_items import (
    register_scatter_radio_items_callbacks,
)
from callbacks.callback_football_pitch import register_pitch_plot_callbacks
from callbacks.callback_violin_plot import register_violin_plot_callbacks
from callbacks.callback_violin_plot_radio_items import (
    register_violin_radio_items_callbacks,
)
from callbacks.callback_dropdown_league_team import register_dropdown_league_team
from callbacks.callback_bar_plot import register_bar_plot_callbacks
from callbacks.callback_horizontal_bar_plot import (
    register_horizontal_bar_plot_callbacks,
)
from callbacks.callback_nested_pie_plot import register_nested_pie_plot_callbacks
from callbacks.callback_slider import register_slider_callbacks
from callbacks.callback_selected_skills_text import register_callback_skills_text

# loads the "darkly" template and sets it as the default
load_figure_template("darkly")

# Title bar
title_bar = html.Div(
    children=[
        html.H1(
            "FIFA 22",
            style={
                "textAlign": "left",
                "color": "#ffffff",
                "padding": "1px",
                "paddingLeft": "75px",
            },
        )
    ],
    style={
        "backgroundColor": "#262626",  # Dark gray background
        "width": "100%",
        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",  # Subtle shadow
    },
)

# Initialize the Dash app
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.DARKLY])

# Main layout - only needs to include the navigation and page container
app.layout = html.Div(
    [
        dash.page_container  # Dynamically loads the content of the current page based on the URL
    ]
)

# Register the callbacks
register_radar_callbacks(app)
register_scatter_callbacks(app)
register_scatter_radio_items_callbacks(app)
register_pitch_plot_callbacks(app)
register_violin_plot_callbacks(app)
register_violin_radio_items_callbacks(app)
register_dropdown_league_team(app)
register_bar_plot_callbacks(app)
register_horizontal_bar_plot_callbacks(app)
register_slider_callbacks(app)
register_callback_skills_text(app)
register_nested_pie_plot_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
