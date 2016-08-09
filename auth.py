import serial
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import gc
from datetime import datetime



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
    
    
code = ''
while True:
    data = serial.readline().strip()
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
        print 'Authenticated!'
    else:
        print 'Failure. Please hover your card again.'
        
