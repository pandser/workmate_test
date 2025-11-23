from .reports import PerformanceReport
from .utils import search_in_current_dir


def test_utils():
    assert search_in_current_dir() == ['employees1.csv', 'employees2.csv']

def test_get_report():
    answer = (
        [
            ('Backend Developer', 4.85),
            ('DevOps Engineer', 4.7),
            ('Data Engineer', 4.7),
            ('Data Scientist', 4.7),
            ('Mobile Developer', 4.6),
            ('Frontend Developer', 4.6),
            ('QA Engineer', 4.5),
        ],
        ['position', 'performance'],
    )
    rep = PerformanceReport(files=['employees1.csv'])
    assert rep.get_report() == answer
