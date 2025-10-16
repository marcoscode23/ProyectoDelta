import reflex as rx 
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.button.button import button
from link_bio.views.products.products import products
from link_bio.views.cart.cart_view import cart_view



#class State(rx.State):
#    pass

def index() -> rx.Component:
    return rx.box(
        rx.center(
            
            rx.vstack(
            navbar(),
            header(),
            button(),
            footer(),
            align="center",  
            color="while",
            width="100%",
            spacing="8",
            
        ),
        ),
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="pink",
        bg="white",
        font_family="Poppins, sans-serif",
        width="100%",
        min_height="100vh",
        bg_size="cover",            
        bg_repeat="no-repeat", 
        bg_position="center",
    )




app = rx.App()
app.add_page(index, route="/")
app.add_page(products, route="/products")
app.add_page(cart_view, route="/cart")

app._compile()

