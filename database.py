from abc import ABC, abstractmethod
import json
from some_models import Event
import mysql.connector


class database(ABC):

  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  def select(self):
    pass

  @abstractmethod
  def insert(self, event: Event):
    pass

  @abstractmethod
  def delete(self, id: int):
    pass

  @abstractmethod
  def update(self, event: Event):
    pass

## postgressqlDB implementation    
import psycopg2
from psycopg2.extras import RealDictCursor

class postgresqlDB(database):
  #establish connection
  def __init__(self, file_loc):
    try:
      with open(file_loc) as c_file:
        config = json.load(c_file)
      print("db config file successfully opened")  
    except Exception as error:
      print("failed to open config file")

    try:
      self.postDB = psycopg2.connect(
        host= config['postgresql']['host'],
        database= config['postgresql']['database'],
        user= config['postgresql']['user'],
        password= config['postgresql']['password'],
        cursor_factory= RealDictCursor
      )
      self.mycursor = self.postDB.cursor()
      print("Connection established succesfully")
    except Exception as error:
      print("failed to connect") 
      print("Error " , error) 

  def select(self):
    query = "SELECT * FROM event"
    self.mycursor.execute(query)
    myresult = self.mycursor.fetchall()
    return myresult

  def insert(self, event: Event):
    query = "INSERT INTO event (venue_id, event_name, event_date) VALUES (%s, %s, %s)"
    self.mycursor.execute(query, (event.venue.venue_id, event.eventName, event.eventDate))
    self.postDB.commit()
    return self.select()

  def delete(self, id:int):
    query="DELETE FROM event WHERE event_id= %s;"
    self.mycursor.execute(query,(str(id)))
    self.postDB.commit()
    return self.select()

  def update(self, event: Event, id: int):
    query = "Update event SET EventName= %s, Venue=%s, EventDate=%s where id= %s;"
    self.mycursor.execute(query, (event.eventName, event.venue, event.eventDate, id))
    self.postDB.commit()
    return self.select()


#mysql implementation
class MysqlDB(database):
  #establish connection
  def __init__(self, file_loc):
    try:
      with open(file_loc) as c_file:
        config = json.load(c_file)
      print("config file successfully opened")  
    except Exception as error:
      print("failed to open config file")

    try:
      self.mydb = mysql.connector.connect(
      host= config['mysql']['host'],
      user= config['mysql']['user'],
      password= config['mysql']['password'],
      database= config['mysql']['database']
      )
      self.mycursor = self.mydb.cursor(dictionary = True)
      print("Connection established succesfully")
    except Exception as error:
      print("failed to connect") 
      print("Error " , error) 

  def select(self):
    query = "SELECT * FROM event"
    self.mycursor.execute(query)
    myresult = self.mycursor.fetchall()
    return myresult

  def insert(self, event: Event):
    query = "INSERT INTO event (EventName, venue_id, EventDate) VALUES (%s, %s, %s)"
    self.mycursor.execute(query, (event.eventName, event.venue.venue_id, event.eventDate))
    self.mydb.commit()
    return self.select()   

  def delete(self, id:int):
    query="DELETE FROM event WHERE id= %s;"
    self.mycursor.execute(query,(id))
    self.mydb.commit()
    return self.select()

  def update(self, event: Event, id: int):
    query = "Update event SET EventName= %s, Venue=%s, EventDate=%s where id= %s;"
    self.mycursor.execute(query, (event.eventName, event.venue, event.eventDate, id))
    self.mydb.commit()
    return self.select()

