from dash import Output, Input, State
from plots.pitch_plot.pitch_plot import create_pitch_figure


def register_pitch_plot_callbacks(app):
    @app.callback(
        Output("pitch-plot", "figure"),
        Output("selected-players-store", "data"),
        Input("pitch-plot", "clickData"),  # Click data from the graph
        State("selected-players-store", "data"),  # The currently selected players
    )
    def football_pitch_section(clickData, selected_players):
        if selected_players is None:  # Ensure that selected_players is initialized
            selected_players = []

        if (
            clickData and "points" in clickData
        ):  # Ensure clickData exists and contains points
            clicked_label = clickData["points"][0][
                "text"
            ]  # Extract the label of the clicked player

            # Toggle player selection
            if clicked_label in selected_players:
                selected_players.remove(clicked_label)
            else:
                selected_players.append(clicked_label)  # Add the player if not selected

        else:
            print("NOT SELECTED?")
        fig = create_pitch_figure(selected_players)
        # Return the updated pitch figure with the new selected players
        return fig, selected_players
