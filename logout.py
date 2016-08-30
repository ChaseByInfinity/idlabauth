import serial
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import gc
from datetime import datetime
import webbrowser
import selenium.webdriver as webdriver
import RPi.GPIO as GPIO
import time



engine = create_engine('mysql+pymysql://root:tatnall@localhost/idlab', echo=False)
serial = serial.Serial('/dev/ttyUSB1', baudrate=9600)




Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

pi1 = pigpio.pi(name)

pi1.write(14, 1)



class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    fname = Column(String(255))
    lname = Column(String(255))
    photo_id = Column(String(255))
    permission = Column(String(255))
    last_access = Column(DateTime)
    card_id = Column(String(255))


    def __init__(self, fname, lname, photo_id, permission, last_access, card_id):
        self.fname = fname
        self.lname = lname
        self.photo_id = photo_id
        self.permission = permission
        self.last_access = last_access
        self.card_id
    
    

class Current(Base):
    __tablename__ = 'current'

    id = Column(Integer, primary_key=True)
    fname = Column(String(255))
    lname = Column(String(255))
    currStation = Column(String(255))

    def __init__(self, fname, lname, currStation):
        self.fname = fname
        self.lname = lname
        self.currStation = currStation
while True:
    data = serial.readline().strip()
    data = data[-12:]
    data = str(data)


    record = session.query(Student).filter(Student.card_id == data).first()
    if record:
        fname = record.fname
        lname = record.lname
        curr = session.query(Current).filter(Current.fname == fname, Current.lname == lname).first()

        if curr:
            session.delete(curr)
            session.commit()
            session.flush()
            pi1.write(14, 0)
            time.sleep(3)
            pi1.write(14, 1)
            
            
        else:
            pi1.write(14, 0)
            time.sleep(3)
            pi1.write(14, 1)
            

            


    else:
        print "Your credentials do not exist"


    
        
