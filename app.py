import dash
import dash_core_components as dcc
import dash_html_components as html


import urllib.request, json

import plotly.express as px

import pandas as pd

df = pd.read_csv("static/csv/be-covid.csv", dtype={"NIS5": str})

with open('static/json/be-geojson.json') as json_file:
    geojson = json.load(json_file)


fig = px.choropleth_mapbox(df, geojson=geojson,
                           locations="NIS5",
                           color='CASES',color_continuous_scale="Viridis",
                            range_color=(0, 300),
                           featureidkey="properties.shn",
                           center={"lat": 50.85045, "lon": 4.34878},
                           mapbox_style="carto-positron", zoom=7,height=900)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash(__name__)
server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='COVID-DATA',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='#UCLouvain #INGI Visualization', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    # Column for app graphs and plots
    html.Div(
        className="map",
        children=[
            dcc.Graph(figure=fig)
        ],
    )


])


if __name__ == '__main__':
    app.run_server(debug=True)
