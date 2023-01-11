from datetime import date
from pydantic import BaseModel

class Location(BaseModel):
  location_id : str
  city : str
  street: str
  house : str


class Venue(BaseModel):
  venue_id : str
  venue_name : str
  location : Location
  capacity: int
  gallery : str
  price: int

class Event(BaseModel):
  event_id: int
  eventName:str
  venue:Venue
  eventDate:date


