import PySimpleGUI as sg
import db_interface


def informatii_revizii_reparatii():
    interogare_info_db = db_interface.vizualizare_informatii_revizii_reparatii()
    return interogare_info_db


def create():
    inregistrari_tabela_revizii_reparatii = informatii_revizii_reparatii()
    headings_revizii_reparatii = ['Autovehicul', 'Utilizator', 'Km Bord', 'Data Interventie', 'Tip Interventie', 'Service Auto', 'Valoare Piese', 'Valoare Manopera', 'Discuri', 'Distributie', 'Ambreaj', 'Placute', 'Anvelope', 'Numar Anvelope Noi', 'Acumulator', 'Observatii']
    revizii_reparatii_layout = [
        [sg.Table(values=inregistrari_tabela_revizii_reparatii, headings=headings_revizii_reparatii, max_col_width=50,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=15,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='Reservations Table')]
    ]
    revizii_reparatii_information_window = sg.Window("Revizii Reparatii Information", revizii_reparatii_layout, modal=True)

    while True:
        event, values = revizii_reparatii_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    revizii_reparatii_information_window.close()