# error handling

while True: 
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)

# except ZeroDivisionError:
#     print("y için 0 girilemez.")
# except ValueError:
#     print("x ve y için sayısal değer girmelisiniz.")


# except (ZeroDivisionError, ValueError) as e:
#     print("Yanlış bilgi girdiniz.")
#     print(e)


    except Exception as ex:
        print("Yanlış bilgi girdiniz.", ex) 
    else:
        break
    finally:
        print("Try except sonlandı.")