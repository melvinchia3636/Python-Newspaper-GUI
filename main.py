from tkinter import *
from bs4 import BeautifulSoup
from tkinter.font import Font
import requests
from PIL import Image, ImageTk
import ctypes

def get_news():
    global title
    global c
    data = []
    temp = []
    title = []
    c = []

    page = requests.get('https://inshorts.com/en/read')
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.findAll('div', {'class':'news-card z-depth-1'})

    for i in content:
        data.append(i.text)

    for i in range(len(data)):
        data[i] = data[i].split('\n')

    for o in range(len(data)):
        [temp.append(i) for i in data[o] if i]

    data = temp

    for i in range(len(data)):
        data[i] = data[i].replace('/','').replace('      ','')

    for a in range(len(data)):
        for i in range(len(data)):
            try:
                if 'read more' in data[i]:
                    del data[i]
                if ''.join(data[i].split(' ')) == '':
                    del data[i]
            except:
                pass

    counter =0
    for i in range(int(len(data)/6)):
        title.append(data[counter])
        counter += 6

    counter =3
    for i in range(int(len(data)/6)):
        c.append(data[counter])
        counter += 6

def init():

    get_news()

    root = Tk()
    root.geometry('1100x800+410+140')
    root.config(bg='white')
    root.resizable(False, False)
    root.title('Python Newspaper')
    root.iconbitmap('icon.ico')

    mainicon = ImageTk.PhotoImage(Image.open('icon.png'))

    titlefont = Font(size=30, family='Bahnschrift SemiBold')
    newstitlefont = Font(size=20, family='Bahnschrift SemiBold')

    titleicon = Label(image=mainicon, bg='white')
    titleicon.place(x=350,y=25)
    titlelabel = Label(root, text='Python Newspaper', bg='white', fg='black', font=titlefont)
    titlelabel.place(x=400, y=20)
    textframe = Frame(root, bg='#829356', width=972, height=652)
    textframe.place(x=63.5, y=96)
    textbox = Text(root, width = 120, height=40, relief=FLAT)
    textbox.place(x=67.5, y=100)
    textbox.tag_configure('titlestyle', background='white', foreground='#829356', font=newstitlefont, relief='raised')
    textbox.tag_configure('contentstyle', background='white', foreground='#131516', font='Helvetica 15', relief='raised')
    for i in range(len(title)):
        textbox.insert(END, title[i]+'\n', 'titlestyle')
        textbox.insert(END, c[i]+'\n\n','contentstyle')
    textbox.config(state=DISABLED)
     
    root.mainloop()

if __name__ == '__main__':
    try:
        requests.get('https://www.google.com')
        init()
    except:
        ctypes.windll.user32.MessageBoxW(0,'Please check your internet connection','Internet Connection Error',0|0x10)
        quit()
