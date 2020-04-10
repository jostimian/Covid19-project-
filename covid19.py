import datetime # So the user can see what time did he/she update the covid19 lists
import time # I use time.sleep to make stop CPU throttling for very slow systems
print("Importing Tkinter")# I add This Callouts so the user can understand what is happening in the background 
from tkinter import *
time.sleep(1)
print("Tkinter Imported")
print("Importing Tkinter Messagebox")
from tkinter import messagebox
time.sleep(1)
print("Tkinter Messagebox Imported")
print("Importing COVID19Py")
import COVID19Py
time.sleep(1)
print("COVID19Py Imported")
print("Importing Pandas")
import pandas as pd
time.sleep(1)
print("Pandas Imported")
def fight_corona(conf_list):
    d = pd.DataFrame.from_dict(conf_list)
    d = pd.concat([d, d['coordinates'].apply(pd.Series),d['latest'].apply(pd.Series)], axis=1)
    d.drop(columns= ['coordinates', 'latest'], inplace= True)
    return d
def confirmed_wrld():
    messagebox.showinfo('Wait',"This Might Take A Min or More")
    conf_list = covid19.getLocations(rank_by='confirmed')
    df = fight_corona(conf_list)
    df.to_excel('confirmed.xlsx')
    print("Confirmed.xlsx is updated on " + str(datetime.datetime.now()))
    messagebox.showinfo('Saved','Saved In confirmed.xlsx')
def ph():
    messagebox.showinfo("Wait","This may take a few minutes")
    location = covid19.getLocationByCountryCode("PH")
    df = fight_corona(location)
    df.to_excel('ph.xlsx')
    print("Ph.xlsx is updated on " + str(datetime.datetime.now()))
    messagebox.showinfo('Saved','Saved in PH.xlsx')
def find():
    messagebox.showinfo("Wait","This may take a few minutes")
    code = find_Entry.get()
    findLocation = covid19.getLocationByCountryCode(code)
    df = fight_corona(findLocation)
    df.to_excel(code + ".xlsx")
    print(code + ".xlsx is updated on " + str(datetime.datetime.now()))
    messagebox.showinfo("Saved", "Saved in" + code +".xlsx")

print("Connecting In Johns Hopkins University's(jhu) Database")
covid19 = COVID19Py.COVID19(data_source="jhu")
print("This may take a few seconds depending on your internet connection")
time.sleep(1)
print("Connection Done")
print("exiting CLI")
print("Opening GUI")
print("""The list is not updating real time each country should report new covid19 cases in JHU so they can update their database.
But the list will be updated day by day <3""")
root = Tk()
messagebox.showinfo("Special Thanks","Special Thanks For The FrontLiners Out There Trying To Find Cure And Helping Serve Their Country And The World #BeatCovid19!")
root.geometry("400x300")
root.title("CoronaVirusLocator Version 1.4")

confirmedBtn = Button(text="confirmed cases death and recoveries of COVID19", command = confirmed_wrld)
confirmedBtn.pack()

phBtn = Button(text = "Covid19 Cases in the PH",command = ph)
phBtn.pack()

find_Entry = Entry()
find_Entry.pack() 

findBtn = Button(text = "Search By Country Code eg.(PH)", command = find)
findBtn.pack()
root.mainloop()
print("Quiting")
print("Thanks For Using This Application ❤😊😊")
time.sleep(2)
print("Confirmed Quit")