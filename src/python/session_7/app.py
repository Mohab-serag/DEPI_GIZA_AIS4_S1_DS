import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Dash ----> main app object
# dcc  ----> dash core component (graph - drop down - sliders)
# html ----> html element (div - h1-h6 , p , ...)
# input + output ----> used in callbacks

df = pd.read_csv("src/python/session_7/Dash.csv")

app = Dash()
app.title = "Interactive Dashboard"

num_cols = df.select_dtypes(include='number').columns

app.layout = html.Div([
    html.H1("Interactive dashboard"),
    html.Label("Select a value to show in the pie chart"),

    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in num_cols],
        value=num_cols[0]
    ),

    dcc.Graph(id='pie-chart')
])


@app.callback(Output('pie-chart', 'figure'),
              Input('column-dropdown', 'value'))


def updated_pie(selected_col):
    grouped = df.groupby('Area')[selected_col].sum().reset_index()
    fig = px.pie(grouped, names='Area', values=selected_col,
                 title=f"Distribution of {selected_col} by Area",
                 hole=0.4,
                 color_discrete_sequence=px.colors.qualitative.Set2)
    return fig


    
    



app.run(debug=True)
