# muunnetaan hex-merkkijono raakabyteihin
salakirjoitus = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

# pisteytysfunktio: laskee kuinka monta englannin yleisintä kirjainta tekstissä on
def pisteytä(teksti_bytes):
    yleisimmät = b"etaoin shrdluETAOIN SHRDLU"
    return sum(1 for byte in teksti_bytes if byte in yleisimmät)

# alustetaan muuttujat parhaan tuloksen tallentamista varten
paras_pistemäärä = 0
paras_tulos = None
paras_avain = None

# kokeillaan kaikki 256 mahdollista yksitavuista avainta
for avain in range(256):
    # XOR:ataan koko salateksti nykyisellä avaimella
    yritys = bytes([byte ^ avain for byte in salakirjoitus])
    # jos tulos sai enemmän pisteitä kuin edellinen paras, päivitetään paras tulos
    if pisteytä(yritys) > paras_pistemäärä:
        paras_pistemäärä = pisteytä(yritys)
        paras_tulos = yritys
        paras_avain = avain

print(f"Paras avain: {paras_avain}")
print(f"Paras tulos: {paras_tulos}")