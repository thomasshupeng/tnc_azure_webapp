import os
from waitress import serve
from hello import app

serve(app, host="0.0.0.0", port=os.environ["SERVER_PORT"])
