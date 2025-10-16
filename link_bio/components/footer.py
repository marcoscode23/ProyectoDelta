import reflex as rx 

def footer() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.image(
                src="ubicacion.png",
                size="8",
                height="35px",
                padding_x="40px",
                padding_y="1px",
                position="sticky",
            ),
        ),
        rx.center(
            rx.link(
                
                rx.button("Ubicación", color="while",border_radius="50px",bg="#007bff",_hover={"bg": "#339cff", "transform": "scale(1.05)"}),
                href="https://www.google.com/maps/place/DELTA+STORE+%2F+DELTA+STREET/@-36.6197025,-64.2978102,17z/data=!3m1!4b1!4m6!3m5!1s0x95c2cd0057ef55cb:0x44e01601d8b4a77c!8m2!3d-36.6197068!4d-64.2952353!16s%2Fg%2F11w7cvfw81?entry=ttu",
                is_external=True,
            ),
        ),
        rx.box(
            rx.text("🏠Nuestro horario de atención es de lunes a sábado, por la mañana de 8:30 a 12:30"
                " y por la tarde de 17:00 a 21:00. ¡Te esperamos en esos horarios para brindarte la mejor atención!",
                align="center",font_size="16px",
            padding_y="8px",
                color="black",
                font_weight="bold",
            ),
            margin_top="100px",
            width="100%",
            
        ),
        # === SECCIÓN INFERIOR: INFORMACIÓN Y CONTACTO ===
        rx.box(
            rx.hstack(
                # Navegación
                rx.vstack(
                    rx.text("NAVEGACIÓN", weight="bold", color="white", font_size="15px"),
                    rx.link("Inicio", href="/", color="white"),
                    rx.link("Productos", href="/products", color="white"),
                    rx.link("Contacto", href="https://wa.me/543794258727?text=Hola%20Delta%20Store%20👋%2C%20quiero%20consultar%20por%20unas%20zapatillas.", color="white"),
                    spacing="2",
                    align="start",
                ),
                # Medios de pago
                rx.vstack(
                    rx.text("MEDIOS DE PAGO", weight="bold", color="white", font_size="15px"),
                    rx.image(src="/tarjetas.png", height="100px"),
                # === FORMAS DE ENVÍO ===
                rx.center(
                    rx.vstack(
                        rx.text("FORMAS DE ENVÍO", weight="bold", font_size="14px", color="white"),
                        rx.image(src="/correoargentino@2x.png", height="30px"),
                        rx.link("SEGUIMIENTO DE ENVIOS",href="https://www.correoargentino.com.ar/formularios/e-commerce",color="white",font_size="15px",weight="bold",),
                        spacing="2",
                ),
                bg="black",
                padding_bottom="20px",
                ),
                spacing="2", 
                align="start",
                ),
                # Contactanos
                rx.vstack(
                    rx.text("CONTACTANOS", weight="bold", color="white", font_size="15px"),
                    rx.hstack(rx.icon("phone", color="white", size=16), rx.text("02954 806873", color="white")),
                    rx.hstack(rx.icon("mail", color="white", size=16), rx.text("shoesdeltastore@gmail.com", color="white")),
                    rx.hstack(rx.icon("map-pin", color="white", size=16), rx.text("JUNIN 868", color="white")),
                    spacing="1",
                    align="start",
                ),
                # Redes + Newsletter
                rx.vstack(
                    rx.text("REDES SOCIALES", weight="bold", color="white", font_size="15px"),
                    rx.link(rx.icon("instagram", color="white", size=22), href="https://www.instagram.com", is_external=True),
                    rx.text("NEWSLETTER", weight="bold", color="white", font_size="15px", margin_top="10px"),
                    rx.hstack(
                        rx.input(placeholder="shoesdeltastore@gmail.com", width="150px", height="35px"),
                        rx.button(rx.icon("send"), bg="white", color="black"),
                    ),
                    spacing="2",
                    align="start",
                ),
                justify="center",
                align="start",
                padding="40px",
                bg="black",
                wrap="wrap",
            ),
            width="100%",
        ),
        # === COPYRIGHT FINAL ===
        rx.center(
            rx.text("COPYRIGHT DELTA STORE - 2025. TODOS LOS DERECHOS RESERVADOS", color="black", font_size="12px"),
            bg="white",
            padding_y="10px",
            border_top="1px solid #333",
        ),

# --- Elementos de la línea de Defensa del Consumidor y Botón de Arrepentimiento ---
    # Texto fijo: DEFENSA DE LAS Y LOS CONSUMIDORES. PARA RECLAMOS 
    rx.text(
        "DEFENSA DE LAS Y LOS CONSUMIDORES. PARA RECLAMOS ",
        color="black",
        font_size="12px",  # Usar un tamaño adecuado, 8px es muy pequeño
        display="inline",
        style={"whiteSpace": "nowrap"} # Previene que el texto se separe
    ),
    
    # 2. Link: INGRESÁ ACÁ.
    rx.link(
        "INGRESÁ ACÁ.",
        href="https://autogestion.produccion.gob.ar/consumidores",  # Reemplaza '#' con la URL real para reclamos
        color="black",
        font_size="12px",
        font_weight="bold",
        text_decoration="none",
        display="inline",
        margin_right="5px", 
        _hover={"text_decoration": "underline"}, 
    ),
    
    # 3. Separador: /
    rx.text(
        " / ",
        color="black",
        font_size="12px",
        display="inline",
    ),
    
    # 4. Link: BOTÓN DE ARREPENTIMIENTO
    rx.link(
        "BOTÓN DE ARREPENTIMIENTO",
        href="#",  
        color="black",
        font_size="12px",
        font_weight="bold",
        text_decoration="none",
        display="inline",
        _hover={"text_decoration": "underline"}, 
    ),
    
    padding_y="3px",      
    width="100%",
    align="center",       
    justify="center",       
    wrap="wrap",
)
