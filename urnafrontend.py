from tkinter import *
from urnabackend import UrnaEletronica


window = Tk()

window.geometry("805x472")
window.configure(bg = "#ffffff")
ico = PhotoImage(file = 'ico.png')
window.iconphoto(False, ico)
window.title('JUSTIÇA ELEITORAL')
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 472,
    width = 805,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    403.5, 222.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked1(),
    relief = "flat")

b0.place(
    x = 551, y = 182,
    width = 44,
    height = 31)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked2(),
    relief = "flat")

b1.place(
    x = 626, y = 182,
    width = 44,
    height = 31)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked3(),
    relief = "flat")

b2.place(
    x = 704, y = 182,
    width = 44,
    height = 31)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked4(),
    relief = "flat")

b3.place(
    x = 551, y = 237,
    width = 44,
    height = 31)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked5(),
    relief = "flat")

b4.place(
    x = 626, y = 237,
    width = 44,
    height = 31)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked6(),
    relief = "flat")

b5.place(
    x = 704, y = 237,
    width = 44,
    height = 31)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked7(),
    relief = "flat")

b6.place(
    x = 551, y = 296,
    width = 44,
    height = 31)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked8(),
    relief = "flat")

b7.place(
    x = 626, y = 296,
    width = 44,
    height = 31)

img8 = PhotoImage(file = f"img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked9(),
    relief = "flat")

b8.place(
    x = 704, y = 296,
    width = 44,
    height = 31)

img9 = PhotoImage(file = f"img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clicked0(),
    relief = "flat")

b9.place(
    x = 626, y = 354,
    width = 44,
    height = 31)

img10 = PhotoImage(file = f"img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clickedVerde(),
    relief = "flat")

b10.place(
    x = 696, y = 388,
    width = 86,
    height = 44)

img11 = PhotoImage(file = f"img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clickedBranco(),
    relief = "flat")

b11.place(
    x = 524, y = 403,
    width = 71,
    height = 29)

img12 = PhotoImage(file = f"img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:urnaeletronica.btn_clickedLaranga(),
    relief = "flat")

b12.place(
    x = 613, y = 403,
    width = 70,
    height = 29)


entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    171.5, 192.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c2c1c1",
    highlightthickness = 0)

entry0.place(
    x = 127, y = 167,
    width = 89,
    height = 48)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    238.0, 244.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 127, y = 225,
    width = 222,
    height = 37)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    302.0, 366.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry2.place(
    x = 191, y = 347,
    width = 222,
    height = 37)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    167.0, 306.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry3.place(
    x = 127, y = 287,
    width = 80,
    height = 37)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    82.0, 30.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#000000",
    highlightthickness = 0)

entry4.place(
    x = 57, y = 16,
    width = 50,
    height = 27)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    228.0, 30.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#000000",
    highlightthickness = 0)

entry5.place(
    x = 203, y = 16,
    width = 50,
    height = 27)


entry6 = Text(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry6.place(
    x = 396, y = 42,
    width = 98,
    height = 123)


entry7 = Text(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry7.place(
    x = 396, y = 169,
    width = 98,
    height = 123)




img13 = PhotoImage(file = f"img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:[urnaeletronica.zerar_marcador(), urnaeletronica.ContagemVotosLula(), urnaeletronica.ContagemVotosBolsonaro()],

    relief = "flat")

b13.place(
    x = 0, y = 375,
    width = 19,
    height = 49)

urnaeletronica = UrnaEletronica(entry0=entry0, entry1=entry1, entry2=entry2, entry3=entry3, entry4=entry4, entry5=
                                entry5, entry6=entry6, entry7=entry7)



urnaeletronica.ContagemVotosLula()
urnaeletronica.ContagemVotosBolsonaro()
window.resizable(False, False)
window.mainloop()

