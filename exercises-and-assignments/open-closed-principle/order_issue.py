from datetime import datetime, timedelta


class Orden:
    def __init__(self):
        self.__articulos = []       # lista de tuplas (nombre, precio, peso_kg)
        self.__metodoEnvio = None   # "tierra" | "aire"

    # ── Métodos públicos ──────────────────────────────────────────────────────

    def total(self) -> float:
        """Suma el precio de todos los artículos."""
        return sum(precio for _, precio, _ in self.__articulos)

    def pesoTotal(self) -> float:
        """Suma el peso de todos los artículos en kilogramos."""
        return sum(peso for _, _, peso in self.__articulos)

    def asignarMetodoEnvio(self, metodo: str) -> None:
        """Asigna el método de envío ('tierra' o 'aire')."""
        metodo = metodo.lower()
        if metodo not in ("tierra", "aire"):
            raise ValueError(f"Método de envío inválido: '{metodo}'. Use 'tierra' o 'aire'.")
        self.__metodoEnvio = metodo

    def costoEnvio(self) -> float:
        """
        Calcula el costo de envío según el método asignado.
          - tierra: $10 por kg (gratis si total() > 100)
          - aire  : $30 por kg
        """
        if self.__metodoEnvio is None:
            raise RuntimeError("Debe asignar un método de envío antes de calcular el costo.")

        if self.__metodoEnvio == "tierra":
            # Envío gratis en órdenes grandes
            if self.total() > 100:
                return 0
            return self.pesoTotal() * 10

        if self.__metodoEnvio == "aire":
            return self.pesoTotal() * 30

    def fechaEnvio(self) -> str:
        """
        Estima la fecha de entrega según el método de envío.
          - tierra : 5 días hábiles
          - aire   : 1 día hábil
        """
        if self.__metodoEnvio is None:
            raise RuntimeError("Debe asignar un método de envío antes de consultar la fecha.")

        dias = 5 if self.__metodoEnvio == "tierra" else 1
        fecha_entrega = datetime.today() + timedelta(days=dias)
        return fecha_entrega.strftime("%d/%m/%Y")

    # ── Helpers ───────────────────────────────────────────────────────────────

    def agregarArticulo(self, nombre: str, precio: float, peso_kg: float) -> None:
        """Agrega un artículo a la orden."""
        self.__articulos.append((nombre, precio, peso_kg))

    def __str__(self) -> str:
        lineas = ["=== Orden ==="]
        for nombre, precio, peso in self.__articulos:
            lineas.append(f"  {nombre}: ${precio:.2f}  ({peso} kg)")
        lineas.append(f"Total artículos : ${self.total():.2f}")
        lineas.append(f"Peso total      : {self.pesoTotal():.2f} kg")
        if self.__metodoEnvio:
            lineas.append(f"Método de envío : {self.__metodoEnvio}")
            lineas.append(f"Costo de envío  : ${self.costoEnvio():.2f}")
            lineas.append(f"Fecha estimada  : {self.fechaEnvio()}")
        return "\n".join(lineas)


# ── Ejemplo de uso ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    orden = Orden()
    orden.agregarArticulo("Laptop",  80.00, 2.5)
    orden.agregarArticulo("Mouse",   15.00, 0.3)
    orden.agregarArticulo("Teclado", 25.00, 0.8)

    # --- Envío por tierra (total > 100 → gratis) ---
    orden.asignarMetodoEnvio("tierra")
    print(orden)

    print()

    # --- Cambiar a envío por aire ---
    orden.asignarMetodoEnvio("aire")
    print(orden)