from dash import Input, Output
from utils import get_league_teams, load_data, get_top_team
from plots.overall_skill.league_slider import create_league_slider


def register_slider_callbacks(app):
    # Callback to update the selected teams and the slider marks based on the range slider value
    @app.callback(
        [
            Output("slider-league", "marks"),
            Output("slider-league", "max"),
            Output("slider-league", "value"),
            Output("previous-selected-league", "data"),
            Output("selected-teams", "data"),
        ],  # Update the previous league value in Store],
        [
            Input("dropdown-leagues", "value"),
            Input("dropdown-teams", "value"),
            Input("slider-league", "value"),
            Input("previous-selected-league", "data"),
        ],
    )
    def update_selected_teams(
        selected_league, selected_team, slider_value, previous_selected_league
    ):
        data_fifa = load_data("data/fifa22.csv")
        data_league = load_data("data/leagues_clubs.csv")

        if previous_selected_league is None:
            previous_selected_league = (
                selected_league  # Set the initial value as the current one
            )

        top_club_data = get_top_team(data_fifa, data_league, selected_league)

        teams_in_league = get_league_teams(data_fifa, data_league, selected_league)

        # Get the slider marks dynamically (this will be updated based on teams)
        slider_marks, total_teams, grouped_df = create_league_slider(teams_in_league)

        slider_max = total_teams

        if selected_league != previous_selected_league:  # If the league has changed
            slider_value = [1, slider_max]  # Reset to default range

        slider_value = (
            [1, slider_max] if slider_value == [1, 100] else slider_value
        )  # Default to select all teams

        # Map slider value to selected team names (the range of teams selected)
        selected_teams = [
            slider_marks[i] for i in range(slider_value[0], slider_value[1] + 1)
        ]  # Add 1 to include the last team

        # Dynamically set styles for marks based on the selected range
        updated_slider_marks = {}
        for i in range(1, total_teams + 1):
            team_name = slider_marks[i]

            if team_name == top_club_data["Original Club"].unique():
                updated_slider_marks[i] = {
                    "label": team_name,
                    "style": {"color": "white", "fontWeight": "bold"},
                }
            elif team_name == selected_team:
                updated_slider_marks[i] = {
                    "label": team_name,
                    "style": {"color": "rgb(224, 58, 58)", "fontWeight": "bold"},
                }
            else:
                if slider_value[0] <= i <= slider_value[1]:
                    # Selected team style: white text, bold
                    updated_slider_marks[i] = {
                        "label": team_name,
                        "style": {"color": "rgb(8, 101, 201)", "fontWeight": "bold"},
                    }
                else:
                    # Deselect team style: gray text
                    updated_slider_marks[i] = {
                        "label": team_name,
                        "style": {"color": "rgb(19, 75, 135)"},
                    }  # gray color for deselected

        previous_selected_league = selected_league

        return (
            updated_slider_marks,
            slider_max,
            slider_value,
            previous_selected_league,
            selected_teams,
        )
