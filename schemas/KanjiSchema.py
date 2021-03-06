from main import ma
from models.Kanji import Kanji
from marshmallow.validate import Length

class KanjiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Kanji

    
    id = ma.auto_field()
    character = ma.String(required=True)
    meaning = ma.String(required=True)
    onyomi = ma.String()
    kunyomi = ma.String()
    
    
kanji_schema = KanjiSchema()
kanjis_schema = KanjiSchema(many=True)
