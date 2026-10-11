#!/usr/bin/env python3
"""DB module that wraps the SQLAlchemy engine and session for users."""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class that stores and queries User objects in SQLite."""

    def __init__(self) -> None:
        """Initialize a new DB instance with a fresh database."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Return the memoized session object, creating it if needed."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save a new user to the database and return the User object."""
        user = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
        return user

    def find_user_by(self, **kwargs) -> User:
        """Return the first user matching the keyword arguments filter."""
        for key in kwargs:
            if not hasattr(User, key):
                raise InvalidRequestError()
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update the attributes of the user with user_id and commit them."""
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise ValueError()
            setattr(user, key, value)
        self._session.commit()
        return None
