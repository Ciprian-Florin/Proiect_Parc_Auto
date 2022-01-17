import PySimpleGUI as sg
import db_interface


def informatii_alocari_soferi():
    interogare_info_db = db_interface.vizualizare_informatii_alocari_soferi()
    return interogare_info_db


def create():
    inregistrari_tabela_alocari_soferi = informatii_alocari_soferi()
    headings_alocari_soferi = ['Autovehicul', 'Data Predarii', 'Utilizator', 'KM Bord', 'Platforma','Departament',]
    alocari_soferi_layout = [
        [sg.Table(values=inregistrari_tabela_alocari_soferi, headings=headings_alocari_soferi, max_col_width=50,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=15,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='Reservations Table')]
    ]
    alocari_soferi_information_window = sg.Window("Nomenclator Information", alocari_soferi_layout, modal=True)

    while True:
        event, values = alocari_soferi_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    alocari_soferi_information_window.close()