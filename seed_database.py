import os
import json
from random import choice, randint
from datetime import datetime, date, time, timedelta

import crud
import model
import app

os.system("dropdb reservations")
os.system('createdb reservations')

model.connect_to_db(app.app)
model.db.create_all()

#Create timeslots for 2022
timeslots_db = []
start_date = date(2022, 1, 1)
end_date = date(2023, 1, 1)
delta = timedelta(days=1)
while start_date < end_date:
    date = start_date.strftime("%Y-%m-%d")
    time_slots = [time(h, m).strftime('%H:%M') for h in range(0, 24) for m in (0,30)]
    for slot in time_slots:
        reservation = crud.create_timeslots(date, slot)
        timeslots_db.append(reservation)
    start_date += delta

model.db.session.add_all(timeslots_db)
model.db.session.commit()


    # for h in range(0, 24):
    #     for m in (0,30):
    #         time = time(h, m).strftime('%H:%M')