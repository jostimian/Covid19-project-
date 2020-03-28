from tkinter import *
from tkinter import messagebox
import COVID19Py
import pandas as pd
def fight_corona(conf_list):
    d = pd.DataFrame.from_dict(conf_list)
    d = pd.concat([d, d['coordinates'].apply(pd.Series),d['latest'].apply(pd.Series)], axis=1)
    d.drop(columns= ['coordinates', 'latest'], inplace= True)
    return d
def confirmed_wrld():
    conf_list = covid19.getLocations(rank_by='confirmed')
    df = fight_corona(conf_list)
    df.to_excel('confirmed.xlsx')
    messagebox.showinfo('Saved','Saved In confirmed.xlsx')
def ph():
    location = covid19.getLocationByCountryCode("PH")
    df = fight_corona(location)
    df.to_excel('PH.xlsx')
    messagebox.showinfo('Saved','Saved in PH.xlsx')
covid19 = COVID19Py.COVID19(data_source="jhu")
root = Tk()
root.geometry("500x500")
root.title("CoronaVirus Locator")
confirmed_BTN = Button(text="confirmed cases death and recoveries of COVID19", command = confirmed_wrld)
confirmed_BTN.pack()
ph_BTN = Button(text = "Covid19 Cases in the PH",command = ph)
ph_BTN.pack()
root.mainloop()
