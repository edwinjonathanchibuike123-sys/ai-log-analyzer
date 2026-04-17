def analyze_logs(file_path):
    errors = []
    warnings = []
    info = []

    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line.strip())
            elif "WARNING" in line:
                warnings.append(line.strip())
            elif "INFO" in line:
                info.append(line.strip())

    print("\n--- LOG ANALYSIS REPORT ---\n")
    print(f"Total INFO: {len(info)}")
    print(f"Total WARNINGS: {len(warnings)}")
    print(f"Total ERRORS: {len(errors)}\n")

    if len(errors) > 0:
        print("ALERT: Critical issues detected!\n")

    print("Errors:")
    for e in errors:
        print(f"- {e}")

    print("\nWarnings:")
    for w in warnings:
        print(f"- {w}")


if __name__ == "__main__":
    analyze_logs("sample.log")
