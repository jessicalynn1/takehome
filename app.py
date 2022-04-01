import calendar
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db, User, Reservation
import crud
import datetime


from jinja2 import StrictUndefined
import webbrowser
import model
import json 


app = Flask(__name__, static_url_path='/static') 
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

model.connect_to_db(app)
model.db.create_all()

@app.route("/")
def welcome_page():
    """Show the Welcome page"""

    return render_template("homepage.html")


@app.route("/reservations", methods=['POST'])
def reservations():
    """Show the calendar picker page"""

    name = request.form.get('name')

    if name:
        session["user"] = name
        flash(f"welcome, {name}!")
        u_name = crud.create_user(name)
        db.session.add(u_name)
        db.session.commit()

    return render_template("reservations.html")


@app.route("/results", methods=['POST'])
def results_page():
    """Show the results page"""

    name = request.form.get('name')
    date =request.form.get('date')
    start = request.form.get('start')
    # start = time.time()
    end = request.form.get('end')
    # end = time.time()
    # u_table = Reservation.query.filter_by(name=name)
    # all_table = Reservation.query.all()

    reservation_times = []
    reservation_times.append(start)
    

    # i = start
    # while i != end: 
    #     reservation_times.append(i)           
    #     # if i in u_table:
    #     #     flash(f"This time is not available. Please pick another time.")
    #     # if i in all_table:
    #     #     flash(f"This time is not available. Please pick another time.")
        
    #     i = i + 30

    # need to send the picked date and time to database

    return render_template("results.html", reservation_times=reservation_times, name=name, date=date)


@app.route("/user_profile")
def user_profile():
    """Show the user_profile page"""

    #need to get reservations from database and print them
    name = request.form.get('name')
    user_id = User.query.filter_by(name=name)

    reservationlst = crud.save_reservation(id, user_id, name)

    return render_template("user_profile.html", reservationlst=reservationlst)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

