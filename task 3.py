import sys
import os
from colorama import Fore, Style



def visualize_directory_structure(directory):
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"{Fore.RED}Error: '{directory}' does not exist or is not a directory.{Style.RESET_ALL}")
        return

    print(f"{Fore.BLUE}Directory structure for '{directory}':{Style.RESET_ALL}")
    visualize_directory(directory, 0)


def visualize_directory(directory, indent_level):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(Fore.BLUE + "  " * indent_level + f"{item}/" + Style.RESET_ALL)
            visualize_directory(item_path, indent_level + 1)
        else:
            print(Fore.GREEN + "  " * indent_level + item + Style.RESET_ALL)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    visualize_directory_structure(directory)


if __name__ == "__main__":
    main()

