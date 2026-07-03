import streamlit as st

from dashboard.config import (
    configure_page
)

from dashboard.auth import (
    AuthenticationManager
)

from dashboard.navigation import (
    DashboardNavigation
)

configure_page()


def main():

    st.title(
        "🏥 HealthRisk Lab"
    )

    AuthenticationManager.login()

    if not (
        AuthenticationManager
        .is_authenticated()
    ):
        st.info(
            "Please Login"
        )
        return

    page = (
        DashboardNavigation.menu()
    )

    st.write(
        f"Current Page: {page}"
    )

    AuthenticationManager.logout()


if __name__ == "__main__":
    main()