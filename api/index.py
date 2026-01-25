from app import app, db

# Ensure database tables exist on cold start
with app.app_context():
    db.create_all()

# Vercel entrypoint
handler = app
