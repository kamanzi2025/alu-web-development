# Session authentication

This project builds on the Basic authentication API. It adds the
`GET /api/v1/users/me` endpoint and a second authentication mechanism,
**Session authentication**: the user logs in once with email and password,
receives a Session ID in a cookie, and then sends that cookie instead of
their credentials.

> In real projects, use a module or framework (for example Flask-Login or
> Flask's built-in session) instead of writing your own. This project builds
> it by hand to show how it works.

## Concepts

- **Session**: server-side state that links a random Session ID to a user.
- **Cookie**: a value the server sets with `Set-Cookie` and the browser sends
  back with each request. Here its name comes from `SESSION_NAME`.
- Sessions are stored in memory (`SessionAuth.user_id_by_session_id`), so
  they are lost when the server restarts.

## Setup and run

```bash
pip3 install -r requirements.txt
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth \
SESSION_NAME=_my_session_id python3 -m api.v1.app
```

`AUTH_TYPE` selects the authentication: `session_auth` uses `SessionAuth`,
`basic_auth` uses `BasicAuth`, any other non-empty value uses `Auth`, and
leaving it unset disables authentication.

```bash
# Log in: returns the user and sets the _my_session_id cookie
curl -XPOST "http://0.0.0.0:5000/api/v1/auth_session/login" \
     -d "email=bob@hbtn.io" -d "password=H0lbertonSchool98!" -c cookies.txt
# Use the session
curl "http://0.0.0.0:5000/api/v1/users/me" -b cookies.txt
# Log out
curl -XDELETE "http://0.0.0.0:5000/api/v1/auth_session/logout" -b cookies.txt
```

## Files

| File | Content |
| --- | --- |
| `api/v1/app.py` | Selects the auth class from `AUTH_TYPE`. Before each request, it returns 401 when there is neither an `Authorization` header nor a session cookie, sets `request.current_user`, and returns 403 when no user is found. |
| `api/v1/auth/auth.py` | `Auth` template, now with `session_cookie(request)`. |
| `api/v1/auth/basic_auth.py` | `BasicAuth` from the previous project. |
| `api/v1/auth/session_auth.py` | `SessionAuth(Auth)`: `create_session`, `user_id_for_session_id`, `current_user` and `destroy_session`. |
| `api/v1/views/users.py` | User CRUD routes. `GET /users/me` returns the authenticated user. |
| `api/v1/views/session_auth.py` | `POST /auth_session/login` and `DELETE /auth_session/logout`. |
| `models/` | `Base` model with file storage and the `User` model. |

## Requests that skip authentication

`/api/v1/status/`, `/api/v1/unauthorized/`, `/api/v1/forbidden/` and
`/api/v1/auth_session/login/` (with or without the trailing slash).
