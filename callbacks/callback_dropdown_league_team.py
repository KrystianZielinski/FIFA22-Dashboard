from dash import Output, Input
from utils import get_leagues, load_data, get_top_team


def register_dropdown_league_team(app):
    # Callback to update team options based on selected league
    @app.callback(
        Output("dropdown-teams", "options"),
        Output("selected-league-text", "children"),
        Input("dropdown-leagues", "value"),
        Input("selected-players-store", "data"),
    )
    def update_team_options(selected_league, selected_positions):
        leagues, data = get_leagues("data/leagues_clubs.csv")

        data_fifa = load_data("data/fifa22.csv")
        data_league = load_data("data/leagues_clubs.csv")
        top_club_data = get_top_team(
            data_fifa, data_league, selected_league, selected_positions
        )
        top_team = top_club_data["Original Club"].iloc[0]

        if selected_league is None:
            # Return an empty list if no league is selected
            return []
        else:
            # Filter teams based on selected league
            league_country = data[data["League_Country"] == selected_league]
            league = league_country["League"].iloc[0]
            country = league_country["Country"].iloc[0]

            filtered_teams = data[
                (data["League"] == league) & (data["Country"] == country)
            ]["Club"]
            # Remove the top team from the filtered list
            filtered_teams = filtered_teams[filtered_teams != top_team]

            league = league + " [" + country + "]"
            # Create options for the team dropdown
            return [{"label": team, "value": team} for team in filtered_teams], league
