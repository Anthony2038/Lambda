from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Pedido:
    identificador: int
    status: str
    valor: Decimal


PEDIDOS = (
    Pedido(1, "pago", Decimal("89.90")),
    Pedido(2, "pendente", Decimal("45.00")),
    Pedido(3, "pago", Decimal("120.10")),
    Pedido(4, "cancelado", Decimal("30.00")),
)


def processar_pedidos_imperativo(pedidos):
    pedidos_pagos = []
    total = Decimal("0.00")

    for pedido in pedidos:
        if pedido.status == "pago":
            pedidos_pagos.append(pedido.identificador)
            total += pedido.valor

    return tuple(pedidos_pagos), total


def processar_pedidos_funcional(pedidos):
    pedidos_pagos = tuple(
        filter(lambda pedido: pedido.status == "pago", pedidos)
    )
    identificadores = tuple(map(lambda pedido: pedido.identificador, pedidos_pagos))
    total = sum(map(lambda pedido: pedido.valor, pedidos_pagos), Decimal("0.00"))

    return identificadores, total


def main():
    resultado_imperativo = processar_pedidos_imperativo(PEDIDOS)
    resultado_funcional = processar_pedidos_funcional(PEDIDOS)

    print(f"Imperativo: pedidos={resultado_imperativo[0]}, total={resultado_imperativo[1]}")
    print(f"Funcional:  pedidos={resultado_funcional[0]}, total={resultado_funcional[1]}")
    assert resultado_imperativo == resultado_funcional


if __name__ == "__main__":
    main()
