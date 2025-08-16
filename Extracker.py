import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Shivaraj.CSV', index_col=False)

print(df.head(3))
print(df.columns)
df['Posting Date'] = pd.to_datetime(df['Posting Date'])



df['Posting Date'] = pd.to_datetime(df['Posting Date'])
# print(df['Posting Date'].dtype) 
Unique = df['Details'].nunique()
print(Unique)


df['Description'] = df['Description'].str.lower()
df['Description'] = df['Description'].str.strip()
df['Description'] = df['Description'].str.replace(r'[*\-#]', ' ', regex=True)



data = {
    'stay': [
        'hilton', 'holiday inn', 'airbnb', 'motel', 'inn', 'suite', 'marriott', 
        'hyatt', 'hotel', 'resort'
    ],
    'travel': [
        'uber', 'lyft', 'metro', 'valley metro', 'bus', 'amtrak', 'southwest', 
        'delta', 'american airlines', 'united', 'airlines', 'trip', 'airport', 'turo'
    ],
    'food': [
        'chipotle', 'starbucks', 'mcdonald', 'chick fil a', 'restaurant', 
        'catering', 'food', 'domino', 'pizza', 'cafe', 'burger', 'kfc', 'subway', 
        'panda express', 'panera', 'popeyes', 'baskin', 'dunkin'
    ],
    'shopping': [
        'walmart', 'amazon', 'target', 'costco', 'temu', 'best buy', 'store', 
        'kohl', 'h&m', 'zara', 'ikea', 'dollar tree', 'five below', 'foot locker'
    ],
    'bills': [
        'verizon', 'srp', 'aps', 'xfinity', 't mobile', 'at&t', 'att', 'utility', 
        'utilities', 'electric', 'internet', 'wifi', 'water', 'gas', 'bill', 
        'payment', 'tmobile', 'comcast'
    ],
    'transfers': [
        'zelle', 'quickpay', 'venmo', 'paypal', 'cash app', 'square', 'remitly', 
        'google pay', 'apple pay', 'transfer', 'splitwise'
    ],
    'others': [
        'deposit', 'fee', 'service', 'charge', 'misc', 'unknown', 'adjustment', 
        'correction'
    ]
}


category_results = []

for index, row in df.iterrows():

    des = row['Description']
    category = 'others'

    for cat, keywords in data.items():
        for keyword in keywords:
            if keyword in des:
                category = cat
                break
        if category != 'others':
            break  
    category_results.append(category)

df['Category'] = category_results
df_expenses = df[df['Details'] == 'DEBIT']
df_expenses['Amount'] = df_expenses['Amount'].abs()

print(df[['Description', 'Category']].head(50))

plt.figure(figsize=(8,8))
category_totals = df_expenses.groupby('Category')['Amount'].sum()
plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)
plt.title("Spending by Category")
plt.axis('equal')  # keeps it as a circle
plt.show()

plt.savefig("category_spending_pie.png")

