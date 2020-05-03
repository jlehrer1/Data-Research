# -*- coding: utf-8 -*-
import dash
import pandas as pd
import plotly.express as px
import plotly
import dash_core_components as dcc
import dash_html_components as html

data = pd.read_csv('pit-stop-locations-1.csv')

print(data.head())
print(data.columns)
print(data['Neighborhood'])

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Pit Stop Locations in SF',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id=''

    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
