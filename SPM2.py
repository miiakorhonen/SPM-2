import csv

print("""SPM-2 on aistitiedon käsittelyn arviointiin kehitetty kyselylomakemenetelmä, joka 
mahdollistaa aistitiedon käsittelyn, suunnittelun ja ideoinnin sekä sosiaalisen osallistumisen 
arvioinnin koko elämänkaaren ajan arjen eri ympäristöissä, esim. kotona, varhaiskasvatuksessa ja 
koulussa.

Tällä ohjelmalla voidaan laskea raakapisteiden perusteella standardoidut T-pisteet ja 
persentiilit sekä tehdä tulkinta tuloksista.

Rajoitukset 25.5.2025: käytössä on vain Kodin ja Koulun kyselylomakkeen pisteytys 5-12-vuotiaille 
lapsille.

Ensimmäiseksi valitaan arvioitavan henkilön ikä (vauva/taapero 4-30kk, pikkulapsi 2-5v, 
lapsi 5-12v, nuori 12-21v tai aikuinen 21-87v).
""")



def kysy_luku():
    """
    Pyytää käyttäjältä numeron ja palauttaa sen, jos se on välillä 10–40.
    :return:
    """
    try:
        raakapisteet = int(input("Syötä raakapisteet: "))
    except ValueError:
        print("Arvon tulee olla kokonaisluku.")
    else:
        if 10 <= raakapisteet <= 40:
            return raakapisteet
        else:
            return


def hae_lomakkeesta(ika, lomake, asteikko, luku):
    """
    Lukee CSV-tiedoston ja palauttaa T-arvon ja prosenttipisteen annetulle asteikolle ja numerolle.
    :param ika:
    :param lomake:
    :param asteikko:
    :param luku:
    :return:
    """
    lomakkeet = {
        "vauva/taapero": {
            "vauvan arviointilomake": "SPM_vauva.csv",
            "taaperon arviointilomake": "SPM_taapero.csv",
            "huoltajan itsearviointi": "SPM_huoltajan_itsearviointi.csv",
        },
        "pikkulapsi": {
            "kodin lomake": "SPM_pikkulapsi_koti.csv",
            "varhaiskasvatuksen lomake": "SPM_pikkulapsi_varhaiskasvatus.csv",
        },
        "lapsi": {
            "kodin lomake": "SPM_lapsi_koti.csv",
            "koulun lomake": "SPM_lapsi_koulu.csv"
        },
        "nuori": {
            "kodin lomake": "SPM_nuori_koti.csv",
            "koulun lomake": "SPM_nuori_koulu.csv",
            "itsearvionti": "SPM_nuori_itsearviointi.csv"
        },
        "aikuinen": {
            "itsearviointi": "SPM_aikuinen_itsearviointi.csv",
            "läheisarviointi": "SPM_aikuinen_laheisarviointi.csv"
        }
    }

    indeksit = {
        "näkö": 0,
        "VIS": 0,
        "kuulo": 1,
        "HEA": 1,
        "tunto": 2,
        "TOU": 2,
        "maku ja haju": 3,
        "T&S": 3,
        "kehotietoisuus": 4,
        "BOD": 4,
        "tasapaino ja liike": 5,
        "BAL": 5,
        "suunnittelu ja oivallukset": 6,
        "PLN": 6,
        "sosiaalinen osallistuminen": 7,
        "SOC": 7
    }

    tiedosto = lomakkeet[ika][lomake]

    with (open(tiedosto, encoding="utf-8-sig", mode="r", newline="") as csv_tiedosto):
       csv_lukija = csv.reader(csv_tiedosto)
       for rivi in csv_lukija:
           rivi = rivi[0].split(";")
           if rivi[indeksit[asteikko]] == "":
               continue
           if "-" in rivi[indeksit[asteikko]]:
               sarja = rivi[indeksit[asteikko]].split("-")
               if int(sarja[0]) <= luku <= int(sarja[1]):
                   return int(rivi[-2]), rivi[-1]
           elif luku == int(rivi[indeksit[asteikko]]):
               return int(rivi[-2]), rivi[-1]


def valitse_asteikko():
    """
    Pyytää käyttäjältä asteikon ja palauttaa sen, jos se on kelvollinen.
    :return:
    """
    vaihtoehdot = ("näkö", "VIS",
                   "kuulo", "HEA",
                   "tunto", "TOU",
                   "maku ja haju", "T&S",
                   "kehotietoisuus", "BOD",
                   "tasapaino ja liike", "BAL",
                   "suunnittelu ja oivallukset", "PLN",
                   "sosiaalinen osallistuminen", "SOC")
    print("\nVaihtoehdot asteikoiksi ovat:\n"
          "näkö (VIS),\n"
          "kuulo (HEA),\n"
          "tunto (TOU),\n"
          "maku ja haju (T&S),\n"
          "kehotietoisuus (BOD),\n"
          "tasapaino ja liike (BAL),\n"
          "suunnittelu ja oivallukset (PLN) ja\n"
          "sosiaalinen osallistuminen (SOC).\n")
    while True:
        asteikko = input("Syötä asteikon nimi tai lyhenne: ").strip()
        if asteikko in vaihtoehdot:
            return asteikko
        elif asteikko == "poistu":
            return
        else:
            print("Valitsemaasi asteikkoa ei ole olemassa.")



