import PySimpleGUI as sg
import db_interface


def informatii_km_alimentari():
    interogare_info_db = db_interface.vizualizare_informatii_km_alimentari()
    return interogare_info_db


def create():
    inregistrari_tabela_km_alimentari = informatii_km_alimentari()
    headings_km_alimentari= ['Autovehicul', 'Anul', 'Luna', 'Km Bord', 'Alimentare Litrii']
    km_alimentari_layout = [
        [sg.Table(values=inregistrari_tabela_km_alimentari, headings=headings_km_alimentari, max_col_width=50,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=15,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='Reservations Table')]
    ]
    km_alimentari_information_window = sg.Window("Km Alimentari Information", km_alimentari_layout, modal=True)

    while True:
        event, values = km_alimentari_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    km_alimentari_information_window.close()