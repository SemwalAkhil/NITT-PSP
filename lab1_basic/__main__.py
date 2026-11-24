from pathlib import Path
import subprocess
import sys
import re

LAB_DIR = Path(__file__).resolve().parent


def natural_file_key(path: Path) -> tuple[int, str]:
    """Extract leading number from filename for numeric sorting, with name tie-breaker."""
    match = re.match(r"^_?(\d+)", path.stem)
    number: int = int(match.group(1)) if match else float("inf")
    return (number, path.name.lower())


def get_lab_scripts(folder: Path) -> list[Path]:
    """Return numerically sorted Python scripts in the folder, excluding __main__.py."""
    scripts = [
        p for p in folder.iterdir()
        if p.is_file() and p.suffix == ".py" and p.name != "__main__.py"
    ]
    return sorted(scripts, key=natural_file_key)

def menu() -> None:
    while True:
        scripts = get_lab_scripts(LAB_DIR)

        if not scripts:
            print(f"No lab scripts found in {LAB_DIR}")
            return

        print(f"\n--- {LAB_DIR.name} ---")
        for idx, script in enumerate(scripts):
            print(f"{idx+1} > {script.name}")

        choice = input("\nEnter code number (or 'q' to quit): ").strip()
        if choice.lower() == "q":
            return

        try:
            idx = int(choice)
            if not (1 <= idx <= len(scripts)):
                print("Invalid number. Please choose an index from the list.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        selected_script = scripts[idx-1]
        print(f"\nRunning {selected_script.name}...\n" + "-" * 40)
        subprocess.run([sys.executable, str(selected_script)], check=False)


if __name__ == "__main__":
    menu()