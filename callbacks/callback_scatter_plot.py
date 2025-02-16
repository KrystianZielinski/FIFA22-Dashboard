from dash import Input, Output
from plots.player_stats.scatter_plot import (
    create_scatter_plot,
)  # Funkcja generująca scatter_plot
from utils import load_data, filter_main_club, get_top_team, get_league_teams
import pandas as pd


def register_scatter_callbacks(app):
    @app.callback(
        Output("scatter-plot", "figure"),  # Output to the radar chart
        [
            Input(
                "scatter-plot-radio_x", "value"
            ),  # Selected X-axis attribute from radio buttons
            Input(
                "scatter-plot-radio_y", "value"
            ),  # Selected Y-axis attribute from radio buttons
            Input("selected-players-store", "data"),  # State of selected positions
            Input("dropdown-teams", "value"),
            Input("dropdown-leagues", "value"),  # State of selected positions
            Input("selected-teams", "data"),
        ],
    )
    def update_scatter_plot(
        x_category,
        y_category,
        selected_positions,
        selected_team,
        selected_leagues,
        selected_teams,
    ):
        if selected_leagues is None:
            scatter_plot_fig = create_scatter_plot(
                pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), x_category, y_category
            )
            return scatter_plot_fig

        # Load dataset (replace with your actual data loading logic)
        data_fifa = load_data("data/fifa22.csv")
        data_league = load_data("data/leagues_clubs.csv")

        # Filter data for two teams (replace with actual filtering logic)
        main_club_data = filter_main_club(data_fifa, selected_team, selected_positions)
        top_club_data = get_top_team(
            data_fifa, data_league, selected_leagues, selected_positions
        )
        teams_in_league = get_league_teams(
            data_fifa,
            data_league,
            selected_leagues,
            selected_positions,
            main_club_data,
            selected_teams,
        )

        if selected_leagues is not None and selected_team is None:
            scatter_plot_fig = create_scatter_plot(
                teams_in_league, top_club_data, pd.DataFrame(), x_category, y_category
            )
            return scatter_plot_fig

        # Generate the updated radar chart based on the selected category and aggregation method
        scatter_plot_fig = create_scatter_plot(
            teams_in_league, top_club_data, main_club_data, x_category, y_category
        )

        return scatter_plot_fig
