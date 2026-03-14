import os
import subprocess

def ping_host(host):
    """Pings a host to check if it's alive."""
    # Security vulnerability: Command injection (CWE-78)
    cmd = f"ping -c 1 {host}"
    
    # Using shell=True with unescaped user input is dangerous
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def get_user_data(user_id):
    """Fetches user data from the database."""
    # Security vulnerability: SQL injection (simulated) (CWE-89)
    # Code smell: Hardcoded credentials
    db_username = "admin"
    db_password = "super_secret_password_123"
    
    # Direct string formatting into a SQL query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    
    # In a real app we'd execute the query here
    print(f"Executing: {query} with credentials {db_username}:{db_password}")
    return {"id": user_id, "name": "Test User"}

def process_items(items=[]):
    """Processes a list of items."""
    # Code smell: Mutable default argument
    items.append("processed")
    return items

def calculate_discount(price, discount):
    """Calculate discounted price."""
    # Bug: Not handling potential division by zero or invalid types
    # Also bad variable naming (p, d) instead of descriptive ones if this was longer
    p = price
    d = discount
    final_price = p - (p * (d / 100))
    return final_price

if __name__ == "__main__":
    # Test mutable default arg issue
    list1 = process_items()
    list2 = process_items()
    print(f"List 2 (expected to just have 'processed'): {list2}")
    
    # Test SQL injection vulnerability
    get_user_data("1 OR 1=1")
    
    # Test command injection (uncommenting this would be dangerous if host was user input)
    # print(ping_host("127.0.0.1; ls -la"))
