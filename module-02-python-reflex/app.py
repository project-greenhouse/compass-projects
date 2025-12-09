"""Starter Reflex App for Sports Data Science"""

import reflex as rx


class State(rx.State):
    """The app state."""
    pass


def index() -> rx.Component:
    """The main page."""
    return rx.container(
        rx.heading("Sports Data Dashboard", size="9"),
        rx.text(
            "Welcome to your sports data science project!",
            size="5",
        ),
        rx.divider(),
        rx.text(
            "This is a starter template for building interactive sports data applications with Reflex.",
        ),
        rx.text(
            "Replace this content with your own visualizations and analysis.",
        ),
    )


app = rx.App()
app.add_page(index)
