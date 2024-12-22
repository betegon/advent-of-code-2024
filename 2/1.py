from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549from utils import read_input


# report = input lines
# level = number
# safe reports must:
#   -> levels are all increasing or all decreasing.
#   ->  any adjacent levels differ by at least one and at most three.
# HOW MANY REPORTS ARE SAFE


def get_safe_reports(reports):
    reports_safe = []
    for report in reports: 
        if is_report_increasing_or_decreasing(report):
            if check_levels_difference(report):
                reports_safe.append(report)
    return reports_safe

def is_report_increasing_or_decreasing(report):
    """There could be same numbers adjacents.
    e.g. [1, 2, 2, 4] - returns True even if 2, 2 are the same number.
    """

    is_increasing = True
    is_decreasing = True
    
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_decreasing = False
        if report[i] > report[i+1]:
            is_increasing = False
    return is_increasing or is_decreasing

def check_levels_difference(report, max_diff=3):
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff == 0 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    reports = read_input()
    reports_safe = get_safe_reports(reports)
    print(len(reports_safe)) # solution: 549