def valitse_lomake(vaihtoehdot):
    """
    Kysyy käyttäjältä lomaketta ja palauttaa sen, jos se on kelvollinen.
    :param vaihtoehdot:
    :return:
    """
    while True:
        lomake = input(f"Valitse täytetty lomake ({', '.join(vaihtoehdot)}) tai poistu: ").strip().lower()
        if lomake in vaihtoehdot:
            return lomake
        elif lomake == "poistu":
            return
        else:
            print("Valitsemaasi lomaketta ei ole olemassa.")


def laske_st_pisteet():
    """
    Laskee ST-pisteet summaamalla yhteen näön (VIS), kuulon (HEA), tunnon (TOU),
    maun ja hajun (T&S), kehotietoisuuden (BOD) sekä tasapainon ja liikeen (BAL) osa-alueiden raakapisteet.
    :return:
    """
    # Kysy käyttäjältä jokaisen osa-alueen raakapisteet (6 kpl)
    print("Aloitetaan näön (VIS) osa-alueesta.")
    vis_pisteet = kysy_luku()
    print("Seuraavaksi kuulon (HEA) osa-alue.")
    hea_pisteet = kysy_luku()
    print("Seuraavaksi tunnon (TOU) osa-alue.")
    tou_pisteet = kysy_luku()
    print("Seuraavaksi maun ja hajun (T&S) osa-alue.")
    ts_pisteet = kysy_luku()
    print("Seuraavaksi kehotietoisuuden (BOD) osa-alue.")
    bod_pisteet = kysy_luku()
    print("Viimeisenä tasapainon ja liikeen (BAL) osa-alue.")
    bal_pisteet = kysy_luku()

    # Laske ST-pisteet yhteenlaskemalla raakapisteet
    st_pisteet = vis_pisteet + hea_pisteet + tou_pisteet + ts_pisteet + bod_pisteet + bal_pisteet

    print(f"Osa-alueiden yhteenlasketut ST-pisteet ovat {st_pisteet}.\n")


def tee_tulkinta(lomake, ika):
    """
    Kysyy käyttäjältä asteikon ja raakapisteet, ja tulkitsee tulokset.
    :return:
    """
    asteikko = valitse_asteikko()
    luku = kysy_luku()
    t_piste, persentiili = hae_lomakkeesta(ika, lomake, asteikko, luku)
    if 40 < t_piste < 59:
        tulkinta = "tyypilliseen reagointiin"
    elif 60 < t_piste < 69:
        tulkinta = "kohtalaisiin vaikeuksiin"
    else:
        tulkinta = "huomattaviin vaikeuksiin"

    print(f"Raakapistettä {luku} vastaava standardoitu T-piste on {t_piste} ja persentiili on"
          f" {persentiili}, joka viittaa {tulkinta}.\n")


def main():
    while True:
        valittu_ika = input("Kirjoita arvioitavan henkilön ikäryhmä (vauva/taapero, pikkulapsi, lapsi, "
                            "nuori tai aikuinen): ").strip().lower()

        if valittu_ika == "vauva/taapero":
            valittu_lomake = valitse_lomake(("vauvan arviointilomake", "taaperon arviointilomake", "huoltajan itsearviointi"))
            print("Tämä toiminto ei ole vielä käytössä.\n")

            if valittu_lomake == "poistu":
                break


        elif valittu_ika == "pikkulapsi":
            valittu_lomake = valitse_lomake(("kodin lomake", "varhaiskasvatuksen lomake"))
            print("Tämä toiminto ei ole vielä käytössä.\n")

            if valittu_lomake == "poistu":
                break


        elif valittu_ika == "lapsi":
            valittu_lomake = valitse_lomake(("kodin lomake", "koulun lomake"))

            while True:
                vastaus = input(f"Lasketaanko ST-pisteet? ").strip().lower()
                if vastaus == "kyllä":
                    laske_st_pisteet()
                    break
                elif vastaus == "ei":
                    print("Tehdään siis tulkintaa yhden osa-alueen tuloksesta.\n")
                    tee_tulkinta(valittu_lomake, valittu_ika)
                    break
                else:
                    print("Valitsemaasi vaihtoehtoa ei ole olemassa.")

                if valittu_lomake == "poistu":
                    break

        elif valittu_ika == "nuori":
            valittu_lomake = valitse_lomake(("kodin lomake", "koulun lomake", "itsearviointi"))
            print("Tämä toiminto ei ole vielä käytössä.\n")
            if valittu_lomake == "poistu":
                break


        elif valittu_ika == "aikuinen":
            valittu_lomake = valitse_lomake(("itsearviointi", "läheisarviointi"))
            print("Tämä toiminto ei ole vielä käytössä.\n")
            if valittu_lomake == "poistu":
                break

        else:
            print("Valitsemaasi ikäryhmää ei ole olemassa.\n")


if __name__ == '__main__':
    main()
