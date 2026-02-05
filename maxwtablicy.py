def znajdz_max(tab):
    max_val = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > max_val:
            max_val = tab[i]
    return max_val

if __name__ == "__main__":
    tab = [4, 6, 2, 1, 3]
    print(f"Max = {znajdz_max(tab)}")

