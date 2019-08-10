from app import db

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(1000))
    price = db.Column(db.Float)

    def __init__(self,name,description,price):
        self.name = name
        self.description = description
        self.price = price

def new_course(new_name, new_description, new_price):
    course = Courses(new_name, new_description, new_price)
    db.session.add(course)
    db.session.commit()

    return course

if __name__ == "__main__":
    print("Building database")
    db.create_all()
    print("Completed")