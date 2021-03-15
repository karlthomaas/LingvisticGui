from tkinter import *
import requests
from bs4 import BeautifulSoup


root = Tk()
root.title('Lingvistik App')
x_resolution = '470'
y_resolution = '380'
root.geometry(f"{x_resolution}x{y_resolution}")

def clearTextInput():
    textBox.delete("1.0","end")

def ekssSearch():
    clearTextInput()
    otsing = otsingEntry.get()
    result = requests.get(f'https://www.eki.ee/dict/ekss/index.cgi?Q={otsing}&F=M')
    rc = result.content
    soup = BeautifulSoup(rc, features='html.parser')
    try:
        sisu = soup.find('span', class_='d').text
        textBox.insert(INSERT, sisu)
    except:
        textBox.insert(INSERT, 'Otsitavat sõna ei leitud.')

def osSearch():
    clearTextInput()
    otsing = otsingEntry.get()
    result = requests.get(f'https://www.eki.ee/dict/qs/index.cgi?Q={otsing}&F=M')
    rc = result.content
    soup = BeautifulSoup(rc, features='html.parser')
    try:
        # Otsib div klassi (seal klassis on kõik see informatsioon)
        sisu = soup.find('div', class_='tervikart').text
        # Lisab need laused, lausete kaupa listi
        uued_laused = sisu.split('.')
        # Võtab listilt nurksed sulud ära, ning kuvab ainult esimesed 5 lauset
        uued_laused2 = ''.join(uued_laused[0:5])

        textBox.insert(INSERT, uued_laused2)
    except:
        textBox.insert(INSERT, 'Otsitavat sõna ei leitud.')


def iesSearch():
    clearTextInput()
    otsing = otsingEntry.get()
    result = requests.get(f'https://www.eki.ee/dict/ies/index.cgi?Q={otsing}&F=M&C06=en')
    rc = result.content
    soup = BeautifulSoup(rc, features='html.parser')
    try:
        for tahendus in soup.find_all('div', class_='tervikart', limit=7):
            textBox.insert(INSERT, tahendus.text)
            textBox.insert(INSERT, '\n')
    except:
        textBox.insert(INSERT, 'Otsitavat sõna ei leitud.')


def susSearch():
    clearTextInput()
    otsing = otsingEntry.get()
    result = requests.get(f'http://www.eki.ee/dict/sys/index.cgi?Q={otsing}&F=M&C06=en')
    rc = result.content
    soup = BeautifulSoup(rc, features='html.parser')
    try:
        sisu = soup.find('div', class_='tervikart').text
        sonad = sisu.split(', ')
        sisu2 = ', '.join(sonad[0: 10])
        textBox.insert(INSERT, sisu2)
    except:
        textBox.insert(INSERT, 'Otsitavat sõna ei leitud.')

# row 0 ->
row0 = Label(root, text='').grid(column=0, row=0)


# row 1 ->
row1Span1 =Label(root, text='                     ').grid(row=1, column=0)
otsingEntry = Entry(root, width=53)
otsingEntry.grid(row=1, column=1, columnspan=4)

# row 2 ->
row2Span1 = Label(root, text='     ').grid(row=2, column=0)
ekssButton = Button(root, text='EKSS', width=10, command=ekssSearch).grid(row=2, column=1)
iesButton = Button(root, text='IES', width=10, command=iesSearch).grid(row=2, column=2)
osButton = Button(root, text='ÕS', width=10, command=osSearch).grid(row=2, column=3)
susButton = Button(root, text='SÜS', width=10, command=susSearch).grid(row=2, column=4)

# row 3 ->
row3Span1 = Label(root, text='     ').grid(row=3, column=0)
# textBox = Text(root, height=15, width=40).grid(row=3, column=1, columnspan=8)
# textBox.insert(INSERT, 'bruh')

# Canvas text box ->
# my_canvas = Canvas(root, height=280, width=320, bg='white')
# my_canvas.grid(row=3, column=1, columnspan=4)
# # my_canvas.create_text(x=0, y=0, text='bruh')

textBox = Text(root, height=18, width=40, wrap=WORD)
textBox.grid(row=3, column=1, columnspan=4)
# textBox.configure(state='disabled')

root.mainloop()