from pathlib import Path

SAFE_DIR = Path("safe_files").resolve()

filename = input("Enter filename: ")

try:
    # Resolve the requested path
    requested_path = (SAFE_DIR / filename).resolve()

    # Ensure the file stays inside the safe directory
    if not requested_path.is_relative_to(SAFE_DIR):
        raise ValueError("Access denied: Invalid file path")

    # Open only validated paths
    with open(requested_path, "r") as file:
        print(file.read())

except (ValueError, OSError) as e:
    print("Error:", e)
