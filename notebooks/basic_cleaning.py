df_LA_parcels_LAcity_filtered = pd.read_pickle(f"{folder_location}/dataframe/df_LA_parcels_LAcity_filtered.pkl")

df_dummy = df_LA_parcels_LAcity_filtered.copy()
len0 = len(df_dummy)

for col in ["YearBuilt", "EffectiveYearBuilt"]:
    # Remove rows if BuiltYear and EffectiveYearBuilt are less than 1850
    len1 = len(df_dummy)
    df_dummy = df_dummy[df_dummy[col] >= 1850]
    len2 = len(df_dummy)
    print(f"The number of rows removed from {col}: {len1 - len2} and it is about {round((len1 - len2)/len1*100, 3)}% of the total number of parcels.")

for col in ["LandBaseYear"]:
    # Remove the parcel with LandBaseYear = 1907
    len1 = len(df_dummy)
    df_dummy = df_dummy[df_dummy[col] >= 1908]
    len2 = len(df_dummy)
    print(f"The number of rows removed from {col}: {len1 - len2} and it is about {round((len1 - len2)/len1*100, 3)}% of the total number of parcels.")

for col in ["TotalValue"]:
    # Limit TotalValue to $50M
    len1 = len(df_dummy)
    df_dummy = df_dummy[df_dummy[col] <= 5e7]
    len2 = len(df_dummy)
    print(f"The number of rows removed from {col}: {len1 - len2} and it is about {round((len1 - len2)/len1*100, 3)}% of the total number of parcels.")

for col in ["Bedrooms"]:
    # Remove Bedrooms more than 19
    len1 = len(df_dummy)
    df_dummy = df_dummy[df_dummy[col] <= 19]
    len2 = len(df_dummy)
    print(f"The number of rows removed from {col}: {len1 - len2} and it is about {round((len1 - len2)/len1*100, 3)}% of the total number of parcels.")

for col in ["Bathrooms"]:
    # Remove Bathrooms more than 20
    len1 = len(df_dummy)
    df_dummy = df_dummy[df_dummy[col] <= 20]
    len2 = len(df_dummy)
    print(f"The number of rows removed from {col}: {len1 - len2} and it is about {round((len1 - len2)/len1*100, 3)}% of the total number of parcels.")

for col in ["SQFTmain"]:
    # Limit SQFTmain in between 500 to 40K
    len1 = len(df_dummy)
    df_dummy = df_dummy[(df_dummy[col] <= 40000) & (df_dummy[col] >= 500)]
    len2 = len(df_dummy)
    print(f"The number of rows removed from {col}: {len1 - len2} and it is about {round((len1 - len2)/len1*100, 3)}% of the total number of parcels.")

for col in ["ShapeSTAre"]:
    # Limit ShapeSTAre in between 1K to 600K
    len1 = len(df_dummy)
    df_dummy = df_dummy[(df_dummy[col] <= 600000) & (df_dummy[col] >= 1000)]
    len2 = len(df_dummy)
    print(f"The number of rows removed from {col}: {len1 - len2} and it is about {round((len1 - len2)/len1*100, 3)}% of the total number of parcels.")

for col in ["ShapeSTLen"]:
    # Limit ShapeSTLen to 4K
    len1 = len(df_dummy)
    df_dummy = df_dummy[df_dummy[col] <= 4000]
    len2 = len(df_dummy)
    print(f"The number of rows removed from {col}: {len1 - len2} and it is about {round((len1 - len2)/len1*100, 3)}% of the total number of parcels.")

len_final = len(df_dummy)
print(f"The number of rows removed: {len0 - len_final} and it is about {round((len0 - len_final)/len0*100, 3)}% of the total number of parcels.")

df_LA_parcels_LAcity_cleaned_REV2 = df_dummy.copy()

# sns.pairplot(df_LA_parcels_LAcity_cleaned_REV2, x_vars=["SQFTmain", "LandBaseYear", "YearBuilt", "EffectiveYearBuilt", "Bedrooms", "Bathrooms", "BusBenchClosestDist", "SubwayStopClosestDist", "ShapeSTAre", "ShapeSTLen"], y_vars=["LandValue", "TotalValue"])

# The number of rows removed from YearBuilt: 139 and it is about 0.032% of the total number of parcels.
# The number of rows removed from EffectiveYearBuilt: 44 and it is about 0.01% of the total number of parcels.
# The number of rows removed from LandBaseYear: 5 and it is about 0.001% of the total number of parcels.
# The number of rows removed from TotalValue: 19 and it is about 0.004% of the total number of parcels.
# The number of rows removed from Bedrooms: 3 and it is about 0.001% of the total number of parcels.
# The number of rows removed from Bathrooms: 7 and it is about 0.002% of the total number of parcels.
# The number of rows removed from SQFTmain: 846 and it is about 0.192% of the total number of parcels.
# The number of rows removed from ShapeSTAre: 109 and it is about 0.025% of the total number of parcels.
# The number of rows removed from ShapeSTLen: 10 and it is about 0.002% of the total number of parcels.
# The number of rows removed: 1182 and it is about 0.268% of the total number of parcels.