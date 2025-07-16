from typing import Any, Union

# primirive types with type hints
company_name: str = "NeuroCore AI"
employee_count: int = 48
valuation_in_millions: float = 15.75
is_profitable: bool =True


# constants (python doesn't enfore but follow UPPER_SNAKE_CASE convention)
API_KEY: str = "123456789abcdef"

# dynamic typing VS explicit typing
def log_metric(metric_name: str, value: Union[int, float, str]) -> None:
    print(f"[METRIC] {metric_name}: {value}")

# mutability trap demo
def list_mutability_trap():
    default_roles = ["viewer"]
    team_roles = [default_roles] * 3 #copies reference

    team_roles[0].append("editor") # mutates all sublists 
    print("team_roles:", team_roles) 

# collections in context
departments: list[str] = ["Engineering", "Marketing", "HR"]
employee_directory: dict[str, dict[str, Union[str, int]]] = {
    "emp_001": {"name": "Sidd", "dept": "Engineering", "age":21},
    "emp_002": {"name": "Bob", "dept": "Marketing", "age":28},
}
access_level: set[str] = {"admin", "read-only", "contributor"}

# tuples for fixed structures
Coordinates = tuple[float, float]
office_location: Coordinates = (12.9611, 77.6387) # Bangalore

# type aliases
UserID = str
UserData = dict[str, Union[str, int]]
users: dict[UserID, UserData] = employee_directory

# demo func
def print_state():
    print("Company:", company_name)
    print("Department:", departments)
    print("Office location:", office_location)
    log_metric("MonthluUsers", 10482)
    log_metric("ConversionRate", "5.3%")

if __name__ == "__main__":
    print_state()
    list_mutability_trap()