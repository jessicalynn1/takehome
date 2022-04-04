import calendar
from datetime import datetime
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db, User, Reservation
import crud

import crud
from jinja2 import StrictUndefined
import webbrowser
import json 


app = Flask(__name__, static_url_path='/static') 
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


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
    end = request.form.get('end')

    reservation_times = crud.show_available_reservations(date, start, end)
    
    return render_template("results.html", reservation_times=reservation_times, name=name, date=date)


@app.route("/save_reservation", methods=['POST'])
def save_reservation():
    """Route to save reservation to user profile"""

    name = session["user"]
    user = User.query.filter_by(name=name).first()
    user_id = user.id
    date = request.form.get('date')
    time = request.form.get('time')

    checked_res = crud.check_user_res_by_date(date, user_id)

    if checked_res:
        flash ("This time slot is not available.")
        return redirect("reservations.html")
    else:
        reservationlst = crud.save_reservation(date=date, time=time, user_id=user_id)
        db.session.add(reservationlst)
        db.session.commit()
        return redirect("/user_profile")


@app.route("/user_profile")
def user_profile():
    """Show the user_profile page"""

    # name = session["user"]
    # user = User.query.filter_by(name=name).first()
    # print(user)
    # user_id = user.id

    # reservationlst = crud.print_reservations(user_id=user_id)
 
    return render_template("user_profile.html")




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

