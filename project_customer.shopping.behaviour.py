import pandas as pd

df= pd.read_csv("customer_shopping.csv")
print(df.head())

df.info()


#1...to check the summary statistics
print(df.describe(include='all'))



#2...TO check the missing values

#print(df.isnull().sum())



#3...replacing the null values in "review rating" with median of the column so that there will be no null values

df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

print(df.isnull().sum())



#4...changing the format of the column names into similar case type by changing it into snakecase i.e. everything in lower case and replacing spaces with underscore
#to amke dealing with data easier

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
print(df.columns)

#replacing the column name "purchase_amount_(usd)" with "purchase_amount"

df = df.rename(columns = {'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)



#5...create a cloumn "age_group"
labels=['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)

print(df[['age', 'age_group']].head(10))


#6...create a cloumn "purchase_frequency_dates"

frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Annually': 365,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Monthly' : 30,
    'Every 3 Months' : 90
}
df["purchase_frequency_dates"]= df["frequency_of_purchases"].map(frequency_mapping)
print(df[["purchase_frequency_dates","frequency_of_purchases"]].head(10))



#7...Removing the "Promo Code" column since it is same as "Discount" column

#to view both the columns
print(df[["discount_applied", "promo_code_used"]].head(10))

#to check if the values in both the cloumn are same

print((df["discount_applied"]== df["promo_code_used"]).all())

# deleting the column "promo_code_used"

df= df.drop('promo_code_used', axis=1)
print(df.columns)




