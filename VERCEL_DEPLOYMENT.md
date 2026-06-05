# Vercel Deployment Guide

## What's been fixed for the 500 error:

1. **Updated `settings.py`** to handle Vercel deployments:
   - Added specific domain `mr-chow.vercel.app` to ALLOWED_HOSTS
   - Configured logging to debug issues
   - Added support for both SQLite and PostgreSQL databases
   - Fixed static file handling with WhiteNoise

2. **Updated `vercel.json`**:
   - Added database migrations to build command
   - Properly configured Django framework settings

3. **Updated `requirements.txt`**:
   - Added `dj-database-url` for PostgreSQL support (optional)

## Setup on Vercel Dashboard:

1. Go to your Vercel project settings
2. Navigate to **Environment Variables**
3. Add these variables:
   - `SECRET_KEY`: Generate a secure key (use Django's `get_random_secret_key()`)
   - `DEBUG`: Set to `False`
   - `ALLOWED_HOSTS`: Already configured for `mr-chow.vercel.app`

## Optional: Use PostgreSQL (recommended for production)

SQLite doesn't persist data on Vercel's ephemeral filesystem. For production, use PostgreSQL:

1. Set up a PostgreSQL database (e.g., on Railway, Render, or AWS)
2. Add `DATABASE_URL` environment variable to Vercel
3. Redeploy - Django will automatically use PostgreSQL

## Testing:

1. Push changes to GitHub
2. Vercel will automatically redeploy
3. Check deployment logs for any errors
4. Visit https://mr-chow.vercel.app/

## Common Issues:

- **Still getting 500 errors**: Check Vercel deployment logs
- **Static files not loading**: Already handled with WhiteNoise
- **Database errors**: Ensure migrations ran during build (check logs)
