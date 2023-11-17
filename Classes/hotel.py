class Restaurant:

    def __init__(self):
        self.menu = {}
        self.table = {}
        self.custOrder = {}
        self.tableNum = 0

    def reserveTable(self, tableNum):
        '''
        To reserve table in the restaurant.
        '''
        self.tableNum = tableNum

        if (tableNum not in self.table) or \
            (tableNum in self.table and self.table[tableNum] == ''):
            self.table[tableNum] = 'filled'
            print(f'Congratulations, you\'ve successfully booked table {tableNum}')
        else:
            print('Sorry, currently this table is not available.')

    def orderFood(self, tableNum):
        '''
        To order food items
        '''
        self.tableNum = tableNum
        order = []

        print(f'ordering food for table {tableNum}:')
        isOrdering = input('Would you like to order, sir? (y/n)')
        if isOrdering == 'y':
            print("Here is the menu:\n")
            for i in self.menu:
                print(i)

            # Ordering as much as food.
            while True:
                item = input('Please enter your choice of food: ')
                if item in self.menu:
                    order.append(item)
                if input('Would you like to order more? (y/n)') == 'n':
                    break

        print('please wait. Your order will be delivered shortly.')
        self.custOrder[tableNum] = order

    def printCustomerOrder(self, tableNum):
        print(f"Food ordered by Table {tableNum}")
        print("--------------------------")
        for each in self.custOrder[tableNum]:
            print(each)

    def addToMenu(self, newItem, price):
        self.menu[newItem] = price

    def printMenu(self):
        print("Menu item : price")
        print("------------------")
        for dish, price in self.menu.items():
            print(f"{dish} : {price}")
            
    def printTableReservations(self):
        print('Table number : status')
        print("------------------------")
        for tableNum, status in self.table.items():
            print(f"{tableNum} : {'unreserved' if status == '' else 'reserved'}")

# driver code
hotel = Restaurant()

hotel.addToMenu('chicken lollipop', 200)
hotel.addToMenu('biriyani', 180)
hotel.addToMenu('masala dosa', 80)
hotel.addToMenu('prawns fry', 200)
hotel.addToMenu('barbeque', 500)


hotel.reserveTable(1)
hotel.reserveTable(2)
hotel.reserveTable(2)

# order food.
hotel.orderFood(1)
hotel.orderFood(2)

# hotel.printMenu()
hotel.printTableReservations()

hotel.printCustomerOrder(1)
hotel.printCustomerOrder(2)