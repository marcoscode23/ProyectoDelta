import reflex as rx

class CartState(rx.State):
    # Lista global del carrito
    cart_items: list[dict] = []

    def add_product(self, product: dict):
        """Agrega un producto al carrito"""
        self.cart_items.append(product)

    def remove_product(self, index: int):
        """Elimina un producto del carrito"""
        if 0 <= index < len(self.cart_items):
            self.cart_items.pop(index)

    def clear_cart(self):
        """Vacía todo el carrito"""
        self.cart_items = []
