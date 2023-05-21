#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd

ticker_symbol = "TSLA"
tesla_data = yf.download(ticker_symbol, start="2021-01-01", end="2021-12-31")
tesla_data.reset_index(inplace=True)
tesla_data.to_csv("tesla_stock_data.csv", index=False)
print(tesla_data.head())





# In[2]:


import pandas as pd
import requests
from bs4 import BeautifulSoup




# In[3]:


url = 'https://finance.yahoo.com/quote/TSLA/financials?p=TSLA'



# In[4]:


response = requests.get(url)


# In[5]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[6]:


revenue_table = soup.find('table', {'class': 'Lh(1.7)'})


# In[8]:


headers = []
data = []

if revenue_table is not None:
    header_row = revenue_table.find('thead').find_all('th')
    for header in header_row:
        headers.append(header.text.strip())

    rows = revenue_table.find('tbody').find_all('tr')
    for row in rows:
        data_row = []
        for cell in row.find_all('td'):
            data_row.append(cell.text.strip())
        data.append(data_row)
else:
    print("Unable to find revenue table.")




# In[9]:


tesla_revenue = pd.DataFrame(data, columns=headers)


# In[10]:


print(tesla_revenue.tail())


# In[11]:


import yfinance as yf
import pandas as pd

# Define the ticker symbol
ticker_symbol = "GME"

# Use yfinance to download the stock data
gme_data = yf.download(ticker_symbol, start="2021-01-01", end="2021-12-31")

# Reset the index
gme_data.reset_index(inplace=True)

# Save the data to a CSV file
gme_data.to_csv("gme_stock_data.csv", index=False)

# Display the first five rows of the DataFrame
print(gme_data.head())


# In[12]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL for the GameStop revenue data
url = 'https://finance.yahoo.com/quote/GME/financials?p=GME'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)

# Create a BeautifulSoup object and parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the revenue data
revenue_table = soup.find('table', {'class': 'Lh(1.7)'})

# Extract the table headers and data into separate lists
headers = []
data = []

if revenue_table is not None:
    header_row = revenue_table.find('thead').find_all('th')
    for header in header_row:
        headers.append(header.text.strip())

    rows = revenue_table.find('tbody').find_all('tr')
    for row in rows:
        data_row = []
        for cell in row.find_all('td'):
            data_row.append(cell.text.strip())
        data.append(data_row)
else:
    print("Unable to find revenue table.")

# Create a pandas DataFrame using the headers and data lists
gme_revenue = pd.DataFrame(data, columns=headers)

# Display the last five rows of the DataFrame
print(gme_revenue.tail())


# In[14]:


import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Define the ticker symbol and download the stock data
ticker_symbol = 'TSLA'
tesla_data = yf.download(ticker_symbol, start='2021-01-01', end='2021-12-31')

# Reset the index
tesla_data.reset_index(inplace=True)

# Plot the Tesla stock graph
make_graph(tesla_data, 'Tesla Stock Data')





# In[15]:


import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Define the ticker symbol and download the stock data
ticker_symbol = 'GME'
gme_data = yf.download(ticker_symbol, start='2021-01-01', end='2021-12-31')

# Reset the index
gme_data.reset_index(inplace=True)

# Plot the GameStop stock graph
make_graph(gme_data, 'GameStop Stock Data')



# In[ ]:





# In[ ]:




