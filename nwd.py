def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    x, y = 123456, 789

    print(f"Wynik: {nwd(x, y)}")
