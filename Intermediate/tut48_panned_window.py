from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

# Panned Window widget
panel_1 = PanedWindow(bd=4, relief=SUNKEN, bg='red')
panel_1.pack(fill=BOTH, expand=True)

left_label = Label(panel_1, text="Left Panel") 
panel_1.add(left_label) 

# Create second panel
panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief=SUNKEN, bg='blue')
panel_1.add(panel_2) 

top = Label(panel_2, text="Top Panel") 
panel_2.add(top) 

bottom = Label(panel_2, text="Bottom Panel")
panel_2.add(bottom)



root.mainloop() 