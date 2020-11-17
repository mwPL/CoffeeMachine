# Write your code here
# Commented below are previous stages of the project
'''
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")
'''
'''
print("Write how many cups of coffee you will need:")
cups = int(input())
print("For", cups, "cups of coffee you will need:")
print(cups * 200, "ml of water")
print(cups * 50, "ml of milk")
print(cups * 15, "g of coffee beans")
'''
'''
print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")
coffee = int(input())


def howmanycups(water, milk, beans):
    return min(water // 200, milk // 50, beans // 15 )


availability = howmanycups(water, milk, beans)
if coffee == availability:
    print("Yes, I can make that amount of coffee")
elif coffee < availability:
    print("Yes I can make that amount of coffee ( and even", availability - coffee, "more than that)")
else:
    print("No, I can only make", availability, "cups of coffee")
'''
'''
money = 550
water = 400
milk = 540
beans = 120
cups = 9


def display_content(money, water, milk, beans, cups):
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")


def fill():
    global water, milk, beans, cups
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())


def take():
    global money
    print("I gave you $", money)
    money = 0


def buy():
    global water, milk, beans, cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = input()
    if choice != 'back':
        if resources(int(choice)):
            print("I have enough resources, making you a coffee!")

            if int(choice) == 1:
                money += 4
                water -= 250
                beans -= 16
                cups -= 1
            elif int(choice) == 2:
                money += 7
                water -= 350
                beans -= 20
                milk -= 75
                cups -= 1
            elif int(choice) == 3:
                money += 6
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1


def action():
    print("Write action (buy, fill, take, remaining, exit:)")
    act = input()
    if act == 'buy':
        buy()
    elif act == 'fill':
        fill()
    elif act == 'take':
        take()
    elif act == 'exit':
        exit()
    elif act == 'remaining':
        display_content(money, water, milk, beans, cups)


def resources(coffee_id):
    global water, cups, beans, milk
    espresso = (250, 1, 16, 0)
    latte = (350, 1, 20, 75)
    cappuccino = (200, 1, 12, 100)
    coffees = [espresso, latte, cappuccino]
    coffee = coffees[coffee_id-1]
    enough_resources = True

    if coffee[0] > water:
        print("Sorry, not enough water!")
        enough_resources = False
    if coffee[1] > cups:
        print("Sorry, not enough cups!")
        enough_resources = False
    if coffee[2] > beans:
        print("Sorry, not enough beans!")
        enough_resources = False
    if coffee[3] > milk:
        print("Sorry, not enough milk!")
        enough_resources = False
    return enough_resources


# display_content(money, water, milk, beans, cups)
#while True:
  #  action()

# display_content(money, water, milk, beans, cups)
'''


class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9

    def action(self):
        print("Write action (buy, fill, take, remaining, exit:)")
        act = input()
        if act == 'buy':
            self.buy()
        elif act == 'fill':
            self.fill()
        elif act == 'take':
            self.take()
        elif act == 'exit':
            exit()
        elif act == 'remaining':
            self.display_content()

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def display_content(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())

    def resources(self, coffee_id):
        espresso = (250, 1, 16, 0)
        latte = (350, 1, 20, 75)
        cappuccino = (200, 1, 12, 100)
        coffees = [espresso, latte, cappuccino]
        coffee = coffees[coffee_id - 1]
        enough_resources = True

        if coffee[0] > self.water:
            print("Sorry, not enough water!")
            enough_resources = False
        if coffee[1] > self.cups:
            print("Sorry, not enough cups!")
            enough_resources = False
        if coffee[2] > self.beans:
            print("Sorry, not enough beans!")
            enough_resources = False
        if coffee[3] > self.milk:
            print("Sorry, not enough milk!")
            enough_resources = False
        return enough_resources

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        choice = input()
        if choice != 'back':
            if self.resources(int(choice)):
                print("I have enough resources, making you a coffee!")

                if int(choice) == 1:
                    self.money += 4
                    self.water -= 250
                    self.beans -= 16
                    self.cups -= 1
                elif int(choice) == 2:
                    self.money += 7
                    self.water -= 350
                    self.beans -= 20
                    self.milk -= 75
                    self.cups -= 1
                elif int(choice) == 3:
                    self.money += 6
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.cups -= 1


x = CoffeeMachine()
while True:
    x.action()
