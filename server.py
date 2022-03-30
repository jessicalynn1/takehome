# #################### OLD DO NOT USE ################


# from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
# from model import connect_to_db, db, User, Reservation
# import crud

# from jinja2 import StrictUndefined
# import webbrowser
# import requests
# import json 



# app = Flask(__name__, static_url_path='/static') 
# app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined

# @app.route("/", methods=['POST'])
# def welcome_page():
#     """Show the Welcome page"""

#     name = request.form.get('name')

#     if name:
#         session["user"] = user.id
#         flash(f"welcome, {user.name}!")
#         return redirect("homepage.html")

#     return render_template("homepage.html")


# @app.route("/reservations")
# def reservations():
#     """Show the calendar picker page"""

#     cal = Calendar(root, selectmode="day", "time")

#     return render_template("reservations.html", calendar=cal)


# @app.route("/results", methods=['POST'])
# def results_page():
#     """Show the results page"""

#     name = request.form.get('name')
#     u_id = User.query.filter_by(name=name)

#     reservationlst = crud.save_reservation(name)

#     return render_template("results.html", reservationlst=reservationlst #need to pass through results of form)


# @app.route("/user_profile")
# def user_profile():
#     """Show the user_profile page"""

#     return render_template("user_profile.html" #need to pass through reservations)


# if __name__ == "__main__":
#     connect_to_db(app)
#     app.run(host="0.0.0.0", debug=True)

# if __name__ == "__main__":
#     connect_to_db(app)
#     app.run(host="0.0.0.0", debug=True)

