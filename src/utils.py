from time import perf_counter
from tkinter import Widget
from typing import Callable, Literal, Optional, TypeVar


def parse_input(input: str) -> list[int]:
    """Converts a string of comma-separated numbers into a list of integers.

    Ignores strings that cannot be converted to integers or are negative!
    """
    return [
        int(section.strip())
        for section in input.split(",")
        if section.strip().isdigit()
    ]


def format_output_numbers(numbers: list[int]) -> str:
    """Formats a list of integers into a comma-separated string."""
    return ", ".join(map(str, numbers))


Result = TypeVar("Result")


def measure_time(func: Callable[..., Result], *args) -> tuple[float, Result]:
    """Measures the execution time of a function and returns the time and result."""
    start_time = perf_counter()
    result = func(*args)
    end_time = perf_counter()
    return end_time - start_time, result


def spawn(
    widget: Widget, indent: Optional[Literal["small"]] = None, zero_width: bool = False
):
    """Adds a widget to the container with optimal padding."""
    if zero_width:
        widget.configure(width=0)
    if indent == "small":
        widget.pack()
    else:
        widget.pack(pady=(0, 10))
