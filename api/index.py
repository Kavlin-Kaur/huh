import os
from app import app, db

# Only initialize DB if using a proper database connection (not SQLite)
# SQLite won't work on Vercel (ephemeral filesystem)
if os.getenv('DATABASE_URL') and 'postgresql' in os.getenv('DATABASE_URL', ''):
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        print(f"Warning: Could not initialize database: {e}")

# Vercel entrypoint
handler = app
