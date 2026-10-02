def TotalBill(billamt, tipPer):
    total = billamt * (1 + 0.01 * tipPer)
    total = round(total,2)
    print("Total Bill : ",total)


TotalBill(1500, 20)

