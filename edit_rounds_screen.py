import tkinter as tk

from tkinter import messagebox

from tkinter import ttk

from datetime import datetime

from uuid import uuid4

from new_round_screen import NewRoundScreen

from round_detail_screen import RoundDetailScreen

import json

class RoundsScreen(tk.Frame):

    def __init__(self, master, window):
        super().__init__(master)
        self.window = window
        self.round_guids = []
        self.load_rounds()
        self.courses = self.load_golf_courses()
        self.create_widgets()
        self.pack(fill='both', expand=True)

    def load_golf_courses(self):

        try:
            with open("golf_courses.json") as file:
                courses = json.load(file)
            return courses
        except Exception as e:
            print(f"Error loading courses: {e}")
            return []
        
    def load_rounds(self):

        try:

            with open("rounds.json", "r") as file:
                    self.round_records = json.load(file)
        except json.JSONDecodeError:
                self.round_records = []

    def create_widgets(self):

        self.rounds_data = tk.Frame(self)
        self.rounds_data.pack(fill='both', expand=True)
        self.rounds_data.columnconfigure(0, weight=1)
        self.rounds_data.rowconfigure(0, weight=1)
        scrollbar = tk.Scrollbar(self.rounds_data, orient='vertical')

        self.rounds_listbox = tk.Listbox(self.rounds_data,font=("Arial", 18),yscrollcommand=scrollbar.set, width=38, justify="center")
        scrollbar.config(command=self.rounds_listbox.yview)

        new_btn = tk.Button(self.rounds_data, font=("Arial",18), text="New", command=lambda: [self.new_round_screen()])
        new_btn.grid(row=2, column=0, columnspan=2, pady=10)

        for round in self.round_records:
            self.rounds_listbox.insert('end', f"{round['course']}, {round['date']}, Score: {round['gross_score']}")
            self.round_guids.append(round['guid'])

        self.rounds_listbox.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.rounds_listbox.bind('<<ListboxSelect>>', self.on_select)

    def on_select(self, event):
            
        selected_index = self.rounds_listbox.curselection()

        if selected_index:
            selected_guid = self.round_guids[selected_index[0]]
            print(selected_guid)   
            edit_btn = tk.Button(self.rounds_data, text="Edit", font=("Arial",18), command=lambda: [self.new_round_detail_screen(selected_guid)])
            edit_btn.grid(row=1, column=0, columnspan=2, pady=10)


    def new_round_detail_screen(self, guid):
         new_round_detail_screen = RoundDetailScreen(master=self.window.get_root(), window= self.window, selected_round_guid=guid)
         self.window.round_detail_screen = new_round_detail_screen
         self.window.show_round_detail_screen()

    def new_round_screen(self):
         new_round_screen = NewRoundScreen(master=self.window.get_root(), window= self.window, courses=self.courses)
         self.window.new_rounds_screen = new_round_screen
         self.window.show_new_round_screen()
        

