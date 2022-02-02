# from tkinter import *
# from tkinter import ttk

# win = Tk()
# win.title("Shafa")
# #function
# def func():
#     x=var.get()
#     print(x)
#     lbl.config(text=x,bg="Orange")
# win.iconbitmap('img.ico')
# win.geometry('600x300')
# #Lable
# lbl=Label(win,text="Nothig",bg="green",fg="white",width="10",height=10)
# lbl.place(x=10,y=100)
# #Entry
# var=StringVar()
# ent = Entry(win,bg="red",fg="white",bd=5,textvariable=var)
# ent.place(x=80,y=10)
# #Button
# btn=Button(win,text="Submit",bg="blue",command=func)
# btn.place(x=10,y=80)
#
# var = StringVar()
# com = ttk.Combobox(win,width=27)
# com['state'] = 'readonly'
# com['values'] = ( 'Jan',
#                   'Feb'
#                  )
# def call():
#     print(Checkbtn1.get())
#     print(Checkbtn2.get())
# com.current(0)
# com.place(x=30,y=40)
# Checkbtn1 = IntVar()
# Checkbtn2= IntVar()
# select= Checkbutton(win,text="Male",variable=Checkbtn1,onvalue=1,offvalue=0).pack()
# select=Checkbutton(win,text="Female",variable=Checkbtn2,onvalue=1,offvalue=0).pack()
# btn=Button(win,text="Pree me",command=call,bg="yellow").pack()
#lbl.pack()
#lbl.grid(row=7,column=10)
# win.maxsize(width=600,height=300)
# win.minsize(width=600,height=800)
#win.mainloop()
##################### Frame ###############################
# from tkinter import *
# win=Tk()
# win.title("Frame")
# win.iconbitmap('img.ico')
# win.geometry('600x500')
#
# top=Frame(win)
# top.pack(side=TOP)
#
# btm=Frame(win)
# btm.pack(side=BOTTOM)
#
# lblt=Label(top,text="Top Frame")
# lblt.pack()
#
# lblb=Label(btm,text="Bottom Frame",bg="red")
# lblb.pack()
#
# win.mainloop()
################################## Msg Box ##########################
# from tkinter import *
# from tkinter import messagebox
# win=Tk()
# win.title("Hello world")
# win.iconbitmap('img.ico')
# win.geometry('600x600')
# def func():
#     var.get()
#     if var.get()=="":
#         messagebox.showwarning("Wrning","Empty filed")
#     else:
#         messagebox.askquestion("Wolkd","Do you want to exit?")
#         win.destroy()
#
# var=StringVar()
# ent=Entry(win,textvariable=var)
# btn=Button(win,text="Clink me",command=func)
# btn.pack()
# ent.pack()
# win.mainloop()
############################################# List Box #######################

