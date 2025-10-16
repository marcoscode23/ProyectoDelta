import reflex as rx 

def button() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.button("Comenzar Compra",color="white",bg="black",border_radius="50px",padding="1em 2em",font_wieght="bold",_hover={"transform": "scale(1.05)"}),
            href="/products",
        )
    )