
import pandas as pd
import json
import matplotlib.pyplot as plt
import datetime as dt


# The three files in this directory bottom_tier.json, middle_tier.xls and top_tier.csv contain monthly variations of the house price index
# in Greenville, SC (USA) from 1997 until October 2017 (for instance, the value 0.67 for October 2016 means that average house prices have increased of
# of 0.67% in October 2016 compared to September 2016.
# Top/Middle/Bottom-tier refers to the type of houses (from expensive to cheap).
# Your task is to do some analysis of the provided data using Pandas, in particular you should do the following:


"""
# 1) Import the three datasets into three different dataframes (note that importing the csv file may not be trivial because of the metadata at the beginning of the file...)
"""
def from_string_to_date(dates):
    """
    This function is GIVEN
    :param dates:
    :return:
    """
    x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
    return x


def imprt(file1, file2, file3):
    df1 = pd.read_csv(file1, sep=',')

    df2 = pd.read_excel(file2, sep=',')



    with open(file3) as data:
        df3 = json.load(data)



    df1x = []
    df1y = []

    df2x = []
    df2y = []

    df3x = []
    df3y = []

    for i in df1['Date']:
        df1x.append(i)
    for i in df1['Value']:
        df1y.append(i)

    for i in df2['Date']:
        df2x.append(i)
    for i in df2['Value']:
        df2y.append(i)

    for i in df3['dataset']['data']:
        print(i[0] , i[1])

        df3x.append(i[0])
        df3y.append(i[1])


    df1x = from_string_to_date(df1x)
    df3x = from_string_to_date(df3x)

    plt.plot(df1x, df1y)
    plt.plot(df2x, df2y)
    plt.plot(df3x, df3y)

    df4y = []
    for i in range(len(df1y)):
        df4y.append((df1y[i] + df2y[i] + df3y[i]) / 3)

    plt.plot(df1x, df4y)

    plt.xlabel('Time')
    plt.ylabel('Value')

    plt.title('HPI')
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()


# 2) Calculate and plot the average house price index monthly variation (that is, an index which is the average of the 3 indexes provided)




# 3) Plot the 4 indexes (the 3 provided and the one that you obtained at step 2) in the same graph (Note: you may want to create first a new dataframe with the 4 indexes, but this is not strictly necessary)


if __name__ == '__main__':
    imprt('top_tier.csv', 'middle_tier.xls', 'bottom_tier.json')



