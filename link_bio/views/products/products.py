import reflex as rx
from link_bio.cart_states import CartState



#---- BUSCADOR ----
def search_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Buscar",
            size="3",
            width="250px",
            border_radius="10px",
            border_color="transparent",
            bg="#444",
            _placeholder={"color": "white"},
            _focus={"border_color": "transparent","box_shadow":"0 0 0 2px #555"}
        ),
        rx.button(
            rx.icon(tag="search"),
            bg="white",
            color="black",
            border="1px solid #ccc",
            border_left="none",
            border_radius="0px 5px 5px 0px",
            height="100%",
            padding_x="10px",
            _hover={"bg": "#050404", "color": "white"},
        ),
        spacing="1",
        align_items="center",
        justify="center",  
        width="100%",       
    )
# ---- CARRITO Y CUENTAS ----
def account_links() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.button(
                    rx.icon(tag="shopping_cart"),
                    rx.text(f"CARRITO ()"),
                    bg="#A9A9A9",
                    color="white",
                    size="3",
                    width=["90%","40%"],
                    padding_x="10px",
                    border_radius="5px",
                    _hover={"bg": "#444"},
                ),
                width="100%",       
                justify="center",
                align="center",     
            ),
            
        rx.hstack(
            rx.link(
                "CREAR CUENTA",
                href="#",
                color="black",
                font_size="10px",
                text_decoration="none",
                _hover={"text_decoration": "underline"},
            ),
            rx.text("|", color="black", font_size="10px"),
            rx.link(
                "INICIAR SESIÓN",
                href="#",
                color="black",
                font_size="10px",
                text_decoration="none",
                _hover={"text_decoration": "underline"},
            ),
            spacing="2",
            align_items="center",
            justify="center",   
            width="100%",
        ),
        direction="column",
        align_items="center",
        spacing="2",
        padding_x=["10px","40px"],
        padding_y="20px",
        justify="center",
        align="center",
        width="100%",           
    ),

