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


    def __repr__(self):
        return f'User {self.username}'