import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_sugar_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content)
    table = soup.find_all('table', {'class': 'tblData'})

    df_month, df_price, df_change = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    for kolom in table:
        rows = kolom.find_all('tr')
        res = []
        for tr in rows:
            td = tr.find_all('td')
            row = [tr.text.strip() for tr in td if tr.text.strip()]
            if row:
                res.append(row)

        arr_month, arr_price, arr_change = [], [], []
        for data in res:
            arr_month.append(data[0])
            arr_price.append(data[1])
            arr_change.append(data[2])

        df_month = pd.concat([df_month, pd.DataFrame({'month': arr_month})], ignore_index=True)
        df_price = pd.concat([df_price, pd.DataFrame({'price': arr_price})], ignore_index=True)
        df_change = pd.concat([df_change, pd.DataFrame({'change': arr_change})], ignore_index=True)

    return pd.concat([df_month, df_price, df_change], axis=1)