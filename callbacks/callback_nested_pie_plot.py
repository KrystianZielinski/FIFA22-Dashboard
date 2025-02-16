from dash import Input, Output
from utils import load_data, get_league_teams
from plots.pitch_plot.nested_pie_plot import create_nested_pie_plot


def register_nested_pie_plot_callbacks(app):
    @app.callback(
        Output("nested-pie-plot", "figure"),
        [Input("dropdown-leagues", "value"), Input("selected-teams", "data")],
    )
    def update_nested_pie_plot(selected_league, selected_teams):
        data_fifa = load_data("data/fifa22.csv")
        data_league = load_data("data/leagues_clubs.csv")

        teams_in_league = get_league_teams(data_fifa, data_league, selected_league)

        pie_fig = create_nested_pie_plot(teams_in_league)

        return pie_fig
