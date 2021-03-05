from main import ma
from models.Suggestion import Suggestion
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class SuggestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Suggestion

    video_title = ma.String(required=True, validate=Length(min=1))
    video_type = ma.String(required=True, validate=Length(min=1))
    genre = ma.String(required=True,validate=Length(min=1))
    date_created = ma.DateTime(required=True)
    user =  ma.Nested(UserSchema)
    
suggestion_schema = SuggestionSchema()
suggestions_schema = SuggestionSchema(many=True)