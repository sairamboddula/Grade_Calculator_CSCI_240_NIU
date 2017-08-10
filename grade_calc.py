from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class GradeCalc:

    def __init__(self, master):
        self.logoStyle = ttk.Style()
        self.logoStyle.configure("BW.TLabel", foreground="white", background="black", font=('Calibri', 20, 'bold'))

        self.logoFrame = ttk.Frame(master)
        self.logo = PhotoImage(file='C:\\Users\\Ram\\PycharmProjects\\GradeCalculator\\NIU_Logo.gif').subsample(2, 2)
        self.logoLabel = ttk.Label(self.logoFrame, image=self.logo, text="CSCI 240 Grade Calculator", style="BW.TLabel"
                                   , compound='left')
        self.logoLabel.grid(row=0, column=0, columnspan=2)
        self.logoFrame.pack(pady=10)

        self.firstFrame = ttk.LabelFrame(master, text="Assignments & Quizzes", padding="5p")
        self.firstFrame.pack(padx=5, pady=5)

        vcmd = (master.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        qcmd = (master.register(self.validate_quiz),
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
        self.quizOne = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizOne.grid(row=0, column=1)
        self.quizTwo = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizTwo.grid(row=1, column=1)
        self.quizThree = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizThree.grid(row=2, column=1)
        self.quizFour = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizFour.grid(row=3, column=1)
        self.quizFive = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizFive.grid(row=4, column=1)
        self.quizSix = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizSix.grid(row=5, column=1)
        self.quizSeven = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizSeven.grid(row=6, column=1)
        self.quizEight = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizEight.grid(row=7, column=1)
        self.quizNine = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizNine.grid(row=8, column=1)
        self.quizTen = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizTen.grid(row=9, column=1)
        self.quizEleven = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
        self.quizEleven.grid(row=10, column=1)
        self.quizTwelve = ttk.Entry(self.quizzesFrame, justify=RIGHT, validate='key', validatecommand=qcmd)
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

        self.statusBarFrame = ttk.Frame(master)
        self.statusBarFrame.pack(fill=X, pady=5)
        self.statusBarText = StringVar()
        self.statusBarLabel = Label(self.statusBarFrame, bd=1, relief=SUNKEN, anchor=W
                                    , textvariable=self.statusBarText
                                    , font=('arial', 8, 'normal'))
        self.statusBarLabel.pack(fill=X)
        self.statusBarText.set("Ready")

    def calculate_grade(self):

        assignment_average = self.get_assignment_avg()
        quiz_and_exam_average = self.get_quiz_and_exam_avg()

        result = self.calculate_result(assignment_average, quiz_and_exam_average)
        self.display_result(result)

    def get_assignment_avg(self):
        assign_mark_list = [float(self.assignOne.get())
                            , float(self.assignTwo.get())
                            , float(self.assignThree.get())
                            , float(self.assignFour.get())
                            , float(self.assignFive.get())
                            , float(self.assignSix.get())
                            , float(self.assignSeven.get())
                            , float(self.assignEight.get())
                            , float(self.assignNine.get())
                            , float(self.assignTen.get())]

        return sum(assign_mark_list) / 1000.0

    def get_quiz_and_exam_avg(self):
        quiz_mark_list = [float(self.quizOne.get())
                            , float(self.quizTwo.get())
                            , float(self.quizThree.get())
                            , float(self.quizFour.get())
                            , float(self.quizFive.get())
                            , float(self.quizSix.get())
                            , float(self.quizSeven.get())
                            , float(self.quizEight.get())
                            , float(self.quizNine.get())
                            , float(self.quizTen.get())
                            , float(self.quizEleven.get())
                            , float(self.quizTwelve.get())]

        exam_mark_list = [float(self.midtermOne.get())
                            , float(self.midtermTwo.get())
                            , float(self.finalExam.get())]

        quiz_mark_list.sort()

        return (sum(quiz_mark_list[2:])+sum(exam_mark_list)) / 400.0

    @staticmethod
    def calculate_result(assignment_average, quiz_and_exam_average):
        return (assignment_average * 70) + (quiz_and_exam_average * 30)

    @staticmethod
    def display_result(result):
        if 90 <= result <= 100:
            message = "You scored an A"
        elif 80 <= result <= 89.99:
            message = "You scored a B"
        elif 70 <= result <= 79.99:
            message = "You scored a C"
        elif 60 <= result <= 69.99:
            message = "You scored a D"
        else:
            message = "You scored an F"

        messagebox.showinfo("info", "You got " + str(result) + "%\n" + message)

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

    @staticmethod
    def validate_quiz(action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if action == '1':
            if text in '0123456789.-+':
                try:
                    if float(value_if_allowed) and (float(value_if_allowed) <= 10.0):
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
