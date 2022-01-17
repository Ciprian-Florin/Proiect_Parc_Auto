import PySimpleGUI as sg
import time
import pyodbc
import sqlite3
import informatii_alocari_soferi
import informatii_nomenclator
import informatii_evenimente
import informatii_asigurari
import informatii_km_alimentari
import informatii_revizii

start_time = time.time()


CONN = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=ADMIN-IT\SQLEXPRESS;'
                      'Database=ParcAuto;'
                      'Trusted_Connection=yes;')

# CONN = sqlite3.connect('parc_auto.db')  # conexiunea cu baza de date
# CURSOR_JOB = CONN.cursor()

sg.theme('LightBrown2')  # Adaugare tema
# Continutul unui layout
layout_nomenclator = [
                      [sg.Text('Autovehicul', font=("Arial", 15) ,size=(19, 1)),sg.InputText(key="-AUTOVEHICULN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Motorizare', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-MOTORIZAREN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Capacitate Cilindrica', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-CAPACITATEN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Producator', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-PRODUCATORN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Marca', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-MARCAN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('An Fabricatie', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-ANFABRICATIEN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('KM La Achizitie', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-KMACHIZITIEN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Valoare Intrare', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-VALINTRAREN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Destinatie', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-DESTINATIEN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Tip Anvelope', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-TIPANVELOPEN-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Interval Revizie 1', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-INTREVIZIE1N-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Limita Int Revizie 1', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-LMTREVIZIE1N-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Interval Revizie 2', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-INTREVIZIE2N-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Limita Int Revizie 2', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-LMTREVIZIE2N-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Interval Revizie 3', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-INTREVIZIE3N-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Text('Limita Int Revizie 3', font=("Arial", 15) ,size=(19, 1)), sg.InputText(key="-LMTREVIZIE3N-", do_not_clear=False, size=(70, 1), justification='center')],
                      [sg.Button('Adauga In Nomenclator', font=(3), size=(25, 5)), sg.Button('Vizualizare Tabela Nomenclator', font=(3) , size=(25, 5)), sg.Button('Modificare Intrari Nomenclator', font=(3) , size=(25, 5))]
]

layout_alocari_soferi = [
    [sg.Text('Autovehicul', font=("Arial", 15), size=(19, 1)), sg.Input(key="-AUTOVEHICULAS-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Data Predarii', font=("Arial", 15), size=(19, 1)), sg.Input(key="-DATAPREDAREAS-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Utilizator', font=("Arial", 15), size=(19, 1)), sg.Input(key="-UTILIZATORAS-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('KM Bord', font=("Arial", 15), size=(19, 1)), sg.Input(key="-KMBORDAS-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Platforma', font=("Arial", 15), size=(19, 1)), sg.Input(key="-PLATFORMAAS-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Departament', font=("Arial", 15), size=(19, 1)), sg.Input(key="-DEPARTAMENTAS-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Button('Adauga Alocari Soferi', font=(3), size=(25, 5)), sg.Button('Vizualizare Tabela Alocari Soferi', font=(3), size=(25, 5)), sg.Button('Modificare Intrari Alocari Soferi', font=(3) , size=(25, 5))]
]

layout_evenimente = [
    [sg.Text('Autovehicul', font=("Arial", 15), size=(19, 1)), sg.Input(key="-AUTOVEHICULEV-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Utilizator', font=("Arial", 15), size=(19, 1)), sg.Input(key="-UTILIZATOREV-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Culpa DA-NU', font=("Arial", 15), size=(19, 1)), sg.Input(key="-CULPAEV-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Data Eveniment', font=("Arial", 15), size=(19, 1)), sg.Input(key="-EVENIMENTEV-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Observatii', font=("Arial", 15), size=(19, 1)), sg.Input(key="-OBSERVATIIEV-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Cost Reparatie', font=("Arial", 15), size=(19, 1)), sg.Input(key="-REPARATIEEV-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Suportat Coriolan', font=("Arial", 15), size=(19, 1)), sg.Input(key="-SUPORTATCRLEV-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Suportat Utilizator', font=("Arial", 15), size=(19, 1)), sg.Input(key="-SUPORTATUTILIZATOREV-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Button('Adauga in Evenimente', font=(3), size=(25, 5)), sg.Button('Vizualizare Tabela Evenimente', font=(3), size=(25, 5)), sg.Button('Modificare Intrari Evenimente', font=(3) , size=(25, 5))]

]

layout_asigurari = [
    [sg.Text('Autovehicul', font=("Arial", 15), size=(19, 1)), sg.Input(key="-AUTOVEHICULASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('RCA Data Exp', font=("Arial", 15), size=(19, 1)), sg.Input(key="-RCAEXPASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('RCA Valoare', font=("Arial", 15), size=(19, 1)), sg.Input(key="-RCAVALASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('RCA Asigurator', font=("Arial", 15), size=(19, 1)), sg.Input(key="-RCAASIGURATORASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('RCA Broker', font=("Arial", 15), size=(19, 1)), sg.Input(key="-RCABROKERASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Casco Data Exp', font=("Arial", 15), size=(19, 1)), sg.Input(key="-CASCOEXPASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Casco Valoare', font=("Arial", 15), size=(19, 1)), sg.Input(key="-CASCOVALASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Casco Asigurator', font=("Arial", 15), size=(19, 1)), sg.Input(key="-CASCOASIGURATORASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Casco Broker', font=("Arial", 15), size=(19, 1)), sg.Input(key="-CASCOBROKERASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('ITP Expirare', font=("Arial", 15), size=(19, 1)), sg.Input(key="-ITPEXPASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Rovinieta Expirare', font=("Arial", 15), size=(19, 1)), sg.Input(key="-ROVINIETAEXPASIG-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Button('Adauga Asigurari', font=(3), size=(25, 5)), sg.Button('Vizualizare Tabela Asigurari', font=(3), size=(25, 5)), sg.Button('Modificare Intrari Asigurari', font=(3) , size=(25, 5))]
]
layout_km_alimentari = [
    [sg.Text('Autovehicul', font=("Arial", 15), size=(19, 1)), sg.Input(key="-AUTOVEHICULKMAL-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Anul', font=("Arial", 15), size=(19, 1)), sg.Input(key="-ANKMAL-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Luna', font=("Arial", 15), size=(19, 1)), sg.Input(key="-LUNAKMAL-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('KM_Bord', font=("Arial", 15), size=(19, 1)), sg.Input(key="-KMBORDKMAL-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Alimentare_Litri', font=("Arial", 15), size=(19, 1)), sg.Input(key="-ALIMENTARELITRIIKMAL-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Button('Adauga In Km Alimentari', font=(3), size=(25, 5)), sg.Button('Vizualizare Tabela KM Alimentari', font=(3), size=(25, 5)), sg.Button('Modificare Intrari KM Alimentari', font=(3) , size=(25, 5))]
]
layout_revizii = [
    [sg.Text('Autovehicul', font=("Arial", 15), size=(19, 1)), sg.Input(key="-AUTOVEHICULRVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Utilizator', font=("Arial", 15), size=(19, 1)), sg.Input(key="-UTILIZATORRVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('KM Bord', font=("Arial", 15), size=(19, 1)), sg.Input(key="-KMBORDRVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Data Interventie', font=("Arial", 15), size=(19, 1)), sg.Input(key="-DATAREVIZIERVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Tip Interventie', font=("Arial", 15), size=(19, 1)), sg.Input(key="-TIPINTERVENTIERVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Service Auto', font=("Arial", 15), size=(19, 1)), sg.Input(key="-SERVICEAUTORVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Valoare Piese', font=("Arial", 15), size=(19, 1)), sg.Input(key="-VALPIESERVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Valoare Manopera', font=("Arial", 15), size=(19, 1)), sg.Input(key="-VALMANOPERARVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Discuri', font=("Arial", 15), size=(19, 1)), sg.Input(key="-DISCURIRVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Distributie', font=("Arial", 15), size=(19, 1)), sg.Input(key="-DISTRIBUTIERVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Ambreaj', font=("Arial", 15), size=(19, 1)), sg.Input(key="-AMBREAJRVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Placute', font=("Arial", 15), size=(19, 1)), sg.Input(key="-PLACUTERVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Anvelope', font=("Arial", 15), size=(19, 1)), sg.Input(key="-ANVELOPERVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Nr Anvelope Noi', font=("Arial", 15), size=(19, 1)), sg.Input(key="-NRANVELOPENOIRVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Acumulator', font=("Arial", 15), size=(19, 1)), sg.Input(key="-ACUMULATORRVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Text('Observatii', font=("Arial", 15), size=(19, 1)), sg.Input(key="-OBSERVATIIRVZ-", do_not_clear=False, size=(70, 1), justification='center')],
    [sg.Button('Adauga In Revizii', font=(3), size=(25, 5)), sg.Button('Vizualizare Tabela Revizii', font=(3), size=(25, 5)), sg.Button('Modificare Intrari Revizii', font=(3) , size=(25, 5))]
]

# Definire tab-uri si asignare layout-uri pt fiecare tab
tabgrp = [
    [sg.TabGroup([[sg.Tab('Nomenclator                 ', layout_nomenclator, element_justification='center'),
                   sg.Tab('Alocari Soferi              ', layout_alocari_soferi, element_justification='center'),
                   sg.Tab('Evenimente                  ', layout_evenimente, element_justification='center'),
                   sg.Tab('Asigurari                   ', layout_asigurari, element_justification='center'),
                   sg.Tab('KM_Alimentari               ', layout_km_alimentari, element_justification='center'),
                   sg.Tab('Revizii                     ', layout_revizii, element_justification='center'),
                   ]], tab_location='centertop',
                   size=(1500, 750)), sg.Button('Inchide', font=(3), size=(20, 10),)]]

# Definire fereastra
window = sg.Window("Dashboard-Parc-Auto", tabgrp)

# Bucla evenimente pentru a procesa „evenimente” și a obține „valorile” intrărilor
while True:

    # Citire valori introduse de user
    event, values = window.read()
    CONN = sqlite3.connect('parc_auto.db')  # conexiunea cu baza de date
    CURSOR_JOB = CONN.cursor()

    if event == sg.WIN_CLOSED or event == 'Inchide':  # Daca userul inchide fereastra sau apasa Cancel
        break
    elif event == 'Adauga In Nomenclator':
        autovehicul = values['-AUTOVEHICULN-'] # chei unice sugestive pt fiecare camp in functie de layout
        motorizare = values['-MOTORIZAREN-']
        capacitate = values['-CAPACITATEN-']
        producator = values['-PRODUCATORN-']
        marca = values['-MARCAN-']
        an_fabricatie = values['-ANFABRICATIEN-']
        km_achizitie = values['-KMACHIZITIEN-']
        valoare_intrare = values['-VALINTRAREN-']
        destinatie = values['-DESTINATIEN-']
        tip_anvelope = values['-TIPANVELOPEN-']
        interval_revizie1 = values['-INTREVIZIE1N-']
        limita_int_revizie1 = values['-LMTREVIZIE1N-']
        interval_revizie2 = values['-INTREVIZIE2N-']
        limita_int_revizie2 = values['-LMTREVIZIE2N-']
        interval_revizie3 = values['-INTREVIZIE3N-']
        limita_int_revizie3 = values['-LMTREVIZIE3N-']

        CURSOR_JOB.execute("""
        INSERT INTO Nomenclator_Auto(Autovehicul, Motorizare, Capacitate_Cilindrica, Producator, Marca, An_Fabricatie, Km_la_Achizitie, Valoare_Intrare, Destinatie, Tip_Anvelope, Interval_Revizie_1, Limita_Interval_Revizie_1, Interval_Revizie_2, Limita_Interval_Revizie_2, Interval_Revizie_3, Limita_Interval_Revizie_3)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        [autovehicul, motorizare, capacitate, producator, marca, an_fabricatie, km_achizitie, valoare_intrare, destinatie, tip_anvelope, interval_revizie1, limita_int_revizie1,interval_revizie2, limita_int_revizie2, interval_revizie3, limita_int_revizie3])
        sg.popup_no_buttons('Datele au fost inserate cu succes!!!')
        CONN.commit()
        CONN.close()

    elif event == 'Vizualizare Tabela Nomenclator':
        informatii_nomenclator.create()

    elif event == 'Modificare Intrari Nomenclator':
        pass

    elif event == 'Adauga Alocari Soferi':
        autovehicul_alocari_soferi = values['-AUTOVEHICULAS-']
        data_predare = values['-DATAPREDAREAS-']
        utilizator = values['-UTILIZATORAS-']
        km_bord = values['-KMBORDAS-']
        platforma = values['-PLATFORMAAS-']
        departament = values['-DEPARTAMENTAS-']
        CURSOR_JOB.execute("""
        INSERT INTO Alocari_Soferi(Autovehicul, Data_Predarii, Utilizator, Km_Bord, Platforma, Departament)
        VALUES(?, ?, ?, ?, ?, ?)""",
        [autovehicul_alocari_soferi, data_predare, utilizator, km_bord, platforma, departament])
        sg.popup_no_buttons('Datele au fost inserate cu succes!!!')
        CONN.commit()
        CONN.close()

    elif event == 'Vizualizare Tabela Alocari Soferi':
        informatii_alocari_soferi.create()

    elif event == 'Adauga in Evenimente':
        autovehicul_evenimente = values['-AUTOVEHICULEV-']
        utilizator_evenimente = values['-UTILIZATOREV-']
        culpa = values['-CULPAEV-']
        data_eveniment = values['-EVENIMENTEV-']
        observatii = values['-OBSERVATIIEV-']
        cost_reparatie = values['-REPARATIEEV-']
        suportat_coriolan = values['-SUPORTATCRLEV-']
        suportat_utilizator = values['-SUPORTATUTILIZATOREV-']
        # Inserare in tabela
        CURSOR_JOB.execute("""
        INSERT INTO Evenimente(Autovehicul, Utilizator, Culpa(DA/NU), Data_Eveniment, Observatii, Cost_Reparatie, Suportat_RCA, Suportat_CASCO, Suportat_Coriolan, Suportat_Utilizator)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        [autovehicul_evenimente, utilizator_evenimente, culpa, data_eveniment, observatii, cost_reparatie, suportat_coriolan, suportat_utilizator])
        sg.popup_no_buttons('Datele au fost inserate cu succes!!!')
        CONN.commit()
        CONN.close()

    elif event == 'Vizualizare Tabela Evenimente':
        informatii_evenimente.create()

    elif event == 'Adauga Asigurari':
        autovehicul_asigurari = values['-AUTOVEHICULASIG-']
        rca_expirare = values['-RCAEXPASIG-']
        rca_valoare = values['-RCAVALASIG-']
        rca_asigurator = values['-RCAASIGURATORASIG-']
        rca_broker = values['-RCABROKERASIG-']
        casco_expirare = values['-CASCOEXPASIG-']
        casco_valoare = values['-CASCOVALASIG-']
        casco_asigurator = values['-CASCOASIGURATORASIG-']
        casco_broker = values['-CASCOBROKERASIG-']
        itp_expirare = values['-ITPEXPASIG-']
        rovinieta_expirare = values['-ROVINIETAEXPASIG-']
        CURSOR_JOB.execute("""
        INSERT INTO Asigurari(Autovehicul, RCA_Data_Expir, RCA_Valoare, RCA_Asigurator, RCA_Broker, CASCO_Data_Expir, CASCO_Valoare, CASCO_Asigurator, CASCO_Broker, Itp_Expir, Rovinieta_Expir)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        [autovehicul_asigurari, rca_expirare, rca_valoare, rca_asigurator, rca_broker, casco_expirare, casco_valoare, casco_asigurator, casco_broker, itp_expirare, rovinieta_expirare])
        sg.popup_no_buttons('Datele au fost inserate cu succes!!!')
        CONN.commit()
        CONN.close()

    elif event == 'Vizualizare Tabela Asigurari':
        informatii_asigurari.create()

    elif event == 'Adauga In Km Alimentari':
        autovehicul_alimentari = values['-AUTOVEHICULKMAL-']
        anul = values['-ANKMAL-']
        luna = values['-LUNAKMAL-']
        km_bord_alimentari = values['-KMBORDKMAL-']
        alimentare_litrii = values['-ALIMENTARELITRIIKMAL-']
        CURSOR_JOB.execute("""
        INSERT INTO Km_Alimentari(Autovehicul, Anul, Luna, Km_Bord, Alimentare_Litri)
        VALUES(?, ?, ?, ?, ?)""",
        [autovehicul_alimentari, anul, luna, km_bord_alimentari, alimentare_litrii])
        sg.popup_no_buttons('Datele au fost inserate cu succes!!!')
        CONN.commit()
        CONN.close()

    elif event == 'Vizualizare Tabela KM Alimentari':
        informatii_km_alimentari.create()

    elif event == 'Adauga In Revizii':
        autovehicul_revizii = values['-AUTOVEHICULRVZ-']  # de facut campurile lipsa si de declarat variabilele
        utilizator_revizii = values['-UTILIZATORRVZ-']
        km_bord_revizii = values['-KMBORDRVZ-']
        data_interventie = values['-DATAREVIZIERVZ-']
        tip_interventie = values['-TIPINTERVENTIERVZ-']
        service_auto = values['-SERVICEAUTORVZ-']
        valoare_piese = values['-VALPIESERVZ-']
        valoare_manopera = values['-VALMANOPERARVZ-']
        discuri = values['-DISCURIRVZ-']
        distributie = values['-DISTRIBUTIERVZ-']
        ambreaj = values['-AMBREAJRVZ-']
        placute = values['-PLACUTERVZ-']
        anvelope_revizii = values['-ANVELOPERVZ-']
        nr_anvelope_noi = values['-NRANVELOPENOIRVZ-']
        acumulator = values['-ACUMULATORRVZ-']
        observatii_revizii = values['-OBSERVATIIRVZ-']
        CURSOR_JOB.execute("""
        INSERT INTO Revizii_Reparatii(Autovehicul, Utilizator, Km_Bord, Data_Interventie, Tip_Interventie, Service_Auto, Valoare_Piese, Valoare_Manopera, Discuri, Distributie, Ambreaj, Placute, Anvelope, Numar_Anvelope_noi, Acumulator, Observatii)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        [autovehicul_revizii, utilizator_revizii, km_bord_revizii, data_interventie, tip_interventie, service_auto, valoare_piese, valoare_manopera, discuri, distributie, ambreaj, placute, anvelope_revizii, nr_anvelope_noi, acumulator, observatii_revizii])
        sg.popup_no_buttons('Datele au fost inserate cu succes!!!',)
        CONN.commit()
        CONN.close()

    elif event == 'Vizualizare Tabela Revizii':
        informatii_revizii.create()

window.close()
