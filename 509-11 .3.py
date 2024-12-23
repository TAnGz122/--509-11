width = float(input("กว้าง: "))
length = float(input("ยาว: "))
depth = float(input("ลึก: "))

volume = width * length * depth

time_seconds = volume * 15

time_minutes = time_seconds / 60

print(f"ต้องใช้เวลาในการเติมนำ้ {time_minutes:.2f} นาที.")
