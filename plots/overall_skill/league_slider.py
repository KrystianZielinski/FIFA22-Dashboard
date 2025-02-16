def create_league_slider(teams_in_league):
    grouped_df = (
        teams_in_league.groupby("Original Club")["Overall"].mean().reset_index()
    )
    # Sort the values from highest to lowest
    grouped_df = grouped_df.sort_values(by="Overall", ascending=False)

    # Generate the marks for the range slider dynamically
    slider_marks = {
        len(grouped_df) + 1 - i: grouped_df["Original Club"].iloc[i - 1]
        for i in range(1, len(grouped_df) + 1)
    }

    return slider_marks, len(grouped_df), grouped_df
