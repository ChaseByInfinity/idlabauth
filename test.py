import serial
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import gc
from datetime import datetime
import webbrowser
import selenium.webdriver as webdriver




engine = create_engine('mysql+pymysql://root:tatnall@localhost/idlab', echo=False)
ser1 = serial.Serial('/dev/ttyUSB0', baudrate=9600)


while True:

    
    data = ser1.readline().strip()
    data = data[-12:]
    data = str(data)

    if data_t = ser2.readline().strip()

    

    

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
        print "It worked"
    else:
        print "DId not work"

        
   
    
