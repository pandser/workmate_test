from .reports import StudentPerformanceReport
from .utils import search_in_current_dir


def test_utils():
    assert search_in_current_dir() == ['students1.csv', 'students2.csv']

def test_get_report():
    answer = (
        [
            ('Семенова Елена', 5),
            ('Власова Алина', 5),
            ('Калинина Ольга', 5),
            ('Игнатьев Роман', 5),
            ('Миронова Вероника', 5),
            ('Орлова Дарья', 5),
            ('Степанов Игорь', 5),
            ('Григорьева Софья', 5),
            ('Титов Владислав', 4),
            ('Белов Станислав', 4),
            ('Максимов Кирилл', 4),
            ('Савельева Анастасия', 4),
            ('Кудрявцев Глеб', 4),
            ('Жуков Александр', 4),
            ('Чернова Виталина', 4),
            ('Дорофеев Никита', 3),
            ('Гусев Артур', 3),
            ('Фомина Ксения', 3),
            ],
            ['student_name', 'grade'],
        )
    rep = StudentPerformanceReport(files=['students1.csv'])
    assert rep.get_report() == answer
