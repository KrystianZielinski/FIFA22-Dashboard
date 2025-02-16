from dash import html, dcc

info_text_link = dcc.Link(
    "About This App",  # Text to display
    href="/info",  # Path to the info page
    style={
        "color": "gray",  # Blue color for the link
        "cursor": "pointer",  # Change cursor to pointer on hover
        "fontSize": "32px",  # Adjust font size
        "margin": "10px 0",  # Add some margin
        "margin-left": "1710px",
        "textDecoration": "none",  # Removes underline
    },
)

title_bar = html.Div(
    children=[
        dcc.Link(
            "FIFA 22",
            style={
                "color": "#ffffff",
                "padding": "2px",
                "paddingLeft": "275px",
                "margin": "10px 0",
                "textDecoration": "none",
                "fontSize": "32px",
            },
            href="/",
        ),
        info_text_link,
    ],
    style={
        "backgroundColor": "#262626",
        "width": "100%",
        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
        "display": "flex",
    },
)
