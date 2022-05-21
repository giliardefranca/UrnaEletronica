import pyodbc

class BancoDeDados():


    def __init__(self):
        self.dados_conexao = ("Driver={SQL Server};"
                         "Server=hostname;"
                         "Database=ContagemDeVotos")
        conexao = pyodbc.connect(self.dados_conexao)
        self.cursor = conexao.cursor()

    def AtualizaContagemVotos_BancoDeDados(self, votos, entry1):
        comando = f"""UPDATE candidatos
                            SET qtde_votos = qtde_votos  + {votos}
                            WHERE nome_candidato = '{entry1.get()}';
                            """
        self.cursor.execute(comando)
        self.cursor.commit()

    def InformacoesBancoDeDados(self):
        comando = f"""SELECT * from candidatos
                        WHERE qtde_votos = qtde_votos;
                        """
        self.cursor.execute(comando)
        lula, bolsonaro = self.cursor.fetchall()
        return lula, bolsonaro

    def Zerar_Marcador(self):
        comando = f"""UPDATE  candidatos
        SET qtde_votos= '0';
                                """
        self.cursor.execute(comando)
        self.cursor.commit()
