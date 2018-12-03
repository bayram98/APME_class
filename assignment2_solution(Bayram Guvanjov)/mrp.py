# implement here your solution
# Bayram Guvanjov
# 20162023


import time
from module06_trees.part00_preclass.linked_binary_tree import LinkedBinaryTree

subs = {}
parts = {}

def readsubs():

    file = open("subassemblies.dat", "r")

    for line in file.readlines():
        val = list(line.split(','))
        subs[val[0].strip()] = int(val[1].strip())

    file.close()

def printsubs():

    print(" Print subassemblies we have ")
    for i in subs:
        print("{0} : {1} ".format(i, subs[i]))
    print()


def readparts():

    file = open("parts.dat", "r")

    for line in file.readlines():
        val = list(line.split(','))
        parts[val[0].strip()] = [int(val[2].strip()), int(val[3].strip())]

    file.close()

def printparts():
    print(" Print parts we have ")
    for i in parts:
        print("{0} : {1} ".format(i, parts[i]))
    print()


class MRP(LinkedBinaryTree):

    def create_decision_tree_from_file(self, file_name):

        # simulate the decision process using a set of pre-provided yes/no answers
        # while current position is not a leaf
        # do: ask question, get answer, select next position to visit
        print("Opening the file {0}...".format(file_name))
        file = open(file_name, "r")
        print("Creating decision tree...")
        current_p = None
        lines = file.readlines()
        curr_level = 0
        for line in lines:
            line.strip()
            values = line.split(',')
            l = values[0].strip()
            level = int(l)
            side = values[1].strip()
            text = values[2].strip()
            if level == 0:
                # create the root and increase level
                curr_level += 1
                current_p = self._add_root(text)
                print("Root created!")
            elif level == curr_level:
                # go one level deeper
                if side == 'left':
                    current_p = self._add_left(current_p, text)
                    print("- add left child at level {0}: {1}".format(curr_level, text))
                elif side == 'right':
                    current_p = self._add_right(current_p, text)
                    print("- add right child at level {0}: {1}".format(curr_level, text))
                curr_level += 1
            elif level < curr_level:
                # go up and continue
                while level != curr_level:
                    current_p = self.parent(current_p)
                    curr_level -= 1
                if side == 'left':
                    current_p = self._add_left(current_p, text)
                    print("- add left child at level {0}: {1}".format(curr_level, text))
                elif side == 'right':
                    current_p = self._add_right(current_p, text)
                    print("- add right child at level {0}: {1}".format(curr_level, text))
                curr_level += 1

        print("Decision tree created, ready for use")
        file.close()
        print("File {0} closed.".format(file_name))






    def preorder_indent(self, p, d):
        """
        This is the function to "pretty" print a tree (already seen in previous sessions)
        """
        print(2 * d * '-' + str(p.element()))
        for c in self.children(p):
            self.preorder_indent(c, d + 1)


    def calculate_and_verify(self, p, d , number):
        sum = 0

        if self.is_root(p) != True:
            if self.is_leaf(p) == True:
                amount_we_have = parts[p.element()][0]
                if amount_we_have < number :
                    print(" We need # {0} from {1} which is equal to = {2}".format(number - amount_we_have,p.element(),max(number - amount_we_have, 0)*parts[p.element()][1]))

                return max(number - amount_we_have, 0)*parts[p.element()][1]


            amount_we_have = subs[p.element()]
            if amount_we_have >= number :
                return 0

            number -= amount_we_have

        for c in self.children(p):
            sum += self.calculate_and_verify(c, d + 1, number)

        return sum

    def Procurement(self, p,number):


        if self.is_root(p) != True:
            if self.is_leaf(p) == True:
                amount_we_have = parts[p.element()][0]
                if amount_we_have < number :

                    amount_we_need = number - amount_we_have
                    if amount_we_need > 6:
                        amount_we_need += 1
                    amount_we_need += 1

                    print(" We procure #{0} from {1} which is equal to = {2}".format(amount_we_need,p.element(),amount_we_need*parts[p.element()][1]))
                    parts[p.element()][0] += amount_we_need
                return


            amount_we_have = subs[p.element()]
            if amount_we_have >= number:
                return

            number -= amount_we_have


        for c in self.children(p):
            self.Procurement(c, number)

    def Execute(self, p,number):


        if self.is_root(p) != True:
            if self.is_leaf(p) == True:

                parts[p.element()][0] -= number
                print(" We took #{0} from {1}".format(number,p.element()))

                return


            amount_we_have = subs[p.element()]
            subs[p.element()] -= min(amount_we_have,number)
            print(" We took #{0} from {1}".format(min(amount_we_have,number), p.element()))

            if amount_we_have >= number:
                return

            number -= amount_we_have


        for c in self.children(p):
            self.Execute(c, number)



