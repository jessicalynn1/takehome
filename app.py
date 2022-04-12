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
        if not User.query.filter(User.name == name).first():
            session["user"] = name
            flash(f"welcome, {name}!")
            u_name = crud.create_user(name)
            db.session.add(u_name)
            db.session.commit()
        else:
            session["user"] = name
            flash(f"welcome, {name}!")

    return render_template("reservations.html")


@app.route("/results", methods=['POST'])
def results_page():
    """Show the results page"""

    name = session["user"]
    date = request.form.get('date')
    start = request.form.get('start')
    end = request.form.get('end')
    user = User.query.filter(User.name == name).first()
    user_id = user.id
    #add some code that forces time picked to be :00 or :30

    reservation_times = crud.show_available_reservations(date, start, end)

    checked_res = crud.check_user_res_by_date(date, user_id)

    if checked_res:
        flash ("This time slot is not available.")
        return redirect("reservations.html")
    
    return render_template("results.html", reservation_times=reservation_times, name=name, date=date)


@app.route("/save_reservation", methods=['POST'])
def save_reservation():
    """Route to save reservation to user profile"""

    name = session["user"]
    user = User.query.filter(User.name == name).first()
    user_id = user.id
    reservation_id = request.form.get('reservation_id')

    res = Reservation.query.get(reservation_id)
    date = res.date
    time = res.time

    checked_res = crud.check_user_res_by_date(date, user_id)

    if checked_res:
        flash ("This time slot is not available.")
        return redirect("reservations.html")
    else:
        saved_res = crud.save_reservation(user_id=user_id, date=date, time=time)

        return redirect("/save_reservation")


@app.route("/user_profile", methods=['POST'])
def user_profile():
    """Show the user_profile page"""
    
    name = session["user"]
    user = User.query.filter(User.name == name).first()
    user_id = user.id
    # date = request.form.get('date')
    # time = request.form.get('time')

    # checked_res = crud.check_user_res_by_date(date, user_id)

    # if checked_res:
    #     flash ("This time slot is not available.")
    #     return redirect("reservations.html")
    # else:
    #     crud.save_reservation(user_id=user_id, date=date, time=time)

    saved_res = Reservation.query.filter(Reservation.user_id == user_id).all()
 
    return render_template("user_profile.html", saved_res=saved_res)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

