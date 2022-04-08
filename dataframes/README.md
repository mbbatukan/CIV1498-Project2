# Dataframes
## This folder contains pickled dataframes.

* Because pickled datasets aren't human-readable files, please include revision number and your initials before the extension of file.

    * E.g., First revision uploaded by Albert Einstein --> df_LA_parcels_cleaned_REV1_AE.pkl
    
* Don't delete old files for version control purposes. 

## Notes:

1. Some outliers were removed from **df_LA_parcels_LAcity_filtered_REV2_MB.pkl** and saved as 
    * **df_LA_parcels_LAcity_cleaned_REV2_MB.pkl**, but this cleaned dataframe still includes outliers. 
    * Use compression="gzip" option to unpickle dataframes if it gives an error.

