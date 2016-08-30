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
import pigpio





engine = create_engine('mysql+pymysql://root:tatnall@localhost/idlab', echo=False)
ser1 = serial.Serial('/dev/ttyUSB0', baudrate=9600)


pi1 = pigpio.pi(name)

pi1.write(14, 1)


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


b = webdriver.Firefox()

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
    
    
while True:
    data = ser1.readline().strip()
    data = data[-12:]
    data = str(data)

    

    record = session.query(Student).filter(Student.card_id == data).first()
    if record:
        
       
        record.last_access = datetime.now()
        session.commit()
        fname = record.fname
        lname = record.lname
        currStation = None
        
        

        check = session.query(Current).filter(Current.fname == fname, Current.lname == lname).first()
        
        if not check:
            newCurrent = Current(fname, lname, currStation)
            session.add(newCurrent)
            session.flush()
            session.commit()
        
     
        url = "file:///home/pi/Authentication/pages/success.html"
        b.get(url)
        pi1.write(14, 0)
        time.sleep(3)
        pi1.write(14, 1)
       

        
       
        
        
    else:
        url = "file:///home/pi/Authentication/pages/failure.html"
        b.get(url)
        pi1.write14, 1)


        
   
    

        
