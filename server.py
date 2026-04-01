import yfinance as yf
from colorama import Fore
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("yfinanceserver")

@mcp.tool()
def stock_price(stock_ticker: str) -> str:
    """This tool returns the last known price for a given stock ticker.
    Args:
        stock_ticker: a alphanumeric stock ticker
        Example payload: "NVDA"
        
        Returns:
        str:"Ticker: Last Price"
        Example Response "NVDA: $100.21"
        """

    dat = yf.Ticker(stock_ticker)
    historical_prices = dat.history(period='1mo')
    last_month_closes = historical_prices['Close']

    print(Fore.YELLOW + str(last_month_closes))
    return str(f"Stock price over the last month for {stock_ticker} : {last_month_closes}")

@mcp.tool()
def stock_info(stock_ticker: str) -> str:
    """This tool returns information about a given stock given it's ticker.
    Args:
        stock_ticker: a alphanumeric stock ticker
        Example payload: "IBM"

    Returns:
        str:information about the company
        Example Respnse "Background information for IBM: {'address1': 'One New Orchard Road', 'city': 'Armonk', 'state': 'NY', 'zip': '10504', 'country': 'United States', 'phone': '914 499 1900', 'website': 
                'https://www.ibm.com', 'industry': 'Information Technology Services',... }" 
        """
    
    dat = yf.Ticker(stock_ticker)
    return str(f"Background information for {stock_ticker} : {dat.info}")

@mcp.tool()
def income_statement(stock_ticker: str) -> str:
    """This tool returns the quarterly income statement for a given stock ticker.
    Args:
        stock_ticker: a alphanumeric stock ticker
        Example payload: "BOA"

    Returns:
        str:quarterly income statement for the company
        Example Respnse "Income statement for BOA: 
        Tax Effect Of Unusual Items                           76923472.474289  ...          NaN
        Tax Rate For Calcs                                            0.11464  ...          NaN
        Normalized EBITDA                                        4172000000.0  ...          NaN
        """
    dat = yf.Ticker(stock_ticker)

    return str(f"Background information for {stock_ticker} {dat.quarterly_income_stmt}")

if __name__ == "__main__":
    mcp.run(transport="stdio")