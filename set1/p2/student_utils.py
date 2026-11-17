
# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P2 - Custom Module
# Date: November 16, 2026


def calculate_average(grades):
    return sum(grades) / len(grades)


def check_status(grades):
    if calculate_average(grades) >= 75:
        return "PASS"
    return "FAIL"


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)
