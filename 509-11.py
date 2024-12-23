def print_stars():
    star = input("เขียนตัวใดก็ได้: ")
    
    try:
        number = int(input("จำนวนที่อยากให้เเสดง: "))
        print(star * number)
    except ValueError:
        print("ผิด! ให้คุณเขียนจำวนสเต็ม")

print_stars()

