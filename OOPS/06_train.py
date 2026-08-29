# Write a class Train which has methods to book a ticket ,
# get status (no of seats) and get fare information of train running under Indian Railways


from random import randint


class Train:
    def __init__(self, train_number, seats):
        self.train_number = train_number
        self.seats = seats

    def book(self, FROM, to):
        print(f"Ticket booked successfully from {FROM} to {to}")
        print(f"Train number is {self.train_number}")

    def status(self):
        print(f"Available seats are {self.seats}")

    def getFare(self, FROM, to):
        print(f"Fare from {FROM} to {to} is ₹{randint(200, 5000)}")


t = Train(1236439, 50)

t.book("Uttarakhand", "Delhi")
t.status()
t.getFare("Uttarakhand", "Delhi")

