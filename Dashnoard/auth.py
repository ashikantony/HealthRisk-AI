import streamlit as st


class AuthenticationManager:

    USERS = {
        "admin": "admin123",
        "analyst": "analyst123",
        "researcher": "research123"
    }

    @classmethod
    def login(cls):

        st.sidebar.title("Login")

        username = st.sidebar.text_input(
            "Username"
        )

        password = st.sidebar.text_input(
            "Password",
            type="password"
        )

        if st.sidebar.button("Login"):

            if (
                username in cls.USERS
                and
                cls.USERS[username]
                == password
            ):

                st.session_state[
                    "authenticated"
                ] = True

                st.session_state[
                    "user"
                ] = username

                st.success(
                    "Login Successful"
                )

            else:
                st.error(
                    "Invalid Credentials"
                )

    @classmethod
    def logout(cls):

        if st.sidebar.button(
            "Logout"
        ):
            st.session_state.clear()

    @classmethod
    def is_authenticated(cls):

        return st.session_state.get(
            "authenticated",
            False
        )