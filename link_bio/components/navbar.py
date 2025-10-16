import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "25% OFF EFECTIVO - 20% OFF TRANSFERENCIA",
            height="50px",font_size="11px",padding="19px",
        ),
        justify="center",bg="black",width="100%",
    ),
