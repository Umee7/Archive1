print("Welcome to currency converter!")
print("select the currency you want to convert")
print("1.Indian Rupees\n2.Euros\n3.US Dollars\n4.Canadian Dollars\n5.Russian Ruble\n6.Chinese Yuan\n7.Japanese Yen")
currency_int=input(">>>>")
if currency_int!= " " and (currency_int== "Indian Rupees" or currency_int=="1"):
  print("Enter the value in Indian Rupees: ")
  INR=float(input())
  print("Choose the currency you want to convert:")
  print("1.Pounds")
  print("2.Euros")
  print("3.US Dollars")
  print("4.Canadian Dollars")
  print("5.Russian Ruble")
  print("6.Chinese Yuan")
  print("7.Japanese Yen") 
  currency_inr = float(input(">>>>>"))
  if currency_inr == 1 or currency_inr == "Pounds":
    pounds=INR*0.011
    print(str(pounds)+" pounds")
  elif currency_inr ==2 or currency_inr == "Euros":
    euros=INR*0.012
    print(str(euros)+" euros")
  elif currency_inr ==3 or currency_inr == "US Dollars":
    usDollars=INR*0.012
    print(str(usDollars)+" USD")
  elif currency_inr ==4 or currency_inr =="Canadian Dollars":
    cnd=INR*0.016
    print(str(cnd)+" Canadian Dollars")
  elif currency_inr ==5 or currency_inr =="Russian Ruble":
    russ=INR*0.74
    print(str(russ)+" Russian Ruble")
  elif currency_inr ==6 or currency_inr == "Chinese Yuan":
    chn=INR*0.088
    print(str(chn)+" Yuan")
  elif currency_inr ==7 or currency_inr =="Japanese":
    yen=INR*1.72
    print(str(yen)+" yen")
elif currency_int!= " " and (currency_int=="Euros" or currency_int=="2"):
  print("Enter the value in EUROS: ")
  EUROS=float(input(">>>>>"))
  print("Choose the currency you want to convert:")
  print("1. Pounds")
  print("2. Inr")
  print("3. US Dollars")
  print("4. Canadian Dollars")
  print("5. Russian Ruble")
  print("6. Chinese Yuan")
  print("7. Japanese Yen")
  currency_eur = float(input(">>>>>"))
  if currency_eur == 1 or currency_eur=="Pounds":
    pounds=EUROS*0.86
    print(str(pounds)+" pounds")
  elif currency_eur ==2 or currency_eur=="Indian Rupees":
    inr=EUROS*85.42
    print(str(inr)+" Rupees")
  elif currency_eur ==3 or currency_eur=="US Dollars":
    usDollars=EUROS*1.03
    print(str(usDollars)+" USD")
  elif currency_eur ==4 or currency_eur=="Canadian Dollars":
    cnd=EUROS*1.40
    print(str(cnd)+" Canadian Dollars")
  elif currency_eur ==5 or currency_eur=="Russian Ruble":
    russ=EUROS*65.71
    print(str(russ)+" Russian Ruble")
  elif currency_eur ==6 or currency_eur=="Chinese Yuan":
    chn=EUROS*7.41
    print(str(chn)+" Yuan")
  elif currency_eur ==7 or currency_eur=="Japanese Yen":
    yen=EUROS*141.80
    print(str(yen)+" yen")
elif currency_int!= " " and (currency_int=="US Dollars" or currency_int=="3"):
  print("Enter the value in US Dollars: ")
  USD=float(input(">>>>>"))
  print("Choose the currency you want to convert:")
  print("1. Pounds")
  print("2. Inr")
  print("3. Euros")
  print("4. Canadian Dollars")
  print("5. Russian Ruble")
  print("6. Chinese Yuan")
  print("7. Japanese Yen")
  currency_usd = float(input(">>>>>"))
  if currency_usd == 1 or currency_usd =="Pounds":
    pounds=USD*0.81
    print(str(pounds)+" pounds")
  elif currency_usd ==2 or currency_usd=="Indian Rupees":
    inr=USD*82.28
    print(str(inr)+" Rupees")
  elif currency_usd ==3 or currency_usd=="Euros":
    usDollars=USD*0.95
    print(str(usDollars)+" Euros")
  elif currency_usd ==4 or currency_usd=="Canadian Dollars":
    cnd=USD*1.36
    print(str(cnd)+" Canadian Dollars")
  elif currency_usd ==5 or currency_usd=="Russian Ruble":
    russ=USD*62.55
    print(str(russ)+" Russian Ruble")
  elif currency_usd ==6 or currency_usd=="Chinese Yuan":
    chn=USD*6.97
    print(str(chn)+" Yuan")
  elif currency_usd ==7 or currency_usd=="Japanese Yen":
    yen=USD*136.49
    print(str(yen)+" yen")
elif currency_int!= " " and (currency_int=="Canadian Dollars" or currency_int=="4"):
  print("Enter the value in Canadian Dollars: ")
  CND=float(input(">>>>>"))
  print("Choose the currency you want to convert:")
  print("1. Pounds")
  print("2. Inr")
  print("3. Euros")
  print("4. US Dollars")
  print("5. Russian Ruble")
  print("6. Chinese Yuan")
  print("7. Japanese Yen")
  currency_cnd = float(input(">>>>>"))
  if currency_cnd == 1 or currency_cnd =="Pounds":
    pounds=CND*0.81
    print(str(pounds)+" pounds")
  elif currency_cnd ==2 or currency_cnd=="Indian Rupees":
    inr=CND*82.28
    print(str(inr)+" Rupees")
  elif currency_cnd ==3 or currency_cnd=="Euros":
    usDollars=CND*0.95
    print(str(usDollars)+" Euros")
  elif currency_cnd ==4 or currency_cnd=="US Dollars":
    cnd=CND*1.36
    print(str(cnd)+" Canadian Dollars")
  elif currency_cnd ==5 or currency_cnd=="Russian Ruble":
    russ=CND*62.55
    print(str(russ)+" Russian Ruble")
  elif currency_cnd ==6 or currency_cnd=="Chinese Yuan":
    chn=CND*6.97
    print(str(chn)+" Yuan")
  elif currency_cnd ==7 or currency_cnd=="Japanese Yen":
    yen=CND*11
    print(str(yen)+" yen")


else:
  print("Wrong Input")