# from tkinter import *
# win=Tk()
# win.title("Hello")
# win.geometry('500x500')
# def dele():
#     lst.delete(ANCHOR)
#
# lst=Listbox(win,width=25)
# lst.pack()
# items= ['Apple','Banana','Armndo']
# for i in items:
#     lst.insert(END,i)
# btn=Button(win,text="Del", command=dele)
# btn.pack()
# win.mainloop()
############################################# Canvas #########################
# from tkinter import *
# win=Tk()
# win.title("Canvas")
# win.geometry('500x500')
# canvas= Canvas(win)
# cord=10,20,259,210
# canvas.create_arc(cord,start=1,extent=180,fill="orange")
# canvas.create_line(cord)
# canvas.pack()
# win.mainloop()
############################Top level##################################
# from tkinter import *
# win=Tk()
# win.title("Canvas")
# win.geometry('500x500')
# def func():
#     top.destroy()
#     win.destroy()
#
# top=Toplevel()
# btn=Button(top,text="Close window",command=func).pack()
# win.mainloop()
################################## Prograss Bar ##############
# from tkinter import *
# from tkinter import ttk
# win=Tk()
# win.title("Canvas")
# win.geometry('500x500')
# def bar():
#     import time
#     prog['value'] =10
#     prog.update_idletasks()
#     time.sleep(0.5)
#
#     prog['value'] = 10
#     prog.update_idletasks()
#     time.sleep(0.5)
#
#     prog['value'] = 10
#     prog.update_idletasks()
#     time.sleep(0.5)
#
#     prog['value'] = 10
#     prog.update_idletasks()
#     time.sleep(0.5)
# prog=ttk.Progressbar(win,orient=HORIZONTAL,length=100,mode="determinate")
# prog.pack()
# btn =Button(win,text="Start",command=bar ).pack()
#
# win.mainloop()
####################################### Scrol Bar ###############################
# from tkinter import *
# from tkinter import ttk
# win=Tk()
# win.title("Canvas")
# win.geometry('500x500')
# scroll= Scrollbar(win)
# scroll.pack(side=RIGHT,fill=Y)
# mylist=Listbox(win,yscrollcommand=Y)
# for i in range(1000):
#     mylist.insert(END,i)
# mylist.pack(side=LEFT,fill=Y)
# scroll.config(command=mylist.yview)
#
#
# win.mainloop()
################################### Manue Bar ###################
# from tkinter import *
# from tkinter import ttk
# win=Tk()
# win.title("Canvas")
# win.geometry('500x500')
# my_menu = Menu(win)
# win.config(menu=my_menu)
# def demo():
#     pass
# file_menu=Menu(my_menu)
# my_menu.add_cascade(label="File",menu=file_menu)
# file_menu.add_cascade(label="New",command=demo)
# file_menu.add_separator()
# file_menu.add_cascade(label="Open",command=demo)
#
# edit_menu=Menu(my_menu)
# my_menu.add_cascade(label="Edit ",command=demo)
#
#
# win.mainloop()
###################################### Privacy_policy_summary_generator_using_ML ##########################

# from tkinter import *
# import tkinter as tk
# from PIL import Image, ImageTk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
# import PyPDF2
#
# from  tkinter import ttk
# pri=Tk()
# pri.title("Privacy Policy Summary Generator Using ML")
# pri.geometry('1000x600+350+100')
# pri.maxsize(width=1000,height=600)
#
#
#
#
# ################################### Reading a file#########################################
# T = Text(pri, height=10, width=70, relief='ridge')  #Dring_a_text_Box
# def select_file():
#     filetypes = (
#         ("PDF Files", "*.pdf"),
#         ("All Files", "*.*")
#
#     )
#
#     file = fd.askopenfile(mode='r', filetypes=filetypes,title='Open a file',initialdir='/')
#     if file is not None:
#         content = file.read()
#         print(content)
#         # Open the pdf file
#         pdf_file = PyPDF2.PdfFileReader(file)
#         # Set the page to read
#         page = pdf_file.getPage(0)
#         # Extract the text from the pdf file
#         page_stuff = page.extractText()
#
#         # Add text to textbox
#         T.insert(1.0, page_stuff)
#
#     showinfo(title='Selected File',message=file)
#
# #    T.insert(tk.END, content) #Inserting_into_textBox
#     file.close()
#
# T.pack(side=BOTTOM, ipadx=200, ipady=60) #packing_text_box
# ################################################ Code start ##########
#
# image = Image.open("bk.jpg")
# resize_image = image.resize((1000,600))
# img= ImageTk.PhotoImage(resize_image)
#
#
#
# button =Button(pri,text="Chose   Book",font='Times',bg='blue',fg='white',activebackground='#00ff00',command=select_file)
# button.place(relx=0.43 , rely=0.1, width=150, height=50)
#
# btn =Button(pri,text="Book Summary",font='Times',bg='blue',fg='white',activebackground='#00ff00')
# #lab=tk.Label(pri,text=" Book Summary",font=('Arial', 25))
# btn.place(relx = 0.5,rely = 0.4,anchor = 'center',width=150, height=50)
#
# txt="Hello"
#pri.mainloop()

#################################################################









# from sklearn.feature_extraction.text import TfidfVectorizer
# from spacy.lang.en import English
# import numpy as np

 # from PyPDF2 import PdfFileReader
