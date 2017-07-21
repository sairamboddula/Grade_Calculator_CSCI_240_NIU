from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class GradeCalc:

    def __init__(self, master):
        self.logoStyle = ttk.Style()
        self.logoStyle.configure("BW.TLabel", foreground="white", background="black", font=('Calibri', 18, 'bold'))

        self.logoFrame = ttk.Frame(master)
        ttk.Label(self.logoFrame, text="CSCI 240 Grade Calculator", style="BW.TLabel") \
            .grid(row=0, column=0, columnspan=2)
        self.logoFrame.pack()

        self.firstFrame = ttk.LabelFrame(master, text="Assignments & Quizzes", padding="5p")
        self.firstFrame.pack(padx=5, pady=5)

        vcmd = (master.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.assignmentsFrame = ttk.LabelFrame(self.firstFrame, text="Assignments", padding="5p")
        self.assignmentsFrame.pack(side=LEFT, padx=2)
        ttk.Label(self.assignmentsFrame, text="Assignment 1: ").grid(row=0, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 2: ").grid(row=1, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 3: ").grid(row=2, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 4: ").grid(row=3, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 5: ").grid(row=4, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 6: ").grid(row=5, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 7: ").grid(row=6, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 8: ").grid(row=7, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 9: ").grid(row=8, column=0, sticky=E)
        ttk.Label(self.assignmentsFrame, text="Assignment 10: ").grid(row=9, column=0, sticky=E)
        self.assignOne = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignOne.grid(row=0, column=1)
        self.assignTwo = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignTwo.grid(row=1, column=1)
        self.assignThree = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignThree.grid(row=2, column=1)
        self.assignFour = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignFour.grid(row=3, column=1)
        self.assignFive = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignFive.grid(row=4, column=1)
        self.assignSix = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignSix.grid(row=5, column=1)
        self.assignSeven = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignSeven.grid(row=6, column=1)
        self.assignEight = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignEight.grid(row=7, column=1)
        self.assignNine = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignNine.grid(row=8, column=1)
        self.assignTen = ttk.Entry(self.assignmentsFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.assignTen.grid(row=9, column=1)

        self.quizzesFrame = ttk.LabelFrame(self.firstFrame, text="Quizzes", padding="5p")
        self.quizzesFrame.pack(side=RIGHT, padx=2)
        ttk.Label(self.quizzesFrame, text="Quiz 1: ").grid(row=0, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 2: ").grid(row=1, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 3: ").grid(row=2, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 4: ").grid(row=3, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 5: ").grid(row=4, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 6: ").grid(row=5, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 7: ").grid(row=6, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 8: ").grid(row=7, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 9: ").grid(row=8, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 10: ").grid(row=9, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 11: ").grid(row=10, column=0, sticky=E)
        ttk.Label(self.quizzesFrame, text="Quiz 12: ").grid(row=11, column=0, sticky=E)
        self.quizOne = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizOne.grid(row=0, column=1)
        self.quizTwo = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizTwo.grid(row=1, column=1)
        self.quizThree = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizThree.grid(row=2, column=1)
        self.quizFour = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizFour.grid(row=3, column=1)
        self.quizFive = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizFive.grid(row=4, column=1)
        self.quizSix = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizSix.grid(row=5, column=1)
        self.quizSeven = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizSeven.grid(row=6, column=1)
        self.quizEight = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizEight.grid(row=7, column=1)
        self.quizNine = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizNine.grid(row=8, column=1)
        self.quizTen = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizTen.grid(row=9, column=1)
        self.quizEleven = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizEleven.grid(row=10, column=1)
        self.quizTwelve = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.quizTwelve.grid(row=11, column=1)

        self.secondFrame = ttk.LabelFrame(master, text="Examinations", padding="5p")
        self.secondFrame.pack(padx=5, pady=5)
        ttk.Label(self.secondFrame, text="Midterm 1: ").grid(row=0, column=0, sticky=E)
        ttk.Label(self.secondFrame, text="Midterm 2: ").grid(row=1, column=0, sticky=E)
        ttk.Label(self.secondFrame, text="Finals: ").grid(row=2, column=0, sticky=E)
        self.midtermOne = ttk.Entry(self.secondFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.midtermOne.grid(row=0, column=1)
        self.midtermTwo = ttk.Entry(self.secondFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.midtermTwo.grid(row=1, column=1)
        self.finalExam = ttk.Entry(self.secondFrame, justify=RIGHT, validate='key', validatecommand=vcmd)
        self.finalExam.grid(row=2, column=1)

        self.thirdFrame = ttk.Frame(master, padding="5p")
        self.thirdFrame.pack(padx=5, pady=5)
        self.calculateBtn = ttk.Button(self.thirdFrame, text="Calculate my grade!", command=self.calculate_grade)
        self.calculateBtn.pack()

    def calculate_grade(self):

        assignment_average = self.get_assignment_avg()
        quiz_average = self.get_quiz_avg()
        exam_average = self.get_exam_avg()

        result = self.calculate_result(assignment_average, quiz_average, exam_average)
        self.display_result(result)

    def get_assignment_avg(self):
        return (float(self.assignOne.get())
                + float(self.assignTwo.get())
                + float(self.assignThree.get())
                + float(self.assignFour.get())
                + float(self.assignFive.get())
                + float(self.assignSix.get())
                + float(self.assignSeven.get())
                + float(self.assignEight.get())
                + float(self.assignNine.get())
                + float(self.assignTen.get())) / 10.0

    def get_quiz_avg(self):
        return (float(self.quizOne.get())
                + float(self.quizTwo.get())
                + float(self.quizThree.get())
                + float(self.quizFour.get())
                + float(self.quizFive.get())
                + float(self.quizSix.get())
                + float(self.quizSeven.get())
                + float(self.quizEight.get())
                + float(self.quizNine.get())
                + float(self.quizTen.get())) / 10.0

    def get_exam_avg(self):
        return (float(self.midtermOne.get())
                + float(self.midtermTwo.get())
                + float(self.finalExam.get())) / 3.0

    @staticmethod
    def calculate_result(assignment_average, quiz_average, exam_average):
        result = (assignment_average * 0.6) + (quiz_average * 0.4) + exam_average
        return result

    @staticmethod
    def display_result(result):
        if result == 20.0:
            messagebox.showinfo("info", "You scored an A!")
        else:
            messagebox.showinfo("info", "You didn't score an A!")

    @staticmethod
    def validate(action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if action == '1':
            if text in '0123456789.-+':
                try:
                    if float(value_if_allowed) and (float(value_if_allowed) <= 100.0):
                        return True
                    else:
                        return False
                except ValueError:
                    return False
            else:
                return False
        else:
            return True


def main():
    root = Tk()
    app = GradeCalc(root)
    root.title("CSCI 240 NIU - Grade Calculator")
    root.iconbitmap('niu_logo.ico')
    root.mainloop()


if __name__ == "__main__":
    main()
