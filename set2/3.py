total_amount = float(input("TOTLA     :    "))
total_item = int(input("NUMBER OF ITEMS:     "))
is_member = input('MEMBER?(T or F)')
if 't' in is_member.lower():
    is_member = True
else:
    is_member = False
is_first_time_buyer = bool(input("ARE you a first time buyer (TRUE Or FALSE)"))
if total_amount > 200:
    if is_member:
        amount = total_amount * 0.8
    else:
        amount = total_amount * 0.9
elif total_amount>=100 and total_amount<=200:
    if total_item>5:
        amount = total_amount * 0.85
    else:
        amount = total_amount * .95
else:
    if is_first_time_buyer:
        amount = total_amount -5
print(amount)