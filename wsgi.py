import os
from fakepay import app


if __name__ == "__main__":
    default_port = int(os.environ.get("PORT", 3000))
    if (os.environ.get("STAGE") == 'DEV'):
        app.run(host='0.0.0.0', port=default_port, debug=True, reloader=True)
    else:
        app.run(host='0.0.0.0', port=default_port)
