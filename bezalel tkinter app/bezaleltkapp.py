

 




import tkinter as tk
from random import choice
from tkinter import Menu, Toplevel
from turtledemo.nim import computerzug


import ttkbootstrap as tb  # Import ttkbootstrap
from tkinter import messagebox
import time
from PIL import Image,ImageTk
import random




from ttkbootstrap.constants import *


options_for_qustions = {
   1: ["a- avegteble", "b- a fruit", "c- mcdonalds prodact", "d- its ashwarma"],
   2: ["a- to be ultra orthodox", "b-to be a crestin ", "c- to eat mcdonalds",
       "d- 42"],
   3: ["a- kurshi ps1", "b- final fantasy 7", "c - far cry 3",
       "d- clash of clans "],
   4: ["a - pink", "b - blue", "c- black (what a dark soul...)",
       "d- all colors are expted"],
   5: [
       "a -שירי ארץ ישראל", "b -אנס גולן (אייל גולן)", "c - country ",
       "d - psychadelic rock"]}


conting_results_player = []
conting_results_python = []
brush_size = 4
cb = 200
changing_button=1
list_of_nums = []
number_of_gusses = 0
we_can_use_it_only_once = 0
choosen_num = 0
list_of_alredy_choosed_nums =[]
def num_is():
   global choosen_num
   global we_can_use_it_only_once
   if len(list_of_nums) == 0:
       pass
   elif we_can_use_it_only_once == 1:
       pass
   else:
       choosen_num = random.choice(list_of_nums)
       we_can_use_it_only_once += 1






faild_gusses = 0


word_chosen = (random.choice( ["parot", "dog", "cat", "bezalel","achonovfamily", "israel"]))
hints = ["_"] * len(word_chosen)
displaying = {0: (""
                 ""
                 ""),
             1: (" o \n"
                 "   \n"
                 "   "),
             2: (" o \n"
                 " | \n"
                 "   "),
             3: (" o \n"
                 "/| \n"
                 "   "),
             4: (" o \n"
                 "/|\\\n"
                 "   "),
             5: (" o \n"
                 "/|\\\n"
                 "/  "),
             6: (" o \n"
                 "/|\\\n"
                 "/ \\")}




def exibittind_hangman():
   global displaying


   for x in displaying[faild_gusses]:
       print(x)
       print(displaying.get(faild_gusses, "image availble"))
       return displaying.get(faild_gusses, "image availble")






