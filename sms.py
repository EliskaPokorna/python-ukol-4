def telefonni_cislo(cislo: str) -> bool:
    upravene_cislo = cislo.replace(" ","")
    if len(upravene_cislo) == 13 and cislo.startswith("+420"):
        return True
    elif len(upravene_cislo) == 9:
        return True
    else:
        return False

def cena_zpravy(zprava: str) -> int:
    cena_zpravy = 3
    delka_zpravy = len(zprava)
    pocet_znaku = 180

    pocet_cen = delka_zpravy // pocet_znaku
    celkem_cena = pocet_cen * cena_zpravy
    return celkem_cena

    
cislo_uzivatele = input("Zadejte telefonní číslo: ")

if telefonni_cislo(cislo_uzivatele):
    zprava_uzivatele = input("Zadejte vaši zprávu: ")
    print(f"Vaše cena za zprávu je {cena_zpravy(zprava_uzivatele)} Kč.")
else:
    print("Zdané číslo není platné.")