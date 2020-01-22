# WSGI entry point for Gunicorn
from api import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True, debug=False)
