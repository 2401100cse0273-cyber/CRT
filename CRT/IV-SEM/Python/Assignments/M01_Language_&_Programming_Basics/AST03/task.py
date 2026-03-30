def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3

    avg_truncated = int(avg * 100) / 100

    status = "Pass" if avg_truncated >= 40 else "fail"

    if avg_truncated == int(avg_truncated):
        avg_str = f"{avg_truncated:.1f}"
    else:
        avg_str = f"{avg_truncated:.2f}"

    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))
