import os
import site
import sys


def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def virtual_env_name() -> str:
    return os.path.basename(os.path.normpath(sys.prefix))


def site_packages_path() -> str:
    try:
        packages = site.getsitepackages()
        return packages[0] if packages else "unknown"
    except (AttributeError, OSError, IndexError):
        return "unknown"


def show_outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again.")


def show_inside_matrix() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {virtual_env_name()}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(site_packages_path())


def main() -> None:
    try:
        if in_virtual_env():
            show_inside_matrix()
        else:
            show_outside_matrix()
    except Exception as error:
        print(f"MATRIX STATUS: signal lost ({error})")


if __name__ == "__main__":
    main()
