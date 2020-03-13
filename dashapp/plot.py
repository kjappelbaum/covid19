import plotly.graph_objects as go

def plot_swiss_italy(df): 
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=list(df['Date_Col']), y=list(df['Switzerland']), name='Switzerland'))

    fig.add_trace(
        go.Scatter(x=list(df['Date_Col']), y=list(df['Italy']), name='Italy'))

    fig.show()

    return fig 