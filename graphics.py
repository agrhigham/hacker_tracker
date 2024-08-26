import tkinter as tk

from uuid import uuid4

import json

from new_round_screen import NewRoundScreen

from edit_rounds_screen import RoundsScreen

from round_detail_screen import RoundDetailScreen

from golf_course_screen import GolfCoursesScreen

from course_detail_screen import GolfCoursesDetailScreen

class Window():

    def __init__(self, width, height):

        self.__root = tk.Tk()
        self.__root.title("Hacker Tracker")
        self.__root.protocol("WM_DELETE_WINDOW", self.__root.destroy)
        self.__canvas = tk.Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.buttons = [] 
        self.round_records = []
        self.courses = self.load_golf_courses()
        self.load_rounds()

    def run(self):
        
        self.__root.mainloop()

    def get_root(self):
        
        return self.__root

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

        self.round_records.sort(key=lambda x: x['gross_score'])
        self.lowest_round = self.round_records[0]

        # self.round_records.sort(key=lambda x: x['date'])

    def add_screens(self):
        self.button_frame = ButtonFrame(self.buttons, master=self.__root, window=self)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)
        self.home_screen = HomeScreen(master=self.__root,low_round= self.lowest_round)
        self.golf_courses_screen = GolfCoursesScreen(master=self.__root, window=self)
        self.create_course_screen = CreateCourseScreen(master=self.__root, window=self)
        self.golf_courses_detail_screen = GolfCoursesDetailScreen(master=self.__root, window=self, selected_course_guid=None)
        self.new_rounds_screen = NewRoundScreen(master=self.__root, window=self, courses=self.courses)
        self.rounds_screen = RoundsScreen(master=self.__root, window=self)
        self.round_detail_screen = RoundDetailScreen(master=self.__root, window= self, selected_round_guid= None)
        self.show_home_screen()

    def show_home_screen(self):
        self.home_screen.pack()
        self.golf_courses_screen.pack_forget()
        self.new_rounds_screen.pack_forget()
        self.golf_courses_detail_screen.pack_forget()
        self.create_course_screen.pack_forget()
        self.rounds_screen.pack_forget()
        self.round_detail_screen.pack_forget()

    def show_golf_courses_screen(self):
        self.golf_courses_screen.pack(fill="x")
        self.home_screen.pack_forget()
        self.new_rounds_screen.pack_forget()
        self.golf_courses_detail_screen.pack_forget()
        self.create_course_screen.pack_forget()
        self.rounds_screen.pack_forget()
        self.round_detail_screen.pack_forget()

    def show_golf_courses_detail_screen(self):
        self.golf_courses_detail_screen.pack()
        self.home_screen.pack_forget()
        self.golf_courses_screen.pack_forget()
        self.new_rounds_screen.pack_forget()
        self.create_course_screen.pack_forget()
        self.rounds_screen.pack_forget()
        self.round_detail_screen.pack_forget()

    def show_create_course_screen(self):
        self.create_course_screen.pack()
        self.golf_courses_detail_screen.pack_forget()
        self.home_screen.pack_forget()
        self.golf_courses_screen.pack_forget()
        self.new_rounds_screen.pack_forget()
        self.rounds_screen.pack_forget()
        self.rounds_screen.pack_forget()
        self.round_detail_screen.pack_forget()

    def show_rounds_screen(self):
        self.load_rounds()
        self.rounds_screen.pack()
        self.new_rounds_screen.pack_forget()
        self.home_screen.pack_forget()
        self.golf_courses_screen.pack_forget()
        self.golf_courses_detail_screen.pack_forget()
        self.create_course_screen.pack_forget()
        self.round_detail_screen.pack_forget()

    def show_round_detail_screen(self):
        self.round_detail_screen.pack()
        self.rounds_screen.pack_forget()
        self.new_rounds_screen.pack_forget()
        self.home_screen.pack_forget()
        self.golf_courses_screen.pack_forget()
        self.golf_courses_detail_screen.pack_forget()
        self.create_course_screen.pack_forget()
        
    def show_new_round_screen(self):
        self.new_rounds_screen.pack()
        self.home_screen.pack_forget()
        self.golf_courses_screen.pack_forget()
        self.golf_courses_detail_screen.pack_forget()
        self.create_course_screen.pack_forget()
        self.rounds_screen.pack_forget()
        self.round_detail_screen.pack_forget()

    def highlight_button(self, clicked_button):
        for button in self.buttons:
            button.config(bg='gray', relief='raised')
        clicked_button.config(bg='white', relief='sunken')

