import pandas as pd
import numpy as np
import random   
from datetime import datetime, timedelta

#Create empty list
data = []

#parameters
num_rows = 300000

#categories
product_types = ["Money transfer","Loan","Insurance","Bill payment"]
Payment_Methods = ["UPI","Bank transfer","Wallet"]
Cities=["Delhi","Pune","Mumbai","Banglore","Chennai","Hydrabad"]

Failure_reasons = ["Bank Denied", "Wrong pin","Network Down", "Insuffiecient Balance","Time out","None"]

#Generate base data
date = []

start_date = datetime(2024,1,1)

for i in range(num_rows):
    transection_id = f"T{i+1:06d}"
    user_id=f"U{random.randint(1000,9999)}"

    #date and time
    date = start_date + timedelta(days=random.randint(0,365))
    time = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"

    product = random.choice(product_types)

    #amount logic

    if product == "loan":
        amount = round(random.uniform(5000,200000),2)
    elif product == "Insuarance":
        amount = round(random.uniform(1000,50000),2)    
    elif product == "Money transfer":
        amount = round(random.uniform(100,50000),2)    
    else:#Bill Payment
        amount = round(random.uniform(50,5000),2)
    
    Payment_Method = random.choice(Payment_Methods)
    city = random.choice(Cities)

    #status logic
    success_prob = 0.80

    # Higher Failure for high-value transection
    if amount>50000:
        success_prob -= 0.15

    # Bill payment mostly successful
    if product == "Bill payment":
        success_prob += 0.10

    # weekend variation
    if date.weekday() >= 5:
        success_prob -= 0.05

    rand = random.random()

    if rand < success_prob:
        status = "Success"
        failure_reason = None
    elif rand < success_prob + 0.15:
        status = "Failed"
        failure_reason = random.choice(Failure_reasons[:-1])
    else:
        status = "Pending"
        failure_reason = None

    data.append(
    [transection_id, user_id, date.date(), time,
     product, amount, Payment_Method,
     status, failure_reason, city])

    # Create DataFrame
columns = [
    "Transaction_ID", "User_ID", "Date", "Time",
    "Product_Type", "Amount", "Payment_Method",
    "Status", "Failure_Reason", "Location"]

df = pd.DataFrame(data, columns=columns)

# Save file
df.to_csv("phonepe_dataset.csv", index=False)

print("Dataset generated successfully!")    