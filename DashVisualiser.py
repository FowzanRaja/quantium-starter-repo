import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

data = pd.read_csv("data/ProcessedQuantiumData.csv")

data["Date"] = pd.to_datetime(data["Date"])

DailySales = data.groupby("Date", as_index=False)["Sales"].sum()

DailySales = DailySales.sort_values("Date")

fig = px.line(
    DailySales,
    x="Date",
    y="Sales",
    title="Pink morsel sales over time",
    labels={"Date": "Date", "Sales": "Sales"}
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink morsel sales visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)