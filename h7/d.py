# avataan tiedosto ja luetaan rivit
with open("ch4.txt") as tiedosto:
    rivit = tiedosto.read().strip().split("\n")

# sama pisteytysfunktio kuin c)-tehtävässä
def pisteytä(teksti_bytes):
    yleisimmät = b"etaoin shrdluETAOIN SHRDLU"
    return sum(1 for byte in teksti_bytes if byte in yleisimmät)

# alustetaan muuttujat parhaan tuloksen tallentamista varten
paras_pistemäärä = 0
paras_tulos = None
paras_avain = None

# käydään jokainen rivi läpi
for rivi in rivit:
    salakirjoitus = bytes.fromhex(rivi.strip())
    # kokeillaan kaikki 256 avainta jokaiselle riville
    for avain in range(256):
        yritys = bytes([byte ^ avain for byte in salakirjoitus])
        if pisteytä(yritys) > paras_pistemäärä:
            paras_pistemäärä = pisteytä(yritys)
            paras_tulos = yritys
            paras_avain = avain

print(f"Paras avain: {paras_avain}")
print(f"Paras tulos: {paras_tulos}")