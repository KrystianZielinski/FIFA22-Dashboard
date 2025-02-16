import pandas as pd


# Load the CSV data into a DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)


# General filter by club (for radar plot)
def filter_main_club(df, club_name, selected_positions):
    df["Original Club"] = df["Club"]
    return df[
        (df["Club"] == club_name) & (df["Best Position"].isin(selected_positions))
    ]


def filter_top_in_league_club(df, club_name, selected_positions):
    return df[
        (df["Club"] == club_name) & (df["Best Position"].isin(selected_positions))
    ]


def filter_avg_league_club(df, club_name, selected_positions):
    return df[
        (df["Club"] == club_name) & (df["Best Position"].isin(selected_positions))
    ]


def get_attributes(attribute_type=None):
    # Define the attribute categories
    attributes = {
        "Physical Condition": [
            "SprintSpeed",
            "Acceleration",
            "Stamina",
            "Strength",
            "Agility",
        ],
        "Passing Skills": [
            "ShortPassing",
            "LongPassing",
            "Curve",
            "Vision",
            "Crossing",
        ],
        "Ball Control Skills": [
            "BallControl",
            "Dribbling",
            "Balance",
            "Reactions",
            "Composure",
        ],
        "Attacking Skills": [
            "Finishing",
            "Positioning",
            "ShotPower",
            "Volleys",
            "LongShots",
        ],
        "Defensive Skills": [
            "Marking",
            "StandingTackle",
            "SlidingTackle",
            "Aggression",
            "Interceptions",
        ],
        "Goalkeeping Skills": [
            "GKDiving",
            "GKHandling",
            "GKKicking",
            "GKPositioning",
            "GKReflexes",
        ],
    }

    # If attribute_type is None, return the entire dictionary for dropdown options
    if attribute_type is None:
        return attributes

    # Return the requested attribute list, or None if the input is invalid
    return attributes.get(attribute_type, None)


def football_pitch_positions():
    # Define the common x and y axis for various positions
    """position_data = {
        'GK': (52, 9),
        'LB': (16, 16), 'CLB': (36, 16), 'CB': (52, 16), 'CRB': (68, 16), 'RB': (88, 16),
        'LWB': (16, 24), 'CLDM': (36, 24), 'CDM': (52, 24), 'CRDM': (68, 24), 'RWB': (88, 24),
        'LM': (16, 34), 'CLM': (36, 34), 'CM': (52, 34), 'CRM': (68, 34), 'RM': (88, 34),
        'LW': (16, 42), 'CLAM': (36, 42), 'CAM': (52, 42), 'CRAM': (68, 42), 'RW': (88, 42),
        'LST': (36, 50), 'ST': (52, 50), 'RST': (68, 50),
        'CF': (52, 58)
    }"""

    player_positions = {
        "GK": (50, -34),
        "LB": (33, -24),
        "CB": (50, -24),
        "RB": (67, -24),
        "LWB": (33, -16),
        "CDM": (50, -16),
        "RWB": (67, -16),
        "LM": (33, -5),
        "CM": (50, -5),
        "RM": (67, -5),
        "LW": (33, 3),
        "CAM": (50, 3),
        "RW": (67, 3),
        "ST": (50, 12),
        "CF": (50, 21),
    }

    # Generate the player positions dynamically using the above data
    # player_positions = [{'id': pos, 'x': x, 'y': y, 'label': pos} for pos, (x, y) in position_data.items()]

    return player_positions


def positions_category():
    positions_cat = {
        "GK": ["GK"],
        "DEF": ["LB", "CB", "RB", "LWB", "CDM", "RWB"],
        "MID": ["LM", "CM", "RM", "LW", "CAM", "RW"],
        "ATK": ["ST", "CF"],
    }

    return positions_cat


def get_leagues(file_path):
    df = pd.read_csv(file_path)
    df["League_Country"] = df["League"] + " [" + df["Country"] + "]"
    leagues = df["League_Country"].unique()
    return leagues, df


def get_league_teams(
    df,
    df_leagues,
    league,
    selected_positions=None,
    selected_team=None,
    selected_teams=None,
):
    df_leagues["League_Country"] = (
        df_leagues["League"] + " [" + df_leagues["Country"] + "]"
    )
    if selected_teams is not None:
        clubs = df_leagues[
            (df_leagues["League_Country"] == league)
            & (df_leagues["Club"].isin(selected_teams))
        ]["Club"].unique()
    else:
        clubs = df_leagues[(df_leagues["League_Country"] == league)]["Club"].unique()

    if selected_team is not None:
        excluded_clubs = set(selected_team["Club"])
        if selected_positions is not None:
            teams = df[
                (df["Club"].isin(clubs))
                & (~df["Club"].isin(excluded_clubs))
                & (df["Best Position"].isin(selected_positions))
            ]
        else:
            teams = df[(df["Club"].isin(clubs)) & (~df["Club"].isin(excluded_clubs))]
    else:
        if selected_positions is not None:
            teams = df[
                (df["Club"].isin(clubs))
                & (df["Best Position"].isin(selected_positions))
            ]
        else:
            teams = df[(df["Club"].isin(clubs))]

    teams["Original Club"] = teams["Club"]
    teams["Club"] = league
    return teams


def get_top_team(df, df_leagues, league, selected_positions=None):
    df_leagues["League_Country"] = (
        df_leagues["League"] + " [" + df_leagues["Country"] + "]"
    )
    clubs = df_leagues[df_leagues["League_Country"] == league]["Club"].unique()
    teams = df[df["Club"].isin(clubs)]
    grouped_df = teams.groupby("Club")["Overall"].mean()
    top_club = grouped_df.idxmax()
    if selected_positions is not None:
        top_club_players = df[
            (df["Club"] == top_club) & (df["Best Position"].isin(selected_positions))
        ]
    else:
        top_club_players = df[(df["Club"] == top_club)]

    top_club_players["Original Club"] = teams["Club"]
    top_club_players["Club"] = top_club + " - Best Team"
    return top_club_players


def colors():
    import plotly.express as px

    color_scale = "Spectral"
    low_color = px.colors.sample_colorscale(color_scale, [0.1])[
        0
    ]  # Selected team color
    color_scale = "RdBu"
    medium_color = px.colors.sample_colorscale(color_scale, [0.55])[
        0
    ]  # Best team color
    high_color = px.colors.sample_colorscale(color_scale, [0.95])[0]  # League color

    return low_color, medium_color, high_color
