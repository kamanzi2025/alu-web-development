# User authentication service

A small user authentication service built with **Flask**, **SQLAlchemy** and
**bcrypt**. Users are stored in a SQLite database (`a.db`). Passwords are
stored only as salted bcrypt hashes. Sessions and password resets use random
UUIDs.

> In real projects, use a module or framework that handles authentication for
> you (for example Flask-User). This project builds it by hand to show how it
> works.

## Layers

| File | Role |
| --- | --- |
| `user.py` | `User` SQLAlchemy model for the `users` table: `id`, `email`, `hashed_password`, `session_id`, `reset_token`. |
| `db.py` | `DB`: `add_user`, `find_user_by` (raises `NoResultFound` / `InvalidRequestError`) and `update_user` (raises `ValueError` for unknown fields). |
| `auth.py` | `_hash_password`, `_generate_uuid` and `Auth`: `register_user`, `valid_login`, `create_session`, `get_user_from_session_id`, `destroy_session`, `get_reset_password_token`, `update_password`. |
| `app.py` | Flask app. It talks only to `Auth` (through `AUTH`), never directly to `DB`. |

## Endpoints

| Method and route | Form / cookie | Success | Failure |
| --- | --- | --- | --- |
| `GET /` | | `{"message": "Bienvenue"}` | |
| `POST /users` | `email`, `password` | `{"email": ..., "message": "user created"}` | 400 `{"message": "email already registered"}` |
| `POST /sessions` | `email`, `password` | `{"email": ..., "message": "logged in"}` and a `session_id` cookie | 401 |
| `DELETE /sessions` | `session_id` cookie | redirect to `GET /` | 403 |
| `GET /profile` | `session_id` cookie | `{"email": ...}` | 403 |
| `POST /reset_password` | `email` | `{"email": ..., "reset_token": ...}` | 403 |
| `PUT /reset_password` | `email`, `reset_token`, `new_password` | `{"email": ..., "message": "Password updated"}` | 403 |

## Setup and run

```bash
pip3 install bcrypt flask "sqlalchemy==1.3.*"
python3 app.py
```

```bash
curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'
curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -c cookies.txt
curl localhost:5000/profile -b cookies.txt
curl -XDELETE localhost:5000/sessions -b cookies.txt
```
