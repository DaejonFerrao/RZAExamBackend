import json

def getUsersDB():
    with open("db/UsersDB.json", "r+") as file:
        return json.load(file)

def saveUsersDB(newUsers):
    with open("db/UsersDB.json", "w+") as file:
         file.write(json.dumps(newUsers))

#the above json files are used to allow new users to register and for existing users to login. 

def getBookingsDB():
    with open("db/BookingsDB.json", "r+") as file:
        return json.load(file)

def saveBookingsDB(newBooking):
    with open("db/BookingsDB.json", "w+") as file:
         file.write(json.dumps(newBooking))

#the booking files are used to allow the user to create bookings for hotels and to purchase tickets, they can also view and manage their confirmed tickets and hotel rooms. 