# from tkinter import *
# from tkinter import filedialog
# from tkinter import scrolledtext
# nlp = English()
#
# ws = Tk()
# ws.title('Book & News Articles Summarizer')
# ws.geometry('1000x600+350+100')
# ws.config(bg='#D9653B')
# ws.iconbitmap('logo.ico')
# l = Label(ws, text = "Summarizer Application", bg = '#D9653B', fg = "white", font = "Castellar 17 bold ")
# l1 = Label(ws, text = "Mehran University of Engineering and Technology", bg = '#D9653B', fg = "white", font = "Castellar 10 bold")
# l1.pack()
# l.pack()
#
# def choose_pdf():
#       filename = filedialog.askopenfilename(
#
#             initialdir = "C:/",   #for windows users
#             title = "Select a File",
#             filetypes = (("PDF files","*.pdf*"),("all files","*.*")))
#       if filename:
#           return filename
#
#
# def read_pdf():
#     filename = choose_pdf()
#     reader = PdfFileReader(filename)
#     pageObj = reader.getNumPages()
#     for page_count in range(pageObj):
#         page = reader.getPage(page_count)
#         page_data = page.extractText()
#
#         ################
#         nlp = English()
#         nlp.add_pipe('sentencizer')
#         doc = nlp(page_data.replace("\n", ""))
#         sentences = [sent.text.strip() for sent in doc.sents]
#         # Let's create an organizer which will store the sentence ordering to later reorganize the
#         # scored sentences in their correct order
#
#         sentence_organizer = {k: v for v, k in enumerate(sentences)}
#         # Let's now create a tf-idf (Term frequnecy Inverse Document Frequency) model
#         tf_idf_vectorizer = TfidfVectorizer(min_df=1, max_features=None,
#                                             strip_accents='unicode',
#                                             analyzer='word',
#                                             token_pattern=r'\w{1,}',
#                                             ngram_range=(1, 3),
#                                             use_idf=1, smooth_idf=1,
#                                             sublinear_tf=1,
#                                             stop_words='english')
#         # Passing our sentences treating each as one document to TF-IDF vectorizer
#         tf_idf_vectorizer.fit(sentences)
#         # Transforming our sentences to TF-IDF vectors
#         sentence_vectors = tf_idf_vectorizer.transform(sentences)
#         # Getting sentence scores for each sentences
#         sentence_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
#         # Sanity checkup
#         print(len(sentences) == len(sentence_scores))
#         # Getting top-n sentences
#         N = 100
#         top_n_sentences = [sentences[ind] for ind in np.argsort(sentence_scores, axis=0)[::-1][:N]]
#         # Let's now do the sentence ordering using our prebaked sentence_organizer
#         # Let's map the scored sentences with their indexes
#         mapped_top_n_sentences = [(sentence, sentence_organizer[sentence]) for sentence in top_n_sentences]
#         #print("Our top_n_sentence with their index: \n")
#         for element in mapped_top_n_sentences:
#             print(element)
#         # Ordering our top-n sentences in their original ordering
#         mapped_top_n_sentences = sorted(mapped_top_n_sentences, key=lambda x: x[1])
#         ordered_scored_sentences = [element[0] for element in mapped_top_n_sentences]
#         # Our final summary
#         summary = " ".join(ordered_scored_sentences)
#         print("Len of summary=",len(summary))
#
#         textbox.insert(END, summary)
#
# def copy_pdf_text():
#     content = textbox.get(1.0, "end-1c")
#     ws.withdraw()
#     ws.clipboard_clear()
#     ws.clipboard_append(content)
#     ws.update()
#     ws.destroy()
#
# textbox = scrolledtext.ScrolledText(
#     ws,
#     height=25,
#     width=100,
#     wrap='word',
#     bg='#D9BDAD',
#    )
# textbox.pack(expand=True)
#
# Button(
#     ws,
#     text='Choose A Book',
#     padx=20,
#     pady=10,
#     bg='#262626',
#     fg='white',
#     command=read_pdf
# ).pack(expand=True, side=LEFT, pady=10)
#
# Button(
#     ws,
#     text="Copy Text",
#     padx=20,
#     pady=10,
#     bg='#262626',
#     fg='white',
#     command=copy_pdf_text
# ).pack(expand=True, side=LEFT, pady=10)
#  ws.mainloop()

# from PyPDF2 import PdfFileReader
# import tkinter as tk
# from tkinter import *
# from tkinter import filedialog
# from tkinter import scrolledtext
# from PIL import ImageTk,Image
# import PyPDF2
# from win32com.client import Dispatch
#
# from sklearn.feature_extraction.text import TfidfVectorizer
# from spacy.lang.en import English
# import numpy as np





