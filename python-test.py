import subprocess

def run_system_command(user_input):
    # Bandit should IGNORE this because of our skips = ["B101"] config
    assert user_input != "", "Input cannot be empty"
    
    # Bandit should CATCH this as a B602 vulnerability
    subprocess.call(f"echo {user_input}", shell=True)
