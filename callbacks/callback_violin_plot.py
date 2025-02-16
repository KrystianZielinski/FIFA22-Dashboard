from dash import Input, Output
from plots.player_stats.violin_plot import (
    create_violin_plot,
)  # Funkcja generująca scatter_plot
from utils import load_data, filter_main_club, get_top_team, get_league_teams
import pandas as pd


def register_violin_plot_callbacks(app):
    @app.callback(
        Output("violin-plot", "figure"),
        [
            Input("violin-plot-radio", "value"),
            Input("selected-players-store", "data"),
            Input("dropdown-teams", "value"),  # State of selected positions
            Input("dropdown-leagues", "value"),  # State of selected positions
            Input("selected-teams", "data"),
        ],
    )
    def update_violin_plot(
        category, selected_positions, selected_team, selected_leagues, selected_teams
    ):
        if selected_leagues is None:
            violin_plot_fig = create_violin_plot(
                pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), category
            )
            return violin_plot_fig

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
            violin_plot_fig = create_violin_plot(
                teams_in_league, top_club_data, pd.DataFrame(), category
            )
            return violin_plot_fig

        # Generate the updated radar chart based on the selected category and aggregation method
        violin_plot_fig = create_violin_plot(
            teams_in_league, top_club_data, main_club_data, category
        )

        return violin_plot_fig