class ThemedApp:
  def __init__(self, window):
      self.window = window
      self.window.title("האפליקציה של בצלאל גירסא 2.0 ")
      self.style = tb.Style("vapor")  # Default theme
      self.window.geometry('600x800')
      self.window.minsize(600,800)




      main_menu = Menu(self.window)
      self.window.config(menu=main_menu)
      self.aplications_menu = tk.Menu(main_menu, tearoff =False )
      self.aplications_menu.add_command(label= "app 1- מבחן אמריקאי", command= lambda :(app1(self) ))
      self.aplications_menu.add_command(label="app 2- צייר", command=lambda: ( app2(self) ))
      self.aplications_menu.add_command(label="app 3- כתבן", command=lambda: ( app3(self) ))
      self.aplications_menu.add_command(label="app 4- טבלאות", command=lambda: (app4(self)))
      self.aplications_menu.add_separator()
      main_menu.add_cascade(label= "aplications",menu= self.aplications_menu )




      self.games_menu = tk.Menu(main_menu, tearoff =False )
      self.games_menu.add_command(label="game 1- איש תלוי", command=lambda: ( game1(self) ))
      self.games_menu.add_command(label="game 2- אבן נייר ומספריים", command=lambda: ( game2(self) ))
      self.games_menu.add_command(label="game 3- מכונת הימורים", command=lambda: ( game3(self) ))
      self.games_menu.add_command(label="game 4- ניחוש מספרים", command=lambda: ( game4(self) ))
      self.games_menu.add_separator()
      main_menu.add_cascade(label= "games",menu= self.games_menu )




      settings_menu = Menu(main_menu, tearoff=0 )
      main_menu.add_cascade(label= "settings", menu = settings_menu)




      # Create "Settings" menu
      themes_menu = Menu(settings_menu, tearoff=0)
      settings_menu.add_cascade(label="thems and colors", menu=themes_menu)
      # Available themes
      themes = self.style.theme_names()
      for theme in themes:
          themes_menu.add_command(label=theme, command=lambda t=theme: change_theme(t))
      def change_theme( theme):
          """Change the theme dynamically"""
          self.style.theme_use(theme)




      # Sample Widget
      self.label = tb.Label(window, text="Hello, and welcome to \n"
                                         "bezalel's aplication 2.0!", font=("Arial black", 25, "bold", ))
      self.label.pack(pady=20)




      main_notebook = tb.Notebook()
      frame11 = tb.Frame(main_notebook)
      frame11.pack(expand=1 ,fill= "both")
      self.label11 = tb.Label(frame11, text="frame1")
      self.label11.pack()




      frame22 = tb.Frame(main_notebook)
      frame22.pack(expand=1 ,fill= "both")
      self.label22 = tb.Label(frame22, text="frame2")
      self.label22.pack()








      frame33 = tb.Frame(main_notebook)
      frame33.pack(expand=1 ,fill= "both")
      self.label33 = tb.Label(frame33, text="frame3")
      self.label33.pack()








      frame44 = tb.Frame(main_notebook)
      frame44.pack(expand=1 ,fill= "both")
      self.label44 = tb.Label(frame44, text="frame4")
      self.label44.pack()








      frame55 = tb.Frame(main_notebook)
      frame55.pack(expand=1 ,fill= "both")
      self.label55 = tb.Label(frame55, text="frame5")
      self.label55.pack()








      frame66 = tb.Frame(main_notebook)
      frame66.pack(expand=1 ,fill= "both")
      self.label66 = tb.Label(frame66, text="frame6")
      self.label66.pack()








      main_notebook.add(frame11, text="דף הבית")
      main_notebook.add(frame22, text="ממיר")
      main_notebook.add(frame33, text="מחשבון")
      main_notebook.add(frame44, text="טבלאות "
                                      "לגיטרה "
                                      "ובנג'ו ")
      main_notebook.add(frame55, text="מחשבים")
      main_notebook.add(frame66, text="גלריה")
      main_notebook.pack(expand=1 ,fill= "both")




      def frame11_func():
          date_entry = tb.DateEntry(frame11, bootstyle="info")
          date_entry.pack()




          def update_clock():
              """Update the clock label and progress bar every second."""
              current_time = time.strftime("%H:%M:%S")  # Get current time
              clock_label.config(text=current_time)  # Update clock label




              seconds = int(time.strftime("%S"))  # Get seconds (0-59)
              progress_bar["value"] = (seconds / 59) * 100  # Update progress bar




              frame11.after(1000, update_clock)  # Call this function again after 1 second








          # Create a clock label
          clock_label = tb.Label(frame11, text="", font=("Helvetica", 48), bootstyle="primary")
          clock_label.pack()#place( relx =o.5,rely=o.3, anchor= 'CENTER')

          # Create a progress bar linked to seconds
          progress_bar = tb.Progressbar(frame11, length=300, mode="determinate", bootstyle="info-striped")
          progress_bar.pack()#place(  relx=o.5,rely=o.3,)





        #   # Create a Canvas inside the Frame
        #   computer_canvas = tk.Canvas(frame11)
        #   computer_canvas.pack(side="left", expand=1, fill="both")

        
        #   # Create an inner Frame inside the Canvas
        #   inner_frame = tk.Frame(computer_canvas)
        #   canvas_window = computer_canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        #   image_path = r"C:\Users\בצלאל\Desktop\מחשב נייד בצלאל\לימודים\תיכנות\תמונות לתכנות\תמונות לאפליקציה\240_F_664620321_Ww8hMtjpcuDCTBUFyzWhnVOxFIPwMA7I.jpg "
        #   image = Image.open(image_path).resize((600, 300), Image.Resampling.LANCZOS)
        #   image_tk = ImageTk.PhotoImage(image)

        #   # Add the Image to the Inner Frame
        #   image_label = tk.Label(inner_frame, image=image_tk)
        #   image_label.image = image_tk  # Keep a reference
        #   image_label.pack()
          
        #   # Ensure the Canvas Updates Its Scroll Region
        #   def update_scroll_region(event=None):
        #       computer_canvas.configure(scrollregion=computer_canvas.bbox("all"))

        #   # Call update when content changes
        #   inner_frame.bind("<Configure>", update_scroll_region)
    






          # Start the clock update
          update_clock()
      frame11_func()
      def frame22_func():
          combo_items = ["dollar $ => shekel", "shekel=> dollar $", "mile=> kilometer", "kilometer=>mile","inch=>meter","meter=> inch","lbs=>kg","kg=>lbs"]
          combo_string= tk.StringVar(value=combo_items[0])




          noombers_var = tb.IntVar()




          choosing_units_combobox = tb.Combobox(frame22, font=("Helvetica", 20), textvariable=combo_string)
          choosing_units_combobox['values'] = combo_items
          choosing_units_combobox.place(relx=0.1, rely= 0.15)

          choosing_number_entry = tb.Entry(frame22, textvariable=noombers_var)
          choosing_number_entry.place(relx=0.7,rely=0.15)

          sending_entry_button = tb.Button(frame22, text=" send", command=lambda :calculating_func())
          sending_entry_button.place(relx= 0.4, rely=0.3)

          displaying_nums_meter = tb.Progressbar(frame22, value=(float(choosing_number_entry.get())) )
          displaying_nums_meter.pack(expand=1, ipadx=200)


          def calculating_func():
              print(str(combo_string.get()))
              print(int(choosing_number_entry.get()))

              if str(combo_string.get()) == "dollar $ => shekel":

                  output_label = tb.Label(frame22, text=f"results:{round(float(choosing_number_entry.get())*3.7,2)}", font=("Helvetica", 20),)
                  output_label.place(relx=0.7, rely=0.3)
              elif str(combo_string.get()) == "shekel=> dollar $":


                  output_label = tb.Label(frame22, text=f"results:{round(float(choosing_number_entry.get())/3.7,2)}", font=("Helvetica", 20),)
                  output_label.place(relx=0.7, rely=0.3)
              elif str(combo_string.get()) == "mile=> kilometer":




                  output_label = tb.Label(frame22, text=f"results:{round(float(choosing_number_entry.get())*1.6,2)}", font=("Helvetica", 20),)
                  output_label.place(relx=0.7, rely=0.3)




              elif str(combo_string.get()) == "kilometer=>mile":




                  output_label = tb.Label(frame22, text=f"results:{round(float(choosing_number_entry.get())/1.6,2)}", font=("Helvetica", 20),)
                  output_label.place(relx=0.7, rely=0.3)




              elif str(combo_string.get()) == "inch=>meter":




                  output_label = tb.Label(frame22, text=f"results:{round(float(choosing_number_entry.get())/39.37,2)}", font=("Helvetica", 20),)
                  output_label.place(relx=0.7, rely=0.3)




              elif str(combo_string.get()) == "meter=> inch":




                  output_label = tb.Label(frame22, text=f"results:{round(float(choosing_number_entry.get())*39.37,2)}", font=("Helvetica", 20),)
                  output_label.place(relx=0.7, rely=0.3)




              elif str(combo_string.get()) == "lbs=>kg":




                  output_label = tb.Label(frame22, text=f"results:{round(float(choosing_number_entry.get())/0.45359237,2)}", font=("Helvetica", 20),)
                  output_label.place(relx=0.7, rely=0.3)




              elif str(combo_string.get()) == "kg=>lbs":




                  output_label = tb.Label(frame22, text=f"results:{round(float(choosing_number_entry.get())*0.45359237,2)}", font=("Helvetica", 20),)
                  output_label.place(relx=0.7, rely=0.3)
      frame22_func()
      def frame33_func():
          print("calculator working")
          #widgits:
          label_var = tb.StringVar()
          label_var.set("")
          calculation_label = tb.Label(frame33, font=("Helvetica", 20), textvariable = label_var)




          plus_button = tb.Button(frame33,text="+",command= lambda :(updating_labelvar_plus()) )
          minus_button = tb.Button(frame33, text="-", command=lambda:(updating_labelvar_minus()))
          multification_button = tb.Button(frame33, text="x", command=lambda:(updating_labelvar1_multy()))
          devision_button = tb.Button(frame33, text="/", command=lambda:(updating_labelvar1_devision()))
          results_button = tb.Button(frame33, text= "=", command=lambda :displaying_results())
          paint_button = tb.Button(frame33, text=".", command=lambda: updating_labelvar_paint())
          clear_button = tb.Button(frame33, text="                   \n"
                                                 "claer all >>>>     \n"
                                                 "                     ", command=lambda: updating_labelvar_clear())
          button111 = tb.Button(frame33, text="1", command=lambda:(updating_labelvar1()))
          button222 = tb.Button(frame33, text="2", command=lambda:(updating_labelvar2()))
          button333 = tb.Button(frame33, text="3", command=lambda:(updating_labelvar3()))
          button444 = tb.Button(frame33, text="4", command=lambda:(updating_labelvar4()))
          button555 = tb.Button(frame33, text="5", command=lambda:(updating_labelvar5()))
          button666 = tb.Button(frame33, text="6", command=lambda:(updating_labelvar6()))
          button777 = tb.Button(frame33, text="7", command=lambda:(updating_labelvar7()))
          button888 = tb.Button(frame33, text="8", command=lambda:(updating_labelvar8()))
          button999 = tb.Button(frame33, text="9", command=lambda:(updating_labelvar9()))
          button000 = tb.Button(frame33, text="0", command=lambda:(updating_labelvar0()))
          #layout:
          calculation_label.place(relx=0.2,rely=0.2)
          plus_button.place(relx=0.2,rely=0.4)
          minus_button.place(relx=0.26,rely=0.4)
          multification_button.place(relx=0.32,rely=0.4)
          devision_button.place(relx=0.38,rely=0.4)
          results_button.place(relx=0.32 ,rely=0.8)
          paint_button.place(relx= 0.2 ,rely=0.8)
          clear_button.place(relx=0.2, rely=0.1,)
          button111.place(relx=0.2,rely=0.5)
          button222.place(relx=0.26,rely=0.5)
          button333.place(relx=0.32,rely=0.5)
          button444.place(relx=0.2,rely=0.6)
          button555.place(relx=0.26,rely=0.6)
          button666.place(relx=0.32,rely=0.6)
          button777.place(relx=0.2,rely=0.7)
          button888.place(relx=0.26,rely=0.7)
          button999.place(relx=0.32,rely=0.7)
          button000.place(relx=0.26,rely=0.8)




          def displaying_results():
              print(f" calculation:{label_var.get()}")
              result = (eval(label_var.get()))
              label_var.set(str(result))




              results_label = tb.Label(frame33, font=("Helvetica", 30), text=(label_var.get()))
              results_label.place(relx=0.2, rely=0.3)




          def updating_labelvar1():
              courent_text = label_var.get()
              new_text = courent_text + "1"
              label_var.set(new_text)
          def updating_labelvar2():
              courent_text = label_var.get()
              new_text = courent_text + "2"
              label_var.set(new_text)
          def updating_labelvar3():
              courent_text = label_var.get()
              new_text = courent_text + "3"
              label_var.set(new_text)
          def updating_labelvar4():
              courent_text = label_var.get()
              new_text = courent_text + "4"
              label_var.set(new_text)
          def updating_labelvar5():
              courent_text = label_var.get()
              new_text = courent_text + "5"
              label_var.set(new_text)
          def updating_labelvar6():
              courent_text = label_var.get()
              new_text = courent_text + "6"
              label_var.set(new_text)
          def updating_labelvar7():
              courent_text = label_var.get()
              new_text = courent_text + "7"
              label_var.set(new_text)
          def updating_labelvar8():
              courent_text = label_var.get()
              new_text = courent_text + "8"
              label_var.set(new_text)
          def updating_labelvar9():
              courent_text = label_var.get()
              new_text = courent_text + "9"
              label_var.set(new_text)
          def updating_labelvar0():
              courent_text = label_var.get()
              new_text = courent_text + "0"
              label_var.set(new_text)
          def updating_labelvar_plus():
              courent_text = label_var.get()
              new_text = courent_text + "+"
              label_var.set(new_text)
          def updating_labelvar_minus():
              courent_text = label_var.get()
              new_text = courent_text + "-"
              label_var.set(new_text)
          def updating_labelvar1_multy():
              courent_text = label_var.get()
              new_text = courent_text + "*"
              label_var.set(new_text)
          def updating_labelvar1_devision():
              courent_text = label_var.get()
              new_text = courent_text + "/"
              label_var.set(new_text)




          def updating_labelvar_paint():
              courent_text = label_var.get()
              new_text = courent_text + "."
              label_var.set(new_text)
          def updating_labelvar_clear():
              courent_text = label_var.get()
              label_var.set("")
      frame33_func()
      def frame44_func():
          
          no_images_label= tk.Label(frame44,font=("david",30),text="no images in this galery yet")
          no_images_label.pack()








        #   # Create a Canvas inside the Frame
        #   guitar_canvas = tk.Canvas(frame44)
        #   guitar_canvas.pack(side="left", expand=1, fill="both")




        #   # Add a Scrollbar
        #   guitar_scrollbar = tb.Scrollbar(frame44, orient="vertical", command=guitar_canvas.yview)
        #   guitar_scrollbar.pack(side="right", fill="y")
        #   guitar_canvas.configure(yscrollcommand=guitar_scrollbar.set)




        #   # Create an inner Frame inside the Canvas
        #   inner_frame = tk.Frame(guitar_canvas)
        #   canvas_window = guitar_canvas.create_window((0, 0), window=inner_frame, anchor="nw")




          # Load the Image
          # List of image paths (Add as many as needed)
          # image_paths = [
          #     r"C:\Users\USER\Desktop\אפליקציה של בצלאל\thhr.jpg",
          #     r"C:\Users\USER\Desktop\אפליקציה של בצלאל\unnamed.jpg",
          #     r"C:\Users\USER\Desktop\אפליקציה של בצלאל\banjo.jpg"
          # ]
          #








          # # Store image references to prevent garbage collection
          # image_refs = []
          #
          # # Add multiple images inside inner_frame
          # for img_path in image_paths:
          #     image = Image.open(img_path).resize((600, 600), Image.Resampling.LANCZOS)
          #     image_tk = ImageTk.PhotoImage(image)
          #     image_refs.append(image_tk)  # Store reference
          #
          #     img_label = tk.Label(inner_frame, image=image_tk)
          #     img_label.pack()  # Stack images vertically




        #   image_path = r"C:\Users\בצלאל\Desktop\מחשב נייד בצלאל\לימודים\תיכנות\תמונות לתכנות\גיטרה ובנג'ו\guitar-chord-chart.png"
        #   image = Image.open(image_path).resize((600, 1000), Image.Resampling.LANCZOS)
        #   image_tk = ImageTk.PhotoImage(image)




        #   # Add the Image to the Inner Frame
        #   image_label = tk.Label(inner_frame, image=image_tk)
        #   image_label.image = image_tk  # Keep a reference
        #   image_label.pack()




        #   image_path2 = r"C:\Users\בצלאל\Desktop\מחשב נייד בצלאל\לימודים\תיכנות\תמונות לתכנות\גיטרה ובנג'ו\a-minor-pentatonic-scale-positions.webp"
        #   image2 = Image.open(image_path2).resize((580, 600), Image.Resampling.LANCZOS)
        #   image_tk = ImageTk.PhotoImage(image2)
        #   # Add the Image to the Inner Frame
        #   image_label2 = tk.Label(inner_frame, image=image_tk)
        #   image_label2.image = image_tk  # Keep a reference
        #   image_label2.pack()




        #   image_path = r"C:\Users\בצלאל\Desktop\מחשב נייד בצלאל\לימודים\תיכנות\תמונות לתכנות\גיטרה ובנג'ו\flat,750x,075,f-pad,750x1000,f8f8f8.u1.jpg"
        #   image = Image.open(image_path).resize((580, 600), Image.Resampling.LANCZOS)
        #   image_tk = ImageTk.PhotoImage(image)




        #   # Add the Image to the Inner Frame
        #   image_label2 = tk.Label(inner_frame, image=image_tk)
        #   image_label2.image = image_tk  # Keep a reference
        #   image_label2.pack()




        #   image_path = r"C:\Users\בצלאל\Desktop\מחשב נייד בצלאל\לימודים\תיכנות\תמונות לתכנות\גיטרה ובנג'ו\Fretboard_Banjo_NS.jpg"
        #   image = Image.open(image_path).resize((580, 300), Image.Resampling.LANCZOS)
        #   image_tk = ImageTk.PhotoImage(image)




        #   # Add the Image to the Inner Frame
        #   image_label = tk.Label(inner_frame, image=image_tk)
        #   image_label.image = image_tk  # Keep a reference
        #   image_label.pack()
        #   image_path = r"C:\Users\בצלאל\Desktop\מחשב נייד בצלאל\לימודים\תיכנות\תמונות לתכנות\גיטרה ובנג'ו\E-Phrygian-Dominant-sharps-letter-8.png"
        #   image = Image.open(image_path).resize((580, 300), Image.Resampling.LANCZOS)
        #   image_tk = ImageTk.PhotoImage(image)




        #   # Add the Image to the Inner Frame
        #   image_label = tk.Label(inner_frame, image=image_tk)
        #   image_label.image = image_tk  # Keep a reference
        #   image_label.pack()








    #       # Ensure the Canvas Updates Its Scroll Region
    #       def update_scroll_region(event=None):
    #           guitar_canvas.configure(scrollregion=guitar_canvas.bbox("all"))




    #       # Call update when content changes
    #       inner_frame.bind("<Configure>", update_scroll_region)




    #       # image11 = Image.open(r"C:\Users\USER\Desktop\אפליקציה של בצלאל\guitar-chord-chart.png")
    #       # image11 =image11.resize((580,1000),Image.Resampling.LANCZOS)
    #       # image11_tk = ImageTk.PhotoImage(image11)
    #       #
    #       # # image11_label = tb.Label(guitar_canvas,text="guitar chords", image= image11_tk)
    #       # # image11_label.image = image11
    #       # # image11_label.pack(expand=1 )
    #       #
    #       #
    #       # inner_frame=tk.Frame(guitar_canvas)
    #       # image11_labe = tk.Label(inner_frame,image=image11_tk)
    #       # image11_labe.pack()
    #       # canvas_window = guitar_canvas.create_window((0,0),window=inner_frame,anchor="nw" )
    #       # inner_frame.update_idletasks()
    #       # guitar_canvas.configure(scrollregion=guitar_canvas.bbox("all"))
      frame44_func()
      def frame55_func():
          
          no_images_label= tk.Label(frame55,font=("david",30),text="no images in this galery yet")
          no_images_label.pack()
      frame55_func()


    #       # Create a Canvas inside the Frame
    #       cumputer_canvas = tk.Canvas(frame55)
    #       cumputer_canvas.pack(side="left", expand=1, fill="both")




    #       # Add a Scrollbar
    #       guitar_scrollbar = tb.Scrollbar(frame55, orient="vertical", command=cumputer_canvas.yview)
    #       guitar_scrollbar.pack(side="right", fill="y")
    #       cumputer_canvas.configure(yscrollcommand=guitar_scrollbar.set)




    #       # Create an inner Frame inside the Canvas
    #       inner_frame = tk.Frame(cumputer_canvas)
    #       canvas_window = cumputer_canvas.create_window((0, 0), window=inner_frame, anchor="nw")




    #       image_path = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\guitar-chord-chart.png"
    #       image = Image.open(image_path).resize((600, 1000), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image)




    #       # Add the Image to the Inner Frame
    #       image_label = tk.Label(inner_frame, image=image_tk)
    #       image_label.image = image_tk  # Keep a reference
    #       image_label.pack()




    #       image_path2 = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\unnamed.jpg"
    #       image2 = Image.open(image_path2).resize((580, 600), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image2)
    #       # Add the Image to the Inner Frame
    #       image_label2 = tk.Label(inner_frame, image=image_tk)
    #       image_label2.image = image_tk  # Keep a reference
    #       image_label2.pack()




    #       image_path = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\flat,750x,075,f-pad,750x1000,f8f8f8.u1.jpg"
    #       image = Image.open(image_path).resize((580, 600), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image)




    #       # Add the Image to the Inner Frame
    #       image_label2 = tk.Label(inner_frame, image=image_tk)
    #       image_label2.image = image_tk  # Keep a reference
    #       image_label2.pack()




    #       image_path = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\thhr.jpg"
    #       image = Image.open(image_path).resize((580, 600), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image)




    #       # Add the Image to the Inner Frame
    #       image_label = tk.Label(inner_frame, image=image_tk)
    #       image_label.image = image_tk  # Keep a reference
    #       image_label.pack()
    #       image_path = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\banjo.jpg"
    #       image = Image.open(image_path).resize((580, 600), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image)




    #       # Add the Image to the Inner Frame
    #       image_label = tk.Label(inner_frame, image=image_tk)
    #       image_label.image = image_tk  # Keep a reference
    #       image_label.pack()








    #       # Ensure the Canvas Updates Its Scroll Region
    #       def update_scroll_region(event=None):
    #           cumputer_canvas.configure(scrollregion=cumputer_canvas.bbox("all"))




    #       # Call update when content changes
    #       inner_frame.bind("<Configure>", update_scroll_region)
                    
      def frame66_func():
          
          no_images_label= tk.Label(frame66,font=("david",30),text="no images in this galery yet")
          no_images_label.pack()



    #       # Create a Canvas inside the Frame
    #       galery_canvas = tk.Canvas(frame66)
    #       galery_canvas.pack(side="left", expand=1, fill="both")




    #       # Add a Scrollbar




    #       guitar_scrollbar = tb.Scrollbar(frame66, orient="vertical", command=galery_canvas.yview)
    #       guitar_scrollbar.pack(side="right", fill="y")
    #       galery_canvas.configure(yscrollcommand=guitar_scrollbar.set)


    #       # Create an inner Frame inside the Canvas
    #       inner_frame = tk.Frame(galery_canvas)
    #       canvas_window = galery_canvas.create_window((0, 0), window=inner_frame, anchor="nw")




    #       image_path = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\guitar-chord-chart.png"
    #       image = Image.open(image_path).resize((600, 1000), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image)




    #       # Add the Image to the Inner Frame
    #       image_label = tk.Label(inner_frame, image=image_tk)
    #       image_label.image = image_tk  # Keep a reference
    #       image_label.pack()




    #       image_path2 = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\unnamed.jpg"
    #       image2 = Image.open(image_path2).resize((580, 600), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image2)
    #       # Add the Image to the Inner Frame
    #       image_label2 = tk.Label(inner_frame, image=image_tk)
    #       image_label2.image = image_tk  # Keep a reference
    #       image_label2.pack()




    #       image_path = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\flat,750x,075,f-pad,750x1000,f8f8f8.u1.jpg"
    #       image = Image.open(image_path).resize((580, 600), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image)




    #       # Add the Image to the Inner Frame
    #       image_label2 = tk.Label(inner_frame, image=image_tk)
    #       image_label2.image = image_tk  # Keep a reference
    #       image_label2.pack()




    #       image_path = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\thhr.jpg"
    #       image = Image.open(image_path).resize((580, 600), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image)




    #       # Add the Image to the Inner Frame
    #       image_label = tk.Label(inner_frame, image=image_tk)
    #       image_label.image = image_tk  # Keep a reference
    #       image_label.pack()
    #       image_path = r"C:\Users\USER\Desktop\אפליקציה של בצלאל\banjo.jpg"
    #       image = Image.open(image_path).resize((580, 600), Image.Resampling.LANCZOS)
    #       image_tk = ImageTk.PhotoImage(image)




    #       # Add the Image to the Inner Frame
    #       image_label = tk.Label(inner_frame, image=image_tk)
    #       image_label.image = image_tk  # Keep a reference
    #       image_label.pack()








    #       # Ensure the Canvas Updates Its Scroll Region
    #       def update_scroll_region(event=None):
    #           galery_canvas.configure(scrollregion=galery_canvas.bbox("all"))




    #       # Call update when content changes
    #       inner_frame.bind("<Configure>", update_scroll_region)
      frame66_func()


      def app1(self):
          print("app1 opennesd- american test")
          messagebox.showinfo('atention!', 'we open your requst on a new window:\n'
                                           '\n"the setings you set in the main window will be displayed in this window automaticly'
                                           '\n so you can work with multypull windows simultiniously\n האפליציה: מבחן אמריקאי' 
                                           )
          def create_extra_window_1():
              print("extra window1 working")
              extra_window_1 = tk.Toplevel()
              extra_window_1.title('app1')
              extra_window_1.geometry('900x500')
              extra_window_1label = tk.Label(extra_window_1, text= " welcome to app 1- american test!")
              extra_window_1label.pack()








              test_notebook= tb.Notebook(extra_window_1)
              frame1= tb.Frame(test_notebook)
              frame1.pack(side="left",anchor= 'n')
              label1= tb.Label(frame1, text="first version\n"
                                            "radio buttons")
              label1.pack(side="left",anchor= 'n')




              frame2 = tb.Frame(test_notebook)
              frame2.pack(side="left",anchor= 'n')
              label2 = tb.Label(frame2, text="second version\n"
                                             "combobox")
              label2.pack(side="left",anchor= 'n')




              test_notebook.add(frame1, text="frame 1")
              test_notebook.add(frame2, text="frame 2")
              test_notebook.pack(side="left",anchor= 'n')








              def american_test_radio_buttons():




                  # make it scrolable(canvas?)
                  # radio buttons
                  # score
                  final_score = 0




                  print("welcome to trivia by bezalel achoonov!")
                  print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
                  questions = ("what is a watermelon?",
                               "what is the meaning of life?",
                               "what is bezalels fevorit video game?",
                               "what is bezalels favorit color?",
                               "what is bezalel favorit type of music?")
                  options_for_qustions = {
                      1: ["a- avegteble", "b- a fruit", "c- mcdonalds prodact", "d- its ashwarma"],
                      2: ["a- to be ultra orthodox", "b-to be a crestin ", "c- to eat mcdonalds",
                          "d- 42"],
                      3: ["a- kurshi ps1", "b- final fantasy 7", "c - far cry 3",
                          "d- clash of clans "],
                      4: ["a - pink", "b - blue", "c- black (what a dark soul...)",
                          "d- all colors are expted"],
                      5: [
                               "a -שירי ארץ ישראל", "b - גולן (אייל גולן)", "c - country ",
                          "d - psychadelic rock"]}
                  answers = ("a", "d", "b", "c", "c")
                  optional_answers = ("a", "b", "c", "d",)




                  option_indexing = 1
                  question_indexing = 0
                  list_indexing = []




                  radios_strigvar1 = tb.StringVar()
                  radios_strigvar2 = tb.StringVar()
                  radios_strigvar3 = tb.StringVar()
                  radios_strigvar4 = tb.StringVar()
                  radios_strigvar5 = tb.StringVar()




                  qustion_1_label = tb.Label(frame1,text=f"{questions[0]}")
                  qustion_1_label.pack()
                  if len(list_indexing) == 0:




                      for option in options_for_qustions[question_indexing + 1]:
                          options_for1 = tb.Radiobutton(frame1,text=f"{option}", value=str(len(list_indexing)),
                                                        variable=radios_strigvar1)
                          options_for1.pack()
                          list_indexing.append(+1)
                          print(list_indexing)
                      if len(list_indexing) == 4:
                          print("222222222222")
                          qustion_2_label = tb.Label(frame1,text=f"{questions[1]}")
                          qustion_2_label.pack()




                          for option in options_for_qustions[question_indexing + 2]:
                              options_for2 = tb.Radiobutton(frame1,text=f"{option}",
                                                            value=str(len(list_indexing)),
                                                            variable=radios_strigvar2)
                              options_for2.pack()




                              list_indexing.append(+1)
                              print(list_indexing)
                              if len(list_indexing) == 8:
                                  print("33333333333333333")
                                  qustion_3_label = tb.Label(frame1,text=f"{questions[2]}")
                                  qustion_3_label.pack()




                                  for option in options_for_qustions[question_indexing + 3]:
                                      options_for3 = tb.Radiobutton(frame1,text=f"{option}",
                                                                    value=str(len(list_indexing)),
                                                                    variable=radios_strigvar3)
                                      options_for3.pack()




                                      list_indexing.append(+1)
                                      print(list_indexing)




                                      if len(list_indexing) == 12:
                                          print("44444444444444")
                                          qustion_4_label = tb.Label(frame1,text=f"{questions[3]}")
                                          qustion_4_label.pack()




                                          for option in options_for_qustions[question_indexing + 4]:
                                              options_for4 = tb.Radiobutton(frame1,text=f"{option}",
                                                                            value=str(
                                                                                len(list_indexing)),
                                                                            variable=radios_strigvar4)
                                              options_for4.pack()




                                              list_indexing.append(+1)
                                              print(list_indexing)




                                              if len(list_indexing) == 16:
                                                  print("33333333333333333")
                                                  qustion_5_label = tb.Label(frame1,text=f"{questions[4]}")
                                                  qustion_5_label.pack()




                                                  for option in options_for_qustions[question_indexing + 5]:
                                                      options_for5 = tb.Radiobutton(frame1,text=f"{option}",
                                                                                    value=str(
                                                                                        len(list_indexing)),
                                                                                    variable=radios_strigvar5)
                                                      options_for5.pack()




                                                      list_indexing.append(+1)
                                                      print(list_indexing)




                  send_answers_button = tb.Button(frame1,text="send answers", command=lambda: sending_answers())
                  send_answers_button.pack()




                  def sending_answers():
                      final_score = 0
                      if str(radios_strigvar1.get()) == "0":
                          final_score += 20




                      if str(radios_strigvar2.get()) == "7":
                          final_score += 20
                      if str(radios_strigvar3.get()) == "9":
                          final_score += 20




                      if str(radios_strigvar4.get()) == "14":
                          final_score += 20
                      if str(radios_strigvar5.get()) == "18":
                          final_score += 20




                      final_score_label = tb.Label(frame1,text=f"your final score is:{final_score}/100")
                      final_score_label.pack()
              american_test_radio_buttons()
              def american_test_combobox():




                  print("welcome to trivia by bezalel achoonov!")
                  print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
                  questions = ("what is a watermelon?",
                               "what is the meaning of life?",
                               "what is bezalels fevorit video game?",
                               "what is bezalels favorit color?",
                               "what is bezalel favorit type of music?")
                  options_for_qustions  = {
                      1: ["a- avegteble", "b- a fruit", "c- mcdonalds prodact", "d- its ashwarma"],
                      2: ["a- to be ultra orthodox", "b-to be a crestin ", "c- to eat mcdonalds",
                          "d- 42"],
                      3: ["a- kurshi ps1", "b- final fantasy 7", "c - far cry 3",
                          "d- clash of clans "],
                      4: ["a - pink", "b - blue", "c- black (what a dark soul...)",
                          "d- all colors are expted"],
                      5: [
                          "a -שירי ארץ ישראל", "b - גולן (אייל גולן)", "c - country ",
                          "d - psychadelic rock"]}
                  answers = ("a", "d", "b", "c", "c")
                  correct_answers = {
                      1:"a- avegteble",
                      2:"d- 42",
                      3:"b- final fantasy 7",
                      4:"c- black (what a dark soul...)",
                      5:"c - country "
                  }


                  optional_answers = ("a", "b", "c", "d",)


                  combobox_list = []  # Store combobox widgets


                  indexing_num = 1
                  for question in questions:
                      asking = tb.Label(frame2, text=question)
                      asking.pack()


                      combo_var = tb.StringVar()  # Variable to store selected answer
                      combo_option = tb.Combobox(frame2, textvariable=combo_var,
                                                 values= options_for_qustions[indexing_num], state="readonly")
                      combo_option.pack()
                      combobox_list.append((indexing_num, combo_var))  # Store index and variable


                      indexing_num += 1


                  def checking_answers_func():
                      correct_count = 0
                      for index, combo_var in combobox_list:
                          user_answer = combo_var.get()
                          correct_answer = correct_answers[index]
                          if user_answer == correct_answer:
                              correct_count += 1


                      result_label.config(text=f"Correct Answers: {correct_count} / {len(questions)}")


                  sending_answers_button = tb.Button(frame2, text="Send Answers", command=checking_answers_func,
                                                     bootstyle="success")
                  sending_answers_button.pack()


                  result_label = tb.Label(frame2, text="Correct Answers: 0 / 0", bootstyle="inverse-primary")
                  result_label.pack()


              american_test_combobox()






          create_extra_window_1()
      def app2(self):
          print("app2 openned- paint")




          messagebox.showinfo('atention!', 'we open your requst on a new window:\n'
                                           '\n"the setings you set in the main window will be displayed in this window automaticly'
                                           ' '
                                           '\n so you can work with multypull windows simultiniously\n '
                                           '\nהאפליקציה:צייר. על ידי גלילה ניתן להגדיר גודל מברשת')
          def create_extra_window_2():
              print("extra window1 working")
              extra_window_2 = tk.Toplevel()
              extra_window_2.title('app2- paint')
              extra_window_2.geometry('900x500')




              extra_window_2label = tb.Label(extra_window_2, text= " welcome to app 2!")
              extra_window_2label.pack()




              canvas_frame = tk.Button(extra_window_2 ,)#text="תוכל לצייר\n לשרטט או לחתום \nכאן. הטקסט יעלם \nכשתעמוד על \nהשוליים\nכמו כן \nגלילה תקטין \nאו תגדיל את\n גודל המברשת"
              # "\n"
              #"you can wright, design or paint right here without pressing on the mouse.\n"
              #"#your text will disapear if you getting close to borders ")




              canvas_frame.pack(side= 'right',ipadx=450, ipady=200, )
              canvas= tb.Canvas(canvas_frame, bg = '#e6e6e6', )
              canvas.pack(ipadx= 180, ipady=300 )




              def draw_on_canvas(event):
                  x = event.x
                  y = event.y
                  canvas.create_oval((x - brush_size/2, y- brush_size/2, x+brush_size/2, y+brush_size/2), fill= 'black')
              def brush_size_adjust(event):
                  global brush_size
                  if event.delta >0:
                      brush_size+=4
                  else:
                      brush_size-=4




                  brush_size = max(0,min(brush_size,50))








              canvas.bind('<Motion>', draw_on_canvas)
              canvas.bind('<MouseWheel>', brush_size_adjust)




          create_extra_window_2()
      def app3(self):
          print("app3 openned- writer")




          messagebox.showinfo('atention!', 'we open your requst on a new window:\n'
                                           '\n"the setings you set in the main window will be displayed in this window automaticly'
                                           ' '
                                           '\n so you can work with multypull windows simultiniously\n ' \
                                           '\nהאפליקציה: כתבן')
          def create_extra_window_3():
              print("extra window3 working")
              extra_window_3 = tk.Toplevel()
              extra_window_3.title('app3')
              extra_window_3.geometry('900x500')
              extra_window_1label = tk.Label(extra_window_3, text= " welcome to app 3 - writer!")
              extra_window_1label.pack()
              text= tk.Text(extra_window_3)
              text.pack(ipadx=150, ipady=50)
              scrollbar_text = tb.Scrollbar(extra_window_3, orient= 'vertical', command= text.yview)
              text.configure(yscrollcommand= scrollbar_text.set)
              scrollbar_text.place(relx=1 ,rely=0 ,relheight=1 ,anchor= 'ne' )




          create_extra_window_3()
      def app4(self):
          print("app4 openned- sheets")




          messagebox.showinfo('atention!', 'we open your requst on a new window:\n'
                                           '\n"the setings you set in the main window will be displayed in this window automaticly'
                                           ' '
                                           '\n so you can work with multypull windows simultiniously\n ' \
                                           'האפליקציה: יצירת טבלאות רנדומלית')




          def create_extra_window_4():
              print("extra window1 working")
              extra_window_4 = tk.Toplevel()
              extra_window_4.title('app1')
              extra_window_4.geometry('900x500')
              extra_window_1label = tk.Label(extra_window_4, text= " welcome to app 4!")
              extra_window_1label.pack()
              table = tb.Treeview(extra_window_4, columns = (1,2,3,4,5) ,show= 'headings')
              table.heading(1, text=" first name")
              table.heading(2, text=" last name")
              table.heading(3, text=" army job")
              table.heading(4, text=" age")
              table.heading(5, text=" job")
              first_names= ["bezalel", "moses", "john", "michel"," bibi",]
              last_names= ["achoonov", "yashar", "dutton", "jackson", "netanyahu"]
              army_job = ["ג'ובניק","הסדר",'הנחל החרדי',"סיירת נחל","סיירת מטכל"]
              ages = ["24","23","54","22", "10"]
              jobs = ["אברך","הייטקיסט","ראפר","זמר","מנקה רחובות"]




              for i in range (100):
                  table.insert(parent='',index= tk.END, values=(choice(first_names),choice(last_names),choice(army_job),choice(ages),choice(jobs)))
              table.pack(expand=1, fill="both")




              scrollbar_table = tb.Scrollbar(extra_window_4, orient='vertical', command= table.yview)
              table.configure(yscrollcommand=scrollbar_table.set)
              scrollbar_table.place(relx=1, rely=0, relheight=1, anchor= 'ne')












          create_extra_window_4()
      def game1(self):
          print("game1 openned -hangman")




          messagebox.showinfo('atention!', 'we open your requst on a new window:\n'
                                           '\n"the setings you set in the main window will be displayed in this window automaticly'
                                           ' '
                                           '\n so you can work with multypull windows simultiniously\n ' \
                                           'המשחק: איש תלוי') 
          def create_extra_window_5():
              print("extra window1 working")
              extra_window_5 = tk.Toplevel()
              extra_window_5.title('game 1 ')
              extra_window_5.geometry('900x500')
              extra_window_5label = tk.Label(extra_window_5, text= " welcome to game1!")
              extra_window_5label.pack()




              def playing_hangman_on_app():


                  extra_window_5.entring_a_letter_gues_entry = tb.Entry(extra_window_5, )
                  extra_window_5.sending_letter_button = tb.Button(extra_window_5, text=" submit gues!",
                                                                   command=lambda: playing_hangmangame_running())
                  extra_window_5.displaying_hints_label = tb.Label(extra_window_5, text=" hints will be shown right here")
                  extra_window_5.output_hangman_label = tb.Label(extra_window_5, text=" welcome to hangman game!\n"
                                                                                      "output will be shown here")
                  extra_window_5.displaying_our_man_label = tb.Label(extra_window_5,text=" our man will be shown here")
                  extra_window_5.to_nuch_letters_label = tb.Label(extra_window_5, text="*********")
                  extra_window_5.checking_input_label = tb.Label(extra_window_5, text=" check")


                  # layout
                  extra_window_5.checking_input_label.place(relx=0.2, rely=0.87)
                  extra_window_5.to_nuch_letters_label.place(relx=0.5, rely=0.7)
                  extra_window_5.entring_a_letter_gues_entry.place(relx=0.5, rely=0.5)
                  extra_window_5.sending_letter_button.place(relx=0.62, rely=0.5)
                  extra_window_5.displaying_hints_label.place(relx=0.5, rely=0.65)
                  extra_window_5.output_hangman_label.place(relx=0.5, rely=0.3)
                  extra_window_5.displaying_our_man_label.place(relx=0.2, rely=0.3)


                  def playing_hangmangame_running():




                      displaying = {0: (""
                                        ""
                                        ""),
                                    1: (" o "
                                        "   "
                                        "   "),
                                    2: (" o "
                                        " | "
                                        "   "),
                                    3: (" o "
                                        "/| "
                                        "   "),
                                    4: (" o "
                                        "/|\\"
                                        "   "),
                                    5: (" o "
                                        "/|\\"
                                        "/  "),
                                    6: (" o "
                                        "/|\\"
                                        "/ \\")}


                      def exibittind_hangman(self):
                          global displaying


                          for x in displaying[faild_gusses]:
                              print(x)
                              print(displaying.get(faild_gusses, "image availble"))
                              return displaying.get(faild_gusses, "image availble")


                      def main1():
                          global exibittind_hangman
                          global displaying


                          playing_again  = True
                          if playing_again:
                              global faild_gusses
                              print("--😀😀😀😀😀🌌🌌🌌🌌🌌😀😀😀😀😀---")
                              print("welcome to hangman by bezalel achoonov!")
                              print("-😀😀😀😀😀🌎🌎🌎🌏🌏🌏🌏😀😀😀😀😀-")


                              runinng_hangman = True
                              if runinng_hangman:


                                  print(hints)
                                  extra_window_5.displaying_hints_label.place_forget()
                                  extra_window_5.displaying_hints_label = tb.Label(extra_window_5,text=f"hints: {hints}")
                                  extra_window_5.displaying_hints_label.place(relx=0.5, rely=0.65)


                                  gues_hangman = str(extra_window_5.entring_a_letter_gues_entry.get()).lower()


                                  extra_window_5.checking_input_label.place_forget()
                                  extra_window_5.checking_input_label = tb.Label(extra_window_5,text=f"your gues is: _'{ str(extra_window_5.entring_a_letter_gues_entry.get()).lower()}'_")
                                  extra_window_5.checking_input_label.place(relx=0.2, rely=0.87)
                                  #
                                  # gues_hangman = input("enter your gues(must be 1 letter)")
                                  # if len(gues_hangman) > 1:
                                  #     print("must be only one letter!")
                                  #     gues_hangman = input("enter your gues(must be 1 letter)")
                                  # while not gues_hangman.isalpha():
                                  #     print("numbers are invalid in this progrom")
                                  #     gues_hangman = input("enter your gues(must be 1 letter)")
                                  # print(f"your gues is {gues_hangman}")


                                  if len(str(extra_window_5.entring_a_letter_gues_entry.get())) > 1:
                                      print("must be only one letter!")
                                      extra_window_5.to_nuch_letters_label.place_forget()
                                      extra_window_5.to_nuch_letters_label = tb.Label(extra_window_5,text="must be only one letter!")
                                      extra_window_5.to_nuch_letters_label.place(relx=0.5, rely=0.7)
                                      gues_hangman = str(extra_window_5.entring_a_letter_gues_entry.get()).lower()


                                  if  str(extra_window_5.entring_a_letter_gues_entry.get()).lower() in word_chosen:
                                      print(f"{ str(extra_window_5.entring_a_letter_gues_entry.get()).lower()} was found in this word!")


                                      extra_window_5.output_hangman_label.place_forget()
                                      extra_window_5.output_hangman_label = tb.Label(extra_window_5,
                                                                                     text=f"{ str(extra_window_5.entring_a_letter_gues_entry.get()).lower()} was found in this word!")
                                      extra_window_5.output_hangman_label.place(relx=0.5, rely=0.3)


                                      for letter in range(len(hints)):


                                          if str(extra_window_5.entring_a_letter_gues_entry.get()).lower() == word_chosen[letter]:


                                              hints[letter] = str(extra_window_5.entring_a_letter_gues_entry.get()).lower()
                                              extra_window_5.displaying_hints_label.place_forget()
                                              extra_window_5.displaying_hints_label = tb.Label(extra_window_5,text=f"hints: {hints}")
                                              extra_window_5.displaying_hints_label.place(relx=0.5, rely=0.65)


                                          # if gues_hangman == word_chosen[letter]:
                                          #     hints[letter] = gues_hangman






                                  else:
                                      global faild_gusses
                                      faild_gusses += 1
                                      print("######################")
                                      exibittind_hangman()
                                      print("######################")


                                      print("letter was not found in this word!")


                                      extra_window_5.displaying_our_man_label.place_forget()
                                      extra_window_5.displaying_our_man_label = tb.Label(extra_window_5,text=f"{exibittind_hangman()}")
                                      extra_window_5.displaying_our_man_label.place(relx=0.2, rely=0.3)


                                      extra_window_5.output_hangman_label.place_forget()
                                      extra_window_5.output_hangman_label = tb.Label(extra_window_5,
                                                                                     text=f"letter was not found in this word!")
                                      extra_window_5.output_hangman_label.place(relx=0.5, rely=0.3)


                                  if "_" not in hints:
                                      print("----------")
                                      print("you won!!!")
                                      print("----------")
                                      runinng_hangman = False


                                      extra_window_5.output_hangman_label.place_forget()
                                      extra_window_5.output_hangman_label = tb.Label(extra_window_5,text=f"you won!!!")
                                      extra_window_5.output_hangman_label.place(relx=0.5, rely=0.3)
                                      #
                                      # play_againn = input(
                                      #     "do you want to play again?(n- to exit, any other key to continue) ")
                                      # if play_againn == "n":
                                      playing_again = False
                                  if faild_gusses == 6:
                                      print("--------------------------------")
                                      print(" to much faild gusses! you lose!")
                                      print("--------------------------------")


                                      extra_window_5.output_hangman_label.place_forget()
                                      extra_window_5.output_hangman_label = tb.Label(extra_window_5,
                                                                                     text=f" to much faild gusses! you lose!")
                                      extra_window_5.output_hangman_label.place(relx=0.5, rely=0.3)


                                      runinng_hangman = False


                                      playing_again = False


                                      # play_againn = input(
                                      #     "do you want to play again?(n- to exit, any other key to continue) ")
                                  # if play_againn == "n":
                                  #         playing_again = False


                              print("////////////////////////////////////////////////")
                              print("thank you for playing hangman by bezalel ahoonov!")
                              print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                              if faild_gusses in displaying:
                                  print(displaying[faild_gusses])
                              else:
                                  print(f"key{faild_gusses}not found in displayng")


                      main1()
              playing_hangman_on_app()
          create_extra_window_5()
      def game2(self):
          print("rps")




          messagebox.showinfo('atention!', 'we open your requst on a new window:\n'
                                           '\n"the setings you set in the main window will be displayed in this window automaticly'
                                           ' '
                                           '\n so you can work with multypull windows simultiniously\n '
                                           'המשחק: אבן נייר ומספריים')




          def create_extra_window_6():
              print("extra window1 working")


              extra_window_6  = tk.Toplevel()
              extra_window_6.title('game 2')
              (extra_window_6.geometry('900x500'))
              extra_window_6label = tk.Label(extra_window_6, text= " welcome to game2!")
              extra_window_6label.pack()
              # stringvars:
              results_label_stringvar = tb.StringVar(extra_window_6)
              # widgits:
              extra_window_6.entering_choice_entry = tb.Entry(extra_window_6, )
              extra_window_6.entering_choice_label = tb.Label(extra_window_6, text="enter a choice:  rock / paper / scissors")
              extra_window_6.sending_choice_button = tb.Button(extra_window_6, text="submit!!!///!!!שלח", command=lambda: playng_rps_running())
              extra_window_6.results_label = tb.Label(extra_window_6, text="text will be shown here")
              extra_window_6.results_label_another_new= tb.Label(extra_window_6,text="its now:\n"
                                                                                     "0 for you \n"
                                                                                     "0 for the computer")


              # layout:
              extra_window_6.results_label_another_new.place(relx=0.5, rely=0.3)


              extra_window_6.results_label.place(relx=0.5, rely=0.6)
              extra_window_6.entering_choice_entry.place(relx=0.5, rely=0.8)
              extra_window_6.entering_choice_label.place(relx=0.5, rely=0.72)
              extra_window_6.sending_choice_button.place(relx=0.85, rely=0.72)


              def playng_rps_running():
                  print("rps workinggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
                  options = ("rock",
                             "paper",
                             "scissors")
                  playing_rps = True
                  if playing_rps:
                      extra_window_6.results_label.place_forget()
                      player_choice = extra_window_6.entering_choice_entry.get()
                      python_choice = random.choice(options)
                      if player_choice not in options:
                          print("must be one of the next options:")
                      else:
                          print(f"you chose:{player_choice}")
                          print(f"the computer chose:{python_choice}")


                          if python_choice == player_choice:
                              print('its a tie game!')
                              extra_window_6.results_label.place_forget()
                              extra_window_6.results_label = tb.Label(extra_window_6,
                                                                      text=f"you chose:  {player_choice}    \n"
                                                                           f"the computer chose:  {python_choice}\n its a tie game!!")
                              extra_window_6.results_label.place(relx=0.5, rely=0.45)
                              extra_window_6.results_label_another_new.place_forget()
                              extra_window_6.results_label_another_new = tb.Label(extra_window_6,text=(f"its now: {sum(conting_results_player)} for you \n {sum(conting_results_python)} for the computer!"))


                              extra_window_6.results_label_another_new.place(relx=0.5, rely=0.3)


                          elif python_choice == "rock" and player_choice == "scissors":
                              print("you lose!")
                              conting_results_python.append(1)
                              extra_window_6.results_label.place_forget()
                              extra_window_6.results_label = tb.Label(extra_window_6,
                                                                      text=f"you chose:  {player_choice}    \n"
                                                                           f"the computer chose:  {python_choice}\n you lose!!!!!!")
                              extra_window_6.results_label.place(relx=0.5, rely=0.45)
                              extra_window_6.results_label_another_new.place_forget()
                              extra_window_6.results_label_another_new = tb.Label(extra_window_6,text=(f"its now: {sum(conting_results_player)} for you \n {sum(conting_results_python)} for the computer!"))


                              extra_window_6.results_label_another_new.place(relx=0.5, rely=0.3)




                          elif python_choice == "paper" and player_choice == "rock":
                              print("you lose!")
                              conting_results_python.append(1)
                              extra_window_6.results_label.place_forget()
                              extra_window_6.results_label = tb.Label(extra_window_6,
                                                                      text=f"you chose:  {player_choice}    \n"
                                                                           f"the computer chose:  {python_choice}\n you lose!!!!!!")
                              extra_window_6.results_label.place(relx=0.5, rely=0.45)
                              extra_window_6.results_label_another_new.place_forget()
                              extra_window_6.results_label_another_new = tb.Label(extra_window_6,text=(f"its now: {sum(conting_results_player)} for you \n {sum(conting_results_python)} for the computer!"))


                              extra_window_6.results_label_another_new.place(relx=0.5, rely=0.3)




                          elif python_choice == "scissors" and player_choice == "paper":
                              print("you lose!")
                              conting_results_python.append(1)
                              extra_window_6.results_label.place_forget()
                              extra_window_6.results_label = tb.Label(extra_window_6,
                                                                      text=f"you chose:  {player_choice}    \n"
                                                                           f"the computer chose:  {python_choice}\n you lose!!!!!!")
                              extra_window_6.results_label.place(relx=0.5, rely=0.6)
                              extra_window_6.results_label_another_new.place_forget()
                              extra_window_6.results_label_another_new = tb.Label(extra_window_6,text=(f"its now: {sum(conting_results_player)} for you \n {sum(conting_results_python)} for the computer!"))


                              extra_window_6.results_label_another_new.place(relx=0.5, rely=0.3)


                          else:
                              print("you winnnnnnnnnnnnnnn!!!!!!!!!!")
                              conting_results_player.append(1)
                              extra_window_6.results_label.place_forget()
                              extra_window_6.results_label = tb.Label(extra_window_6,
                                                                      text=f"you chose:          {player_choice}\nthe computer chose:       {python_choice}\n you winnn!!!!!!")
                              extra_window_6.results_label.place(relx=0.5, rely=0.6)
                              print(
                                  f"its now: {sum(conting_results_player)} for you //// {sum(conting_results_python)} for the computer!")
                              extra_window_6.results_label_another_new.place_forget()
                              extra_window_6.results_label_another_new = tb.Label(extra_window_6,
                                                                                  text=(
                                                                                      f"its now: {sum(conting_results_player)} for you \n {sum(conting_results_python)} for the computer!"))
                          extra_window_6.results_label_another_new.place(relx=0.5, rely=0.3)


                      playing_rps = False
          create_extra_window_6()
      def game3(self):
          print("game3 openned- gussing number")








          messagebox.showinfo('atention!', 'we open your requst on a new window:\n'
                                           '\n"the setings you set in the main window will be displayed in this window automaticly'
                                           ' '
                                           '\n so you can work with multypull windows simultiniously\n '
                                           'המשחק: מכונת הימורים. יש להכניס סכום להימור ולסובב. \nזוכים כאשר מקבלים שלושה בשורה. ניתן לפרוש כשרוצים')




          def create_extra_window_7():
              print("extra window7 working")
              extra_window_7 = tk.Toplevel()
              extra_window_7.title('game 3')
              extra_window_7.geometry('900x500')
              extra_window_7label = tk.Label(extra_window_7, text= " welcome to app 7!")
              extra_window_7label.pack()


              def playing_slotmachine_on_app():
                  # widgits:


                  extra_window_7.output_slotmachine_label = tb.Label(extra_window_7, text="slotmachine text will be shown here!")
                  extra_window_7.spinning_button = tb.Button(extra_window_7, text="spin now!", command=lambda: (time.sleep(1),
                                                                                                                     playing_slotmachine_running()))
                  extra_window_7.balance_slotmachine_lable = tb.Label(extra_window_7, text=f"your starting balance is 200")
                  extra_window_7.entering_a_bett_entry = tb.Entry(extra_window_7, )
                  extra_window_7.winning_animation_label = tb.Label(extra_window_7,text="------------")
                  extra_window_7.exit_label = (tb.Label(extra_window_7,
                                                             text=f"thank you for playing slotmachine spinning gambeling by bezalel achoonov!!!!!!!\n"
                                                                  f"(this app do not souport gambeling. dont try it at home. or enywhere else.)\n"
                                                                  f"have a nice day!"))


                  extra_window_7.exit_button = tb.Button(extra_window_7, text="exit",
                                                              command=lambda: (extra_window_7.entering_a_bett_entry.place_forget(),
                                                                               extra_window_7.exit_label.place(relx=0.2, rely=0.2)))
                  extra_window_7.spinning_animation_label = tb.Label(extra_window_7, text=" simbols- [  ],[  ],[  ]")
                  extra_window_7.rewards_label = tb.Label(extra_window_7, text="/////////////")
                  # layout
                  extra_window_7.rewards_label.place(relx=0.5, rely=0.65)
                  extra_window_7.winning_animation_label.place(relx=0.5, rely=0.6)
                  extra_window_7.balance_slotmachine_lable.place(relx=0.5, rely=0.5)
                  extra_window_7.spinning_button.place(relx=0.84, rely=0.5)
                  extra_window_7.output_slotmachine_label.place(relx=0.5, rely=0.7)
                  extra_window_7.entering_a_bett_entry.place(relx=0.7, rely=0.5)
                  extra_window_7.exit_button.place(relx=0.5, rely=0.3, )
                  extra_window_7.spinning_animation_label.place(relx=0.5, rely=0.8)
                  def playing_slotmachine_running():
                      # functionality:
                      running_spinnmachine = True
                      def spinning():
                          global cb


                          symbolls_list = []


                          optional_symbolls = ("🍕", "🥩", "🥕", "🍄")
                          for symboll in range(3):
                              symboll = random.choice(optional_symbolls)
                              symbolls_list.append(symboll)


                          extra_window_7.spinning_animation_label.place_forget()
                          extra_window_7.spinning_animation_label = tb.Label(extra_window_7,text=f"/////////////////////\n"
                                                                                  f"//machine results://\n"
                                                                                  f"///{symbolls_list}///\n"
                                                                                  f"/////////////////////")
                          extra_window_7.spinning_animation_label.place(relx=0.5, rely=0.8)


                          if symbolls_list[0] == symbolls_list[1] and symbolls_list[0] == symbolls_list[2]:
                              global cb


                              print("you got 3 in a row!")
                              print("🤑🤑🤑🤑🤑🤑🤑🤑")
                              extra_window_7.winning_animation_label.place_forget()
                              extra_window_7.winning_animation_label = tb.Label(extra_window_7,text="you got 3 in a row!\n"
                                                                                     "🤑🤑🤑🤑🤑🤑🤑🤑")
                              extra_window_7.winning_animation_label.place(relx=0.5, rely=0.5)


                              if symbolls_list[0] == "🍕":
                                  cb += 20 * courent_betting
                                  extra_window_7.rewards_label.place_forget()
                                  extra_window_7.rewards_label = tb.Label(extra_window_7,
                                      text=f"you won {int(extra_window_7.entering_a_bett_entry.get()) * 20}$\n"
                                           f"your balance after rewards:{cb}")
                                  extra_window_7.rewards_label.place(relx=0.5, rely=0.65)
                              elif symbolls_list[0] == "🥩":
                                  cb += 30 * courent_betting


                                  extra_window_7.rewards_label.place_forget()
                                  extra_window_7.rewards_label = tb.Label(extra_window_7,
                                      text=f"you won {int(extra_window_7.entering_a_bett_entry.get()) * 30}$\n"
                                           f"your balance after rewards:{cb}")
                                  extra_window_7.rewards_label.place(relx=0.5, rely=0.65)


                              elif symbolls_list[0] == "🥕":
                                  cb += 40 * courent_betting


                                  extra_window_7.rewards_label.place_forget()
                                  extra_window_7.rewards_label = tb.Label(extra_window_7,
                                      text=f"you won {int(extra_window_7.entering_a_bett_entry.get()) * 40}$\n"
                                           f"your balance after rewards:{cb}")
                                  extra_window_7.rewards_label.place(relx=0.5, rely=0.65)
                              elif symbolls_list[0] == "🍄":
                                  cb += 100 * courent_betting


                                  extra_window_7.rewards_label.place_forget()
                                  extra_window_7.rewards_label = tb.Label(extra_window_7,
                                      text=f"you won {int(extra_window_7.entering_a_bett_entry.get()) * 100}$"
                                           f"your balance after rewards:{cb}")
                                  extra_window_7.rewards_label.place(relx=0.5, rely=0.65)
                          return print(symbolls_list)


                      print("welcome to gambeling spinnning machin by bezalel achoonov!")


                      if running_spinnmachine:
                          extra_window_7.output_slotmachine_label.place_forget()
                          extra_window_7.balance_slotmachine_lable.place_forget()


                          global cb
                          if cb == 0:
                              extra_window_7.winning_animation_label.place_forget()
                              extra_window_7.output_slotmachine_label.place_forget()
                              extra_window_7.output_slotmachine_label = tb.Label(extra_window_7,text="///////////////////////\n"
                                                                                      "your money is over!!!!!\n"
                                                                                      "you lose 200$ dolars\n"
                                                                                      "///////////////////////")
                              extra_window_7.output_slotmachine_label.place(relx=0.5, rely=0.7)
                              print("/////////////////////////")
                              print("your mony is over!!!!!!!!")
                              print("you lose 200$ dolars")
                              print("/////////////////////////")
                              running_spinnmachine = False
                          else:
                              courent_betting = int(extra_window_7.entering_a_bett_entry.get())
                              extra_window_7.balance_slotmachine_lable.place_forget()
                              extra_window_7.balance_slotmachine_lable = tb.Label(extra_window_7,
                                  text=f"your balnce is {cb - courent_betting}")
                              extra_window_7.balance_slotmachine_lable.place(relx=0.5, rely=0.5)
                              print(f"your balnce is {cb}")


                              if courent_betting > cb:
                                  print("you dont have enugh money!")


                                  extra_window_7.output_slotmachine_label.place_forget()
                                  extra_window_7.output_slotmachine_label = tb.Label(extra_window_7,
                                      text="//////////////////////////\n"
                                           "you dont have enugh money!\n"
                                           "//////////////////////////")
                                  extra_window_7.output_slotmachine_label.place(relx=0.5, rely=0.7)


                              else:
                                  cb -= courent_betting
                                  print("wwwwwwwwwwwwwwww")
                                  print("your results is:")
                                  print("wwwwwwwwwwwwwwww")
                                  spinning()


                                  running_spinnmachine = False
              playing_slotmachine_on_app()
          create_extra_window_7()
      def game4(self):
          print("game4 openned- hangman")








          messagebox.showinfo('atention!', 'we open your requst on a new window:\n'
                                           '\n"the setings you set in the main window will be displayed in this window automaticly'
                                           ' '
                                           '\n so you can work with multypull windows simultiniously\n '
                                           'המשחק: ניחוש מספר.\n'
                                           'יש להציב למחשב מספר גבוהה ומספר נמוך ולנחש מספר ביניהם')
          def create_extra_window_8():
              print("extra window8 working")
              extra_window_8 = tk.Toplevel()
              extra_window_8.title('game4')
              extra_window_8.geometry('900x500')
              extra_window_8label = tk.Label(extra_window_8, text= " welcome to app 8!")
              extra_window_8label.pack()


              def playing_gussing_numbers_on_app():
                  extra_window_8.scale_strigvar = tb.IntVar(extra_window_8, )
                  extra_window_8.displaying_output_scale_label = tb.Label(extra_window_8, text="scale:")
                  extra_window_8.entering_low_number_entry = tb.Entry(extra_window_8, )
                  extra_window_8.entering_high_number_entry = tb.Entry(extra_window_8)
                  extra_window_8.sending_entering_low_high_button = tb.Button(extra_window_8, text="enter here low number\n\n\n\n"
                                                                                "enter here high number",
                                                                     command=lambda: playing_gussingnum_running())
                  extra_window_8.signaling_high_low_label = tb.Label(extra_window_8, text="high/low output will be shown here")
                  extra_window_8.list_of_guesed_nums = tb.Label(extra_window_8, text=" guessed numbers will be shown here")
                  extra_window_8.scale_guesing_slider = tb.Scale(extra_window_8, from_=0, to=30, variable=extra_window_8.scale_strigvar, length=400)
                  extra_window_8.sending_answer_button = tb.Button(extra_window_8, text=" choose your answer and submit here",
                                                          command=lambda: playing_gussingnum_running())
                  extra_window_8.number_of_guesses_for_nums_label = tb.Label(extra_window_8, text="you guesed 0 times alredy")
                  extra_window_8.winning_and_displaying_number_label = tb.Label(extra_window_8, text="//////////////////")


                  # layout


                  extra_window_8.entering_low_number_entry.place(relx=0.5, rely=0.4)
                  extra_window_8.entering_high_number_entry.place(relx=0.5, rely=0.5)
                  extra_window_8.sending_entering_low_high_button.place(relx=0.65, rely=0.4)
                  extra_window_8.signaling_high_low_label.place(relx=0.5, rely=0.7)
                  extra_window_8.list_of_guesed_nums.place(relx=0.2, rely=0.3)
                  extra_window_8.scale_guesing_slider.place(relx=0.5, rely=0.6)
                  extra_window_8.sending_answer_button.place(relx=0.65, rely=0.65)
                  extra_window_8.number_of_guesses_for_nums_label.place(relx=0.2, rely=0.8)
                  extra_window_8.winning_and_displaying_number_label.place(relx=0.5, rely=0.8)
                  extra_window_8.displaying_output_scale_label.place(relx=0.45, rely=0.6)


                  def playing_gussingnum_running():








                      playing_guesing = True


                      def range_nums(low, high):
                          for num in range(low, high):
                              list_of_nums.append(num)
                          print(list_of_nums)


                      print("welcome to gambeling game by bezalel achoonov!!!")
                      print("(this app do not suport gambaling or incorage you to wast your mony on gambeling )")
                      print(" rulls:")
                      print(" you have to chose the range of nubers to gues from,")
                      print(" then the computer will choose one number from the list you just created")
                      print("and you will have to gues the nuber as soon as posible.")
                      print("------------------------------------------------------------")


                      while playing_guesing:


                          running = True


                          extra_window_8.scale_doublevar = tb.DoubleVar(extra_window_8,
                              value=round(extra_window_8.scale_guesing_slider.get()))


                          low = int(
                              extra_window_8.entering_low_number_entry.get())  ###################int(input(f"---enter range of numbers to choose from:(lowest)----"))
                          high = int(
                              extra_window_8.entering_high_number_entry.get())  ######################int(input(f"---enter range of numbers to choose from:(highest)----"))
                          extra_window_8.scale_guesing_slider.place_forget()
                          extra_window_8.scale_guesing_slider = tb.Scale(extra_window_8,
                              command=lambda value: print(round(extra_window_8.scale_guesing_slider.get())),
                              from_=round(int(extra_window_8.entering_low_number_entry.get())),
                              to=int(extra_window_8.entering_high_number_entry.get()), length=400,
                              variable=extra_window_8.scale_doublevar)
                          extra_window_8.scale_guesing_slider.place(relx=0.5, rely=0.6)


                          extra_window_8.displaying_output_scale_label.place_forget()
                          extra_window_8.displaying_output_scale_label = tb.Label(extra_window_8,
                              textvariable=extra_window_8.scale_doublevar)
                          extra_window_8.displaying_output_scale_label.place(relx=0.45, rely=0.6)


                          if running:
                              print("the list you chosen:")
                              print(range_nums(low, high))


                              # app_running.sending_answer_button.place_forget()
                              # app_running.sending_answer_button = ttk.Button(text= "press here to send")
                              # app_running.sending_answer_button.place(relx=0.65, rely=0.6)
                              player_gues = extra_window_8.scale_doublevar.get()
                              num_is()


                              global choosen_num
                              if player_gues > choosen_num:
                                  global number_of_gusses
                                  print("to high!")
                                  number_of_gusses += 1
                                  extra_window_8.signaling_high_low_label.place_forget()
                                  extra_window_8.signaling_high_low_label = tb.Label(extra_window_8,
                                      text=f"{int(extra_window_8.scale_guesing_slider.get())} is to high!")
                                  extra_window_8.signaling_high_low_label.place(relx=0.5, rely=0.7)


                                  extra_window_8.number_of_guesses_for_nums_label.place_forget()
                                  extra_window_8.number_of_guesses_for_nums_label = tb.Label(extra_window_8,
                                      text=f" number of guesses is: {number_of_gusses - 1} ")
                                  extra_window_8.number_of_guesses_for_nums_label.place(relx=0.2, rely=0.8)


                                  list_of_alredy_choosed_nums.append(player_gues)


                                  extra_window_8.list_of_guesed_nums.place_forget()
                                  extra_window_8.list_of_guesed_nums = tb.Label(extra_window_8,
                                      text=f"numbers you alredy choosen: {list_of_alredy_choosed_nums}")
                                  extra_window_8.list_of_guesed_nums.place(relx=0.2, rely=0.3)


                              elif player_gues < choosen_num:


                                  print("to low!")
                                  number_of_gusses += 1


                                  extra_window_8.signaling_high_low_label.place_forget()
                                  extra_window_8.signaling_high_low_label = tb.Label(extra_window_8,
                                      text=f"{int(extra_window_8.scale_guesing_slider.get())} is to low!")
                                  extra_window_8.signaling_high_low_label.place(relx=0.5, rely=0.7)


                                  list_of_alredy_choosed_nums.append(player_gues)


                                  extra_window_8.list_of_guesed_nums.place_forget()
                                  extra_window_8.list_of_guesed_nums = tb.Label(extra_window_8,
                                      text=f"numbers you alredy choosen: {list_of_alredy_choosed_nums}")
                                  extra_window_8.list_of_guesed_nums.place(relx=0.2, rely=0.3)


                                  extra_window_8.number_of_guesses_for_nums_label.place_forget()
                                  extra_window_8.number_of_guesses_for_nums_label = tb.Label(extra_window_8,
                                      text=f" number of guesses is: {number_of_gusses - 1} ")
                                  extra_window_8.number_of_guesses_for_nums_label.place(relx=0.2, rely=0.8)




                              else:


                                  number_of_gusses += 1
                                  print(f"{choosen_num} is the number!")
                                  print("-----------------------------------")
                                  print(f"number of guesses is: {number_of_gusses} ")
                                  print("-----------------------------------")


                                  extra_window_8.signaling_high_low_label.place_forget()


                                  extra_window_8.number_of_guesses_for_nums_label.place_forget()
                                  extra_window_8.number_of_guesses_for_nums_label = tb.Label(extra_window_8,
                                      text=f" number of guesses is: {number_of_gusses - 1} ")
                                  extra_window_8.number_of_guesses_for_nums_label.place(relx=0.2, rely=0.8)


                                  extra_window_8.winning_and_displaying_number_label.place_forget()
                                  extra_window_8.winning_and_displaying_number_label = tb.Label(extra_window_8,text=f"you won\n"
                                                                                                   f"{choosen_num} is the number!")
                                  extra_window_8.winning_and_displaying_number_label.place(relx=0.5, rely=0.8)


                          running = False


                          playing_guesing = False


                      print("////////////////////////////////////////////////")
                      print("you played gamblang numbers by bezalel achoonov!")
                      print("have a nice day! goodbay!")
                      print("////////////////////////////////////////////////")
              playing_gussing_numbers_on_app()
          create_extra_window_8()




# Run the Application
if __name__ == "__main__":
  window = tk.Tk()
  app = ThemedApp(window)
  window.mainloop()

