from connexion.resolver import RestyResolver
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import connexion

_connexion = connexion.FlaskApp(
    __name__,
    specification_dir='specification/',
    options={
        "swagger_ui": False,
    }
)
app = _connexion.app

# Enable CORS (Cross Origin Resource Sharing)
CORS(app)

# Global rate limiting
limiter = Limiter(
    app,
    # rate limit by remote address of request
    key_func=get_remote_address,
    # values are set rediculously high until testing can be done
    default_limits=[
        '100000 per day',
        '10000 per hour',
        '10000 per minute',
    ],
)

_connexion.add_api(
    'open_api_specification.yaml',
    validate_responses=True,
    resolver=RestyResolver('api.endpoints'),
)
