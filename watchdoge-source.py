import pandas_datareader as web
import matplotlib.pyplot as plt
plt.ioff()
import mplfinance as mpf
import yfinance as yf
import matplotlib as matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *
import datetime as dt
from datetime import timedelta
from PIL import ImageTk, Image

start = dt.date.today()
end = dt.datetime.now()


root = Tk()
root.title("WATCH-DOGE")
root.geometry('600x600')

#setting up frames
graphFrame = Frame(root, width=600, height= 300, bg='white')
graphFrame.grid(row=1, column=0, padx=10, pady=5)
bottomFrame = Frame(root, width=600, height= 275)
bottomFrame.grid(row=0, column=0, padx=10, pady=5)

#retrieving intraday price fluctuation
intraday = yf.download("DOGE-USD",start,end,interval='15m')

#plotting price evolution
fig, ax = mpf.plot(intraday,type='candle',
                      tight_layout=True, 
                      figratio=(12,6),
                      figscale=0.50,
                      scale_padding=dict(bottom=2.90,top=0.5, left=0.7),
                      returnfig=True
                      )
    
  
canvas = FigureCanvasTkAgg(fig, master=graphFrame)   
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)

#putting dope image on the grid
image = Image.open("logo1.png")
photo = ImageTk.PhotoImage(image.resize((550,250),Image.ANTIALIAS))

label = Label(bottomFrame,image=photo)
label.image=photo
label.grid()


#getting live price from yahoo
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

#defining phrase and live price
var = DoubleVar()
var.set(get_current_price('DOGE-USD'))

var2 = StringVar()
var2.set("Current DOGE price is:")

#placing phrase and live price on the screen
label2 = Label(root, textvariable=var)
label2.place(x=150,y=560)

label3 = Label(root, textvariable=var2)
label3.place(x=20,y=560)


root.mainloop()