# class Win:
#     def __init__(self, root):
#         """Define window for the app"""
#         self.root = root
#         self.root.geometry("1000x600+400+50")
#         self.root.title('Privacy Policy Summary Generator Using ML')
#         self.root.iconbitmap('logo.ico')
#         Label(self.root, text="Mam Rabia Iftikhar", font=('Helvetica bold', 38), fg='navy blue').place(x=520, y=130)
#         Label(self.root, text="Muhammd Azeem (18SW62)", font=('Helvetica bold', 25), fg='black').place(x=540, y=230)
#         Label(self.root, text="Abdul Qudoos (18SW145)", font=('Helvetica bold', 25), fg='black').place(x=540, y=300)
#         label = Label(self.root, text="Mehran University of Engineering and Technology", fg='navy blue',
#                       font="Castellar 15 bold").pack(pady=10)
#         btn = Button(
#             self.root,
#             text='Click  me ',
#             padx=20,
#             pady=10,
#             bg='#262626',
#             fg='white',
#             command=lambda: self.new_window(Win2),
#         ).place(x=430, y=500)
#
#     def new_window(self, _class):
#         try:
#             if self.new.state() == "normal":
#                 self.new.focus()
#         except:
#             self.new = tk.Toplevel(self.root)
#             _class(self.new)
#
#
# class Win2:
#     def __init__(self, root):
#         print(app.new.state())
#         self.root = root
#         self.root.geometry("1000x600+350+100")
#         self.root["bg"] = "steel blue"
#         self.root.title('Book & News Articles Summarizer')
#         self.root.iconbitmap('logo.ico')
#         self.l1 = Label(self.root, text="Mehran University of Engineering and Technology", bg='steel blue', fg='white',
#                         font="Castellar 17 bold").pack()
#         self.lebl = Label(self.root, text="Summarizer Application", bg='steel blue', fg="white",font="Castellar 17 bold ").pack()
#         ############################
#         def read_pdf():
#             pass
#         ###########################
#         def openTextFile():
#             tf = filedialog.askopenfilename(
#                 initialdir="C:/",
#                 title="Open Text file",
#                 filetypes=(("Text Files", "*.txt"),)
#             )
#
#             tf = open(tf, encoding="utf8")  # or tf = open(tf, 'r')
#             data = tf.read()
#
#             print("Orgnal length",len(data))
#             textbox.delete("1.0", "end")
# ##########################################################
#             nlp = English()
#             nlp.add_pipe('sentencizer')
#             doc = nlp(data.replace("\n", ""))
#             sentences = [sent.text.strip() for sent in doc.sents]
#             # Let's create an organizer which will store the sentence ordering to later reorganize the
#             # scored sentences in their correct order
#
#             sentence_organizer = {k: v for v, k in enumerate(sentences)}
#             # Let's now create a tf-idf (Term frequnecy Inverse Document Frequency) model
#             tf_idf_vectorizer = TfidfVectorizer(min_df=2, max_features=None,
#                                                 strip_accents='unicode',
#                                                 analyzer='word',
#                                                 token_pattern=r'\w{1,}',
#                                                 ngram_range=(1, 3),
#                                                 use_idf=1, smooth_idf=1,
#                                                 sublinear_tf=1,
#                                                 stop_words='english')
#             # Passing our sentences treating each as one document to TF-IDF vectorizer
#             tf_idf_vectorizer.fit(sentences)
#             # Transforming our sentences to TF-IDF vectors
#             sentence_vectors = tf_idf_vectorizer.transform(sentences)
#             # Getting sentence scores for each sentences
#             sentence_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
#             # Sanity checkup
#             print(len(sentences) == len(sentence_scores))
#             # Getting top-n sentences
#             N = 2
#             top_n_sentences = [sentences[ind] for ind in np.argsort(sentence_scores, axis=0)[::-1][:N]]
#             # Let's now do the sentence ordering using our prebaked sentence_organizer
#             # Let's map the scored sentences with their indexes
#             mapped_top_n_sentences = [(sentence, sentence_organizer[sentence]) for sentence in top_n_sentences]
#             # print("Our top_n_sentence with their index: \n")
#             for element in mapped_top_n_sentences:
#                   print("Element len",len(element))
#             # Ordering our top-n sentences in their original ordering
#             mapped_top_n_sentences = sorted(mapped_top_n_sentences, key=lambda x: x[1])
#             ordered_scored_sentences = [element[0] for element in mapped_top_n_sentences]
#             # Our final summary
#             summary = " ".join(ordered_scored_sentences)
#             print("Summary length",len(summary))
#             text=summary
#             textbox.insert(END, summary)