if __name__ == '__main__':

    # create decision tree for coolbike
    coolbike = MRP()
    coolbike.create_decision_tree_from_file("coolbike.dat")

    print()
    print()

    coolbike.preorder_indent(coolbike.root(), 0)

    print()
    print()

    # create decision tree for boringbike
    boringbike = MRP()
    boringbike.create_decision_tree_from_file("boringbike.dat")

    print()
    print()

    boringbike.preorder_indent(boringbike.root(), 0)

    print()
    print()

    # Parts we have
    readparts()
    printparts()

    # subassemblies we have
    readsubs()
    printsubs()

    # receiving order

    file = open("order.dat", "r")

    for line in file.readlines():
        line.strip()
        values = line.split(',')
        type = values[0].strip()
        amount = int(values[1].strip())

        if type == "boringbike":
            print()
            print(" Calculate and verify the material requirements to BoringBike ")
            value = boringbike.calculate_and_verify(boringbike.root(), 0, amount)
            if value > 0:

                print()
                print()
                print()

                print("It is not honoured so we need Procurement")
                time.sleep(1)

                boringbike.Procurement(boringbike.root(), amount)

                print("Now it is honoured we can order boringbike!!!!!")
                time.sleep(1)

            else:
                print()
                print()
                print()

                print("It is honoured we can now order boringbike!!!!!")
                time.sleep(1)
                print()
                print()

            print()
            printparts()
            printsubs()
            print()
            print()

            print(" Executer {0} amount of boringbike".format(amount))
            time.sleep(1)
            boringbike.Execute(boringbike.root(), amount, )

            print()
            print()
            print("Done!!! Ordered {} boringbike".format(amount))
            time.sleep(1)
            print()

            printsubs()
            printparts()

            if amount <= 5:
                amount = 1
            else:
                amount = amount // 3

            subs["SA04"] += amount
            subs["SA05"] += amount
            subs["SA06"] += amount


            print()

            printsubs()
            print()
            print()
            print("-------------------######---------------------------")
            print("-------------------######---------------------------")
            print()
            print()

            time.sleep(2)


        elif type == "coolbike":

            print()
            print(" Calculate and verify the material requirements to CoolBike ")
            value = coolbike.calculate_and_verify(coolbike.root(), 0, amount)
            if value > 0:

                print()
                print()
                print()

                print("It is not honoured so we need Procurement")
                time.sleep(1)

                coolbike.Procurement(coolbike.root(), amount)

                print("Now it is honoured we can order coolbike!!!!!")
                time.sleep(1)

            else:
                print()
                print()
                print()

                print("It is honoured we can now order coolbike!!!!!")
                time.sleep(1)
                print()
                print()

            print()
            printparts()
            printsubs()
            print()
            print()

            print(" Executer {0} amount of coolbike".format(amount))
            time.sleep(1)
            coolbike.Execute(coolbike.root(), amount,)

            print()
            print()

            print("Done!!! Ordered {0} of coolbike".format(amount))
            time.sleep(1)
            print()

            printsubs()
            printparts()

            if amount <= 5:
                amount = 1
            else:
                amount = amount // 3

            subs["SA01"] += amount
            subs["SA02"] += amount
            subs["SA03"] += amount
            subs["SA04"] += amount


            print()

            printsubs()
            print()
            print()
            print("-------------------######---------------------------")
            print("-------------------######---------------------------")
            print()
            print()

            time.sleep(2)


        else:
            print(" wrong data type. Try again ")

    file.close()


