import tkinter as tk

import json

class GolfCoursesDetailScreen(tk.Frame):

    def __init__(self, master, window, selected_course_guid):
        super().__init__(master)
        self.window = window
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.selected_course_guid = selected_course_guid
        if self.selected_course_guid != None:
            self.selected_golf_course = self.get_golf_course_record()
            self.create_course_editor()

    def get_golf_course_record(self):
        for course in self.window.courses:
            if course["guid"] == self.selected_course_guid:
                return course

    def create_course_editor(self):

        self.name_label = tk.Label(self, text="Course Name: ", font=("Arial", 18))
        self.name_label.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.course_name = tk.Entry(self, font= ("Arial", 18))
        self.course_name.insert(0, self.selected_golf_course["name"])
        self.course_name.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.hole1_label = tk.Label(self, text="Hole 1 par:", font=("Arial", 18))
        self.hole1_label.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.hole1_par = tk.Entry(self, font=("Arial", 18))
        self.hole1_par.insert(0, self.selected_golf_course["1"])
        self.hole1_par.grid(row=1, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole2_label = tk.Label(self, text="Hole 2 par:", font=("Arial", 18))
        self.hole2_label.grid(row=2, column=0, sticky=tk.W+tk.E)
        self.hole2_par = tk.Entry(self, font=("Arial", 18))
        self.hole2_par.insert(0, self.selected_golf_course["2"])
        self.hole2_par.grid(row=2, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole3_label = tk.Label(self, text="Hole 3 par:", font=("Arial", 18))
        self.hole3_label.grid(row=3, column=0, sticky=tk.W+tk.E)
        self.hole3_par = tk.Entry(self, font=("Arial", 18))
        self.hole3_par.insert(0, self.selected_golf_course["3"])
        self.hole3_par.grid(row=3, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole4_label = tk.Label(self, text="Hole 4 par:", font=("Arial", 18))
        self.hole4_label.grid(row=4, column=0, sticky=tk.W+tk.E)
        self.hole4_par = tk.Entry(self, font=("Arial", 18))
        self.hole4_par.insert(0, self.selected_golf_course["4"])
        self.hole4_par.grid(row=4, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole5_label = tk.Label(self, text="Hole 5 par:", font=("Arial", 18))
        self.hole5_label.grid(row=5, column=0, sticky=tk.W+tk.E)
        self.hole5_par = tk.Entry(self, font=("Arial", 18))
        self.hole5_par.insert(0, self.selected_golf_course["5"])
        self.hole5_par.grid(row=5, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole6_label = tk.Label(self, text="Hole 6 par:", font=("Arial", 18))
        self.hole6_label.grid(row=6, column=0, sticky=tk.W+tk.E)
        self.hole6_par = tk.Entry(self, font=("Arial", 18))
        self.hole6_par.insert(0, self.selected_golf_course["6"])
        self.hole6_par.grid(row=6, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole7_label = tk.Label(self, text="Hole 7 par:", font=("Arial", 18))
        self.hole7_label.grid(row=7, column=0, sticky=tk.W+tk.E)
        self.hole7_par = tk.Entry(self, font=("Arial", 18))
        self.hole7_par.insert(0, self.selected_golf_course["7"])
        self.hole7_par.grid(row=7, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole8_label = tk.Label(self, text="Hole 8 par:", font=("Arial", 18))
        self.hole8_label.grid(row=8, column=0, sticky=tk.W+tk.E)
        self.hole8_par = tk.Entry(self, font=("Arial", 18))
        self.hole8_par.insert(0, self.selected_golf_course["8"])
        self.hole8_par.grid(row=8, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole9_label = tk.Label(self, text="Hole 9 par:", font=("Arial", 18))
        self.hole9_label.grid(row=9, column=0, sticky=tk.W+tk.E)
        self.hole9_par = tk.Entry(self, font=("Arial", 18))
        self.hole9_par.insert(0, self.selected_golf_course["9"])
        self.hole9_par.grid(row=9, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole10_label = tk.Label(self, text="Hole 10 par:", font=("Arial", 18))
        self.hole10_label.grid(row=10, column=0, sticky=tk.W+tk.E)
        self.hole10_par = tk.Entry(self, font=("Arial", 18))
        self.hole10_par.insert(0, self.selected_golf_course["10"])
        self.hole10_par.grid(row=10, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole11_label = tk.Label(self, text="Hole 11 par:", font=("Arial", 18))
        self.hole11_label.grid(row=11, column=0, sticky=tk.W+tk.E)
        self.hole11_par = tk.Entry(self, font=("Arial", 18))
        self.hole11_par.insert(0, self.selected_golf_course["11"])
        self.hole11_par.grid(row=11, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole12_label = tk.Label(self, text="Hole 12 par:", font=("Arial", 18))
        self.hole12_label.grid(row=12, column=0, sticky=tk.W+tk.E)
        self.hole12_par = tk.Entry(self, font=("Arial", 18))
        self.hole12_par.insert(0, self.selected_golf_course["12"])
        self.hole12_par.grid(row=12, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole13_label = tk.Label(self, text="Hole 13 par:", font=("Arial", 18))
        self.hole13_label.grid(row=13, column=0, sticky=tk.W+tk.E)
        self.hole13_par = tk.Entry(self, font=("Arial", 18))
        self.hole13_par.insert(0, self.selected_golf_course["13"])
        self.hole13_par.grid(row=13, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole14_label = tk.Label(self, text="Hole 14 par:", font=("Arial", 18))
        self.hole14_label.grid(row=14, column=0, sticky=tk.W+tk.E)
        self.hole14_par = tk.Entry(self, font=("Arial", 18))
        self.hole14_par.insert(0, self.selected_golf_course["14"])
        self.hole14_par.grid(row=14, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole15_label = tk.Label(self, text="Hole 15 par:", font=("Arial", 18))
        self.hole15_label.grid(row=15, column=0, sticky=tk.W+tk.E)
        self.hole15_par = tk.Entry(self, font=("Arial", 18))
        self.hole15_par.insert(0, self.selected_golf_course["15"])
        self.hole15_par.grid(row=15, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole16_label = tk.Label(self, text="Hole 16 par:", font=("Arial", 18))
        self.hole16_label.grid(row=16, column=0, sticky=tk.W+tk.E)
        self.hole16_par = tk.Entry(self, font=("Arial", 18))
        self.hole16_par.insert(0, self.selected_golf_course["16"])
        self.hole16_par.grid(row=16, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole17_label = tk.Label(self, text="Hole 17 par:", font=("Arial", 18))
        self.hole17_label.grid(row=17, column=0, sticky=tk.W+tk.E)
        self.hole17_par = tk.Entry(self, font=("Arial", 18))
        self.hole17_par.insert(0, self.selected_golf_course["17"])
        self.hole17_par.grid(row=17, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole18_label = tk.Label(self, text="Hole 18 par:", font=("Arial", 18))
        self.hole18_label.grid(row=18, column=0, sticky=tk.W+tk.E)
        self.hole18_par = tk.Entry(self, font=("Arial", 18))
        self.hole18_par.insert(0, self.selected_golf_course["18"])
        self.hole18_par.grid(row=18, column=1, sticky=tk.W+tk.E, padx=10)

        par_label = tk.Label(self, text="Par: ", font=("Arial", 18))
        par_label.grid(row=20, column=0, sticky=tk.W+tk.E)
        self.par = tk.Label(self, text=self.selected_golf_course["par"], font=("Arial", 18))
        self.par.grid(row=20, column=1, sticky=tk.W+tk.E)

        save_btn = tk.Button(self, text="Save", font=("Arial", 18),
                            command=lambda: [self.update_golf_course()])
        save_btn.grid(row=21, column=0, sticky=tk.W+tk.E)
       
        self.pack(fill=tk.BOTH, expand=True)              

    def update_golf_course(self):

        par_calc = []

        par_calc.append(int(self.hole1_par.get()))
        par_calc.append(int(self.hole2_par.get()))
        par_calc.append(int(self.hole3_par.get()))
        par_calc.append(int(self.hole4_par.get()))
        par_calc.append(int(self.hole5_par.get()))
        par_calc.append(int(self.hole6_par.get()))
        par_calc.append(int(self.hole7_par.get()))
        par_calc.append(int(self.hole8_par.get()))
        par_calc.append(int(self.hole9_par.get()))
        par_calc.append(int(self.hole10_par.get()))
        par_calc.append(int(self.hole11_par.get()))
        par_calc.append(int(self.hole12_par.get()))
        par_calc.append(int(self.hole13_par.get()))
        par_calc.append(int(self.hole14_par.get()))
        par_calc.append(int(self.hole15_par.get()))
        par_calc.append(int(self.hole16_par.get()))
        par_calc.append(int(self.hole17_par.get()))
        par_calc.append(int(self.hole18_par.get()))

        self.selected_golf_course['name'] = self.course_name.get()
        self.selected_golf_course['1'] = self.hole1_par.get()
        self.selected_golf_course['2'] = self.hole2_par.get()
        self.selected_golf_course['3'] = self.hole3_par.get()
        self.selected_golf_course['4'] = self.hole4_par.get()   
        self.selected_golf_course['5'] = self.hole5_par.get()
        self.selected_golf_course['6'] = self.hole6_par.get()
        self.selected_golf_course['7'] = self.hole7_par.get()
        self.selected_golf_course['8'] = self.hole8_par.get()
        self.selected_golf_course['9'] = self.hole9_par.get()
        self.selected_golf_course['10'] = self.hole10_par.get()
        self.selected_golf_course['11'] = self.hole11_par.get()
        self.selected_golf_course['12'] = self.hole12_par.get()
        self.selected_golf_course['13'] = self.hole13_par.get()
        self.selected_golf_course['14'] = self.hole14_par.get()
        self.selected_golf_course['15'] = self.hole15_par.get()
        self.selected_golf_course['16'] = self.hole16_par.get()
        self.selected_golf_course['17'] = self.hole17_par.get()
        self.selected_golf_course['18'] = self.hole18_par.get()
        self.selected_golf_course['par'] = sum(par_calc)
        
        try:

            with open("golf_courses.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = [] 

        for data in existing_data:
            if data.get('guid') == self.selected_course_guid:
                # Update the existing dictionary's contents
                data.update(self.selected_golf_course)
                print("Updated data:", data)
                break
        
        # Save updated data back to JSON
        try:
            with open("golf_courses.json", "w") as file:
                json.dump(existing_data, file, indent=4)
            print("Data has been updated!")
        except IOError:
            print("An error occurred while writing to the file.")