#
#
#
#
# ##########################################################
#
#
#
#         textbox = scrolledtext.ScrolledText(
#             self.root,
#             height=25,
#             width=100,
#             wrap='word',
#             bg='#D9BDAD',
#         )
#         textbox.pack(expand=True)
#
#         Button(
#             self.root,
#             text='Book Summary',
#             padx=20,
#             pady=10,
#             bg='#262626',
#             fg='white',
#             command=openTextFile
#         ).pack(expand=True, side=LEFT, pady=10)
#
#         Button(
#             self.root,
#             text="Web Page Summary",
#             padx=20,
#             pady=10,
#             bg='#262626',
#             fg='white',
#             command=openTextFile
#         ).pack(expand=True, side=LEFT, pady=10)
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Win(root)
#     img = Image.open("win.png")
#     img = img.resize((450, 350), Image.ANTIALIAS)
#     photo = ImageTk.PhotoImage(img)
#     lab = Label(image=photo).place(x=50, y=90)
#     app.root.title("Lezioni")
#
#     root.mainloop()


# def Speck(sum):
#     speak = Dispatch(("SAPI.SpVoice"))
#     speak.Speak(sum)
# book=""
# pdfReader=PyPDF2.PdfFileReader(book)
# pages=pdfReader.numPages
#
# for num in range(0,pages):
#     page=pdfReader.getPage(num)
#     text=page.extractText()
#     print(text)



















