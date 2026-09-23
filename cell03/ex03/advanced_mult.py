argv = __import__('sys').argv
if len(argv) != 1:
    print("none")
else:
    i = 0
    while i <= 10:
        row = f"Table de {i}:"
        j = 0
        while j <= 10:
            row += f" {i * j}"
            j += 1
        print(row)
        i += 1