from tkinter import *
import mysql.connector

#GUI class
class AttendanceGUI:
    def __init__(self, master):
        #create a database connection
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='attendance_db'
        )
        self.c = self.conn.cursor()

        #create a table if it does not exist
        self.c.execute("CREATE TABLE IF NOT EXISTS attendance (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), present INTEGER, absent INTEGER)")

        #GUI elements
        self.master = master
        master.title("Attendance System")


        #Name label and entry box
        self.name_label = Label(master, text="Name:")
        # self.name_label.grid(row=1, column=1)
        self.name_label.place(relx = 0.2, rely=0.1)
        self.name_entry = Entry(master)
        # self.name_entry.grid(row=1, column=2)
        self.name_entry.place(relx = 0.4, rely=0.1)


        #Present checkbox
        self.present_var = IntVar()
        self.present = Checkbutton(master, text="Present", variable=self.present_var)
        self.present.place(relx = 0.3, rely = 0.3)
        # self.present.grid(row=2, column=1)

        # Absent checkbox
        self.absent_var = IntVar()
        self.absent = Checkbutton(master, text="Absent", variable=self.absent_var)
        self.absent.place(relx = 0.6, rely = 0.3)

        # self.absent.grid(row=2, column=2)

        #Submit button
        self.submit_button = Button(master, text="Submit", command=self.submit)
        self.submit_button.place(relx = 0.4, rely = 0.5)

        # self.submit_button.grid(row=4, column=0)

    #Submit function
    def submit(self):
        name = self.name_entry.get()
        present = self.present_var.get()
        absent = self.absent_var.get()

        #insert data into database
        self.c.execute("INSERT INTO attendance (name, present, absent) VALUES (%s, %s, %s)", (name, present, absent))

        self.conn.commit()

        #clear name entry box
        self.name_entry.delete(0, "end")
        self.present_var.set(0)
        self.absent_var.set(0)


#main program
root = Tk()
root.geometry("400x150")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
app = AttendanceGUI(root)
root.mainloop()