import csv
from pathlib import Path


class Report:
    def __init__(self, files: list[Path]):
        self.files = files


class StudentPerformanceReport(Report):
    def __init__(self, files):
        super().__init__(files)
        self.headers = ['student_name', 'grade']
    
    def calculate_avg_grade(self, grades: list[int]) -> float:
        return sum(grades) / len(grades)

    def get_report(self):
        result: dict = {}
        for file in self.files:
            with open(file) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_name = row.get('student_name')
                    grade = row.get('grade')
                    if student_name not in result:
                        result[student_name] = [int(grade)]
                    else:
                        result[student_name].append(int(grade))
        for i in result:
            result[i] = self.calculate_avg_grade(result[i])
        sort_result = sorted(
            result.items(),
            key=lambda item: item[1], 
            reverse=True,
        )
        return (sort_result, self.headers)
