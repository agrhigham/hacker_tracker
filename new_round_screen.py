import tkinter as tk

from tkinter import messagebox

from tkinter import ttk

from datetime import datetime

from uuid import uuid4

import json

class NewRoundScreen(tk.Frame):

    def __init__(self, master, window, courses):
        super().__init__(master)
        self.window = window
        self.courses = courses
        self.round_course = None
        self.course_options = self.create_options()
        self.new_round_record = {}
        self.round_holes = []
        self.new_hole_record = {}
        self.create_round_detail_widget()

    def create_options(self):

        options = []
        for course in self.courses:
            options.append(course['name'])
        return options

    def create_round_detail_widget(self):

        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%d-%m-%Y")
        
        round_data = tk.Frame(master=self)
        round_data.columnconfigure(0, weight=1)
        round_data.columnconfigure(1, weight=1)
        round_data.pack(side=tk.TOP)

        date_of_round_label = tk.Label(master=round_data, text="Date of round: ", font=("Arial, 18"))
        date_of_round_label.grid(row=0, column=0)
        self.date_of_round_entry = tk.Entry(round_data, font=("Arial",18))
        self.date_of_round_entry.insert(0, formatted_date)
        self.date_of_round_entry.grid(row=0, column=1)

        round_course_label = tk.Label(round_data, text="Course: ", font=("Arial", 18))
        round_course_label.grid(row=1,column=0)
        self.round_course_dropbox = ttk.Combobox(round_data, values=self.course_options, font=("Arial", 18))
        self.round_course_dropbox.set(self.course_options[0])
        self.round_course_dropbox.grid(row=1,column=1)

        test_button = tk.Button(round_data, text="Test", font=("Arial", 18), command=self.test_button)
        test_button.grid(row=2,column=0)

    def test_button(self):

        self.round_guid = str(uuid4())

        for course in self.courses:

            if course.get('name') == self.round_course_dropbox.get():
                self.round_course = course
                self.create_round_holes_list()
                self.create_holes_detail_widget()
                break

        self.new_round_record['guid'] = self.round_guid
        self.new_round_record['date'] = self.date_of_round_entry.get()
        self.new_round_record['course'] = self.round_course_dropbox.get()
        self.new_round_record['gross_score'] = 0
        self.new_round_record['score_to_par'] = 0
        self.new_round_record['total_fairways'] = 0
        self.new_round_record['gir'] = 0
        self.new_round_record['agir'] = 0
        self.new_round_record['total_putts'] = 0
        self.new_round_record['total_sand_shots'] = 0
        self.new_round_record['total_penalties'] = 0

    def create_round_holes_list(self):

        self.round_holes = [
            { 
                "hole": 1,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 2,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 3,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 4,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 5,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 6,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 7,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 8,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 9,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 10,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 11,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 12,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 13,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 14,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 15,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 16,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 17,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             },
             { 
                "hole": 18,
                "round_guid": self.round_guid,
                "par": "",
                "score": "",
                "result": "",
                "tee_club": "",
                "fairway": "N/a",
                "gir": 0,
                "agir": 0,
                "number_of_putts": "",
                "sand_shots": 0,
                "penalties": 0
             }
        ]

    def create_holes_detail_widget(self):

        tee_clubs = ['Driver', '3 Wood', '7 Wood', '5 Hybrid', '6 Iron', '7 Iron', '8 Iron', '9 Iron', 'PW']
        fairway_options = ['Hit', 'Right', 'Left', 'Short', 'Long', 'N/a']

        self.hole_index = 0

        hole_data = tk.Frame(master=self)
        hole_data.columnconfigure(0, weight=1)
        hole_data.columnconfigure(1, weight=1)
        hole_data.pack(side=tk.BOTTOM)

        self.hole_number_label = tk.Label(hole_data, text= self.round_holes[self.hole_index]['hole'], font=("Arial", 18))
        self.hole_number_label.grid(row=0,column=0)
        self.hole_par_label = tk.Label(hole_data, text= "Par: " + str(self.round_course.get('1')), font=("Arial", 18))
        self.hole_par_label.grid(row=0,column=1)

        hole_score_label = tk.Label(hole_data, text="Score: ", font=("Arial", 18))
        hole_score_label.grid(row=1,column=0)
        self.hole_score_entry = tk.Entry(hole_data, font=("Arial",18), justify="center",)
        self.hole_score_entry.insert(0,self.round_holes[self.hole_index].get('score'))
        self.hole_score_entry.grid(row=1,column=1)

        hole_putts_label = tk.Label(hole_data, text="Number of putts: ", font=("Arial", 18))
        hole_putts_label.grid(row=2,column=0)
        self.hole_putts_entry = tk.Entry(hole_data, font=("Arial",18), justify="center", )
        self.hole_putts_entry.insert(0,self.round_holes[self.hole_index].get('number_of_putts'))
        self.hole_putts_entry.grid(row=2,column=1)

        tee_club_label = tk.Label(hole_data, text="Tee Club:", font=("Arial", 18))
        tee_club_label.grid(row=3,column=0)
        self.tee_club_dropbox = ttk.Combobox(hole_data, justify="center",values=tee_clubs, font=("Arial",18), width=19)
        self.tee_club_dropbox.grid(row=3, column=1)

        fairway_label = tk.Label(hole_data, text="Fairway:", font=("Arial", 18))
        fairway_label.grid(row=4,column=0)
        self.fairway_dropbox = ttk.Combobox(hole_data, justify="center",values=fairway_options, font=("Arial",18), width=19)
        self.fairway_dropbox.grid(row=4, column=1)

        hole_sand_label = tk.Label(hole_data, text="Number of sand shots: ", font=("Arial", 18))
        hole_sand_label.grid(row=5,column=0)
        self.hole_sand_entry = tk.Entry(hole_data, font=("Arial",18), justify="center", )
        self.hole_sand_entry.insert(0,self.round_holes[self.hole_index].get('sand_shots'))
        self.hole_sand_entry.grid(row=5,column=1)

        hole_penalty_label = tk.Label(hole_data, text="Number of penalties: ", font=("Arial", 18))
        hole_penalty_label.grid(row=6,column=0)
        self.hole_penalty_entry = tk.Entry(hole_data, font=("Arial",18), justify="center", )
        self.hole_penalty_entry.insert(0,self.round_holes[self.hole_index].get('penalties'))
        self.hole_penalty_entry.grid(row=6,column=1)

        self.prev_hole_button = tk.Button(hole_data, text="Previous", font=("Arial", 18), command=self.save_round_record_prev)
        self.finish_holes_button = tk.Button(hole_data, text="Finish", font=("Arial",18), command=self.finish_holes)
        self.next_hole_button = tk.Button(hole_data, text="Next", font=("Arial", 18), command=self.save_round_record_next)
        self.next_hole_button.grid(row=7, column=1)

    def save_round_record_prev(self):

        if self.hole_score_entry.get():

            self.round_holes[self.hole_index]["par"] = self.round_course.get(f'{self.hole_index + 1}')
            self.round_holes[self.hole_index]["score"] = self.hole_score_entry.get()
            self.round_holes[self.hole_index]['result'] = self.calculate_result()
            self.round_holes[self.hole_index]["number_of_putts"] = self.hole_putts_entry.get()
            self.round_holes[self.hole_index]['tee_club'] = self.tee_club_dropbox.get()
            self.round_holes[self.hole_index]['fairway'] = self.fairway_dropbox.get()
            self.round_holes[self.hole_index]["gir"] = self.calculate_gir(par=self.round_holes[self.hole_index]["par"],
                                                                        score=self.round_holes[self.hole_index]["score"],
                                                                        putts=self.round_holes[self.hole_index]["number_of_putts"])
            self.round_holes[self.hole_index]["agir"] = self.calculate_agir(par=self.round_holes[self.hole_index]["par"],
                                                                        score=self.round_holes[self.hole_index]["score"],
                                                                        putts=self.round_holes[self.hole_index]["number_of_putts"])
            self.round_holes[self.hole_index]["sand_shots"] = self.hole_sand_entry.get()
            self.round_holes[self.hole_index]["penalties"] = self.hole_penalty_entry.get()
            print(self.round_holes[self.hole_index])

        self.hole_index -= 1
        print(self.all_dicts_have_values())
        self.update_hole_entry()

    def save_round_record_next(self):

        if self.hole_score_entry.get():

            self.round_holes[self.hole_index]["par"] = self.round_course.get(f'{self.hole_index + 1}')
            self.round_holes[self.hole_index]["score"] = self.hole_score_entry.get()
            self.round_holes[self.hole_index]['result'] = self.calculate_result()
            self.round_holes[self.hole_index]["number_of_putts"] = self.hole_putts_entry.get()
            self.round_holes[self.hole_index]['tee_club'] = self.tee_club_dropbox.get()
            self.round_holes[self.hole_index]['fairway'] = self.fairway_dropbox.get()
            self.round_holes[self.hole_index]["gir"] = self.calculate_gir(par=self.round_holes[self.hole_index]["par"],
                                                                        score=self.round_holes[self.hole_index]["score"],
                                                                        putts=self.round_holes[self.hole_index]["number_of_putts"])
            self.round_holes[self.hole_index]["agir"] = self.calculate_agir(par=self.round_holes[self.hole_index]["par"],
                                                                        score=self.round_holes[self.hole_index]["score"],
                                                                        putts=self.round_holes[self.hole_index]["number_of_putts"])
            self.round_holes[self.hole_index]["sand_shots"] = self.hole_sand_entry.get()
            self.round_holes[self.hole_index]["penalties"] = self.hole_penalty_entry.get()
            print(self.round_holes[self.hole_index])

        self.hole_index += 1
        print(self.all_dicts_have_values())
        self.update_hole_entry()

    def calculate_result(self):

        par = int(self.round_course[f'{(self.hole_index + 1)}'])
        score = int(self.round_holes[self.hole_index]['score'])

        if score == par:
            result = "Par"
        elif score == (par + 1):
            result = "Bogey"
        elif score == (par + 2):
            result = "Double Bogey"
        elif score == (par + 3):
            result = "Triple Bogey"
        elif score == (par + 4):
            result = "Quadruple Bogey"
        elif score == (par -1):
            result = "Birdie"
        elif score == (par - 2):
            result = "Eagle"
        elif score == (par - 3):
            result = "Albatross"
        elif score == (par - 4):
            result = "Condor"
        else:
            result = "Blob"

        return result
            
    def calculate_gir(self, par, score, putts):
        
        if int(score) - int(putts) <= int(par) - 2:
            return 1
        else:
            return 0
        
    def calculate_agir(self, par, score, putts):
        
        if int(score) - int(putts) <= int(par) - 1:
            return 1
        else:
            return 0

    def all_dicts_have_values(self):

        for hole in self.round_holes:
            
            if any(value is None or value == '' for value in hole.values()):
                return False
        return True

    def update_hole_entry(self):

        if self.hole_index == 0:
            self.prev_hole_button.grid_forget()
        else:
            self.prev_hole_button.grid(row=7,column=0)

        if self.hole_index == 17:
            self.next_hole_button.grid_forget()
            self.finish_holes_button.grid(row=7,column=1)
        else:
            self.next_hole_button.grid(row=7,column=1)

        self.hole_number_label.configure(text=self.round_holes[self.hole_index]['hole'])
        self.hole_par_label.configure(text="Par:" + str(self.round_course.get(f'{self.hole_index + 1}')))
        self.hole_score_entry.delete(0,tk.END)
        self.hole_score_entry.insert(0,self.round_holes[self.hole_index].get('score'))
        self.hole_putts_entry.delete(0,tk.END)
        self.hole_putts_entry.insert(0,self.round_holes[self.hole_index].get('number_of_putts'))
        self.tee_club_dropbox.delete(0,tk.END)
        self.tee_club_dropbox.insert(0, self.round_holes[self.hole_index].get('tee_club'))
        self.fairway_dropbox.delete(0,tk.END)
        self.fairway_dropbox.insert(0, self.round_holes[self.hole_index].get('fairway'))
        self.hole_sand_entry.delete(0,tk.END)
        self.hole_sand_entry.insert(0,self.round_holes[self.hole_index].get('sand_shots'))
        self.hole_penalty_entry.delete(0,tk.END)
        self.hole_penalty_entry.insert(0,self.round_holes[self.hole_index].get('penalties'))

    def finish_holes(self):

        self.round_holes[self.hole_index]["par"] = self.round_course.get(f'{self.hole_index + 1}')
        self.round_holes[self.hole_index]["score"] = self.hole_score_entry.get()
        self.round_holes[self.hole_index]['result'] = self.calculate_result()
        self.round_holes[self.hole_index]["number_of_putts"] = self.hole_putts_entry.get()
        self.round_holes[self.hole_index]['tee_club'] = self.tee_club_dropbox.get()
        self.round_holes[self.hole_index]['fairway'] = self.fairway_dropbox.get()
        self.round_holes[self.hole_index]["gir"] = self.calculate_gir(par=self.round_holes[self.hole_index]["par"],
                                                                      score=self.round_holes[self.hole_index]["score"],
                                                                      putts=self.round_holes[self.hole_index]["number_of_putts"])
        self.round_holes[self.hole_index]["agir"] = self.calculate_agir(par=self.round_holes[self.hole_index]["par"],
                                                                      score=self.round_holes[self.hole_index]["score"],
                                                                      putts=self.round_holes[self.hole_index]["number_of_putts"])
        self.round_holes[self.hole_index]["sand_shots"] = self.hole_sand_entry.get()
        self.round_holes[self.hole_index]["penalties"] = self.hole_penalty_entry.get()
        print(self.round_holes[self.hole_index])

        if self.all_dicts_have_values() == False:
            messagebox.showerror("Error", "One or more of your holes is incomplete!") 
        else: 

            self.save_round_record()

            try:

                with open("holes.json", "r") as file:
                    existing_holes_data = json.load(file)
            except json.JSONDecodeError:
                existing_holes_data = []
                   
            existing_holes_data.extend(self.round_holes)

            try:
                with open("holes.json", "w") as file:
                    json.dump(existing_holes_data, file, indent=4)
                messagebox.showinfo("Round saved", "Your round was saved!")
                self.reset_new_round()
            except IOError:
                print("An error occurred while writing to the file.")

    def save_round_record(self):

        self.calculate_total_putts()
        self.calculate_gross_score()
        self.calculate_score_to_par()
        self.calculate_total_sand_shots()
        self.calculate_total_penalties()
        self.calculate_total_fairways()
        self.calculate_total_gir()
        self.calculate_total_agir()

        try:

                with open("rounds.json", "r") as file:
                    existing_rounds_data = json.load(file)
        except json.JSONDecodeError:
                existing_rounds_data = []
                   
        existing_rounds_data.append(self.new_round_record)

        try:
                with open("rounds.json", "w") as file:
                    json.dump(existing_rounds_data, file, indent=4)
                print("Data has been updated!")
        except IOError:
                print("An error occurred while writing to the file.")

    def calculate_total_putts(self):

        total = 0
        for hole in self.round_holes:
            total += int(hole['number_of_putts'])
        self.new_round_record['total_putts'] = total

    def calculate_gross_score(self):

        total = 0
        for hole in self.round_holes:
            total += int(hole['score'])
        self.new_round_record['gross_score'] = total

    def calculate_score_to_par(self):

       self.new_round_record['score_to_par'] = int(self.new_round_record['gross_score']) - (self.round_course['par'])

    def calculate_total_sand_shots(self):

        total = 0
        for hole in self.round_holes:
            total += int(hole['sand_shots'])
        self.new_round_record['total_sand_shots'] = total

    def calculate_total_penalties(self):

        total = 0
        for hole in self.round_holes:
            total += int(hole['penalties'])
        self.new_round_record['total_penalties'] = total

    def calculate_total_fairways(self):

        total = 0
        for hole in self.round_holes:
            if hole['fairway'] == "Hit":
                total += 1
        self.new_round_record['total_fairways'] = total

    def calculate_total_gir(self):

        total = 0
        for hole in self.round_holes:
            total += hole['gir']
        self.new_round_record['gir'] = total

    def calculate_total_agir(self):

        total = 0
        for hole in self.round_holes:
            total += hole['agir']
        self.new_round_record['agir'] = total

    def reset_new_round(self):

        self.hole_index = 0
        self.new_hole_record = []
        self.round_holes = []
        self.window.show_home_screen()