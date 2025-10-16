import reflex as rx
from link_bio.cart_states import CartState

def cart_view() -> rx.Component:
    """Vista del carrito de compras"""
    return rx.box(
        rx.center(
            rx.vstack(
                rx.text("🛒 Tu carrito", font_size="24px", font_weight="bold", margin_bottom="20px", color="black"),
                # Lista de productos en el carrito
                rx.foreach(
                    CartState.cart_items,
                    lambda item, index: rx.hstack(
                        rx.image(src=item["image"], width="100px", height="100px", border_radius="10px"),
                        rx.vstack(
                            rx.text(item["name"], font_weight="bold", color="black"),
                            rx.text(f"${item['price']}", color="gray"),
                        ),
                        rx.button(
                            "Eliminar",
                            color="white",
                            bg="red",
                            border_radius="10px",
                            _hover={"bg": "#900"},
                            on_click=lambda: CartState.remove_product(index),
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        padding="10px",
                        border_bottom="1px solid #ddd"
                    )
                ),
                rx.cond(
                    CartState.cart_items,
                    rx.button(
                        "Finalizar compra",
                        bg="black",
                        color="white",
                        border_radius="10px",
                        _hover={"bg": "#333"},
                        margin_top="20px"
                    ),
                    rx.text("Tu carrito está vacío 🛍️", color="gray", font_size="18px")
                ),
                spacing="4",
                align="center",
                width="100%",
                padding="40px",
            ),
        ),
        bg="white",
        width="100%",
        min_height="100vh",
    )
