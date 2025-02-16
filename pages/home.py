from dash import html
from layouts.dropdown import dropdown_list
from layouts.layout_dropdown_leagues import dropdown_leagues
from layouts.layout_dropdown_teams import dropdown_teams
from layouts.layout_radar_plot import radar_plot_section
from layouts.layout_scatter_plot import scatter_plot_section
from layouts.layout_pitch import football_pitch_layout
from layouts.layout_violin_plot import violin_plot_section
from layouts.layout_bar_plot import bar_plot_section
from layouts.layout_horizontal_bar_plot import horizontal_bar_plot_section
from layouts.layout_league_slider import league_slider
from layouts.layout_nested_pie_plot import nested_pie_plot_section
from layouts.title_bar_layout import title_bar
import dash

# Register the page to be shown at the root path
dash.register_page(__name__, path="/")  # Make sure this is for the home page
# Title bar (optional: you can move this into app.py if you want the title bar common to all pages)

# Home page layout
layout = html.Div(
    [
        title_bar,  # The title bar is now part of the home page layout
        html.Div(
            [
                # First column: League & Team select dropdowns
                html.Div(
                    [
                        dropdown_leagues,
                        dropdown_teams,
                        html.Div(
                            horizontal_bar_plot_section,
                            style={"align-self": "center", "padding-top": "20px"},
                        ),
                        html.Div(
                            league_slider,
                            style={"align-self": "left", "padding-top": "20px"},
                        ),
                    ],
                    style={
                        "width": "15%",
                        "display": "flex",
                        "borderRadius": "15px",
                        "boxShadow": "0 4px 8px rgba(10, 10, 10, 0.5)",
                        "padding": "20px",
                        "justify-content": "top",
                        "flexDirection": "column",
                    },
                ),
                # Second column: Football Pitch
                html.Div(
                    [football_pitch_layout, nested_pie_plot_section],
                    style={
                        "width": "18%",
                        "display": "flex",
                        "borderRadius": "15px",
                        "boxShadow": "0 4px 8px rgba(10, 10, 10, 0.5)",
                        "padding": "20px",
                        "justify-content": "top",
                        "alignItems": "center",
                        "flexDirection": "column",
                        "margin-right": "15%",
                    },
                ),
                # Third column: Plots
                html.Div(
                    style={
                        "width": "65%",
                        "borderRadius": "15px",
                        "boxShadow": "0 4px 8px rgba(10, 10, 10, 0.5)",
                        "padding": "20px",
                        "marginLeft": "-15%",
                    },
                    children=[
                        html.Div(
                            [dropdown_list],
                            style={
                                "width": "80%",
                                "margin-bottom": "20px",
                                "margin-left": "12px",
                            },
                        ),  # Margin for spacing
                        # Plots section
                        html.Div(
                            [
                                html.Div(
                                    [scatter_plot_section, violin_plot_section],
                                    style={
                                        "width": "48%",
                                        "display": "flex",
                                        "flexDirection": "column",
                                    },
                                ),
                                html.Div(
                                    [radar_plot_section, bar_plot_section],
                                    style={"width": "48%", "margin-left": "200px"},
                                ),
                            ],
                            style={
                                "display": "flex",
                                "justify-content": "space-between",
                            },
                        ),  # Side-by-side columns
                    ],
                ),
            ],
            style={
                "display": "flex",
                "justify-content": "space-between",
                "marginTop": "20px",
            },
        ),
    ],
    style={"display": "flex", "flexDirection": "column", "width": "100%"},
)
