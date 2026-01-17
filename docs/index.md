# h1 Scope First, Controls Later

## a) Perustaso

### In-Scope / Soveltamisalaani kuuluvat

#### Kotiverkon perusinfrastruktuuri
- Internetyhteys: DNA valokuitu ja Wi-Fi
- Mobiili-internetyhteys: Telia 5G
- Verkkolaite: Wi-Fi-reititin (DNA Mesh WiFi F-3896)
- Kotiverkon sisäiset kaapeloinnit
- VPN-palvelu: NordVPN (käytössä pöytäkoneella, läppärillä, puhelimella)

#### Kurssiharjoituksiin käytettävät laitteet
- Itse rakennettu pöytäkone  
  - Dual boot: Linux Mint (main) / Windows  
  - GTX 1070, Ryzen 7 1700  
  - Pääasiallinen opiskelulaite kotona
- Läppäri: MacBook Air M2 (2023)  
  - QEMU-emuloitu Linux Debian -virtuaalikone  
  - Pääasiallinen opiskelulaite koululla
- Puhelin: iPhone 14 Pro Max  
  - Käytössä monivaiheiseen tunnistautumiseen (MFA) ja tarvittaessa internet-yhteyspisteen jakoon

#### Tiedot ja tietoaineistot
- Tunnistautumistiedot: Microsoft Authenticator
- Salasanat: iCloud Password Manager
- Lähdekoodi: GitHub-repositoriot
- Opiskeludokumentaatio:
  - Google Drive
  - iCloud
  - Microsoft 365 / OneDrive

---

### Out-of-Scope / Soveltamisalan ulkopuolelle rajatut

- Työnantajan hallinnoima työläppäri  
  - Ei täysin omassa hallinnassani 
  - Käyttää työnantajan omaa VPN:ää
  - Saa käyttää vain työasioihin
  - Merkityksetön kurssin näkökulmasta
- Apple TV  
  - Kuluttaja-IoT-laite  
  - Merkityksetön kurssin näkökulmasta
- Internet operaattorin verkko (internetin puolella)
  - Ei ole hallinnassani ja perustuu palveluntarjoajan vastuuseen
- Mobiilioperaattorin verkko (internetin puolella)
  - Ei ole hallinnassani ja perustuu palveluntarjoajan vastuuseen

#### Rajaukset perustuvat omistajuuteen, hallittavuuteen ja merkityksellisyyteen kurssin näkökulmasta.

---

### Keskeiset rajapinnat

- Pilvipalvelut
  - Google Drive
  - iCloud
  - GitHub
  - Microsoft 365 / OneDrive
- Verkkorajapinnat
  - Wi-Fi-reititin: DNA Mesh WiFi F-3896
  - iPhonen internet-yhteyspiste: Telia 5G
- Etäyhteydet
  - VPN: NordVPN
- Sisäänrakennetut palomuurit
  - Linux
  - MacOS
  - Windows
- Toimittajat
  - DNA: internetyhteys
  - Telia: mobiili-internetyhteys
  - NordVPN: VPN

---

![Verkko- ja rajapintakaavio](Verkko&Rajapintakaavio.png)

---

### Mitä näyttöä voisin esittää?

- Verkkoyhteydet: Kuvakaappaus Wi-Fi-reitittimen (DNA Mesh WiFi F-3896) yleisistä asetuksista sekä iPhonen internet-yhteyspisteen (Telia 5G) asetuksista.
- Laitteet ja harjoitusympäristö: Kuvat käytössä olevien laitteiden specseistä sekä QEMU-virtuaalikoneen perustiedot ja verkkoasetukset.
- Tiedot ja tallennus: Linkki GitHub-repositorioon sekä listaus käytössä olevista pilvitallennuspalveluista (Drive, iCloud, OneDrive).
- VPN: Kuvakaappaus VPN asetuksista

---

### b) Sidotaan standardiin (Interested Parties)

| Sidosryhmä | Tarve / Vaatimus | ISO 27001 -viite (Vaatimusalue) | Miten osoitat (Evidence) |
|-----------|---------------------------|----------------------------------|--------------------------------------|
| Minä itse (ympäristön omistaja ja käyttäjä) | Opiskeluun käytettävän ympäristön on oltava hallinnassani ja ymmärrettävissä kokonaisuutena, jotta tiedän missä harjoitukset tehdään ja mihin ne voivat vaikuttaa. | Johtajuus (Leadership) – vastuun ottaminen ja rajojen määrittely | - Tämä dokumentti, jossa in-scope- ja out-of-scope-alueet on kuvattu.<br>- Verkko- ja rajapintakaavio havainnollistaa ympäristön rakenteen. |
| Kurssin järjestäjä / oppilaitos | Kurssiharjoitukset tulee suorittaa rajatussa, sallitussa ympäristössä siten, ettei toiminta kohdistu ulkopuolisiin järjestelmiin tai verkkoihin. | Konteksti (Context of the organization) – toimintaympäristön rajaus | - Tämä dokumentti joka määrittelee soveltamisalan ja jossa harjoitusympäristö ja sen rajaukset on kuvattu kirjallisesti.<br>- Virtuaalikoneen verkkomalli (NAT), joka rajoittaa suorat yhteydet ulkopuolisiin verkkoihin.|

---

## Lähteet
- SFS-EN ISO/IEC 27001:2023. *Tietoturvallisuus, kyberturvallisuus ja tietosuoja. Tietoturvallisuuden hallintajärjestelmät. Vaatimukset*
- SFS-ISO/IEC 27003:2017. *Informaatioteknologia. Turvallisuustekniikat. Tietoturvallisuuden hallintajärjestelmät. Ohjeistusta*
- Asioiden rautalangasta vääntämiseen ja sparraukseen OpenAI ChatGPT 5.2

---
