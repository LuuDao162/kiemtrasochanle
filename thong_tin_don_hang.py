tien_nhap=float(input("Số tiền chi là: "))
if (tien_nhap >= 150):
    thanh_toan = tien_nhap - 50
    print("số tiền cần thanh toán là: " + str(thanh_toan))
elif (tien_nhap >=100):
    thanh_toan = tien_nhap - 25
    print("Số tiền cần thanh toán là: " +str(thanh_toan))
elif (tien_nhap >=75):
    thanh_toan = tien_nhap - 15
    print("Số tiền cần thanh toán là: " +str(thanh_toan))
else: 
    print("Số tiền cần thanh toán là: " +str(tien_nhap))
