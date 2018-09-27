import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')
import plotly
from dash.dependencies import Input, Output

df=pd.read_csv('HackerRank-Developer-Survey-2018-Values.csv',low_memory=False)
###########Dataframe computations
gender = df['q3Gender'].value_counts()[:3]
countries=df['CountryNumeric2'].value_counts().to_frame()
print(gender)
###########
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div([
    html.H1('Hacktour task: Hackerank Data'),
    html.H2('Dissagregation by gender of respondants'),
    dcc.Graph(
        id = 'mvsf',
        figure={
                'data':[
               go.Bar(
    x=['Male', 'Female', 'non Binary', 'Total'],
    y=[gender[0], gender[1], gender[2], df.shape[0]],
    marker=dict(
        color=['rgba(204,204,204,1)', 'rgba(222,45,38,0.8)',
               'rgba(204,204,204,1)'])
    )]

                }
    ),
    dcc.Graph(
        id = 'map',
        figure = {
            'data': [ dict(
            type = 'choropleth',
            locations = countries.index,
            locationmode = 'country names',
            z = countries['CountryNumeric2'],
            text = countries['CountryNumeric2'],
            colorscale ='Viridis',
            autocolorscale = False,
            reversescale = False,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '',
                title = 'Survey Respondents'),
          )],
        'layout': dict(
        title = 'Survey Respondents by Nationality',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )
        }
    ),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'
    ),
    html.Div(id='output-container'),
    html.Div('code : https://github.com/prabhant/hacktour-tartu'),
    ])


@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server()