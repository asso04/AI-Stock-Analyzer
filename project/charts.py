import plotly.graph_objects as go


def create_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Close"
        )
    )

    fig.update_layout(
        title="Stock Price",
        xaxis_title="Date",
        yaxis_title="Price ($)"
    )

    return fig.to_html(full_html=False)