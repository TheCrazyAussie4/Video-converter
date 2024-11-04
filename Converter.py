from ast import mod
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Function to modify and run the existing batch script based on user inputs
def modify_and_run_batch(input_file, end_format, output_path):
    try:
        # Extract the starting format from the input file's extension
        start_format = os.path.splitext(input_file)[1].lstrip(".")

        # Read the original Run.bat file with placeholders
        with open("Run.bat", "r") as file:
            template = file.read()

        # Replace placeholders with user inputs
        updated_script = (
            template.replace("{start_format}", start_format)
            .replace("{end_format}", end_format)
            .replace("{output_path}", output_path)
            .replace("{input_file}", input_file)
        )

        # Write the modified script to Run.bat
        with open("Run.bat", "w") as file:
            file.write(updated_script)

        # Run the modified batch script
        subprocess.run("Run.bat", shell=True)

        # Restore the original placeholders in Run.bat
        with open("Run.bat", "w") as file:
            file.write(template)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



# Function for the main GUI
def run_gui():
    def open_follow_up_gui(end_format, output_path):
        def run_new_conversion():
            input_file = input_file_entry.get().strip()
            if input_file:
                modify_and_run_batch(input_file, end_format, output_path)
                messagebox.showinfo("Success", "Conversion completed.")
                follow_up.destroy()
                ask_for_another_file(end_format, output_path)
            else:
                messagebox.showwarning("Input Error", "Please select a file to convert.")

        follow_up = tk.Tk()
        follow_up.title("Convert Another File")

        tk.Label(follow_up, text="Select another file to convert:").grid(row=0, column=0, padx=10, pady=5)
        input_file_entry = tk.Entry(follow_up, width=50)
        input_file_entry.grid(row=0, column=1, padx=10, pady=5)

        browse_input_button = tk.Button(follow_up, text="Browse", command=lambda: input_file_entry.insert(0, filedialog.askopenfilename()))
        browse_input_button.grid(row=0, column=2, padx=5, pady=5)

        convert_button = tk.Button(follow_up, text="Convert", command=run_new_conversion)
        convert_button.grid(row=1, column=1, pady=10)

        follow_up.mainloop()

    def ask_for_another_file(end_format, output_path):
        another = messagebox.askyesno("Another File", "Would you like to convert another file with the same settings?")
        if another:
            open_follow_up_gui(end_format, output_path)

    # Main window for initial setup
    root = tk.Tk()
    root.title("Video converter")

    # Labels and entry fields
    tk.Label(root, text="File to Convert:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    input_file_entry = tk.Entry(root, width=50)
    input_file_entry.grid(row=0, column=1, padx=10, pady=5)

    def browse_input_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            input_file_entry.delete(0, tk.END)
            input_file_entry.insert(0, file_path)

    browse_input_button = tk.Button(root, text="Browse", command=browse_input_file)
    browse_input_button.grid(row=0, column=2, padx=5, pady=5)

    tk.Label(root, text="Desired End Format (e.g., mp4):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    end_format_entry = tk.Entry(root)
    end_format_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Output Path:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    output_path_entry = tk.Entry(root, width=50)
    output_path_entry.grid(row=2, column=1, padx=10, pady=5)

    def browse_output_path():
        path = filedialog.askdirectory()
        if path:
            output_path_entry.delete(0, tk.END)
            output_path_entry.insert(0, path)

    browse_output_button = tk.Button(root, text="Browse", command=browse_output_path)
    browse_output_button.grid(row=2, column=2, padx=5, pady=5)

    def run_script():
        input_file = input_file_entry.get().strip()
        end_format = end_format_entry.get().strip()
        output_path = output_path_entry.get().strip()

        if input_file and end_format and output_path:
            root.destroy()  # Close the initial GUI before starting the script
            modify_and_run_batch(input_file, end_format, output_path)
            ask_for_another_file(end_format, output_path)
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    run_button = tk.Button(root, text="Run", command=run_script)
    run_button.grid(row=3, column=1, pady=10)

    # Start the GUI loop
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    run_gui()