# from PyPDF2 import PdfFileReader
# import tkinter as tk
# from tkinter import *
# from tkinter import filedialog
# from tkinter import scrolledtext
# from PIL import ImageTk,Image
# import PyPDF2
# from win32com.client import Dispatch
# from sklearn.feature_extraction.text import TfidfVectorizer
# import spacy
# from spacy.lang.en import English
# import numpy as np
# from functools import partial
#
#
# #creates a Tk() object
# master = Tk()
# master.title('Privacy Policy Summary Generator Using ML')
# master.geometry("1000x600+350+100")
# master.iconbitmap('logo.ico')
# img  = Image.open("win.png")
# img = img.resize((450, 350), Image.ANTIALIAS)
# photo=ImageTk.PhotoImage(img)
# lab=Label(image=photo).place(x=50,y=90)
#
#
# def Speck(text):
#     speak = Dispatch(("SAPI.SpVoice"))
#     speak.Speak(text)
#
# # function to open a new window
# # on a button click
# def openNewWindow():
#     # Toplevel object which will
#     # be treated as a new window
#     ws = Toplevel(master)
#     # Creating a photoimage object to use image
#     photo = PhotoImage(file=r"C:\Users\Shafaullah Malik\PycharmProjects\Tkinter\icon.png")
#
#     # Resizing image to fit on button
#     photoimage = photo.subsample(3, 3)
#
#     ws.title('Book & News Articles Summarizer')
#     ws.geometry('1000x600+400+50')
#     ws.config(bg='steel blue')
#     ws.iconbitmap('logo.ico')
#     l = Label(ws, text="Summarizer Application", bg='steel blue', fg="white", font="Castellar 17 bold ")
#     l1 = Label(ws, text="Mehran University of Engineering and Technology", bg='steel blue', fg='white',font="Castellar 17 bold")
#     l1.pack()
#     l.pack()
#
#     def choose_pdf():
#         filename = filedialog.askopenfilename(
#
#             initialdir="C:/",  # for windows users
#             title="Select a File",
#             filetypes=(("PDF files", "*.pdf*"), ("all files", "*.*")))
#         if filename:
#             return filename
# ##################################################
#     def read_pdf():
#         pass
# ##################################################
#     def openTextFile():
#         tf = filedialog.askopenfilename(
#             initialdir="C:/",
#             title="Open Text file",
#             filetypes=(("Text Files", "*.txt"),)
#         )
#
#         tf = open(tf, encoding="utf8")  # or tf = open(tf, 'r')
#         data = tf.read()
#         nlp = English()
#         nlp.add_pipe('sentencizer')
#         doc = nlp(data.replace("\n", ""))
#         sentences = [sent.text.strip() for sent in doc.sents]
#         # Let's create an organizer which will store the sentence ordering to later reorganize the
#         # scored sentences in their correct order
#
#         sentence_organizer = {k: v for v, k in enumerate(sentences)}
#         # Let's now create a tf-idf (Term frequnecy Inverse Document Frequency) model
#         tf_idf_vectorizer = TfidfVectorizer(min_df=2, max_features=None,
#                                             strip_accents='unicode',
#                                             analyzer='word',
#                                             token_pattern=r'\w{1,}',
#                                             ngram_range=(1, 3),
#                                             use_idf=1, smooth_idf=1,
#                                             sublinear_tf=1,
#                                             stop_words='english')
#         # Passing our sentences treating each as one document to TF-IDF vectorizer
#         tf_idf_vectorizer.fit(sentences)
#         # Transforming our sentences to TF-IDF vectors
#         sentence_vectors = tf_idf_vectorizer.transform(sentences)
#         # Getting sentence scores for each sentences
#         sentence_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
#         # Sanity checkup
#         print(len(sentences) == len(sentence_scores))
#         # Getting top-n sentences
#         N = 2
#         top_n_sentences = [sentences[ind] for ind in np.argsort(sentence_scores, axis=0)[::-1][:N]]
#         # Let's now do the sentence ordering using our prebaked sentence_organizer
#         # Let's map the scored sentences with their indexes
#         mapped_top_n_sentences = [(sentence, sentence_organizer[sentence]) for sentence in top_n_sentences]
#         # print("Our top_n_sentence with their index: \n")
#         for element in mapped_top_n_sentences:
#             print("Element len", len(element))
#         # Ordering our top-n sentences in their original ordering
#         mapped_top_n_sentences = sorted(mapped_top_n_sentences, key=lambda x: x[1])
#         ordered_scored_sentences = [element[0] for element in mapped_top_n_sentences]
#         # Our final summary
#         summary = " ".join(ordered_scored_sentences)
#         print("Summary length", len(summary))
#
#         textbox.insert(END, summary)
#
#         Button(
#             ws,
#             text="Speck",
#             image=photoimage,
#             compound=LEFT,
#             padx=20,
#             pady=10,
#             bg='#262626',
#             fg='white',
#             command=partial(Speck,summary)
#         ).pack(expand=True, side=LEFT, pady=15)
#
#     textbox = scrolledtext.ScrolledText(
#         ws,
#         height=25,
#         width=100,
#         wrap='word',
#         bg='#D9BDAD',
#     )
#     textbox.pack(expand=True)
#
#     Button(
#         ws,
#         text='Book Summary',
#         padx=20,
#         pady=10,
#         bg='#262626',
#         fg='white',
#         command=openTextFile
#     ).pack(expand=True, side=LEFT, pady=10)
#
#     Button(
#         ws,
#         text="Web Page Summary",
#         padx=20,
#         pady=10,
#         bg='#262626',
#         fg='white',
#         command=openTextFile
#     ).pack(expand=True, side=LEFT, pady=10)
# Label(master,text = "Mam Rabia Iftikhar",font=('Helvetica bold',38),fg = 'navy blue').place(x = 520,y = 130)
# Label(master,text = "Muhammd Azeem (18SW62)",font=('Helvetica bold',25),fg = 'black').place(x = 540,y = 230)
# Label(master,text = "Abdul Qudoos (18SW145)",font=('Helvetica bold',25),fg = 'black').place(x = 540,y = 300)
# label = Label(master, text = "Mehran University of Engineering and Technology", fg = 'navy blue', font = "Castellar 15 bold")
# label.pack(pady=10)
# btn=Button(
#     master,
#     text='Click  me ',
#     padx=20,
#     pady=10,
#     bg='#262626',
#     fg='white',
#     command=openNewWindow,
# )
# btn.place(x=430, y=500)
# # mainloop, runs infinitely
# mainloop()



