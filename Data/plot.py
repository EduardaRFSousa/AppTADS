import yfinance as yf
import plotly.express as px # criação de mapas (tabelas) interativos

def plot_price(ticker):
    """
    A function to plot the close price given a ticker.

    """
    data = yf.download(
            ticker,
            multi_level_index = False
    )

    fig = px.line( # fig = sigla para figura
            data.reset_index(),
            x = 'Date', y = ['Close']
    )

    return fig

def get_stock_data(ticker, start_date, end_date):
    """Obtém dados históricos de ações do Yahoo Finance."""
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

# Exemplo de uso
ticker = "AAPL"  # Sigla para Apple
start_date = "2024-01-01"
end_date = "2024-03-01"

data = get_stock_data(ticker, start_date, end_date)
print(data.head())


"""Se quiser testar a busca pelo interactive window, execute: plot_price('SIGLA')
Ex.: Coca-cola = COKE
Apple = APPL
Bradesco = BBDC4.SA """