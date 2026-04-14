import csv
import json
import os

def process_data():
    if not os.path.exists("students.csv"):
        print("❌ students.csv file not found!")
        return

    students = []

    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        rows = list(reader)

        if len(rows) == 0:
            print("❌ CSV file is empty!")
            return

        data = rows[1:]

        for row in data:
            
            if len(row) < 2:
                continue

            try:
                name = row[0]
                marks = list(map(int, row[1:]))

                total = sum(marks)
                average = total / len(marks)


                if average >= 90:
                    grade = "A"
                elif average >= 75:
                    grade = "B"
                elif average >= 50:
                    grade = "C"
                else:
                    grade = "F"

                students.append({
                    "name": name,
                    "marks": marks,
                    "total": total,
                    "average": round(average, 2),
                    "grade": grade
                })

            except ValueError:
                print(f"Skipping invalid data: {row}")

    # Save to JSON
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Data processed successfully!")
    print("Output saved in students.json")


if __name__ == "__main__":
    process_data()
