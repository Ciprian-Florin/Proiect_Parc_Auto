import PySimpleGUI as sg
import db_interface


def informatii_evenimente():
    interogare_info_db = db_interface.vizualizare_informatii_evenimente()
    return interogare_info_db


def create():
    inregistrari_tabela_evenimente = informatii_evenimente()
    headings_evenimente= ['Autovehicul', 'Utilizator', 'Culpa Da/Nu', 'Data Eveniment', 'Observatii','Cost Reparatie', 'Suportat RCA', 'Suportat Casco', 'Suportat Coriolan', 'Suportat Utilizator']
    evenimente_layout = [
        [sg.Table(values=inregistrari_tabela_evenimente, headings=headings_evenimente, max_col_width=50,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=15,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='Reservations Table')]
    ]
    evenimente_information_window = sg.Window("Evenimente Information", evenimente_layout, modal=True)

    while True:
        event, values = evenimente_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    evenimente_information_window.close()