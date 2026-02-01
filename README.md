# Profile Project: Frontend & Backend Deployment

This repository contains a static frontend (for GitHub Pages) and a Python Flask backend (for Render).

## Structure

```
Profile/
├── backend/         # Flask backend (for Render)
│   ├── app.py
│   ├── main.py
│   ├── README.md
│   ├── requirements.txt
│   └── render.yaml
├── frontend/        # Static frontend (for GitHub Pages)
│   ├── index.html
│   ├── unlock-pdf.html
│   ├── css/
│   ├── js/
│   ├── Files/
│   ├── fonts/
│   └── ...
└── .github/
    └── workflows/
        └── gh-pages.yml
```

## Frontend Deployment (GitHub Pages)
- The `frontend/` folder is deployed automatically to GitHub Pages using the workflow in `.github/workflows/gh-pages.yml`.
- On every push to `master` (or `main`), the workflow uploads the contents of `frontend/` to GitHub Pages.
- Your site will be available at: `https://<username>.github.io/<repo>/`

### To trigger a deploy:
1. Make any change in the repo (e.g., edit a file in `frontend/`).
2. Commit and push to `master`.
3. The workflow will run and deploy your site.

## Backend Deployment (Render)
- The `backend/` folder contains a Flask app ready for deployment on [Render](https://render.com).
- Includes `app.py` (Flask API), `requirements.txt`, and `render.yaml` (Render config).

### To deploy backend:
1. Push your repo to GitHub.
2. Go to [Render](https://render.com), create a new Web Service, and connect your repo.
3. Set the root directory to `backend/`.
4. Set the build command: `pip install -r requirements.txt`
5. Set the start command: `gunicorn -b 0.0.0.0:$PORT app:app`
6. Deploy and get your backend URL.

## Frontend/Backend Integration
- In `frontend/unlock-pdf.html`, update the fetch URL to your Render backend URL after deployment.

## Troubleshooting
- If GitHub Pages does not update, make a new commit to trigger the workflow.
- If Render deploy fails, check logs for missing dependencies or errors in `app.py`.

---

For any issues, check the Actions and Pages tabs on GitHub, or Render logs for backend errors.
