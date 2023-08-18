"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from sys import argv
import argparse
from datetime import datetime

def valid_date(date):
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


parser = argparse.ArgumentParser(description='Check date.')
parser.add_argument('date', type=str, help='Date to check in the format DD.MM.YYYY')

args = parser.parse_args()

print(valid_date(args.date))