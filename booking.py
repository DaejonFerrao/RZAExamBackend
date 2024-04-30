from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random
from cred import getBookingsDB, saveBookingsDB

router = APIRouter()

#the router is used to link the booking page to the fastapi main module so that the developer can view and test the funcitonality of the system.

class Booking(BaseModel):
    id: str
    email: str
    ticket: int
    date : str


#the class model is for the booking system to have the proper credentials for the users to be provide the neccesary information for their booking. 


@router.post("/booking")
def booking(info: Booking):
    users = getBookingsDB()
    booking_id = random.randint(1000000, 9999999)

    calculate = info.ticket * 12

    new_booking = {
        'id': booking_id,
        'no_of_tickets': info.ticket,
        'price': calculate,
        'date': info.date
    }

    for user in ['users']:
        in info.email == users['email']:
            users('booking').append(new_booking)
            saveBookingsDB(new_booking)
            return new_booking

#the router functionality contains the logic that will allow the user to book ticets and get the prices calculated for their bookings. 