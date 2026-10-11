# Basic authentication

A simple Flask API with one model, `User`, protected step by step by a
hand-written **Basic authentication** system. Users are stored by serializing
them to a JSON file (`.db_User.json`).

> In real projects, use a library such as Flask-HTTPAuth instead of writing
> your own Basic authentication. This project builds it by hand to show how it
> works.

## Concepts

- **Authentication**: proving who is making a request.
- **Base64**: an encoding that represents binary data with 64 ASCII
  characters. It is *not* encryption.
- **Basic authentication**: the client sends
  `Authorization: Basic <base64(email:password)>` with each request.
- **401 Unauthorized**: no credentials, or credentials could not be checked.
  **403 Forbidden**: credentials were sent but they don't match a user.

## Setup and run

```bash
pip3 install -r requirements.txt
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```

`AUTH_TYPE` selects the authentication: `basic_auth` uses `BasicAuth`, any
other non-empty value uses `Auth`, and leaving it unset disables
authentication.

```bash
curl "http://0.0.0.0:5000/api/v1/users" \
     -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
```

## Files

| File | Content |
| --- | --- |
| `api/v1/app.py` | Flask app, 401/403/404 JSON error handlers, `AUTH_TYPE` selection and the `before_request` filter. |
| `api/v1/views/index.py` | `/status`, `/stats`, `/unauthorized` (aborts 401) and `/forbidden` (aborts 403). |
| `api/v1/views/users.py` | CRUD routes for `User`. |
| `api/v1/auth/auth.py` | `Auth`: template class with `require_auth` (slash-tolerant excluded paths), `authorization_header` and `current_user`. |
| `api/v1/auth/basic_auth.py` | `BasicAuth(Auth)`: extracts and decodes the Base64 header, splits `email:password`, looks up the `User` and checks the password. |
| `models/base.py`, `models/user.py` | `Base` model with file storage and the `User` model. |

## Requests that skip authentication

`/api/v1/status/`, `/api/v1/unauthorized/` and `/api/v1/forbidden/` (with or
without the trailing slash). Every other route needs an `Authorization`
header (otherwise 401) that identifies a valid user (otherwise 403).
