import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#sgrdhttfgfyjhgkujhjkn
df=pd.read_csv(r"C:\Users\91934\OneDrive\Desktop\Electric_Vehicle_Population_Data.csv")
print(df.isnull().sum())
df["County"]=df["County"].fillna(df["County"].mode()[0])
df["City"]=df["City"].fillna(df["City"].mode()[0])
df["Postal Code"]=df["Postal Code"].fillna(df["Postal Code"].median())
df["Legislative District"]=df["Legislative District"].fillna(df["Legislative District"].median())
df["Vehicle Location"]=df["Vehicle Location"].fillna(df["Vehicle Location"].mode()[0])
df["Electric Utility"]=df["Electric Utility"].fillna(df["Electric Utility"].mode()[0])
df["2020 Census Tract"]=df["2020 Census Tract"].fillna(df["2020 Census Tract"].mode()[0])
print(df.isnull().sum())
#1)Find out which electric vehicle types are common in top cities

# Count vehicle types per city
top_cities = df['City'].value_counts().head(10).index
filtered = df[df['City'].isin(top_cities)]

# Group by city and vehicle type
type_counts = filtered.groupby(['City', 'Electric Vehicle Type']).size().unstack()
type_counts.plot(kind='bar', figsize=(12,6))
plt.title("Electric Vehicle Types in Top Cities")
plt.xlabel("City")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(title="Vehicle Type")
plt.tight_layout()
plt.show()

# 2. Check how electric range changes across different vehicle makes

plt.figure(figsize=(12,6))
sns.scatterplot(x="Make", y="Electric Range",data=df)
plt.title("Electric Range by Vehicle Make")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


#3 Compare number of EVs by model year
model_year_counts = df['Model Year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.bar(model_year_counts.index.astype(str), model_year_counts.values, color='skyblue')
plt.xlabel("Model Year")
plt.ylabel("Number of EVs")
plt.title("EV Adoption by Model Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#4.Find the most popular vehicle in "make" and "model"
top_makes = df['Make'].value_counts().head(5)

plt.figure(figsize=(8,5))
plt.pie(top_makes.values, labels=top_makes.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 5 EV Makes")
plt.show()

# Optional: Top models
top_models = df['Model'].value_counts().head(5)
plt.figure(figsize=(8,5))
plt.bar(top_models.index, top_models.values, color='green')
plt.title("Top 5 EV Models")
plt.xlabel("Model")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


#5. Explore EV popularity by ZIP Code or City


zip_counts = df['Postal Code'].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.bar(zip_counts.index.astype(str), zip_counts.values, color='orange')
plt.title("Top 10 ZIP Codes with Most EVs")
plt.xlabel("ZIP Code")
plt.ylabel("Number of EVs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#6.Finding out which electric car make is used the most by using a bar graph

# Count the number of cars for each make
make_counts = df['Make'].value_counts().head(10)  # Top 10 makes

# Create bar graph
plt.figure(figsize=(10,5))
plt.bar(make_counts.index, make_counts.values, color='skyblue')
plt.title("Top 10 Most Used Electric Vehicle Makes")
plt.xlabel("Make")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#7. This will show how many vehicles fall into different electric range values.

# Histogram of Electric Range
plt.figure(figsize=(10,5))
plt.hist(df['Electric Range'], bins=20, color='purple', edgecolor='black')
plt.title("Distribution of Electric Range")
plt.xlabel("Electric Range (miles)")
plt.ylabel("Number of Vehicles")
plt.grid()
plt.tight_layout()
plt.show()





#8.Heatmap: Correlation Between Numeric Columns
#This will show relationships between numeric features like Electric Range, Model Year


# Selecting numeric columns for correlation
numeric_data = df[['Model Year', 'Electric Range']]

# Create the correlation matrix
corr_matrix = numeric_data.corr()

# Plot heatmap
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
















