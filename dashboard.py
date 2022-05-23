import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/dashboard/df_dashboard.csv")

app = dash.Dash()

app.layout=html.Div(children=[
    html.H1(children="Climate change sentiment Dashboard"),
    dcc.Dropdown(id="sentiment-dropdown",
                options=[{'label':i, 'value':i}
                    for i in df.drop(['Unnamed: 0', 'date'], axis=1).columns],
                    value='snippet-count'),
    dcc.Graph(id="sentiment-graph")
])

@app.callback(
    Output(component_id='sentiment-graph', component_property='figure'),
    Input(component_id='sentiment-dropdown', component_property='value')
)

def update_graph(selected_column):
    line_fig = px.line(x=df['date'], y=df[selected_column],
                    title=f'Column selected - {selected_column}',
                    labels={'x': 'Date', 'y': selected_column})
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)
