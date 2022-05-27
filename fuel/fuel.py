while True:

    try:
        exp = input("Fraction: ").split("/")

        if len(exp) > 1:
            if "." in exp[0] or "." in exp[1]:
                raise ValueError

        exp[0] = float(exp[0])
        exp[1] = float(exp[1])

        if exp[0] > exp[1] and exp[1] != 0:
            raise ValueError

        res = round(exp[0] / exp[1] * 100)

        if res >= 99:
            print("F")
            break
        elif res <= 1:
            print("E")
            break
        else:
            print(str(int(res)) + "%")
            break

    except ValueError:
        continue

    except ZeroDivisionError:
        continue