import reflex as rx 


# --- Estilos ---
nav_item_style = {
    "color": "white",
    "font_weight": "bold",
    "padding_x": "1em",
    "padding_y": "0.5em",
    "_hover": {"background_color": "#2a2a2a", "cursor": "pointer"},
}

menu_item_style = {
    "color": "white",
    "background_color": "black",
    "_hover": {"background_color": "#2a2a2a", "cursor": "pointer"},
}


# --- Submenú ZAPATILLAS ---
def submenu_zapatillas() -> rx.Component:
    return rx.menu.sub(
        rx.menu.sub_trigger(
            rx.hstack(
                rx.text("ZAPATILLAS", color="white"),
                rx.icon("chevron-right", size=16, color="white"),
                justify="between",   
                width="100%",
            ),
            bg="black",
            padding_x="1em",
            padding_y="0.5em",
            border_radius="none",
            _hover={"background_color": "#2a2a2a"},
        ),
        rx.menu.sub_content(
            rx.menu.item("RUNNING", **menu_item_style),
            rx.menu.item("URBANAS", **menu_item_style),
            bg="black",
            border="none",
        ),
    )


# --- Menú PRODUCTOS ---
def menu_productos() -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.text("PRODUCTOS", **nav_item_style),
        ),
        rx.menu.content(
            submenu_zapatillas(),
            rx.menu.item("IMPORTADAS", **menu_item_style),
            rx.menu.item("NACIONALES", **menu_item_style),
            rx.menu.item("DEPORTIVAS", **menu_item_style),
            bg="black",
            border="none",
            min_width="200px",
        ),
    )


# --- HEADER + NAVBAR (combinados) ---
def header() -> rx.Component:
    return rx.vstack(
        # Logo + mensaje
        rx.image(
            src="/logo_tienda.png",
            width="400px",
            max_windth="90%", 
            margin_top="50px",
        ),
        rx.text(
            "BIENVENIDO A DELTA STORE 👋 SOMOS UNA TIENDA QUE SE DEDICA A LA VENTA DE 👟ZAPATILLAS!",
            font_size=["0.9em","1em"],
            font_weight="bold",
            color="black",
            text_align="center",
            margin_top="0.8em",
            padding_x="10px",
        ),

        # Barra de navegación debajo del logo
        rx.box(
            rx.hstack(
                rx.link(rx.text("INICIO", **nav_item_style), href="/"),
                menu_productos(),
                rx.link(rx.text("CONTACTO", **nav_item_style),href="https://wa.me/543794258727?text=Hola%20Delta%20Store%20👋%2C%20quiero%20consultar%20por%20unas%20zapatillas."),
                direction="row",
                justify="center",
                align="center",
                spacing="4",
            
            ),
            background_color="black",
            width=["90%","60%","40%"],
            padding_y="1em",
            border_bottom="2px solid white",
            border_radius="12px",
            margin_top="20px",
            box_shadow="0px 0px 10px rgba(0,0,0,0.3)",
            font_wieght="bold",
        ),
        rx.vstack(
            rx.center(
                rx.image(
                    src="delta.png",
                ),
            ),
        ),
        rx.vstack(
            rx.box(
                rx.box(
                #imagen con efecto hover (zoom)
                    rx.image(
                        src="/INSTAGRAMDELTA.png",
                        width="400px",
                        height="auto",
                        border_radius="15px",
                        transition="transform 0.6s ease-in-out",
                        _hover={"transform": "scale(1.1)"}, #zoom sueve
                    ),
                    
                ),
                #texto y boton superpuestos
                rx.box(
                    rx.vstack(
                        rx.text(
                            "NUESTRO NUEVO INSTAGRAM",
                            font_size="20px",
                            font_weight="bold",
                            color="white",
                            align="center",
                            justify="center",
                        ),
                        rx.link(
                            rx.button(
                                "SOMOSDST",
                                bg="black",
                                color="white",
                                font_weight="bold",
                                border_radius="30px",
                                _hover={"bg": "gray"},
                            ),
                            href="https://www.instagram.com/somosdst/",
                            is_external=True,
                        ),
                        spacing="4",
                        align="center",
                        justify="center",
                        margin_top="200px",
                    ),
                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    align="center",
                    justify="center",
                    bg="rgba(0, 0, 0, 0.4)",  # Oscurece la imagen
                    border_radius="20px",
                    opacity="0",
                    transition="opacity 0.4s ease",
                    _hover={"opacity": "1"},  # Aparece el texto al pasar el mouse
                ),
                position="relative",
                width="400px",
                height="auto",
                overflow="hidden",
            ),
            align="center",
            justify="center",
            margin_top="50px",
        ),
        spacing="9",
        align="center",
        width="100%",
    ),
