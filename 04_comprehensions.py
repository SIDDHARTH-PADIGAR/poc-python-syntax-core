from typing import Any

# === Sample Input: Raw user data (mocked from an API) ===

raw_users: list[dict[str, Any]] = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "active": True},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "active": False},
    {"id": 3, "name": "Carol", "email": "carol@example.com", "active": True},
    {"id": 4, "name": "Dave", "email": "dave@example.com", "active": False}
]

# === List Comprehension: Extract active user emails ===

active_emails: list[str] = [user["email"] for user in raw_users if user["active"]]

# === Dict Comprehension: ID → Name mapping ===

id_name_map: dict[int, str] = {user["id"]: user["name"] for user in raw_users}

# === Set Comprehension: All domain names in email list ===

email_domains: set[str] = {user["email"].split("@")[1] for user in raw_users}

# === Nested Comprehension: Flatten multi-role data ===

roles: dict[str, list[str]] = {
    "Engineering": ["Alice", "Carol"],
    "Marketing": ["Bob"],
    "HR": ["Dave"]
}
flat_roles: list[str] = [user for dept in roles.values() for user in dept]

# === Real-World Use Case: Flag inactive users ===

inactive_flags: list[dict[str, Any]] = [
    {**user, "flagged": True}
    for user in raw_users
    if not user["active"]
]

# === Conditional Transform: Custom display name ===

display_names = [
    f"{user['name']} (INACTIVE)" if not user["active"] else user["name"]
    for user in raw_users
]

if __name__ == "__main__":
    print("Active Emails:", active_emails)
    print("ID → Name Map:", id_name_map)
    print("Email Domains:", email_domains)
    print("All Users (Flattened):", flat_roles)
    print("Inactive User Flags:", inactive_flags)
    print("Display Names:", display_names)
