# How the dataset was filtered:

1. “Residential” parcels from “GeneralUseType” column

2. “SFR” parcels from “PropertyType” column

3. “Unit == 1” from “Units” column

4. “totBuildingDataLines == 1” from “totBuildingDataLines” column

5. “["0100", "0101", "0103", "0104"]” from “PropertyUseCode” column
    * See columns for more information
    
6. Rows with [“Public (non-taxable government-owned)”, "Public Entity (Green Code)", “"State Board of Equilization Assessed"] were all removed from “SpecialParcelClassification” column
    * It basically means that dataset only includes “Private” parcels
    
7. The percentage of taxable parcels in the dataset (verified from “isTaxableParcel?” column)
    * 100%

8. The remaining parcels were filtered based on the “ZIPcode5” column to just include Los Angeles City Zip codes
    * LA Zip codes can be accessed from the following link: https://geohub.lacity.org/datasets/lahub::los-angeles-city-zip-codes/explore?location=34.021109%2C-118.411777%2C11.28

9. “[“RollYear” == 2021]” from “RollYear” column to get the most recent data for “LandValue” and “TotalValue”


# Columns in the data: (Number of rows = 168869)

1. “AIN” = unique identifier for each parcel (int)
2. “SQFTmain” = Area of building (float)
3. “ShapeSTAre” = Area of parcel (SQFT – float)
4. “ShapeSTLen” = Length of the parcel (didn’t check unit (probably FT) – float)
5. “Bedrooms” (int)
6. “Bathrooms” (int)
7. “PropertyUseCode” = (object)
    * No Pool (“100”)
    * Pool (“101”) 
    * Pool and Miscellaneous (“103”)
    * Therapy Pool (“104”)
8. “YearBuilt” = (int)
9. “EfectiveYearBuilt” = (int)
10. “TaxRateArea” = Haven’t checked what that means (int)
11. “Cluster” = would be great if you could figure it out how parcels were clustered. (int)
12. “ZIPcode5” and “ZIPcode4” = self-explanatory (int)
13. “BusBenchClosestDist” = Haversine distance between center of parcel to nearest bus bench (FT – float)
14. “SubwayStopClosestDist” = Haversine distance between center of parcel to nearest subway station (FT – float)
15. “Neighborhood” = name of the neighborhood where parcel is located (object)

16. **Total ImprovementValue from 2006 to 2021 (float) (This column will be added later)**
17. **How many times it was improved between 2006-2021 (int) (This column will be added later)**

**Please let me know if we can improve the existing features or add new ones to the list.**

