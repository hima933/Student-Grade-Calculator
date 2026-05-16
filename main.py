from src.grades import calculate_grade


def calculate_average(lst):
    with open("C:\\Users\\bindu\\Downloads\\Grade Calculator\\data\\results.txt", "a") as file:
        for i in lst:
            name = i[0]
            scores = i[1:]
            avg = sum(scores) / len(scores)
            grade = calculate_grade(avg)
            file.write(f"{name} - Average:{round(avg,2)} - Grade:{grade}\n")

def main():
    try:
        with open("C:\\Users\\bindu\\Downloads\\Grade Calculator\\data\\students.txt", "r") as file:
            lst = []
            for line in file:
                parts = line.strip().split(",")
                if parts:
                    name = parts[0]
                    scores = list(map(float, parts[1:]))
                    lst.append([name] + scores)
                #print(lst)
        calculate_average(lst)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except ZeroDivisionError:
        print("No scores found for a student. Please check the input data.")

main()
print("Grade calculation completed. Check results.txt for details.")
