#user input
wt_lb = float(input("input weight in pounds: "))
ht_in = float(input("input height in inches: "))
BMI = (703*wt_lb)/ht_in**2

print (f"your BMI is {BMI:.2f}")

if (BMI<18.5):
    print("and it categorized as underweight")

elif (18.5<=BMI<=24.9):
    print("and it categorized as normal")

elif (25.0<=BMI<=29.9):
    print("and it categorized as overweight")

else:
    print("and it categorized as obese")