from dash import Input, Output


def register_callback_skills_text(app):
    @app.callback(
        Output("selected-skills-text", "children"), Input("category-dropdown", "value")
    )
    def update_skills_text(selected_value):
        return f"{selected_value} - Overview"
