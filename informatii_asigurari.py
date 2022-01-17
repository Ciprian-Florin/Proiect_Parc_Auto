import PySimpleGUI as sg
import db_interface


def informatii_evenimente():
    interogare_info_db = db_interface.vizualizare_informatii_asigurari()
    return interogare_info_db


def create():
    inregistrari_tabela_asigurari = informatii_evenimente()
    headings_asigurari= ['Autovehicul', 'RCA Data Expir', 'RCA Valoare', 'RCA Asigurator', 'RCA Broker','CASCO Data Expir', 'CASCO Valoare', 'CASCO Asigurator', 'CASCO Broker', 'ITP Expir', 'Rovinieta Expir']
    asigurari_layout = [
        [sg.Table(values=inregistrari_tabela_asigurari, headings=headings_asigurari, max_col_width=50,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=15,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='Reservations Table')]
    ]
    asigurari_information_window = sg.Window("Asigurari Information", asigurari_layout, modal=True)

    while True:
        event, values = asigurari_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    asigurari_information_window.close()