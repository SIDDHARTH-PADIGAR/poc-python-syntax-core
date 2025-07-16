from typing import NamedTuple


#  sample data: Timesheet (Name + Hours for 5 Days) 

class Timesheet(NamedTuple):
    employee: str
    hours: tuple[int, int, int, int, int]  # Mon to Fri


weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sheets: list[Timesheet] = [
    Timesheet("Sidd", (8, 9, 8, 8, 6)),
    Timesheet("Bob", (9, 8, 7, 5, 0)),
    Timesheet("Joe", (8, 8, 8, 8, 8)),
]


#  use case 1: Tuple unpacking in loop 

def print_total_hours():
    for name, hours in sheets:
        print(f"{name} worked total {sum(hours)} hrs")


#  use case 2: zip() to analyze per-day performance 

def daily_totals():
    print("\nTotal Hours per Day")
    # zip(*iterables) = transpose
    for day, totals in zip(weekdays, zip(*(sheet.hours for sheet in sheets))):
        print(f"{day}: {sum(totals)} hrs")


#  use case 3: enumerate() for indexed access 

def print_report_headers():
    print(" Report ")
    for idx, day in enumerate(weekdays, start=1):
        print(f"{idx}. {day}")


#  use case 4: Manual unpacking with underscore 

def get_first_employee() -> str:
    first, *_ = sheets
    return first.employee


if __name__ == "__main__":
    print_total_hours()
    daily_totals()
    print_report_headers()
    print("First employee on record:", get_first_employee())