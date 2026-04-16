import tkinter as tk
import numpy as np

class SalaryPredApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Depi round 4 DS")
        self.root.geometry("500x400")
        self.create_widgets()
    def create_widgets(self):
        header = tk.Label(self.root, text="Mohab Serag Eldin", bg="blue", fg="white", font=("Arial", 28, "bold"))
        header.pack(fill=tk.X)

        # Sidebar
        sidebar = tk.Frame(self.root, bg="lightgrey", width=150)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        projects = ["Linear Regression", "Project2", "Project3", "Project4", "Project5", "Project6", "Project7", "Project8", "Project9"]

        for project in projects:
            lbl = tk.Label(sidebar, text=project, bg="lightgrey", font=("Arial", 12), anchor="w")
            lbl.pack(fill=tk.X, padx=7, pady=7)

        # Main section for salary prediction
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20)

        title = tk.Label(main_frame, text="Salary Prediction", font=("Arial", 24))
        title.pack(pady=10)
        
        # Experience input
        label = tk.Label(main_frame, text="Enter years of experience:", font=("Arial", 18))
        label.pack()
        self.experience_entry = tk.Entry(main_frame, font=("Arial", 18))
        self.experience_entry.pack()

        # Execute button
        execute_button = tk.Button(main_frame, text="Execute", command=self.predict_salary, bg="grey", fg="black", font=("Arial", 18))
        execute_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(main_frame, text="", font=("Arial", 20, "bold"))
        self.result_label.pack()

    def predict_salary(self):
        try:
            new_input = float(self.experience_entry.get())
            predict_salary = 9357 * new_input + 26089
            self.result_label.config(text=f"Your Expected Salary is: {int(predict_salary)}", fg="green")
        except ValueError:
            self.result_label.config(text="Please enter a valid number", fg="red")






if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryPredApp(root)
    root.mainloop()