import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read processed data
df = pd.read_csv("data/ProcessedQuantiumData.csv")

# Make sure Date is treated as a date
df["Date"] = pd.to_datetime(df["Date"])

# Group by date and total the sales
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Sort by date
daily_sales = daily_sales.sort_values("Date")

# Create line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Sales"}
)

# Create app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)