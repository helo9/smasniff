from smasniff import speedwire

EXAMPLE_TELEGRAMS = [
    b"SMA\x00\x00\x04\x02\xa0\x00\x00\x00\x01\x02L\x00\x10`i\x01t\xb3\xd6\xcc\x02\x07\xb0)\xc1\x00\x01\x04\x00\x00\x00\x00\x00\x00\x01\x08\x00\x00\x00\x00\x00\xb2\xaf\x13\xa8\x00\x02\x04\x00\x00\x00F\xc4\x00\x02\x08\x00\x00\x00\x00\x02\x80WK\x08\x00\x03\x04\x00\x00\x00\x00\x00\x00\x03\x08\x00\x00\x00\x00\x00p\xd8\xd0@\x00\x04\x04\x00\x00\x00\x00\x89\x00\x04\x08\x00\x00\x00\x00\x00\x0b\x98\xc6h\x00\t\x04\x00\x00\x00\x00\x00\x00\t\x08\x00\x00\x00\x00\x00\xc7\xc2\xd1\xd0\x00\n\x04\x00\x00\x00F\xc4\x00\n\x08\x00\x00\x00\x00\x02\x8b$u`\x00\r\x04\x00\x00\x00\x03\xe8\x00\x0e\x04\x00\x00\x00\xc3.\x00\x15\x04\x00\x00\x00\x00\x00\x00\x15\x08\x00\x00\x00\x00\x00\x90\x86\x83\xb0\x00\x16\x04\x00\x00\x00*\x9b\x00\x16\x08\x00\x00\x00\x00\x018\xcd\xfaX\x00\x17\x04\x00\x00\x00\x00\x00\x00\x17\x08\x00\x00\x00\x00\x00\x86\x85\x17(\x00\x18\x04\x00\x00\x00\x00B\x00\x18\x08\x00\x00\x00\x00\x00\x02;\x80\xd8\x00\x1d\x04\x00\x00\x00\x00\x00\x00\x1d\x08\x00\x00\x00\x00\x00\xb2<\xa0p\x00\x1e\x04\x00\x00\x00*\x9b\x00\x1e\x08\x00\x00\x00\x00\x01H{\xf5\x90\x00\x1f\x04\x00\x00\x00\x12\x92\x00 \x04\x00\x00\x03\x88\xaa\x00!\x04\x00\x00\x00\x03\xe8\x00)\x04\x00\x00\x00\x00\x00\x00)\x08\x00\x00\x00\x00\x00\x17\xdco\xd8\x00*\x04\x00\x00\x00\x1cx\x00*\x08\x00\x00\x00\x00\x01dK\x08\xb0\x00+\x04\x00\x00\x00\x00\x00\x00+\x08\x00\x00\x00\x00\x00\x00\xff\xe7\x90\x00,\x04\x00\x00\x00\x00<\x00,\x08\x00\x00\x00\x00\x00%6@(\x001\x04\x00\x00\x00\x00\x00\x001\x08\x00\x00\x00\x00\x000\x05k\xc8\x002\x04\x00\x00\x00\x1cx\x002\x08\x00\x00\x00\x00\x01d\xbaz\xb0\x003\x04\x00\x00\x00\x0c\x9b\x004\x04\x00\x00\x03\x8c\xc7\x005\x04\x00\x00\x00\x03\xe8\x00=\x04\x00\x00\x00\x00O\x00=\x08\x00\x00\x00\x00\x00'\r\xd5P\x00>\x04\x00\x00\x00\x00\x00\x00>\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x04\x00\x00\x00\x00\x00\x00?\x08\x00\x00\x00\x00\x00\x06\x8f\xb3 \x00@\x04\x00\x00\x00\x00\x0b\x00@\x08\x00\x00\x00\x00\x00\x01b\xeb8\x00E\x04\x00\x00\x00\x00P\x00E\x08\x00\x00\x00\x00\x00)\xa0l\xd8\x00F\x04\x00\x00\x00\x00\x00\x00F\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00G\x04\x00\x00\x00\x00#\x00H\x04\x00\x00\x03\x86~\x00I\x04\x00\x00\x00\x03\xdf\x90\x00\x00\x00\x02\x0e\rR\x00\x00\x00\x00"
]

def test_decode_telegram():

    parsed = speedwire.decode_telegram(EXAMPLE_TELEGRAMS[0])

    assert parsed
    assert parsed["Susy-ID"] == 372
    assert parsed["SerNo"] == 52226
    assert parsed["totalPowerBuy"] == 0.0
    assert parsed["totalPowerSell"] == 1811.6
    assert parsed["phaseL1PowerBuy"] == 0.0
    assert parsed["phaseL1PowerSell"] == 1090.7
    assert parsed["phaseL2PowerBuy"] == 0.0
    assert parsed["phaseL2PowerSell"] == 728.8
    assert parsed["phaseL3PowerBuy"] == 7.9
    assert parsed["phaseL3PowerSell"] == 0.0