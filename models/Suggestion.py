from main import db
from datetime import datetime




class Suggestion(db.Model):
    __tablename__ = "suggestions"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.String(30),nullable=False)
    genre = db.Column(db.String(),default='Dont know what genre to call it')
    date_created = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def __repr__(self):
        return f"<Suggestion ( '{self.title}', '{self.date_created}'>"