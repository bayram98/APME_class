"""
Data about the 2012 edition of the European football championships are available in the file euro2012.csv
Import the data into a Pandas dataframe, then answer the following questions:
"""
import pandas as pd
import matplotlib.pyplot as plt

"""
0) Import the data into a dataframe
"""


def imprt(in_file):
    df = pd.read_csv(in_file, sep=',')
    print(df, '\n')
    return df


"""
1) How many columns are in this dataset?
"""


def columns(df):
    print(df.shape[1], 'columns\n')


"""
2) Filter the columns "Team", "Yellow Cards" and "Red Cards" and assign them to a dataframe called "discipline"
"""


"""
3) Show a bar chart diagram of the number of yellow cards received by each team
(see hint_bar_chart.png for a hint...)
"""
"""
4) Sort the data in "discipline" by red card first, then yellow card and save the sorted data in a dataframe called "disc_sorted"
"""

"""
5) What is the average number of yellow cards received by a team at Euro 2012?
"""

"""
6) Create a new dataframe with only data of teams that scored 4 or more goals
"""
def filter(df):
    dis = {}
    dis['Team'] = list(df["Team"])
    dis['Yellow Cards'] = list(df["Yellow Cards"])
    dis['Red Cards'] = list(df["Red Cards"])

    discip = pd.DataFrame(dis)
    print(discip, '\n')
    plt.bar(list(dis['Team']), dis['Yellow Cards'], align='center')
    plt.xticks(dis['Team'])
    plt.show()

    dis_sort = discip.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)

    print('Sorted Dataframe\n', dis_sort)
    print('Average of Yellow Cards: ', float(discip['Yellow Cards'].sum()) / float(discip['Yellow Cards'].count()))


if __name__ == '__main__':
    df = imprt('euro2012.csv')
    columns(df)
    filter(df)

