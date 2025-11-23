import csv
from pathlib import Path


class Report:
    def __init__(self, files: list[Path]):
        self.files = files

    def calculate_avg(self, grades: list[int]) -> float:
        return sum(grades) / len(grades)

class PerformanceReport(Report):
    def __init__(self, files):
        super().__init__(files)
        self.headers = ['position', 'performance']
    
    def get_report(self):
        result: dict = {}
        for file in self.files:
            with open(file) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    position = row.get(self.headers[0])
                    performance = row.get(self.headers[1])
                    if position not in result:
                        result[position] = [float(performance)]
                    else:
                        result[position].append(float(performance))
        for i in result:
            result[i] = self.calculate_avg(result[i])
        sort_result = sorted(
            result.items(),
            key=lambda item: item[1], 
            reverse=True,
        )
        return (sort_result, self.headers)
