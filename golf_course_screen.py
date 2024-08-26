import tkinter as tk

from tkinter import messagebox

from tkinter import ttk

from datetime import datetime

from uuid import uuid4

import json

from course_detail_screen import GolfCoursesDetailScreen

class GolfCoursesScreen(tk.Frame):
    def __init__(self, master, window):
        super().__init__(master)
        self.window = window
        self.create_widgets(self.window.courses)
    
    def create_widgets(self, courses):
        course_guids = {}

        self.gc_frame = tk.Frame(self)
        self.gc_frame.columnconfigure(0, weight=1)
        self.gc_frame.pack(side=tk.TOP)
        scrollbar = tk.Scrollbar(self.gc_frame, orient='vertical')

        self.listbox = tk.Listbox(self.gc_frame, font=("Arial", 18), justify="center", width=38,yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        for course in courses: 
            course_guids[course["name"]] = course["guid"]
            self.listbox.insert(tk.END, course["name"])
        self.course_guids = course_guids

        self.listbox.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        
        btn5 = tk.Button(self.gc_frame,text="New", font=("Arial", 18), command=self.window.show_create_course_screen)
        btn5.grid(row=1, column=0,columnspan=2,pady=10)
    
    def on_select(self, event):
        
        indexes = self.listbox.curselection()
        if indexes:
            index = indexes[0] 
            selected_name = self.listbox.get(index)
            selected_course_guid = self.course_guids.get(selected_name, None)
            print("Selected GUID:", selected_course_guid)
            btn4 = tk.Button(self.gc_frame, text="Edit", font=("Arial", 18),
                            command=lambda: [self.new_details_screen(selected_course_guid)])
            btn4.grid(row=2, column=1)

    def new_details_screen(self, course_guid):
        new_detail_screen = GolfCoursesDetailScreen(master=self.window.get_root(), window=self.window, selected_course_guid=course_guid)
        self.window.golf_courses_detail_screen = new_detail_screen
        self.window.show_golf_courses_detail_screen()