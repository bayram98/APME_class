"""
The file chipotle_orders.csv contains data about orders at a branch of the world-famous text-mex chain "Chipotle".
Note that columns are separated by the "tab" character
"""

import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


"""
1) Import the data into a dataframe
"""
def imprt(in_file):

    df = pd.read_csv(in_file, sep='\t')
    print(df)
    return df



"""
1bis) The same data can be downloaded at 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
How could you load the data directly from the url?
"""


"""
2) Transform the values in the item_price column into a float.
Hint: the data are currently a string of the type "$<price>", so...
"""
def price_to_foat(l):
    for x in range(len(l)):
        l[x] = float(l[x][1:])
    return l
"""
3) Filter the items that cost more than 10$ and assign them to a new dataframe (how many are these items?)
"""
def filt(df, price):
    print(df[df.item_price > price])

"""
4) Create a new dataframe containing only information about item_name and item_price of only items for which
 quantity is equal to 1, removing duplicates
"""
def filt_name(df):
    print(df[['item_name', 'item_price']][df.quantity==1])
"""
5) Create a bar chart diagram using the data obtained in (4). Each bar should show the number of items
found in a certain price interval. Use intervals of 3$
(see chipotle_result.png for the expected result)
"""
def create(df):

    mx = int(df['item_price'].max())
    l = list(df['item_price'])
    t = []
    r = []
    for y in range(0, mx, 3):
        r.append(y+1.5)
        cur = 0
        for x in range(len(l)):
            if l[x] >= float(y) and l[x] < float(y+3):
               cur += 1
        t.append(cur)
    plt.bar(r, t, align='center', width=2.5)

    t2 = np.arange(1, 40, 3)
    plt.xticks(t2)
    plt.show()

if __name__ == '__main__':
    data = []
    df = imprt('chipotle_orders.csv')

    df['item_price'] = pd.Series(price_to_foat(list(df['item_price']))).values
    time.sleep(1)
    filt(df, 10)
    time.sleep(1)
    filt_name(df)
    time.sleep(1)
    create(df)





