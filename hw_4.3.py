def print_tree(directory: Path, indent: str = ""):
    print(f"{indent}{Fore.BLUE}{directory.name}/")
    try:
        entries = sorted(directory.iterdir(), key=lambda p:(p.is_file(), p.name.lower()))
    except PermissionError:
        print(f"{indent} {Fore.RED}[Немає доступу до {directory}]")
        return
    new_indent = indent + "    "
    for entry in entries:
        if entry.is_dir():
            print_tree(entry, new_indent)
        else:
            print(f"{new_indent}{Fore.GREEN}{entry.name}")
def main():
    if len(sys.argv)<2:
        print("Вкажіть шлях до директорії")
        print("Наприклад, python hw_4.3.py C:\\Users\\rviderko\\Pictures")
        return
    raw_path = sys.argv[1]
    directory = Path(raw_path)
    if not directory.exists():
        print(f"Шлях {directory} не існує")
        return
    if not directory.is_dir():
        print(f"Шлях{directory} не є директорією")
        return
    print_tree(directory)
if __name__=="__main__":
    main