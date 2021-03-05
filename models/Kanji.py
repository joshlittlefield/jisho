from main import db
from datetime import datetime




class Kanji(db.Model):
    __tablename__ = "kanjis"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.String(30),nullable=False)
    genre = db.Column(db.String(),default='Dont know what genre to call it')
    date_created = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    
    
    heisig_level=db.Column(db.Integer)
    jlpt_level=db.Column(db.Integer)
    school_level=db.Column(db.Integer)
    character=
    meaning=
    onyomi=
    kunyomi=
    is_radical=
    R1_radical_used=
    R2_radical_used=
    R3_radical_used=
    R4_radical_used=
    R5_radical_used=
    story=
    
    
    
    def __repr__(self):
        return f"<Kanji ( '{self.title}', '{self.date_created}'>" 