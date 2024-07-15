

weights = [206700]

numbers_of_bag = [3090]

moisture_values = [9,10,11,12,16,14,12,15,13,10,14,13,15,17,18,19,12,13,12,12,12,14,16,12,11,13,18,19,13,14]



















weig =0
for i in weights:
   weig += i





num =0
for i in numbers_of_bag:
   num += i





mois = 0
for i in moisture_values:
    mois += i






wet_bag= mois/len(moisture_values)
average_moisture = wet_bag+0.5



c=average_moisture-8
a=weig*c*len(moisture_values)
b=num*100
discount = a/b



print(' DISCOUNT CALCULATOR\n')



print(f" TOTAL NUMBER OF BAG:=  {num}\n")
print(f"        TOTAL WEIGHT:=  {weig}\n")
print(f"    AVERAGE MOISTURE:=  {average_moisture}\n")
print(f"      TOTAL DISCOUNT:=  {discount}\n")