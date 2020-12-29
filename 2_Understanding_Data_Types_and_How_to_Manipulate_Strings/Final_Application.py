print("Welcome to the KKB tip calculator!")
bill = float(input("\nHow much is the total bill?\n"))
percent = float(input("\nHow many percentage are you willing to pay?\n")) / 100
quantity = int(input("\nHow many are going to split the bill?\n"))

tcost = float(bill)
pcost = float(percent)
qcost = int(quantity)

tiptotal = round(tcost * pcost, 2)
tipeach = round(tiptotal / qcost, 2)

msgbill = f"Since the total cost is {round(bill, 2)} pesos, "
msgquantity = f"and {quantity} persons present on the table, "
msgtip = f"your total tip is {tiptotal}, which is {tipeach} each."

print(msgbill + msgquantity + msgtip)