############################## Web App #######################

import streamlit as st
from PIL import Image
from PyPDF2 import PdfFileReader
import pdfplumber
import docx2txt
import fitz
import re
import nltk.corpus
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from spacy.lang.en import English
import numpy as np

stop = stopwords.words('english')
img = Image.open("web_lo.png")
st.image(img, width=730)
html_temp = """
    <div style ="background-color:LightBlue;padding:0px">
    <h2 style ="color:green;text-align:center;">Privacy Policy Summary Generator Using ML</h2>
    </div>
    """
# this line allows us to display the front end aspects we have
# defined in the above code
st.markdown(html_temp, unsafe_allow_html=True)

def summarizer(text):
    data = text.replace("Chapter", "")
    data= ''.join([i for i in data if not i.isdigit()])

    nlp = English()
    nlp.add_pipe('sentencizer')
    doc = nlp(data.replace("\n", ""))
    sentences = [sent.text.strip() for sent in doc.sents]
    # Let's create an organizer which will store the sentence ordering to later reorganize the
    # scored sentences in their correct order

    sentence_organizer = {k: v for v, k in enumerate(sentences)}
    # Let's now create a tf-idf (Term frequnecy Inverse Document Frequency) model
    tf_idf_vectorizer = TfidfVectorizer(min_df=2, max_features=None,
                                        strip_accents='unicode',
                                        analyzer='word',
                                        token_pattern=r'\w{1,}',
                                        ngram_range=(1, 3),
                                        use_idf=1, smooth_idf=1,
                                        sublinear_tf=1,
                                        stop_words='english')
    # Passing our sentences treating each as one document to TF-IDF vectorizer
    tf_idf_vectorizer.fit(sentences)
    # Transforming our sentences to TF-IDF vectors
    sentence_vectors = tf_idf_vectorizer.transform(sentences)
    # Getting sentence scores for each sentences
    sentence_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
    # Sanity checkup
    print(len(sentences) == len(sentence_scores))
    # Getting top-n sentences
    N = 2
    top_n_sentences = [sentences[ind] for ind in np.argsort(sentence_scores, axis=0)[::-1][:N]]
    # Let's now do the sentence ordering using our prebaked sentence_organizer
    # Let's map the scored sentences with their indexes
    mapped_top_n_sentences = [(sentence, sentence_organizer[sentence]) for sentence in top_n_sentences]
    # print("Our top_n_sentence with their index: \n")
    for element in mapped_top_n_sentences:
        print("Element len", len(element))
    # Ordering our top-n sentences in their original ordering
    mapped_top_n_sentences = sorted(mapped_top_n_sentences, key=lambda x: x[1])
    ordered_scored_sentences = [element[0] for element in mapped_top_n_sentences]
    # Our final summary
    summary = " ".join(ordered_scored_sentences)
    summary=" ".join(summary.split())
    st.text(summary)

st.subheader("DocumentFiles")
docx_file = st.file_uploader("Upload File", type=['txt', 'docx', 'pdf'])
if st.button("Process"):
    if docx_file is not None:
        file_details = {"Filename": docx_file.name, "FileType": docx_file.type, "FileSize": docx_file.size}
        st.write(file_details)
        # Check File Type
        if docx_file.type == "text/plain":

            raw_text = str(docx_file.read(), "utf-8")  # works with st.text and st.write,used for futher processing
            summarizer(raw_text)


        elif docx_file.type == "application/pdf":
            if docx_file is not None:
                doc = fitz.open(stream=docx_file.read(), filetype="pdf")
                text = ""
                for page in doc:
                    text += page.getText()
                summarizer(text)
                doc.close()

        elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            # Use the right file processor ( Docx,Docx2Text,etc)
            raw_text = docx2txt.process(docx_file)  # Parse in the uploadFile Class directory
            st.write(raw_text)

else:
    st.subheader("About")
    st.info("Supervised By: Mam Rabia Iftikhar")
    st.success("Muhammd Azeem (18SW62)")
    st.success("Abdul Qudoos (18SW145)")










































