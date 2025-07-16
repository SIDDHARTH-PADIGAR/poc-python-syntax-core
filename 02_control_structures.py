from typing import Literal

# use-case 1: permission engine
def has_access(user_role: str, resources: str) -> bool:
    if user_role =="admin":
        return True
    elif user_role == "manager" and resources != "financials":
        return True
    elif user_role == "viewer" and resources in ("dashboard", "logs"):
        return True
    else:
        return False
    
# use case 2: dispatch logic using match-case
def route_request(endpoint: str) -> str:
    match endpoint:
        case "/login":
            return "AuthController.login()"
        case "/users":
            return "UserController.list_users()"
        case "/metrics":
            return "MetricsController.get_metrics()"
        case _:
            return "404Controller.handle_404()"
        
#use case 3: threshold evaluator
def evaluate_risk_score(score: float) -> Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]:
        if score < 0.3:
            return "LOW"
        elif score < 0.6:
            return "MEDIUM"
        elif score < 0.85:
            return "HIGH"
        else:
            return "CRITICAL"
    

# use case 4: loopo with contorl
def sanitize_usernames(usernames: list[str]) -> list[str]:
    clean = []
    for user in usernames:
        if not user:
            continue
        if " " in user:
            print(f"Skipping invalid username: {user}")
            continue
        clean.append(user.strip().lower())
    return clean


# use case 5: looping with else clause
def search_user(usernames: list[str], target: str) -> str:
    for user in usernames:
        if user == target:
            return f"{target} found."
        else:
            return f"{target} not found." 
        
if __name__ == "__main__":
    print("Access Check:", has_access("viewer", "logs"))
    print("Route:", route_request("/metrics"))
    print("Risk:", evaluate_risk_score(0.87))
    print("Sanitized:", sanitize_usernames([" Sidd ", "bob", "admin user", "", "Eve"]))
    print(search_user(["Sidd", "bob", "joe"], "chris"))