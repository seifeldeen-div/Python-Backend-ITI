# # -------------------------------Task one---------------------------------------
# name1, name2 = input().split()
# score1, score2 = 85.5, 92.0
#
# name1, name2, score1, score2 = name2, name1, score2, score1
#
# print("[RECORD] ", name1, score1, name2, score2, sep=' ::: ', end='\n--- FINISHED RECORD ---\n')
# print('Total Score (INT):', (score1 + score2), " | ", 'Total Score (Type):', type(str(score1 + score2)))
#
# # -------------------------------Task Two---------------------------------------
# amount , country = input().replace("Amount = ","").replace("Country = ","").split(", ")
# amount = int (amount)
# country = country.lower()
#
# country_list = ['egypt', 'uae', 'saudi', 'kuwait']
#
# eligibility = 'Free delivery applies' if (amount >= 500.0 and country in country_list) else 'Standard Shipping (50 EGP)'
#
# print('Delivery', eligibility, " | ", 'VIP Logistics Flag:', eligibility == 'Free delivery applies')
#
# # -------------------------------Task Three---------------------------------------
# units, Type = input().replace("Units = ", "").replace("Type = ", "").split(", ")
# units = int(units)
# tax = 0
# bill = 0
#
# if units <= 100:
#     bill = units * 0.75
# elif units <= 250:
#     bill = (100 * 0.75) + ((units - 100) * 1.20)
# else:
#     bill = (100 * 0.75) + (150 * 1.20) + ((units - 250) * 1.80)
#
# if Type == 'res':
#     tax = bill * 0.05
# else:
#     tax = (bill * 0.12) + 20
# total = bill + tax
#
# print("Base Bill:", bill, " | ", "Tax:", tax, " | ", "Total Due:", total)
#
# # -------------------------------Task Four---------------------------------------
#
# HTTPREQ = int(input())
#
# match HTTPREQ:
#     case 200 | 201:
#         res = 'SUCCESS: Request fulfilled and resource ready.'
#     case 400 | 422:
#         res = 'CLIENT ERROR: Bad request or unprocessable payload.'
#     case 401 | 403:
#         res = 'ACCESS DENIED: Authentication required or forbidden.'
#     case 404:
#         res = 'NOT FOUND: The requested resource does not exist.'
#     case 500 | 502 | 503:
#         res = 'SERVER ERROR: Upstream server is unavailable.'
#     case _:
#         res = 'UNKNOWN CODE: Protocol response code unmapped.'
# print("[", "Response", HTTPREQ, "]", res)
#
# # -------------------------------Task Five---------------------------------------
#
# start, end, step = input().replace("start =", "").replace("stop =", "").replace("step =", "").split(", ")
# start = int(start)
# end = int(end)
# step = int(step)
#
# for i in range(start, end, step):
#     if i % 3 == 0 or i % 10 == 5:
#         continue
#     if i > 80:
#         break
#     print(i, " ", end="#")
# print(" [SCAN COMPLETE]", end='')
#
# # -------------------------------Task Six---------------------------------------
#
# for row in range(3):
#     print()
#     for col in range(3):
#         if row == col:
#             print("[X]", end='')
#         else:
#             print('(', row, ",", col, ")", sep=" ", end='')
#
# # -------------------------------Task seven---------------------------------------
# stock = 50
# reStock = 0
# disPatch = 0
# while True:
#     adjustment = int(input())
#     if adjustment == 0:
#         break
#     elif adjustment > 0:
#         stock += adjustment
#         reStock += 1
#
#     else:
#         adjustmentPositive = abs(adjustment)
#         if adjustmentPositive > stock:
#             print("Dispatch Rejected: Insufficient inventory")
#         else:
#             stock -= adjustmentPositive
#             disPatch += 1
#     if stock == 0:
#         print("Warning: Stock Depleted!")
# print("[INVENTORY FINAL REPORT]", "Current Units:", stock, ' | ', "Restocks:", reStock, " | ", "Dispatches:", disPatch)
# # [INVENTORY FINAL REPORT] Current Units: 0 | Restocks: 1 | Dispatches: 2
#
# # -------------------------------Task seven ( Bonus  )---------------------------------------
# print('(1) Standard 2D Ticket - 80 EGP')
# print('(2) IMAX 3D Ticket - 130 EGP')
# print('(3) VIP Recliner Ticket - 200 EGP')
# print('(4) Popcorn Combo - 45 EGP')
# print('(5) Soda Beverage - 25 EGP')
# print('(0) Proceed to Payment')
#
# totalBill = 0
# items = []
#
# while True:
#     choice, quantity = input('Enter Your Choice and Quantity:- ').split(" ")
#     choice = int(choice)
#     quantity = int(quantity)
#     supTotal = 0
#     if choice == 0 : break
#     match choice:
#         case 1:
#             supTotal = quantity * 80
#             items.append((choice, quantity))
#         case 2:
#             supTotal = quantity * 130
#             items.append((choice, quantity))
#         case 3:
#             items.append((choice, quantity))
#             supTotal = quantity * 200
#         case 4:
#             supTotal = quantity * 45
#             items.append((choice, quantity))
#         case 5:
#             supTotal = quantity * 25
#             items.append((choice, quantity))
#         case _:
#             print('Not Defined, please Coose valid case')
#             continue
#
#
#     totalBill += supTotal
#
# final = totalBill - (totalBill * 0.1) if totalBill > 250 else 0
#
# cache = int(input("Enter Cache: "))
# while True:
#     if cache < final:
#         print('Not Enough')
#         cache = int(input("Enter Cache: "))
#     else:
#         change = cache - final
#         break
# print()
# print("User books: ")
# for c, q in items:
#     print("(", c, "Qty", q, ")")
#
# print("Subtotal ", totalBill, " -> 10% Discount applied")
# print("Final ", final)
# print("Paid", cache, "-> Change: ", change)
