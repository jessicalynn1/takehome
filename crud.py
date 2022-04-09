from model import db, User, Reservation


def create_user(name):
    """Create and return a new user."""

    user = User(name=name)

    return user


def get_user_by_id(id):
    """Return a user object by its ID"""
    
    return User.query.get(id)


# def save_reservation(user_id, date, time):
#     """Create reservation"""
    
#     user_id = User(id=user_id)
#     date = Reservation(date=date)
#     time = Reservation(time=time)
    
#     result = Reservation(user_id=user_id, date=date, time=time)
#     db.session.add(result)
#     db.session.commit()

#     return result

def save_reservation(user_id, date, time):
    """Create reservation"""

    result = db.session.query(Reservation).filter(Reservation.time == time, Reservation.date == date).update({'user_id': user_id})
    db.session.commit()
    
    return result

def create_timeslots(date, time, user_id=None):
    """Create and return a a new timeslot."""

    reservation = Reservation(date=date, time=time, user_id=None)
    
    return reservation

def show_available_reservations(date, start=None, end=None):
    """Return all available reservations given a date, start and end time"""
    
    if start and end:
        return Reservation.query.filter(Reservation.date == date, Reservation.time>start, Reservation.time<end, Reservation.user_id == None).all()
    elif start and not end:
        return Reservation.query.filter(Reservation.date == date, Reservation.time>start, Reservation.user_id == None).all()
    elif end and not start:
        return Reservation.query.filter(Reservation.date == date, Reservation.time<end, Reservation.user_id == None).all()
    else:
        return Reservation.query.filter(Reservation.date == date, Reservation.user_id == None).all()

def check_user_res_by_date(date, user_id):
    """Check if user already has reservation for that date and time."""
    
    return Reservation.query.filter(Reservation.date == date, Reservation.user_id == user_id).first() 

def print_reservations(user_id):
    """Print all reservations on user profile page"""

    return Reservation.query.filter_by(user_id=user_id).all()



if __name__ == '__main__':
    from app import app
    connect_to_db(app)