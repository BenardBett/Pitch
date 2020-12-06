from . import db

    
#create pitch categories   
class PitchCategory(db.Model):
    __tablename__ = 'users'
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