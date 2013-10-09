from app import frontend_app, backend_app
from config import APP_IS_LIVE

if __name__ == "__main__":
    if APP_IS_LIVE:
        app.run()
    else:
        app.run(debug=True)