def products() -> rx.Component:
    return rx.box(
        # Título centrado
        #----- PAGINA DE PRODUCTOS -----
        rx.box(
            rx.center(
                rx.hstack(
                    rx.spacer(),
                    search_bar(),
                    rx.spacer(),
                    account_links(),
                    align="center",
                    justify="start",
                    padding_x=["10px","50px"],  # ✅ margen lateral adaptable
                    height="auto",              
                    bg="white",                 
                    wrap="wrap",                # ✅ evita que se desborde en celular
                    spacing="4",                
                ),
            ),
            rx.center(
                rx.text(
                    "Nuestros Productos - Zapatillas",
                    font_size=["20px","28px"],     
                    font_weight="bold",
                    color="black",
                    text_align="center",
                    margin_y="10px",
                    padding_x="10px",                
                    
            ),
            position="sticky",
            top="0",
            z_index="10",
            box_shadow="0 2px 5px rgba(0,0,0,0.2)",
            ),
            rx.center(
                rx.image(
                    src="delta.png",
                    margin_top="50px",
                    width=["100%", "auto"],              
                    ),
            ),
        ),
        rx.hstack(
            rx.link(rx.button("VOLVER",font_size="16px", color="white",border_radius="30px",font_weight="bold",bg="black",margin_top="100px",_hover={"transform": "scale(1.05)"}),
                    href="/",
            
        ),
        justify="center",
        align="center",
        ),

        # Contenedor FLEX de productos
        rx.flex(
            # Lista de productos
            *[
                rx.box(
                    rx.vstack(
                                rx.image(src=src, width="200px", height="250px"),
                                rx.text(nombre, color="black"),
                                rx.text(precio, color="black"),
                        rx.box(
                            rx.text("3 cuotas sin interés de $30.000,00",color="black",font_size="10px",font_weight="medium",border=""),
                            
                            border="1px solid black",  
                            padding="5px",             
                            border_radius="5px",       
                            bg="white",
                        ),
                        rx.button(
                            efectivo, color="grey", bg="white", opacity="1"
                        ),
                        rx.button(
                            "Añadir al carrito", color="white", bg="black",_hover={"transform": "scale(1.05)"},href="/cart",
                            on_click=lambda: CartState.add_product({
                                "name": nombre,
                                "price": precio,
                                "image": src
                            }),
                    
                        ),
                        spacing="3",
                        align="center",
                    ),
                    max_width="200px",
                    width=["45%","30%","18%"],
                    mix_width="220",
                    bg="transparent",  # sin fondo
                    border="none",     # sin borde
                    box_shadow="none", # sin sombra
                    align="center",
                    justify="center",
                    margin_bottom="40px",
                )
                for src, nombre, precio, efectivo in [
                    ("VANSSKNUSKOOL.png", "VANS KNU SKOOL #793", "$50.000", "$60.500 con efectivo (en el local)"),
                    ("vans u hylane.png", "VANS U HYLANE", "$80.000", "$60.500 con efectivo (en el local)"),
                    ("puma 180.png", "PUMA", "$90.000", "$67.500 con efectivo (en el local)"),
                    ("SAMBAXLG.png", "SAMBA XLG", "$80.000", "$60.000 con efectivo (en el local)"),
                    ("AIRFORCE.png", "AIR FORCE", "$80.000", "$60.000 con efectivo (en el local)"),
                    ("CAMPUSXBADBUNNY.png","CAMPUS X BAD BUNNY","$90.000","$67.500 con efectivo (en el local)"),
                    ("SAMBA795.png"," SAMBA #795","$90.000","$80.500 con efectivo (en el local)"),
                    ("DOBLEBDARK669.jpg"," DOBLEB DARK #669","$90.000","$67.500 con efectivo (en el local)"),
                    ("ADI 2000.png","ADI 2000","$110.000","$92.500 con efectivo (en el local)"),
                    ("CAMPUSXBADBUNNY783.png","CAMPUS X BADBUNNY #783 ","$90.000","$67.500 con efectivo (en el local)"),
                    ("SBDUNK778.png"," SB DUNK #778","$90.000","$67.500 con efectivo (en el local)"),
                    ("JORDAN1-823.png"," JORDAN 1 #823","$90.000","$67.500 con efectivo (en el local)"),
                    ("CASUALDOBLEBCOCOA.png","CASUAL DOBLEB COCOA #841","$90.000","$67.500 con efectivo (en el local)"),
                    ("ADIDASORMILLEN850.png","ADIDAS ZORMILLEN #841","$90.000","$67.500 con efectivo (en el local)"),
                    ("CONVERSEALLSTAR717.png"," CONVERSE ALL STAR #717","$90.000","$67.500 con efectivo (en el local)"),
                    ("SBDUNKLOW.png","SB DUNK LOW #798 ","$90.000","$67.500 con efectivo (en el local)"),
                    ("VANSKNUSKOOLL.png","VANS KNU SKOOL #676","$90.000","$67.500 con efectivo (en el local)"),
                    ("JORDAN1LOWXTRAVISSCOTT.png","JORDAN 1 LOW X TRAVIS SCOTT #769","$90.000","$67.500 con efectivo (en el local)"),
                    ("DOBLEBSKY.png","DOBLED SKY","$90.000","$67.500 con efectivo (en el local)"),
                    ("JORDAN1MIDBROWN.png","JORDAN 1 MID BROWN","$90.000","$67.500 con efectivo (en el local)"),
                    ("VANSUUPLAND.png","VANS U UPLAND","$90.000","$67.500 con efectivo (en el local)"),
                ]
            ],
            justify="center",  
            align="start",  
            wrap="wrap",       
            spacing="9",
            row_gap="50px",    
            width="100%",
            padding_y="100px",
        ),
        # --- BOTÓN MOSTRAR MÁS ---
        rx.center(
            rx.button(
                "Mostrar más productos",
                bg="black",
                color="white",
                border_radius="5px",
                padding_x="20px",
                padding_y="10px",
                _hover={"bg": "#444"},
                margin_top="20px",
            ),
            margin_bottom="50px",
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
            text_align="center",
            justify="center",
        ),

# --- Elementos de la línea de Defensa del Consumidor y Botón de Arrepentimiento ---
    # Texto fijo: DEFENSA DE LAS Y LOS CONSUMIDORES. PARA RECLAMOS 
    rx.center(
    rx.text(
        "DEFENSA DE LAS Y LOS CONSUMIDORES. PARA RECLAMOS ",
        color="black",
        font_size="12px", 
        display="inline",
        style={"whiteSpace": "nowrap"}, 
    ),
    ),
    
    # 2. Link: INGRESÁ ACÁ.
    rx.center(
    rx.link(
        "INGRESÁ ACÁ.",
        href="https://autogestion.produccion.gob.ar/consumidores",  
        color="black",
        font_size="12px",
        font_weight="bold",
        text_decoration="none",
        display="inline",
        margin_right="5px", 
        _hover={"text_decoration": "underline"}, 
    ),
    ),
    
    # 3. Separador: /
    rx.center(
    rx.text(
        " / ",
        color="black",
        font_size="12px",
        display="inline",
    ),
    ),
    
    # 4. Link: BOTÓN DE ARREPENTIMIENTO
    rx.center(
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
    ),
    padding_y="60px",      
    width="100%",
    align="center",       
    justify="center",     
    wrap="wrap",
    row_gap="40px",
    bg="white",
    ),
    