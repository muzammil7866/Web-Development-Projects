FastAPI Examples
================

This folder contains small FastAPI example projects used for learning and demonstration. Each example is isolated in its own subfolder with a short README and can be run with `uvicorn`.

Structure:

- `01-basic-endpoint/` — a simple root and POST greeting example.
- `02-parameters/` — examples showing path and query parameters.
- `03-request-body/` — request body example using Pydantic models.
- `99-setup/` — small project setup notes.

Quick start (create and activate a virtualenv, then):

```bash
pip install -r requirements.txt
uvicorn fastapi_examples.01_basic_endpoint.creating_first_endpoint:app --reload
```

Remove the `testvenv/` folder before publishing or add it to `.gitignore`.

If you want, I can split this into a dedicated Git repo and prepare a polished README for publishing.
