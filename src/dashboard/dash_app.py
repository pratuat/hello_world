from dash import Dash, dcc, html

def build_app(server, base_pathname):
    dash_app = Dash(
        name = __name__,
        server = server,
        url_base_pathname=base_pathname
    )

    dash_app.layout = html.Div(
        ['This is dash app.']
    )
