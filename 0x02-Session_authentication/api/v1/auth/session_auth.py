#!/usr/bin/env python3
"""Module contains the sessionAuth class."""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session for UserId"""
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns UserId based on a particular session."""
        if session_id is None or not isinstance(session_id, str):
            return None
        else:
            User = self.user_id_by_session_id.get(session_id)
            return User
