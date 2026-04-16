import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load and prepare data
data = pd.read_csv("data/ProcessedQuantiumData.csv")
data["Date"] = pd.to_datetime(data["Date"])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f8",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1200px",
                "margin": "0 auto"
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualiser",
                    style={
                        "textAlign": "center",
                        "color": "#1f2d3d",
                        "marginBottom": "30px"
                    }
                ),

                html.Div(
                    style={
                        "backgroundColor": "white",
                        "padding": "20px",
                        "borderRadius": "12px",
                        "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                        "marginBottom": "20px"
                    },
                    children=[
                        html.Label(
                            "Filter by Region",
                            style={
                                "fontWeight": "bold",
                                "display": "block",
                                "marginBottom": "10px",
                                "color": "#334e68"
                            }
                        ),
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            style={"color": "#102a43"},
                            labelStyle={"marginRight": "20px"}
                        )
                    ]
                ),

                html.Div(
                    style={
                        "backgroundColor": "white",
                        "padding": "20px",
                        "borderRadius": "12px",
                        "boxShadow": "0 4px 12px rgba(0,0,0,0.08)"
                    },
                    children=[
                        dcc.Graph(id="sales-chart")
                    ]
                )
            ]
        )
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_data = data.copy()

    if selected_region != "all":
        filtered_data = filtered_data[filtered_data["Region"].str.lower() == selected_region]

    daily_sales = filtered_data.groupby("Date", as_index=False)["Sales"].sum()
    daily_sales = daily_sales.sort_values("Date")

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title="Sales over time",
        labels={"Date": "Date", "Sales": "Sales"}
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_font_size=24
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)