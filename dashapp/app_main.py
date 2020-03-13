# -*- coding: utf-8 -*-
import dash_html_components as html
import pandas as pd
import dash_table
import dash_core_components as dcc
from . import app
from .plot import plot_swiss_italy

ABOUT = """
Design of experiments is the study of how to choose experiments---in the most efficient way---to understand the influence of some factors on the experimental outcome.

There are myriads of different techniques that allow this. To faciliate their use, especially in experimental chemistry, this app allows to create experimental design for arbitrary number of factors.
"""

df = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
)
df = df.drop(columns=["Province/State", "Lat", "Long"]).melt(
    id_vars="Country/Region", var_name="Date", value_name="Value"
)
df2 = df.pivot_table(columns="Country/Region", index="Date", values="Value")
df2["Date_Col"] = pd.to_datetime(df2.index)
df2 = df2.sort_values(by='Date_Col')

layout = [
    html.Div(
        [html.H1("CoVID19 plots"), dcc.Graph(figure=plot_swiss_italy(df2))],
        id="container",
        # tag for iframe resizer
        **{"data-iframe-height": ""},
    )
]
