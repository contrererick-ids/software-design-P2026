from abc import ABC, abstractmethod
from datetime import datetime, timedelta


# ══════════════════════════════════════════════════════════════════════════════
#  <<interface>>  MetodoEnvio
#  Define el contrato que toda estrategia de envío debe cumplir.
#  Aplicando OCP: Orden nunca necesita modificarse para soportar nuevos métodos.
# ══════════════════════════════════════════════════════════════════════════════

class MetodoEnvio(ABC):

    @abstractmethod
    def obtenerCosto(self, orden: "Orden") -> float:
        """Calcula el costo de envío para la orden dada."""
        ...

    @abstractmethod
    def obtenerFecha(self, orden: "Orden") -> str:
        """Estima la fecha de entrega para la orden dada."""
        ...


# ══════════════════════════════════════════════════════════════════════════════
#  Implementación concreta: Tierra
# ══════════════════════════════════════════════════════════════════════════════

class Tierra(MetodoEnvio):
    COSTO_POR_KG = 10
    DIAS_ENTREGA = 5
    MINIMO_GRATIS = 100

    def obtenerCosto(self, orden: "Orden") -> float:
        # Envío gratis en órdenes grandes
        if orden.total() > self.MINIMO_GRATIS:
            return 0
        return orden.pesoTotal() * self.COSTO_POR_KG

    def obtenerFecha(self, orden: "Orden") -> str:
        fecha = datetime.today() + timedelta(days=self.DIAS_ENTREGA)
        return fecha.strftime("%d/%m/%Y")


# ══════════════════════════════════════════════════════════════════════════════
#  Implementación concreta: Aire
# ══════════════════════════════════════════════════════════════════════════════

class Aire(MetodoEnvio):
    COSTO_POR_KG = 30
    DIAS_ENTREGA = 1

    def obtenerCosto(self, orden: "Orden") -> float:
        return orden.pesoTotal() * self.COSTO_POR_KG

    def obtenerFecha(self, orden: "Orden") -> str:
        fecha = datetime.today() + timedelta(days=self.DIAS_ENTREGA)
        return fecha.strftime("%d/%m/%Y")


# ══════════════════════════════════════════════════════════════════════════════
#  Clase principal: Orden
#  SRP → solo gestiona artículos y delega TODO lo relacionado al envío
#         a la estrategia (MetodoEnvio) que se le inyecte.
#  OCP → abierta para extensión (nuevos MetodoEnvio), cerrada para modificación.
# ══════════════════════════════════════════════════════════════════════════════

class Orden:
    def __init__(self):
        self.__articulos: list[tuple[str, float, float]] = []  # (nombre, precio, peso_kg)
        self.__metodoEnvio: MetodoEnvio | None = None

    # ── Gestión de artículos ──────────────────────────────────────────────────

    def agregarArticulo(self, nombre: str, precio: float, peso_kg: float) -> None:
        self.__articulos.append((nombre, precio, peso_kg))

    def total(self) -> float:
        return sum(precio for _, precio, _ in self.__articulos)

    def pesoTotal(self) -> float:
        return sum(peso for _, _, peso in self.__articulos)

    # ── Configuración del método de envío ─────────────────────────────────────

    def asignarMetodoEnvio(self, envio: MetodoEnvio) -> None:
        if not isinstance(envio, MetodoEnvio):
            raise TypeError("El envío debe implementar la interfaz MetodoEnvio.")
        self.__metodoEnvio = envio

    # ── Delegación al método de envío ─────────────────────────────────────────

    def costoEnvio(self) -> float:
        self._verificarMetodoEnvio()
        return self.__metodoEnvio.obtenerCosto(self)

    def fechaEnvio(self) -> str:
        self._verificarMetodoEnvio()
        return self.__metodoEnvio.obtenerFecha(self)

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _verificarMetodoEnvio(self) -> None:
        if self.__metodoEnvio is None:
            raise RuntimeError("Debe asignar un método de envío primero.")

    def __str__(self) -> str:
        lineas = ["=== Orden ==="]
        for nombre, precio, peso in self.__articulos:
            lineas.append(f"  {nombre}: ${precio:.2f}  ({peso} kg)")
        lineas.append(f"Total artículos : ${self.total():.2f}")
        lineas.append(f"Peso total      : {self.pesoTotal():.2f} kg")
        if self.__metodoEnvio is not None:
            lineas.append(f"Método de envío : {type(self.__metodoEnvio).__name__}")
            lineas.append(f"Costo de envío  : ${self.costoEnvio():.2f}")
            lineas.append(f"Fecha estimada  : {self.fechaEnvio()}")
        return "\n".join(lineas)


# ══════════════════════════════════════════════════════════════════════════════
#  Ejemplo de uso
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    orden = Orden()
    orden.agregarArticulo("Laptop",  80.00, 2.5)
    orden.agregarArticulo("Mouse",   15.00, 0.3)
    orden.agregarArticulo("Teclado", 25.00, 0.8)

    print("── Envío por Tierra (total > $100 → gratis) ──")
    orden.asignarMetodoEnvio(Tierra())
    print(orden)

    print()

    print("── Envío por Aire ──")
    orden.asignarMetodoEnvio(Aire())
    print(orden)

    # OCP en acción: agregar un nuevo método sin tocar Orden ni las clases existentes
    print()
    print("── Nuevo método: Express (sin modificar Orden) ──")

    class Express(MetodoEnvio):
        def obtenerCosto(self, orden: Orden) -> float:
            return orden.pesoTotal() * 50  # $50/kg

        def obtenerFecha(self, orden: Orden) -> str:
            fecha = datetime.today() + timedelta(hours=12)
            return fecha.strftime("%d/%m/%Y %H:%M")

    orden.asignarMetodoEnvio(Express())
    print(orden)