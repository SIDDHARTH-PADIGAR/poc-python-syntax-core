from typing import Any

## positional and keyword args
def register_user(name: str, email: str, role: str = "viewer") -> dict[str, str]:
    return {
        "name": name,
        "email": email,
        "role": role,
    }

## *args: flexible positional parameters 
def batch_log(*messages: str) -> None:
    for i, msg in enumerate(messages, start=1):
        print(f"[LOG-{i}] {msg}")

## **kwargs: configurable API style
def create_connection(**config: Any) -> None:
    print("[DB-CONNECT] Using config:")
    for key, value in config.items():
        print(f"    {key} {value}")

## default parameters 
def get_user_profile(user_id: str, include_logs: bool = False) -> str:
    profile = f"Profile of {user_id}"
    if include_logs:
        profile += " (with logs)"
    return profile

## real-world pattern: function dispatcher
def handle_command(command: str, *args, **kwargs) -> Any:
    def say_hello(name: str) -> str:
        return f"Hello, {name}!"

    def add_numbers(x: int, y: int) -> int:
        return x + y

    dispatch = {
        "greet": say_hello,
        "sum": add_numbers
    }

    if command not in dispatch:
        raise ValueError(f"Unknown command: {command}")

    return dispatch[command](*args, **kwargs)


if __name__ == "__main__":
    user = register_user("Alice", "alice@example.com")
    print("Registered User:", user)

    batch_log("Server started", "DB connected", "Worker initialized")

    create_connection(
        host="localhost",
        port=5432,
        user="admin",
        password="secret"
    )

    print(get_user_profile("user_01", include_logs=True))

    print("Greet command:", handle_command("greet", "Sidd"))
    print("Sum command:", handle_command("sum", 12, 8))