from model import db, User, Reservation


def create_user(name):
    """Create and return a new user."""

    user = User(name=name)

    return user


def get_user_by_id(id):
    """Return a user object by its ID"""
    
    return User.query.get(id)


def save_reservation(id, user_id, time):
    """Reservations"""
    
    id = Reservation(id=id)
    user_id = User(user_id=user_id)
    time = Reservation(time=time)
    
    result = Reservation(id=id, user_id=user_id, time=time)

    return result


def print_reservations(id):
    """Print all reservations on user profile page"""

    return Reservation.query.filter_by(id=id).all()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)