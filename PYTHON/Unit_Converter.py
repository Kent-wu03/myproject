while True:
    try:
        print("Unit Converter")
        list_convert = [(1,'km','m'),
                        (2,'m','km'),
                        (3,'*C','*F'),
                        (4,'*F','*C'),
                        (5,'kg','lbs'),
                        (6,'lbs','kg'),
                        ]
        for number,unit1,unit2 in list_convert:
            print(f"{number}. {unit1} > {unit2}")

        pilihan = int(input("Pilih (1-6) "))

        if pilihan == 1:
            print("kamu memilih km > m")
            a1 = int(input("input km = "))
            print(f"hasilnya adalah {a1 * 1000} m")
        elif pilihan == 2:
            print("kamu memilih m > km")
            a1 = int(input("input m = "))
            print(f"hasilnya adalah {a1 / 1000} km")
        elif pilihan == 3:
            print("kamu memilih *C > *F")
            a1 = float(input("input *C = "))
            print(f"hasilnya adalah {((9/5) * a1) + 32}")
        elif pilihan == 4:
            print("kamu memilih *F > *C")
            a1 = float(input("input *F = "))
            print(f"hasilnya adalah {(5/9) * (a1 - 32)}")
        elif pilihan == 5:
            print("kamu memilih kg > lbs")
            a1 = float(input("input kg = "))
            print(f"hasilnya adalah {a1 * 2.20462} (nilai = 2.20462)")
            print(f"hasilnya adalah {a1 * 2.2} (nilai = 2.2)")
        elif pilihan == 6:
            print("kamu memilih lbs > kg")
            a1 = float(input("input lbs = "))
            print(f"hasilnya adalah {a1 / 2.20462} (nilai = 2.20462)")
            print(f"hasilnya adalah {a1 / 2.2} (nilai = 2.2)")
        break
    except ValueError:
        print("yang bener")
