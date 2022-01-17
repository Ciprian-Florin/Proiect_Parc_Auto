import sqlite3


# Functie vizualizare informatii din tabela nomenclator
def vizualizare_informatii_nomenclator():
    rezultat = []
    CONN = sqlite3.connect('parc_auto.db')
    CURSOR_JOB = CONN.cursor()
    for randuri in CURSOR_JOB.execute("SELECT * FROM Nomenclator_Auto"):
        # Intrarile sunt tuple le convertim in lista
        rezultat.append(list(randuri))
    return rezultat



# Functie vizualizare informatii din tabela alocari soferi
def vizualizare_informatii_alocari_soferi():
    rezultat = []
    CONN = sqlite3.connect('parc_auto.db')
    CURSOR_JOB = CONN.cursor()
    for randuri in CURSOR_JOB.execute("SELECT * FROM Alocari_Soferi"):
        # Intrarile sunt tuple le convertim in lista
        rezultat.append(list(randuri))
    return rezultat


# Functie vizualizare informatii din tabela evenimente
def vizualizare_informatii_evenimente():
    rezultat = []
    CONN = sqlite3.connect('parc_auto.db')
    CURSOR_JOB = CONN.cursor()
    for randuri in CURSOR_JOB.execute("SELECT * FROM Evenimente"):
        # Intrarile sunt tuple le convertim in lista
        rezultat.append(list(randuri))
    return rezultat


# Functie vizualizare informatii din tabela asigurari
def vizualizare_informatii_asigurari():
    rezultat = []
    CONN = sqlite3.connect('parc_auto.db')
    CURSOR_JOB = CONN.cursor()
    for randuri in CURSOR_JOB.execute("SELECT * FROM Asigurari"):
        # Intrarile sunt tuple le convertim in lista
        rezultat.append(list(randuri))
    return rezultat


# Functie vizualizare informatii din tabela km alimentari
def vizualizare_informatii_km_alimentari():
    rezultat = []
    CONN = sqlite3.connect('parc_auto.db')
    CURSOR_JOB = CONN.cursor()
    for randuri in CURSOR_JOB.execute("SELECT * FROM Km_Alimentari"):
        # Intrarile sunt tuple le convertim in lista
        rezultat.append(list(randuri))
    return rezultat


# Functie vizualizare informatii din tabela revizii_reparatii
def vizualizare_informatii_revizii_reparatii():
    rezultat = []
    CONN = sqlite3.connect('parc_auto.db')
    CURSOR_JOB = CONN.cursor()
    for randuri in CURSOR_JOB.execute("SELECT * FROM Revizii_Reparatii"):
        # Intrarile sunt tuple le convertim in lista
        rezultat.append(list(randuri))
    return rezultat
