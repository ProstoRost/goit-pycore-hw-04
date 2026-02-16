def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 2:
                    continue
                name, salary_str = parts
                try:
                    salary = int(salary_str)
                except ValueError:
                    continue
                total += salary
                count += 1
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0
    if count == 0:
        return 0, 0
    average = total/count
    return total, average
total, average = total_salary("Salaries.txt")
print(f"Загальна сума зарплатні: {total}, Середня зарплатня: {average}")
