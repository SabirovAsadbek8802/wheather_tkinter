from tkinter import *
from PIL import ImageTk,Image
import requests
from io import BytesIO

oyna = Tk()
oyna.geometry("900x523+300+50")
oyna.resizable(FALSE,FALSE)
oyna.configure(bg='#b7b7a4')
oyna.title("Searching...")
oyna.iconbitmap("iconapp.ico")

bg_img = PhotoImage(file='background.png')
Label(oyna, image=bg_img).pack()


searchtxt = StringVar()
searchent = Entry(oyna, textvariable=searchtxt, font=("MV Boli", 30), width=20, justify=CENTER)
searchent.place(x=165,y = 200)

img2 = ImageTk.PhotoImage(Image.open('searchbg.png').resize((40,40)))


img = ImageTk.PhotoImage(Image.open('cloud.png').resize((150,150)))
def click():
    global img
    oyna.wm_attributes('-alpha', 0.5)
    top = Toplevel()
    top.iconbitmap("iconapp.ico")
    top.title(searchtxt.get())
    top.configure(bg="#bde0fe")
    top.geometry("580x300+450+100")

    api_url = f'https://api.weatherapi.com/v1/current.json?key=9e070c3df80441ffb0b113050232703&q={searchtxt.get()}&aqi=no'
    data = requests.get(api_url)
    data = data.json()
    if len(data.keys())>1:
        gradus = Label(top, text='23°C', font=("MV Boli",50), bg="#bde0fe")
        gradus.place(x=160,y=70)

        time_def = Label(top, text='18:23 28.05.2023', font=('MV Boli',11), bg='#bde0fe')
        time_def.place(x=160, y=175)

        holati = Label(top, text='Cloudy', font=("MV Boli",15), bg='#bde0fe')
        holati.place(x=160,y=150)

        region_def = Label(top, text='Khorezm', font=('MV Boli',11), bg='#bde0fe')
        Label(top, text='Region: ', font=('MV Boli',11), bg='#bde0fe').place(x=335, y=60)
        region_def.place(x=413, y=60)

        country_def = Label(top, text='Uzbekistan', font=('MV Boli', 11), bg='#bde0fe')
        Label(top, text='Country: ', font=('MV Boli', 11), bg='#bde0fe').place(x=335, y=85)
        country_def.place(x=413, y=85)

        feell = Label(top, text='23.0', font=("MV Boli", 11), bg="#bde0fe")
        Label(top, text='Feel like: ', font=('MV Boli', 11), bg='#bde0fe').place(x=335, y=110)
        feell.place(x=413, y=110)

        kun_nomi = Label(top, text='', font=("MV Boli", 11), bg="#bde0fe")
        Label(top, text='Weekday: ', font=('MV Boli', 11), bg='#bde0fe').place(x=333, y=135)
        kun_nomi.place(x=415, y=135)

        wet = Label(top, text='12%', font=("MV Boli", 11), bg="#bde0fe")
        Label(top, text='Humidity: ', font=('MV Boli', 11), bg='#bde0fe').place(x=335, y=160)
        wet.place(x=415, y=160)

        shamol = Label(top, text='24', font=("MV Boli", 11), bg="#bde0fe")
        Label(top, text='Wind speed: ', font=('MV Boli', 11), bg='#bde0fe').place(x=335, y=185)
        shamol.place(x=426, y=185)


        region = data["location"]["region"]
        country = data['location']['country']
        temp = data["current"]["temp_c"]
        time_data = data["location"]["localtime"]
        text_w = data["current"]['condition']['text']
        image_url = data["current"]['condition']['icon']
        feellike = data["current"]['feelslike_c']
        day_num = data["current"]['is_day']
        namlik = data["current"]['humidity']
        wind_speed_km = data["current"]['wind_kph']

        match day_num:
            case 1:
                kun_nomi['text'] = 'Sunday',
            case 2:
                kun_nomi['text'] = 'Monday',
            case 3:
                kun_nomi['text'] = 'Tuesday',
            case 4:
                kun_nomi['text'] = 'Wednesday',
            case 5:
                kun_nomi['text'] = 'Thursday',
            case 6:
                kun_nomi['text'] = 'Friday',
            case 7:
                kun_nomi['text'] = 'Saturday',

        region_def['text']=region
        country_def['text']=country
        gradus['text']=str(int(temp))+'°C'
        time_def['text']=time_data
        holati['text']=text_w
        feell["text"]=str(feellike)+'°C'
        wet['text']=str(namlik)+'%'
        shamol['text']=str(wind_speed_km)+'km/h'

        image=requests.get('https:'+image_url)
        response = image.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(response)).resize((150, 150)))
        Label(top, image=img, bg="#bde0fe").place(x=10, y=50)

        Button(top, text='click to close', bg='red', activebackground='green', command=lambda :oyna.destroy()).place(x=360,y=230)



search_btn = Button(oyna, text='OK',bg='blue',width=10, activebackground='green', command=click).place(x=420,y=290)

oyna.mainloop()