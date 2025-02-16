from dash import Input, Output
from utils import load_data, filter_main_club, get_top_team, get_league_teams
from plots.overall_skill.horizontal_bar_plot import create_horizontal_bar_plot
import pandas as pd


def register_horizontal_bar_plot_callbacks(app):
    @app.callback(
        Output("horizontal-bar-plot", "figure"),
        [
            Input("selected-players-store", "data"),
            Input("dropdown-teams", "value"),
            Input("dropdown-leagues", "value"),
        ],
    )
    def update_horizontal_bar_plot(selected_positions, selected_team, selected_leagues):
        data_fifa = load_data("data/fifa22.csv")
        data_league = load_data("data/leagues_clubs.csv")

        # Filter data for two teams (replace with actual filtering logic)
        main_club_data = filter_main_club(data_fifa, selected_team, selected_positions)
        top_club_data = get_top_team(
            data_fifa, data_league, selected_leagues, selected_positions
        )
        teams_in_league = get_league_teams(
            data_fifa, data_league, selected_leagues, selected_positions, main_club_data
        )

        if selected_team is None:
            horizontal_bar_plot_fig = create_horizontal_bar_plot(
                teams_in_league, top_club_data, pd.DataFrame()
            )
            return horizontal_bar_plot_fig

        # Generate the updated radar chart based on the selected category and aggregation method
        bar_plot_fig = create_horizontal_bar_plot(
            teams_in_league, top_club_data, main_club_data
        )

        return bar_plot_fig
