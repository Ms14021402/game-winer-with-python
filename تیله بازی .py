while True:
    n = int(input("تعداد تيله ها را وارد کنيد"))
    if n % 3 == 0:
        print("نفر دوم هستم")
    else:
        print("من نفر اول هستم")
        m = n%3
        print(f"من {m}تيله برمي دارم")
        n = n - m
    while n > 0:
            print(f"الان {n}تيله روي مميز هست")
            m = int(input("چند تيله برمي داري"))
            if m <1 or m > 2:
                print("تعداد نادرستي تيله برداشتي")
                print("تيله ها بايد 1 يا 2 باشد")
                continue
                
            n = n - m
            
            m = n % 3
            print(f"من {m}تيله برمي دارم")
            n = n - m
    print("من برنده شدم هوراااااا")
    a = input("مي خواي ادامه بدي آره يا نه ؟")
    if a == "آره":
        pass
    elif a == "نه":
        exit()
    else:
        print("اشتباه وارد کردي")
        print("پس يک دست ديگه بازي کن")
    print("**********************")
    print()
    print()
    print()
    print()
    print()

