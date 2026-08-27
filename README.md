# ETL GitHub Actions Starter

A tiny, beginner-friendly ETL (Extract, Transform, Load) pipeline:

```
customers.csv --> extract.py --> transform.py --> load.py --> etl.db (SQLite)
```

It also runs automatically in **GitHub Actions** on every push, on a daily
schedule, and on demand.

## Run it locally

```bash
cd etl-github-actions
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

This creates a file called `etl.db` in the project folder — that's your
loaded, cleaned data.

## Run the tests

```bash
pytest
```

## Push to GitHub and let Actions run it

```bash
git init
git add .
git commit -m "Initial ETL pipeline"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

Go to your repo on GitHub → **Actions** tab → you'll see the "ETL Pipeline"
workflow run automatically.

## Switching to PostgreSQL later

Set an environment variable (or a GitHub Actions secret) called
`DATABASE_URL`, e.g.:

```
postgresql://user:password@host:5432/etl
```

`src/main.py` already reads `DATABASE_URL` if it's set, and falls back to
SQLite if it isn't. No code changes needed.
