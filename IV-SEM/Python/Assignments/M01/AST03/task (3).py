def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    average = round((n1 + n2 + n3) / 3, 2)

    # Ensure format like 50.0 instead of 50
    if average == int(average):
        average = float(int(average))

    status = "Pass" if average >= 40 else "fail"

    return f"Average grade: {average}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))