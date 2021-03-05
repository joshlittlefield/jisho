from main import ma
from models.Kanji import Kanji
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class KanjiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Kanji

    video_title = ma.String(required=True, validate=Length(min=1))
    video_type = ma.String(required=True, validate=Length(min=1))
    genre = ma.String(required=True,validate=Length(min=1))
    date_created = ma.DateTime(required=True)
    user =  ma.Nested(UserSchema)
    
kanji_schema = KanjiSchema()
kanjis_schema = KanjiSchema(many=True)
