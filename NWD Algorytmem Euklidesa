def nwd_iteracyjnie(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nwd_rekurencyjnie(a, b):
    if b == 0:
        return a
    return nwd_rekurencyjnie(b, a % b)

if __name__ == "__main__":
    test_a, test_b = 112, 42

    print(f"Test dla liczb {test_a} i {test_b}:")
    print(f"Wynik (iteracyjnie): {nwd_iteracyjnie(test_a, test_b)}")
    print(f"Wynik (rekurencyjnie): {nwd_rekurencyjnie(test_a, test_b)}")