class ButtonFrame(tk.Frame):

    def __init__(self, buttons_list, master= None, window= None):
        super().__init__(master)
        self.window = window
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        btn1 = tk.Button(
            self, text="Home", font=('Arial', 18), 
            command=lambda: [self.window.show_home_screen(), self.window.highlight_button(btn1)])
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
        buttons_list.append(btn1)

        btn2 = tk.Button(
            self, text="Golf Courses", font=('Arial', 18), 
            command=lambda: [self.window.show_golf_courses_screen(), self.window.highlight_button(btn2)])
        btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
        buttons_list.append(btn2)

        btn3 = tk.Button(
            self, text="Rounds", font=('Arial', 18),
            command=lambda: [self.window.show_rounds_screen(), self.window.highlight_button(btn3)])
        btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
        buttons_list.append(btn3)

        self.pack()

class HomeScreen(tk.Frame):
    def __init__(self, master= None, low_round= None):
        super().__init__(master)
        self.lowest_round = low_round
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        home_frame = tk.Frame(master=self)
        home_frame.columnconfigure(0, weight=1)
        home_frame.pack(side=tk.BOTTOM)

        lowest_round_label = tk.Label(home_frame, font=("Arial", 18))
        lowest_round_label.grid(row=1,column=0, columnspan=2, pady=10,padx=10)

        if int(self.lowest_round['gross_score']) < 95:
            lowest_round_label.config(text=f"Your lowest score to date is {self.lowest_round['gross_score']}! Nice improvement, keeping going!")
        elif int(self.lowest_round['gross_score']) < 90:
            lowest_round_label.config(text=f"Your lowest score to date is {self.lowest_round['gross_score']}! Wow, you have come along way!")
        elif int(self.lowest_round['gross_score']) < 85:
            lowest_round_label.config(text=f"Your lowest score to date is {self.lowest_round['gross_score']}! OMG, you are a golfer!")
        else:
            lowest_round_label.config(text=f"Your lowest score to date is {self.lowest_round['gross_score']}! You can do better than that!")

