can_nang = float(input("Nhập vào cân nặng: "))
chieu_cao = float(input("Nhập vào chiều cao: "))

bmi = can_nang/(chieu_cao**2)
if (bmi<16):
    print("Gầy cấp độ 3")
elif (16<=bmi<17):
    print("Gầy cấp độ 2")
elif (17<=bmi<18.5):
    print("Gầy cấp độ 1")
elif (18.5<=bmi<25):
    print("Bình thường")
elif (25<=bmi<30):
    print("Thừa cân")
elif (30<=bmi<35):
    print("Béo phì cấp độ 1")
elif (35<=bmi<40):
    print("Béo phì cấp độ 2")
elif (bmi>40):
    print("Béo phì cấp độ 3")