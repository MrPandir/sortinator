from tkinter import messagebox

import customtkinter as ctk

from .sorting import SortingAlgorithm, SortingDirection, sort_executor
from .utils import format_output_numbers, measure_time, parse_input, spawn

# Create the main application window
root = ctk.CTk()
root.title("Sortinator")
root.geometry("400x380")
root.minsize(400, 380)

# Add input field for numbers
spawn(ctk.CTkLabel(root, text="Enter numbers separated by commas:"), indent="small")
input_entry = ctk.CTkEntry(root, width=300, placeholder_text="1, 34, 74, 6, 31")
input_entry.pack(padx=30, pady=(0, 15), fill="x")

# Select sorting direction
sort_direction = ctk.StringVar(value=SortingDirection.ASCENDING)
spawn(
    ctk.CTkOptionMenu(root, variable=sort_direction, values=list(SortingDirection)),
    zero_width=True,
)

# Select sorting algorithm
sort_algorithm = ctk.StringVar(value=SortingAlgorithm.PYTHON_SORT)
spawn(ctk.CTkOptionMenu(root, values=list(SortingAlgorithm)), zero_width=True)

# Button to start sorting
spawn(
    ctk.CTkButton(
        root,
        text="Start",
        fg_color="#1c8e64",
        hover_color="#146648",
        command=lambda: start_sorting(),
    )
)

# Display sorted sequence of numbers
spawn(ctk.CTkLabel(root, text="Sorted sequence:"), indent="small")
output_text = ctk.CTkTextbox(root, height=130)
output_text.pack(padx=30, pady=(0, 10), fill="both", expand=True)

# Sorting time
time_value = ctk.StringVar(value=f"Sorting time: {0:.9f} seconds")
spawn(ctk.CTkLabel(root, textvariable=time_value))


def update_output(sorted_numbers: list[int], sorting_time: float):
    """Updates the output text field with sorted numbers and sorting time."""
    output_text.delete("1.0", ctk.END)
    output_text.insert(ctk.END, format_output_numbers(sorted_numbers))
    time_value.set(f"Sorting time: {sorting_time:.9f} seconds")


def show_input_error_message():
    """Displays an input error message."""
    messagebox.showwarning("Error", "Please enter numbers separated by commas")


def start_sorting():
    """Starts the number sorting process based on input data and selected parameters."""
    input_string: str = input_entry.get()
    direction = SortingDirection(sort_direction.get())
    algorithm = SortingAlgorithm(sort_algorithm.get())

    numbers = parse_input(input_string)

    if not numbers:
        return show_input_error_message()

    args = numbers, algorithm, direction
    execution_time, result = measure_time(sort_executor, *args)

    update_output(result, execution_time)


def run_app():
    """Runs the main application loop."""
    root.mainloop()
