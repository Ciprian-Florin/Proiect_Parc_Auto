import sqlite3
import pyodbc
import dashboard


def modificare_intrari_tabela_nomenclator():
    CONN = sqlite3.connect('parc_auto.db')
    CURSOR_JOB = CONN.cursor()
    CONN.close()
