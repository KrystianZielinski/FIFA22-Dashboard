import pandas as pd
import plotly.express as px


def create_nested_pie_plot(df):
    # Example sectors, regions, and sales (like you mentioned)

    positions_1st_level = [
        "GK",
        "DEF",
        "DEF",
        "DEF",
        "DEF",
        "DEF",
        "DEF",
        "MID",
        "MID",
        "MID",
        "MID",
        "MID",
        "MID",
        "ATK",
        "ATK",
    ]

    positions_2nd_level = [
        None,
        "LB",
        "CB",
        "RB",
        "LWB",
        "CDM",
        "RWB",
        "LM",
        "CM",
        "RM",
        "LW",
        "CAM",
        "RW",
        "ST",
        "CF",
    ]

    positions = [
        "GK",
        "LB",
        "CB",
        "RB",
        "LWB",
        "CDM",
        "RWB",
        "LM",
        "CM",
        "RM",
        "LW",
        "CAM",
        "RW",
        "ST",
        "CF",
    ]

    positions_count = [
        int(df["Best Position"].value_counts().get(position, 0))
        for position in positions
    ]
    positions_count = list(positions_count)  # Ensures it's not a nested list
    print(positions_count)

    # Create DataFrame
    df = pd.DataFrame(
        dict(
            positions_1st_level=positions_1st_level,
            positions_2nd_level=positions_2nd_level,
            positions_count=positions_count,
        )
    )

    # Add a "root" column with a space (' ') for an empty center
    df["root"] = " "

    color_scale = "Magenta"  # You can change to 'viridis' or any other Plotly scale
    gk_color = px.colors.sample_colorscale(color_scale, [0.8])[0]  # Lowest color
    def_color = px.colors.sample_colorscale(color_scale, [0.6])[0]  # Lowest color
    mid_color = px.colors.sample_colorscale(color_scale, [0.4])[0]  # Lowest color
    atk_color = px.colors.sample_colorscale(color_scale, [0.2])[0]  # Lowest color

    color_mapping = {
        "GK": gk_color,
        "DEF": def_color,
        "MID": mid_color,
        "ATK": atk_color,  # 1st level color
    }

    # Create the sunburst chart with the empty center
    fig = px.sunburst(
        df,
        path=["positions_1st_level", "positions_2nd_level"],
        values="positions_count",
        color="positions_1st_level",
        color_discrete_map=color_mapping,
    )

    # Use `hovertemplate` to specify exactly what information you want to display in the hover
    fig.update_traces(
        hovertemplate=(
            "Best Position: %{label}<br>"  # For first-level (positions_1st_level)
            + "Count: %{value}<br>"  # Show positions_count for both levels
            + "<extra></extra>"  # This removes unwanted info like ID
        ),
    )

    fig.update_layout(
        title={
            "text": "Player position distribution",  # Dynamic title text
            "x": 0.5,  # Centers title horizontally
            "xanchor": "center",  # Ensures proper centering
            "yanchor": "top",  # Keeps title anchored at the top
            "y": 0.96,  # Moves title slightly higher
        },
        title_font=dict(
            family="Roboto, Arial, sans-serif",  # Font family
            size=22,  # Font size
            weight="bold",
        ),
        height=475,
        width=475,
        margin=dict(t=60, l=0, r=0, b=50),  # Adjust the margins
    )

    return fig
