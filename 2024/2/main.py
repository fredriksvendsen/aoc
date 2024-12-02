def get_reports():
    with open("2_input.txt", "r") as f:
        reports = []
        for line in f.readlines():
            nums = list(int(x) for x in line.split(" "))
            reports.append(nums)
        return reports

def get_safe_reports_0(reports):
    return len([report for report in reports if is_safe(report)])
            
def get_damped_safe(reports):
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                if is_safe(report[0:i] + report[i+1:len(report)]):
                    safe_reports += 1
                    break
    return safe_reports

def is_safe(report):
    prev = None
    increasing = None
    for idx, num in enumerate(report):
        if idx == 0:
            prev = num
            continue
        if idx == 1:
            increasing = True if num > prev else False
        if increasing and not (num > prev and num <= prev + 3):
            return False
        if not increasing and not (num < prev and num >= prev - 3):
            return False
        prev = num
    return True

def main():
    reports = get_reports()
    n_safe_reports = get_safe_reports_0(reports)
    print(f"Result: {n_safe_reports}")
    damped_safe = get_damped_safe(reports)
    print(f"Result damped safe: {damped_safe}")

if __name__ == "__main__":
    main()
