# Vercel Deploy Guide - Happy Trails

## Files Setup ✅ Done

1. **api/index.py** - Serverless handler (exists)
2. **vercel.json** - Updated to use api/index.py ✅
3. **.vercelignore** - Created to ignore build files ✅

## Deploy Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Setup Vercel deployment"
git push origin main
```

### 2. Go to Vercel Dashboard
- Visit https://vercel.com/dashboard
- Click "Add New..." → "Project"
- Import your GitHub repo

### 3. Configure Environment Variables
In Vercel Project Settings → Environment Variables, add:

```
HAPPYTRAILS_SECRET_KEY=your-secret-key-here-change-this
DATABASE_URL=postgresql://user:password@host/dbname
GOOGLE_MAPS_API_KEY=your-google-maps-key
WEATHER_API_KEY=your-openweather-key
FLASK_ENV=production
```

### 4. Framework & Build
- Framework: **Other**
- Build Command: (leave empty)
- Output Directory: (leave empty)

### 5. Deploy
Click "Deploy" button. Vercel will:
- Build using Python 3.11
- Install requirements.txt dependencies
- Run api/index.py
- Route all requests → /api/index.py

## Important Notes

⚠️ **Database**: SQLite won't work on Vercel (ephemeral filesystem).
- Use PostgreSQL (recommended), MongoDB, or other cloud database
- Update DATABASE_URL in .env and Vercel settings

✅ **Static files**: Served directly from /static folder

## Troubleshooting

If deployment fails:
1. Check Vercel build logs: Dashboard → Project → Deployments
2. Ensure all env vars are set correctly
3. Verify requirements.txt has all dependencies
4. Check that api/index.py can import app.py

## Local Test Before Deploy

```bash
# Test serverless entry
python -c "from api.index import app; print('✅ api/index.py works')"
```

That's it! Your Happy Trails app will be live on vercel.app after deployment.
