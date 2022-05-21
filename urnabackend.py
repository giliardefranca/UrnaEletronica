import tkinter.messagebox
from tkinter import *
import tkinter.font as tkFont
from playsound import playsound
import threading
from bancodedados import BancoDeDados
from PIL import Image, ImageTk

class UrnaEletronica:

    def __init__(self, entry0, entry1, entry2, entry3, entry4, entry5, entry6, entry7):
        self.entry0 = entry0
        self.entry1 = entry1
        self.entry2 = entry2
        self.entry3 = entry3
        self.entry4 = entry4
        self.entry5 = entry5
        self.entry6 = entry6
        self.entry7 = entry7
        self.entry6_img = ''
        self.entry7_img = ''

        self.banco_dados = BancoDeDados()
        self.zerar_marcador = self.banco_dados.Zerar_Marcador
        self.cursor = self.banco_dados.cursor


        self.NUMERO_PARTIDO_LULA = '13'
        self.NUMERO_PARTIDO_BOLSONARO = '22'


    def FonteFormatadaContagemVotos(self, entry):
        self.font = tkFont.Font(family="Arial", size=20)
        entry.configure(font=self.font, foreground="white")

    def ContagemVotosLula(self):
        self.lula, self.bolsonaro = self.banco_dados.InformacoesBancoDeDados()
        self.entry4.delete(0, END)
        self.entry4.insert(END, self.lula[5])
        self.FonteFormatadaContagemVotos(self.entry4)

    def ContagemVotosBolsonaro(self):
        lula, bolsonaro = self.banco_dados.InformacoesBancoDeDados()
        self.entry5.delete(0, END)
        self.entry5.insert(END, bolsonaro[5])
        self.FonteFormatadaContagemVotos(self.entry5)

    def FonteFormatadaNumero(self, entry):
        self.font = tkFont.Font(family="Arial", size=30)
        entry.configure(font=self.font)

    def FonteFormatadaLetras(self, entry):
        self.font = tkFont.Font(family="Arial", size=14)
        entry.configure(font=self.font)

    def Som(self):
        playsound('Urna Eletrônica.mp3')

    def SomNotificacao(self):
        playsound('Urna Eletrônica notificacao.mp3')
        self.msg = tkinter.messagebox.askquestion(title='JUSTIÇA ELEITORAL', message="É o seu Candidato?")
        return self.msg

    def MensagemError(self):
        tkinter.messagebox.showerror(title='JUSTIÇA ELEITORAL', message=f'Número Inválido.')

    def SomMensagemError(self):
        playsound('Alerta - Emergência.mp3')

    def CarregandoImagemDosCandidato(self,presidente, vice):
        self.entry6_img = ImageTk.PhotoImage(Image.open(presidente))
        self.entry6.image_create(END, image=self.entry6_img)
        self.entry7_img = ImageTk.PhotoImage(Image.open(vice))
        self.entry7.image_create(END, image=self.entry7_img)

    def ImagemPresidenteEVice(self):
        self.lula = 'lula.png'
        self.alckim = 'alckmin.png'
        self.bolsonaro = 'bolsonaro.png'
        self.braganeto = 'braganeto.png'
        return self.lula, self.alckim, self.bolsonaro, self.braganeto

    def FonteFormatada(self):
        self.FonteFormatadaLetras(self.entry1)
        self.FonteFormatadaLetras(self.entry2)
        self.FonteFormatadaLetras(self.entry3)

    def Entrys(self, candidato):
        self.entry1.insert(END, candidato[2])
        self.entry2.insert(END, candidato[4])
        self.entry3.insert(END, candidato[3])

    def CanditatoLula(self):
        self.lula, self.bolsonaro = self.banco_dados.InformacoesBancoDeDados()
        self.Entrys(self.lula)
        self.FonteFormatada()

    def CanditatoBosonaro(self):
        self.lula, self.bolsonaro = self.banco_dados.InformacoesBancoDeDados()
        self.Entrys(self.bolsonaro)
        self.FonteFormatada()

    def VotoBranco(self):
        self.entry0.insert(END, ' ')
        self.entry1.insert(END, ' ')
        self.entry2.insert(END, ' ')
        self.entry3.insert(END, ' ')

    def NumeroDoPartido(self):
        return self.entry0.get()

    def Votacao(self):
        lula, alckim, bolsonaro, braganeto = self.ImagemPresidenteEVice()
        if self.NumeroDoPartido() == self.NUMERO_PARTIDO_LULA:
            self.CanditatoLula()
            self.CarregandoImagemDosCandidato(lula, alckim)
            return self.NUMERO_PARTIDO_LULA
        elif self.NumeroDoPartido() == self.NUMERO_PARTIDO_BOLSONARO:
            self.CanditatoBosonaro()
            self.CarregandoImagemDosCandidato(bolsonaro, braganeto)
            return self.NUMERO_PARTIDO_BOLSONARO
        else:
            pass


    def btn_clicked1(self):
        self.entry0.insert(END, '1')
        self.Votacao()
        self.FonteFormatadaNumero(self.entry0)

    def default(self):
        if self.entry0.get():
            self.entry0.delete(0, END)
        if self.entry1.get():
            self.entry1.delete(0, END)
        if self.entry2.get():
            self.entry2.delete(0, END)
        if self.entry3.get():
            self.entry3.delete(0, END)
        if self.entry6.get("1.0", END):
            self.entry6.delete("1.0", END)
        if self.entry7.get("1.0", END):
            self.entry7.delete("1.0", END)

    def btn_clicked2(self):
        self.entry0.insert(END, '2')
        self.Votacao()
        self.FonteFormatadaNumero(self.entry0)

    def btn_clicked3(self):
        self.entry0.insert(END, '3')
        self.Votacao()
        self.FonteFormatadaNumero(self.entry0)

    def btn_clicked4(self):
        self.entry0.insert(END, '4')
        self.FonteFormatadaNumero(self.entry0)

    def btn_clicked5(self):
        self.entry0.insert(END, '5')
        self.FonteFormatadaNumero(self.entry0)

    def btn_clicked6(self):
        self.entry0.insert(END, '6')
        self.FonteFormatadaNumero(self.entry0)

    def btn_clicked7(self):
        self.entry0.insert(END, '7')
        self.FonteFormatadaNumero(self.entry0)

    def btn_clicked8(self):
        self.entry0.insert(END, '8')
        self.FonteFormatadaNumero(self.entry0)

    def btn_clicked9(self):
        self.entry0.insert(END, '9')
        self.FonteFormatadaNumero(self.entry0)

    def btn_clicked0(self):
        self.entry0.insert(END, '0')
        self.FonteFormatadaNumero(self.entry0)


    def btn_clickedVerde(self):
        self.numero = self.NumeroDoPartido()
        if self.numero == self.NUMERO_PARTIDO_LULA:
            self.VOTOSLULA = 1
            self.banco_dados.AtualizaContagemVotos_BancoDeDados(self.VOTOSLULA, self.entry1)
            self.Som()
            self.ContagemVotosLula()
            tkinter.messagebox.showinfo(title="JUSTIÇA ELEITORAL", message='FIM!')
            self.default()
        elif self.numero == self.NUMERO_PARTIDO_BOLSONARO:
            self.VOTOSBOSONARO = 1
            self.banco_dados.AtualizaContagemVotos_BancoDeDados(self.VOTOSBOSONARO, self.entry1)
            self.Som()
            self.ContagemVotosBolsonaro()
            tkinter.messagebox.showinfo(title='JUSTIÇA ELEITORAL', message='FIM!')
            self.default()
        elif self.NumeroDoPartido() == ' ':
            self.Som()
            tkinter.messagebox.showinfo(title='JUSTIÇA ELEITORAL', message='VOTO EM BRANCO')
            self.default()
        else:
            som = threading.Thread(target=self.MensagemError)
            msg = threading.Thread(target=self.SomMensagemError)
            som.start()
            msg.start()
            self.entry0.delete(0, END)

    def btn_clickedLaranga(self):
        self.default()

    def btn_clickedBranco(self):
        self.VotoBranco()

