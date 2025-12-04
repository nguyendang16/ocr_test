# WSGI entry point for Vercel
from main import app

# Vercel expects an 'app' or 'application' variable
application = app

if __name__ == "__main__":
    app.run()

