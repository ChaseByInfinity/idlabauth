import serial
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine('mysql+pymysql://root:tatnall@localhost/idlab', echo=False)
serial = serial.Serial('/dev/ttyUSB0', baudrate=9600)


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

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
    data = serial.readline().strip()
    data = data[1:11]
    
    if len(data) == 10:
        if str(data) == '80000AA599':
            print 'Success'
            
               
           
        
        

    
