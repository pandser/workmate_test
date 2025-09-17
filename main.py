import argparse
from pathlib import Path
from tabulate import tabulate

from constants import REPORTS
from utils import search_in_current_dir


parser = argparse.ArgumentParser()
parser.add_argument(
    '--files',
    type=Path,
    nargs='*',
    help='file name',
)
parser.add_argument(
    '--report',
    type=str,
    help='report name',
    default='student-performance',
)
args = parser.parse_args()

files = args.files
if not files:
    try:
        files = search_in_current_dir()
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
for file in files:
    if not Path(file).exists():
        raise FileNotFoundError(f'Файл {file} не найден.')

report = REPORTS[args.report](files=files)
rep_for_print = report.get_report()
print(tabulate(rep_for_print[0], headers=rep_for_print[1]))
