#Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

weight = 41.5
groundShipping_flat = 20
groundShipping_premium = 125
shipping_method=""

print("What is the cheapest method of shipping a " + str(weight) + " pound package and how much would it cost?")
print("\n")

#Ground shipping
if weight >=10:
  gs_cost = weight * 4.75
elif weight > 6:
  gs_cost = weight * 4.00
elif weight > 2:
  gs_cost = weight * 3.00
else:
  gs_cost = weight * 1.50
  
#Drone Shipping
if weight >=10:
  dr_cost = weight * 14.25
elif weight > 6:
  dr_cost = weight * 12.00
elif weight > 2:
  dr_cost = weight * 9.00
else:
  dr_cost = weight * 4.50

if gs_cost + groundShipping_flat < groundShipping_premium:
  shipping_method = "Ground Shipping"
  cost = gs_cost + groundShipping_flat
elif groundShipping_premium < dr_cost:
  shipping_method = "Ground Shipping Premium"
  cost = groundShipping_premium
else:
  shipping_method = "Drone Shipping"
  cost = dr_cost


print("Ground Shipping: $" + str(gs_cost + groundShipping_flat))
print("Ground Shipping Premium: $" + str(groundShipping_premium))
print("Drone Shipping: $" + str(dr_cost))
print("\n")
print("Shipping Method: " + shipping_method)
print("Cost: $" + str(cost))