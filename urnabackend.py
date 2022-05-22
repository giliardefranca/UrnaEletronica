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

        self.font_size_letra = 14
        self.font_size_numero = 30
        self.color_font = 'black'
        self.color_font_placar = 'white'
        self.font_size_placar= 20


    def FonteFormatada(self, entry, cor, size):
        self.font = tkFont.Font(family="Arial", size=size)
        entry.configure(font=self.font, foreground=cor)

    def ContagemVotosLula(self):
        self.lula, self.bolsonaro = self.banco_dados.InformacoesBancoDeDados()
        self.entry4.delete(0, END)
        self.entry4.insert(END, self.lula[5])
        self.FonteFormatada(self.entry4,self.color_font_placar, self.font_size_placar)

    def ContagemVotosBolsonaro(self):
        lula, bolsonaro = self.banco_dados.InformacoesBancoDeDados()
        self.entry5.delete(0, END)
        self.entry5.insert(END, bolsonaro[5])
        self.FonteFormatada(self.entry5, self.color_font_placar, self.font_size_placar)


    def Som(self):
        playsound('Urna Eletrônica.mp3')

    def SomNotificacao(self):
        playsound('Urna Eletrônica notificacao.mp3')
        self.msg = tkinter.messagebox.askquestion(title='JUSTIÇA ELEITORAL', message="É o seu Candidato?")
        return self.msg

    def MensagemVotoNulo(self):
        tkinter.messagebox.showerror(title='JUSTIÇA ELEITORAL', message=f'NÚMERO ERRADO. VOTO NULO!')

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

    def FonteFormatadaEntrys(self):
        self.FonteFormatada(self.entry1, self.color_font, self.font_size_letra)
        self.FonteFormatada(self.entry2, self.color_font, self.font_size_letra)
        self.FonteFormatada(self.entry3, self.color_font, self.font_size_letra)

    def Entrys(self, candidato):
        self.entry1.insert(END, candidato[2])
        self.entry2.insert(END, candidato[4])
        self.entry3.insert(END, candidato[3])

    def CanditatoLula(self):
        self.lula, self.bolsonaro = self.banco_dados.InformacoesBancoDeDados()
        self.Entrys(self.lula)
        self.FonteFormatadaEntrys()

    def CanditatoBosonaro(self):
        self.lula, self.bolsonaro = self.banco_dados.InformacoesBancoDeDados()
        self.Entrys(self.bolsonaro)
        self.FonteFormatadaEntrys()

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
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

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
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

    def btn_clicked3(self):
        self.entry0.insert(END, '3')
        self.Votacao()
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

    def btn_clicked4(self):
        self.entry0.insert(END, '4')
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

    def btn_clicked5(self):
        self.entry0.insert(END, '5')
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

    def btn_clicked6(self):
        self.entry0.insert(END, '6')
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

    def btn_clicked7(self):
        self.entry0.insert(END, '7')
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

    def btn_clicked8(self):
        self.entry0.insert(END, '8')
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

    def btn_clicked9(self):
        self.entry0.insert(END, '9')
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)

    def btn_clicked0(self):
        self.entry0.insert(END, '0')
        self.FonteFormatada(self.entry0, self.color_font, self.font_size_numero)


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
            som = threading.Thread(target=self.MensagemVotoNulo)
            msg = threading.Thread(target=self.Som)
            som.start()
            msg.start()
            self.entry0.delete(0, END)

    def btn_clickedLaranga(self):
        self.default()

    def btn_clickedBranco(self):
        self.VotoBranco()

