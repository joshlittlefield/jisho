from controllers.suggestions_controller import suggestions
from controllers.auth_controller  import auth
from controllers.kanjis_controller import kanjis

registerable_controllers = [
    auth,
    suggestions,
    kanjis
]