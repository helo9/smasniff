"""SMA Speedwire Protocol decoding module.

The module provides functionality to decode raw telegrams from SMA Speedwire devices, see https://www.sma.de/fileadmin/content/global/Partner/Documents/SMA_Labs/EMETER-Protokoll-TI-en-10.pdf
"""
from construct import ExprAdapter, Pointer, Const, Int16ub, Struct, obj_


def decode_telegram(telegram_raw: bytes) -> dict[str, any]:
    return _telegram_struct.parse(telegram_raw)


_ScaledPower = ExprAdapter(
    Int16ub,
    encoder=obj_ * 10,
    decoder=obj_ / 10.0
)


_telegram_struct = Struct(
    Const(b"SMA"),
    "Susy-ID" / Pointer(18, Int16ub),
    "SerNo" / Pointer(22, Int16ub),
    "totalPowerBuy" / Pointer(34, _ScaledPower),
    "totalPowerSell" / Pointer(54, _ScaledPower),
    "phaseL1PowerBuy" / Pointer(164+6, _ScaledPower),
    "phaseL1PowerSell" / Pointer(164+26, _ScaledPower),
    "phaseL2PowerBuy" / Pointer(308+6, _ScaledPower),
    "phaseL2PowerSell" / Pointer(308+26, _ScaledPower),
    "phaseL3PowerBuy" / Pointer(452+6, _ScaledPower),
    "phaseL3PowerSell" / Pointer(452+26, _ScaledPower),
)
