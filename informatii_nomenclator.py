import PySimpleGUI as sg
import db_interface


def informatii_nomenclator():
    interogare_info_db = db_interface.vizualizare_informatii_nomenclator()
    return interogare_info_db


def create():
    inregistrari_tabela_nomenclator = informatii_nomenclator()
    headings_nomenclator = ['Autovehicul', 'Motorizare', 'Capacitate Cilindrica', 'Producator', 'Marca',
                            'An Fabricatie', 'Km la Achizitie', 'Valoare Intrare', 'Destinatie', 'Tip Anvelope',
                            'Interval Revizie 1',
                            'Limita Interval Revizie 1', 'Interval Revizie 2', 'Limita Interval Revizie 2',
                            'Interval Revizie 3', 'Limita Interval Revizie 3'
                            ]
    nomenclator_layout = [
        [sg.Table(values=inregistrari_tabela_nomenclator, headings=headings_nomenclator, max_col_width=50,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=15,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='Reservations Table')]
    ]
    nomenclator_information_window = sg.Window("Nomenclator Information", nomenclator_layout, modal=True)

    while True:
        event, values = nomenclator_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    nomenclator_information_window.close()


