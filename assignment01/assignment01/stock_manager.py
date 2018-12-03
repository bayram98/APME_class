"""
Refer to the assignment specification for more details
ID: 20162023
Name: Bayram Guvanjov
"""


from module03_stacks_and_queues.part00_preclass.stack import ArrayStack


class StockManager:


    def __init__(self, o_name, o_surname):
        """
        Initialises the Stock Manager with the name and surname of the portfolio
        :param o_name: name of the owner of the porfolio
        :param o_surname: surname of the portfolio
        """
        self._o_name = o_name
        self._o_surname = o_surname
        self._list = {}
        self._size = {}
        self._profit = 0


    def buy_shares(self, company, number, buy_price):
        """
        Buy stocks
        :param company: the company of which shares are being bought
        :param number: the number of shares to buy
        :param buy_price: the price (per share) at which shares are bought
        """

        q = ArrayStack()
        if company not in self._list:
            self._list[company] = q
            self._size[company] = 0

        self._list[company].push([number, buy_price])
        self._size[company] += number


    def sell_shares(self, company, number, sell_price):
        """
        Sell shares (only if you have enough to sell!)
        :param company: the company of which shares are being bought
        :param number: the number of shares to buy
        :param sell_price: the price (per share) at which shares are sold
        """

        profit = 0
        if company in self._list:

            if number > self._size[company]:
                print(" Invalid amount of stock.")
            else:
                while number > 0:
                    last = self._list[company].top()
                    num = min( number , last[0] )
                    profit += ( sell_price - last[1] ) * num
                    number -= num
                    last[0] -= num

                    if last[0] == 0 :
                        self._list[company].pop()

        else:
            print("Invalid input")

        self._profit +=profit

        return profit

    def buy_multiple(self, company_list, number_list, price_list):
        for i in range(len(company_list)) :
            self.buy_shares(company_list[i], number_list[i], price_list[i])


    def sell_multiple(self, company_list, number_list, price_list):
        Profit = 0
        for i in range(len(company_list)) :
            Profit += self.sell_shares(company_list[i], number_list[i], price_list[i])
        return Profit


    def get_profit(self):
        print(self._profit)
        if self._profit < 0:
            print("Loss of ${0} from stock manager initialisation".format(self._profit * (-1)))
        else:
            print("Gain of ${0} from stock manager initialisation".format(self._profit))
        return self._profit
    """
    allows to print the current stock held by the investor (name of stocks, numbers of stocks, and
    prices at which they were bought)
    """
    def print_portfolio(self):
        print("Name : {}".format(self._o_name))
        print("Surname : {}".format(self._o_surname))
        print("Net Profit by now :{}".format(self.get_profit()))
        for i in self._list:
            print(i)
            self._list[i].print_contents()
            print()
            


if __name__ == '__main__':
    # extend this code to test all the functions of your portfolio manager

    P = StockManager("Donald", "Trump")

    P.buy_shares("UNIST", 20, 100)
    P.buy_shares("Google", 20, 100)

    print("Profit: {0}".format(P.sell_shares("Google", 5, 120)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    print("Profit: {0}".format(P.sell_shares("Google", 31, 127)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    print("Profit: {0}".format(P.sell_shares("Google", 2, 23)))
    print("Current cumulative profit: {0}".format(P.get_profit()))
    P.print_portfolio()

    P.sell_shares("Google", 50, 150)
    P.buy_multiple(["Google", "Apple"], [10, 56], [56, 27])
    P.sell_multiple(["Google", "Apple"], [1, 1], [56, 27])
    P.print_portfolio()
