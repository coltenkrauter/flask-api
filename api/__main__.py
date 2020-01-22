# This is needed to access the modules' own instance of flask (app)
import sys
import os

path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, "..")
sys.path.insert(0, path)

from api import app

# guard for testing and running locally
if __name__ == "__main__":
    print(" * Entrypoint:", __file__)

    # run the flask app through Connexion with debugging turned on
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=False)
