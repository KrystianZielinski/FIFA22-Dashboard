from dash import Input, Output
from plots.player_stats.radar_chart import create_radar_chart
from utils import load_data, filter_main_club, get_top_team, get_league_teams
import pandas as pd


def register_radar_callbacks(app):
    @app.callback(
        Output("radar-chart", "figure"),  # Output to the radar chart
        [
            Input("category-dropdown", "value"),
            Input("avg-median-radio", "value"),
            Input("selected-players-store", "data"),
            Input("dropdown-teams", "value"),
            Input("dropdown-leagues", "value"),
            Input("selected-teams", "data"),
        ],
    )
    def update_radar_chart(
        selected_category,
        aggregation_method,
        selected_positions,
        selected_team,
        selected_leagues,
        selected_teams,
    ):
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
            radar_fig = create_radar_chart(
                teams_in_league,
                top_club_data,
                pd.DataFrame(),
                selected_category,
                aggregation_method,
            )
            return radar_fig

        # Generate the updated radar chart based on the selected category and aggregation method
        radar_fig = create_radar_chart(
            teams_in_league,
            top_club_data,
            main_club_data,
            selected_category,
            aggregation_method,
        )

        return radar_fig
