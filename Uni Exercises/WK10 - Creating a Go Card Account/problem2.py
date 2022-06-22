
class GoCard:
    """A class to hold the balance and transactions for a Go Card account"""

    def __init__(self):
        self.balance = float(input("Creating account. Input initial balance: "))
        self.statement = [self.balance]

    def top_up(self, num):
        self.balance += num
        self.statement.append(num)

    def deduct(self, num):
        self.balance -= num
        num = -abs(num)
        self.statement.append(num)

    def balance(self):
        return self.balance

    def print_statement(self):
        balance = self.statement[0]
        print("Statement:")
        print("event", "{: >32}".format("amount ($)"), "{: >17}".format("balance ($)"))
        print("Initial balance", "{: >40,.2f}".format(balance))
        for num in self.statement[1:]:
            if num > 0:
                balance += num
                print("Top up", "{: >30,.2f}".format(num), "{: >18,.2f}".format(balance))
            else:
                balance -= abs(num)
                print("Ride", "{: >32,.2f}".format(num), "{: >18,.2f}".format(balance))
        print("Final balance", "{: >42,.2f}".format(balance))


my_gocard = GoCard()
word = ""
variables = {}

while word != "q":
    command = input()
    command = command.split()
    if command[0] == "t" and len(command) == 2:
        try:
            amount = float(command[1])
            my_gocard.top_up(amount)
        except ValueError:
            print("Bad command")
    elif command[0] == "r" and len(command) == 2:
        try:
            amount = float(command[1])
            my_gocard.deduct(amount)
        except ValueError:
            print("Bad command")
    elif command[0] == "b" and len(command) == 1:
        print(my_gocard.balance)
    elif command[0] != "q":
        print("Bad command")
    word = command[0]
my_gocard.print_statement()