class CreateCourseScreen(tk.Frame):

    def __init__(self, master, window):
        super().__init__(master)
        self.window = window
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.new_golf_course = {}
        self.create_course_editor()

    def create_course_editor(self):

        self.name_label = tk.Label(self, text="Course Name: ", font=("Arial", 18))
        self.name_label.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.course_name = tk.Entry(self, font= ("Arial", 18))
        self.course_name.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.hole1_label = tk.Label(self, text="Hole 1 par:", font=("Arial", 18))
        self.hole1_label.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.hole1_par = tk.Entry(self, font=("Arial", 18))
        self.hole1_par.grid(row=1, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole2_label = tk.Label(self, text="Hole 2 par:", font=("Arial", 18))
        self.hole2_label.grid(row=2, column=0, sticky=tk.W+tk.E)
        self.hole2_par = tk.Entry(self, font=("Arial", 18))
        self.hole2_par.grid(row=2, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole3_label = tk.Label(self, text="Hole 3 par:", font=("Arial", 18))
        self.hole3_label.grid(row=3, column=0, sticky=tk.W+tk.E)
        self.hole3_par = tk.Entry(self, font=("Arial", 18))
        self.hole3_par.grid(row=3, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole4_label = tk.Label(self, text="Hole 4 par:", font=("Arial", 18))
        self.hole4_label.grid(row=4, column=0, sticky=tk.W+tk.E)
        self.hole4_par = tk.Entry(self, font=("Arial", 18))
        self.hole4_par.grid(row=4, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole5_label = tk.Label(self, text="Hole 5 par:", font=("Arial", 18))
        self.hole5_label.grid(row=5, column=0, sticky=tk.W+tk.E)
        self.hole5_par = tk.Entry(self, font=("Arial", 18))
        self.hole5_par.grid(row=5, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole6_label = tk.Label(self, text="Hole 6 par:", font=("Arial", 18))
        self.hole6_label.grid(row=6, column=0, sticky=tk.W+tk.E)
        self.hole6_par = tk.Entry(self, font=("Arial", 18))
        self.hole6_par.grid(row=6, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole7_label = tk.Label(self, text="Hole 7 par:", font=("Arial", 18))
        self.hole7_label.grid(row=7, column=0, sticky=tk.W+tk.E)
        self.hole7_par = tk.Entry(self, font=("Arial", 18))
        self.hole7_par.grid(row=7, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole8_label = tk.Label(self, text="Hole 8 par:", font=("Arial", 18))
        self.hole8_label.grid(row=8, column=0, sticky=tk.W+tk.E)
        self.hole8_par = tk.Entry(self, font=("Arial", 18))
        self.hole8_par.grid(row=8, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole9_label = tk.Label(self, text="Hole 9 par:", font=("Arial", 18))
        self.hole9_label.grid(row=9, column=0, sticky=tk.W+tk.E)
        self.hole9_par = tk.Entry(self, font=("Arial", 18))
        self.hole9_par.grid(row=9, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole10_label = tk.Label(self, text="Hole 10 par:", font=("Arial", 18))
        self.hole10_label.grid(row=10, column=0, sticky=tk.W+tk.E)
        self.hole10_par = tk.Entry(self, font=("Arial", 18))
        self.hole10_par.grid(row=10, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole11_label = tk.Label(self, text="Hole 11 par:", font=("Arial", 18))
        self.hole11_label.grid(row=11, column=0, sticky=tk.W+tk.E)
        self.hole11_par = tk.Entry(self, font=("Arial", 18))
        self.hole11_par.grid(row=11, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole12_label = tk.Label(self, text="Hole 12 par:", font=("Arial", 18))
        self.hole12_label.grid(row=12, column=0, sticky=tk.W+tk.E)
        self.hole12_par = tk.Entry(self, font=("Arial", 18))
        self.hole12_par.grid(row=12, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole13_label = tk.Label(self, text="Hole 13 par:", font=("Arial", 18))
        self.hole13_label.grid(row=13, column=0, sticky=tk.W+tk.E)
        self.hole13_par = tk.Entry(self, font=("Arial", 18))
        self.hole13_par.grid(row=13, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole14_label = tk.Label(self, text="Hole 14 par:", font=("Arial", 18))
        self.hole14_label.grid(row=14, column=0, sticky=tk.W+tk.E)
        self.hole14_par = tk.Entry(self, font=("Arial", 18))
        self.hole14_par.grid(row=14, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole15_label = tk.Label(self, text="Hole 15 par:", font=("Arial", 18))
        self.hole15_label.grid(row=15, column=0, sticky=tk.W+tk.E)
        self.hole15_par = tk.Entry(self, font=("Arial", 18))
        self.hole15_par.grid(row=15, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole16_label = tk.Label(self, text="Hole 16 par:", font=("Arial", 18))
        self.hole16_label.grid(row=16, column=0, sticky=tk.W+tk.E)
        self.hole16_par = tk.Entry(self, font=("Arial", 18))
        self.hole16_par.grid(row=16, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole17_label = tk.Label(self, text="Hole 17 par:", font=("Arial", 18))
        self.hole17_label.grid(row=17, column=0, sticky=tk.W+tk.E)
        self.hole17_par = tk.Entry(self, font=("Arial", 18))
        self.hole17_par.grid(row=17, column=1, sticky=tk.W+tk.E, padx=10)

        self.hole18_label = tk.Label(self, text="Hole 18 par:", font=("Arial", 18))
        self.hole18_label.grid(row=18, column=0, sticky=tk.W+tk.E)
        self.hole18_par = tk.Entry(self, font=("Arial", 18))
        self.hole18_par.grid(row=18, column=1, sticky=tk.W+tk.E, padx=10)

        save_btn = tk.Button(self, text="Save", font=("Arial", 18),
                            command=lambda: [self.save_golf_course()])
        save_btn.grid(row=21, column=0, sticky=tk.W+tk.E)
       
        self.pack(fill=tk.BOTH, expand=True)              

    def save_golf_course(self):

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

        self.new_golf_course['guid'] = str(uuid4())
        self.new_golf_course['name'] = self.course_name.get()
        self.new_golf_course['holes'] = 18
        self.new_golf_course['par'] = sum(par_calc)
        self.new_golf_course['1'] = self.hole1_par.get()
        self.new_golf_course['2'] = self.hole2_par.get()
        self.new_golf_course['3'] = self.hole3_par.get()
        self.new_golf_course['4'] = self.hole4_par.get()   
        self.new_golf_course['5'] = self.hole5_par.get()
        self.new_golf_course['6'] = self.hole6_par.get()
        self.new_golf_course['7'] = self.hole7_par.get()
        self.new_golf_course['8'] = self.hole8_par.get()
        self.new_golf_course['9'] = self.hole9_par.get()
        self.new_golf_course['10'] = self.hole10_par.get()
        self.new_golf_course['11'] = self.hole11_par.get()
        self.new_golf_course['12'] = self.hole12_par.get()
        self.new_golf_course['13'] = self.hole13_par.get()
        self.new_golf_course['14'] = self.hole14_par.get()
        self.new_golf_course['15'] = self.hole15_par.get()
        self.new_golf_course['16'] = self.hole16_par.get()
        self.new_golf_course['17'] = self.hole17_par.get()
        self.new_golf_course['18'] = self.hole18_par.get()

        try:

            with open("golf_courses.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = [] 

        existing_data.append(self.new_golf_course)
        
        # Save updated data back to JSON
        try:
            with open("golf_courses.json", "w") as file:
                json.dump(existing_data, file, indent=4)
            print("Data has been updated!")
        except IOError:
            print("An error occurred while writing to the file.")