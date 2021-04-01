#made by https://github.com/ExaSakiMaka
import webbrowser
from tkinter import * 


#opens the tkinter window
fenetre = Tk(className='Sauce Finder')

#defineing the window opending function
def openweb():
    num = E1.get()
    #print(num)         (debug line)
    webbrowser.open("https://nhentai.net/g/"+num+"/")       #open's the web page
    history = open("bin/history.txt","a")                   #open's the hitory file
    history.write(num+" , ")                                #adding the code to the history with a separator : " , "


#the history opening function
def openHistory():
    history = open("bin/history.txt","r")       #open's the hitory file in read mode only

    SERIALDATA= history.read()                  #Read line of text from file
    DATASPLIT= SERIALDATA.split(' , ')          #Splits the line of text into array of strings composed of each individual sensor data
    stringcount = len(DATASPLIT)                #count's the codes in the file

    counter = 0                                 #initialize the counter

    for i in range(stringcount):                            #open's codes until there is no more
        num = DATASPLIT[counter]                            #chosing codes from the first to the last 
        webbrowser.open("https://nhentai.net/g/"+num+"/")   #open's the web page
        counter = counter+1                                 #add's one to the counter


#set's the window size (250 x 300 px)
fenetre.geometry("250x300")

#making the window not resizable
fenetre.resizable(False, False)

#ad's an indicative text
label = Label(fenetre, text="What are those numbers boy ?")
label.pack(pady = 30)

#place to entre the numbers
E1 = Entry(fenetre, bd =5)
E1.pack()

#comfirmation button
B = Button(fenetre, text ="Open", command = openweb)
B.pack(pady = 20)

#history button
H = Button(fenetre, text="historique", command = openHistory)
H.pack(pady = 10)

#close button
bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack(pady = 30)

fenetre.mainloop()
