from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80), unique=False, nullable=False)
    user_name = db.Column(db.String(80), unique=False, nullable=False)
    done = db.Column(db.String(5), unique=False, nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.label

    def serialize(self):
        return {
            "label": self.label,
            "user_name": self.user_name,
            "done": self.done
        }

    class Name(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=False, nullable=False)
        

    def __repr__(self):
        return '<Name %r>' 

    def serialize(self):
        return {
            "name": self.name
        }

