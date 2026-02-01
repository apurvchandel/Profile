# Profile — Website Only

This repository contains **only the website** (portfolio + tool frontends). It is deployed on **GitHub Pages**.

## Structure

```
Profile/
├── frontend/           # Static site (deployed to GitHub Pages)
│   ├── index.html      # Main portfolio
│   ├── unlock-pdf.html # PDF Unlocker tool (frontend)
│   ├── css/
│   ├── js/
│   ├── Files/
│   └── ...
└── .github/
    └── workflows/
        └── gh-pages.yml
```

## Tools (separate repos + Render)

Each tool has its **own GitHub repo** and is hosted on **Render**. The website only contains the frontend and calls the tool’s API URL.

| Tool          | Repo (example)     | Website page        |
|---------------|--------------------|---------------------|
| PDF Unlocker  | `pdf-unlocker`     | `frontend/unlock-pdf.html` |

### Workflow for each tool

1. **Create a repo** for the tool (e.g. `pdf-unlocker`) in a folder **sibling** to `Profile`:
   ```
   Github/
   ├── Profile/          ← this repo (website only)
   └── pdf-unlocker/     ← separate repo (backend)
   ```

2. **Push the tool repo** to GitHub (e.g. `apurvchandel/pdf-unlocker`).

3. **Deploy on Render**: New Web Service → connect the tool repo → set build/start commands (see that repo’s README).

4. **Use the API URL in the website**: In `frontend/unlock-pdf.html`, set `API_URL` to your Render service URL (e.g. `https://pdf-unlocker-xxxx.onrender.com/unlock`).

### Adding another tool

1. Create a new folder (e.g. `Github/qr-generator`).
2. Add the backend/frontend for that tool, `git init`, push to a new GitHub repo.
3. Deploy that repo on Render (or use a static frontend in Profile and only host the API on Render).
4. Add a page or link in this website that uses the new tool’s URL.

## Website deployment (GitHub Pages)

- The `frontend/` folder is deployed via the workflow in `.github/workflows/gh-pages.yml`.
- On push to `master` (or `main`), the site is published.
- Site URL: `https://<username>.github.io/Profile/`

### Deploy steps

1. Commit and push to `master`.
2. In repo **Settings → Pages**, set **Source** to **GitHub Actions**.

## Summary

- **This repo** = website only (frontend).
- **Tool repos** = one repo per tool, hosted on Render; website calls their APIs.
