# PDF Unlocker Backend

Flask API for unlocking password-protected PDFs. Deploy on [Render](https://render.com).

## Setup (local)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

## Run locally

```bash
python app.py
```

API runs at `http://localhost:10000`.

## CLI (unlock PDF from command line)

```bash
python main.py input.pdf [password]
```

## API

- **GET /** – Health check
- **POST /unlock** – Form fields: `file` (PDF), `password` (optional)

## Deploy on Render

Set **Root Directory** to `backend`, **Start Command** to:

```bash
gunicorn -b 0.0.0.0:$PORT app:app
```
