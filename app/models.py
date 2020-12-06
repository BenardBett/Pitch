from . import db
from werkzeug.security import generate_password_hash,check_password_hash
   
class User(db.Model):
    """ class modelling the users """

    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    pass_secure = db.Column(db.String(255))

   pass_secure  = db.Column(db.String(255))

        @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password) 
        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

#create pitch categories   
class PitchCategory(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    
    
    def save_category(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_categories(cls):
        categories = PitchCategory.query.all()
        return categories

class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="pitches", lazy = "dynamic")
    vote = db.relationship("Votes", backref="pitches", lazy = "dynamic")



    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()
       
    def get_pitches(id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches          
 
    def __repr__(self):
        return f'User {self.username}'