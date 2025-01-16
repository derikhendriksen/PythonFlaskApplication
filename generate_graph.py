import yfinance as yf
import plotly.graph_objects as go

index_tickers = {
    "SP500": "^GSPC",
    "DJI": "^DJI",
    "NASDAQ": "^NASDAQ",
    "RUSSEL": "^RUT",
    "CBOE": "^VIX"
}


def generate_graph(ticker):
    index = yf.Ticker(ticker)
    data = index.history(period="1d", interval="1m")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='S&P500'))
    fig.update_layout(
        autosize=True,
        height=None,
        width=None,
        title="S&P500 Performance",
        title_x=0.5,
        xaxis_title="Time",
        yaxis_title="Closing Price",
        template="plotly_white",
        margin=dict(l=10, r=10, t=40, b=10),
    )
    return fig.to_html(full_html=False, config={"responsive": True, "displaylogo": False,
                                                "modeBarButtonsToRemove": ['autoscale', 'zoom']})
