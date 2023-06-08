from tkinter import *

root = Tk()
root.geometry("500x500")


label_hospital_alloted = Label(root)
label_hospital_alloted.place(relx= 0.1 , rely= 0.3 , anchor = CENTER)
label_IT_alloted = Label(root)
label_IT_alloted.place(relx= 0.1 , rely= 0.6 , anchor = CENTER)
label_chemical_alloted = Label(root)
label_chemical_alloted.place(relx= 0.1 , rely= 0.9 , anchor = CENTER)

def hospital() :
    label_hospital_alloted["text"] = "Micheal has been alloted to Galaxy"
    
def IT_company() :
    label_IT_alloted["text"] = "Jessica has been alloted to I Code"
    
def chemical() :
    label_chemical_alloted["text"] = "Peter has been alloted to DuPont"
    

btn_hospital = Button(root , text = "Show the Hospital alloted" , command= hospital)
btn_hospital.place(relx= 0.1 , rely= 0.2 , anchor = CENTER)
btn_IT = Button(root , text = "Show the IT company alloted" , command= IT_company)
btn_IT.place(relx= 0.1 , rely= 0.5 , anchor = CENTER)
btn_chemical = Button(root , text = "Show the Chemical Company alloted" , command= chemical)
btn_chemical.place(relx= 0.1 , rely= 0.8 , anchor = CENTER)


root.mainloop()