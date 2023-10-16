import pyodbc
import pandas as pd

class DatabaseOperations:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};'
                                   'SERVER=server_name;'
                                   'DATABASE=database_name;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def create_voo(self, voo):
        sql = 'INSERT INTO TabelaVoos (Empresa, CompanhiaVoo, PrecoTotal, TaxaEmbarque, TaxaServico, TempoVooMinutos, DataHoraIda, DataHoraVolta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        values = (voo.empresa, voo.companhia, voo.preco_total, voo.taxa_embarque, voo.taxa_servico, voo.tempo_voo, voo.data_hora_ida,voo.data_hora_volta, voo.data_insercao)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def execute_procedure_and_export_to_excel(self):
        self.cursor.execute("EXEC ObterMelhorPrecoPorEmpresa")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in self.cursor.description])
        df.to_excel('melhores_precos.xlsx', index=False)

