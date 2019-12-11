import pandas as pd
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import geopandas as gpd

df = pd.read_csv('food-inspections.csv')
df.set_index('Inspection ID', inplace=True)
df.to_csv('food-inspections(old).csv')
print("Old food inspections file saved to food-inspections(old).csv")

df['DBA Name'] = df['DBA Name'].apply(lambda x: x.upper())

'''The cleaning is only applied to the DBA Names'''
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.replace("'", '')) #Removing single quotes (')
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.replace(",", '')) #Removing commas (,)
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.replace("LTD", '')) #Removing the word LTD
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.replace(".", '')) #Removing full stops (.)
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.replace("INC", '')) #Removing INC
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.replace("LLC", '')) #Removing LLC
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.replace("  ", ' ')) #Removing double spacing
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.replace("   ", ' ')) #Removing triple spacing
df['DBA Name'] = df['DBA Name'].apply(lambda x: x.strip()) #Removing spaces in the end and in the beginning

'''Handling of special stores, such as chains or brands'''
df['DBA Name'] = df['DBA Name'].apply(lambda x: "SUBWAY" if "subway" in x.lower()  else x) #Removing different writings of subway
df['DBA Name'] = df['DBA Name'].apply(lambda x: "MCDONALDS" if ("mc" in x.lower() and "donald" in x.lower() ) else x) #Removing different writings of mcdonalds
df['DBA Name'] = df['DBA Name'].apply(lambda x: "DUNKIN DONUTS" if ("dunkin" in x.lower() and "donuts" in x.lower() )  else x) #Removing different writings of dunkin donuts
df['DBA Name'] = df['DBA Name'].apply(lambda x: "KFC" if ("kfc" in x.lower() or ("kentucky" in x.lower() and "fried" in x.lower() and "chicken" in x.lower() ))  else x) #Removing different writings of KFC
df['DBA Name'] = df['DBA Name'].apply(lambda x: "STARBUCKS" if "starbucks" in x.lower()  else x) #Removing different writings of starbucks
df['DBA Name'] = df['DBA Name'].apply(lambda x: "7-ELEVEN" if ("7" in x.lower() and "eleven" in x.lower() )  else x) #Removing different writings of 7 - Eleven
df['DBA Name'] = df['DBA Name'].apply(lambda x: "AFC SUSHI" if ("afc" in x.lower() and "sushi" in x.lower() )  else x) #Removing different writings of AFC Sushi
df['DBA Name'] = df['DBA Name'].apply(lambda x: "ALDI" if "aldi" in x.lower()  else x) #Removing different writings of ALDI
df['DBA Name'] = df['DBA Name'].apply(lambda x: "POPEYES" if "popeyes" in x.lower()  else x) #Removing different writings of Popeyes
df['DBA Name'] = df['DBA Name'].apply(lambda x: "CHIPOTLE MEXICAN GRILL" if "chipotle" in x.lower()  else x) #Removing different writings of Chipotle
df['DBA Name'] = df['DBA Name'].apply(lambda x: "WENDYS" if "wendys" in x.lower()  else x) #Removing different writings of WENDYS
df['DBA Name'] = df['DBA Name'].apply(lambda x: "TACO BELL" if ("taco" in x.lower() and "bell" in x.lower() )  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "PIZZA HUT" if ("pizza" in x.lower() and "hut" in x.lower() )  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "WHOLE FOODS" if ("whole" in x.lower() and "foods" in x.lower() )  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "BURGER KING" if ("burger" in x.lower() and "king" in x.lower() )  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "DOMINOS" if ("dominos" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "ARBYS" if ("arbys" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "JEWEL FOOD STORE" if ("jewel" in x.lower() and "food" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "CHURCHS CHICKEN" if ("churchs" in x.lower() and "chicken" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "WALMART " if "walmart" in x.lower()  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "POTBELLY SANDWICH WORKS" if ("potbelly" in x.lower() and "sandwich" in x.lower() and "works" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "JIMMY JOHNS" if ("jimmy" in x.lower() and "johns" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "HAROLDS CHICKEN" if ("harolds" in x.lower() and "chicken" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "PAPA JOHNS PIZZA" if ("papa" in x.lower() and "johns" in x.lower() and "pizza" in x.lower())  else x)

#------------------RUSTY CODE----------------------------------------
df['DBA Name'] = df['DBA Name'].apply(lambda x: "LOLAS CONEY" if ("lolas" in x.lower() and "coney" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "SALERNOS PIZZA" if ("salernos" in x.lower() and "pizza" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "SONGBIRD ACADEMY" if ("songbird" in x.lower() and "academy" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "DA LOBSTA" if ("da" in x.lower() and "lobsta" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "GIORDANOS PIZZA" if ("giordanos" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "BOTTLED BLONDE" if ("bottled" in x.lower() and "blonde" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "ROSATIS PIZZA" if ("rosatis" in x.lower() and "pizza" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "YMCA" if ("ymca" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "TIPPY TOT DAYCARE" if ("tippy" in x.lower() and "tot" in x.lower() and "daycare" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "QUIOTE" if ("quiote" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "MCCORMICK PLACE" if ("mccormick" in x.lower() and "place" in x.lower() or "mccornick" in x.lower() and "place" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "FOOD 4 LESS" if ("food" in x.lower() and "4" in x.lower() and "less" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "LEVY RESTAURANTS" if ("levys" in x.lower() and "restaurants" in x.lower() or "levy" in x.lower() and "restaurants" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "PETES MEAT & GROCERY #2" if ("PETES MEAT & GROCERY#2" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "SKYHIGH-101" if ("skyhigh" in x.lower() and "-" in x.lower() and "101" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "SUNSET CAFE" if ("sunset" in x.lower() and "cafe" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "SPORT SERVICE SOLDIER FIELD" if ("sport" in x.lower() and "service" in x.lower() and "soldier" in x.lower() and "field" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "PETES MARKET" if ("petes" in x.lower() and "market" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "GACE PARK FOOD" if ("gace" in x.lower() and "park" in x.lower() and "food" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "CASA CENTRAL COMMUNITY SERVICE" if ("casa central community services" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "ST ELIZABETH ELEMENTARY SCHOOL" if ("St Elizabeth Elem School" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "ALS PIZZA" if ("als" in x.lower() and "pizza" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "PRET A MANGER" if ("pret a manager" in x.lower())  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "I-CAFE" if ("I - CAFE SUKURS PLACE PIDE VE LAHMACUN" in x or "I - CAFE" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "UNITED FIRST INTERNATIONAL LOUNGE T1CONCOURSE C" if ("UNITED FIRST INTERNATIONAL LOUNGE T-1 CONCOURSE C" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "SUNSET CAFE" if ("SUNSET CAFFE" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "LA CABANA GRILL" if ("LA CAVANA" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "EURO CONVENIENT" if ("EURO CONVENIENT STORE" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "THE TWO LIONS PUB & GRILL" if ("THE RED LION PUB AND GRILLE" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "OH FUSION THAI & SUSHI BAR" if ("NINEFACE THAI & SUSHI BAR" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "GATEWAY NEWSTAND" if ("GATEWAY NEWSTANDS" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "JENNYS GOURMET RESTAURANT" if ("JEANNYS GOURMET RESTAURANT" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "GOLDEN HOOKS FISH & CHICKEN" if ("GOLDEN HOOKS FISH & CHICAGO" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "AL MEDINA RESTAURANT" if ("AL MEDINA RESTAURANT & GRILL" in x)  else x)
df['DBA Name'] = df['DBA Name'].apply(lambda x: "HOOK FISH AND CHICKEN" if ("HOOK FISH & CHICKEN" in x)  else x)

df['Facility Type'] = df['Facility Type'].apply(lambda x: str(x))
df['Facility Type'] = df['Facility Type'].apply(lambda x: x.upper())

df['Facility Type'] = df['Facility Type'].apply(lambda x: x.replace("  ", ' ')) #Removing double spacing
df['Facility Type'] = df['Facility Type'].apply(lambda x: x.replace("/ ", '/')) #Removing double spacing
df['Facility Type'] = df['Facility Type'].apply(lambda x: x.replace(" /", '/')) #Removing double spacing
df['Facility Type'] = df['Facility Type'].apply(lambda x: x.replace("   ", ' ')) #Removing triple spacing
df['Facility Type'] = df['Facility Type'].apply(lambda x: "CONVENIENCE STORE" if ("(convenience store)" == x.lower() or "convenience" == x.lower() or "convenient store" == x.lower() or "convnience store" == x.lower() )  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "LONG-TERM CARE" if ("long" in x.lower() and "term" in x.lower() and "care" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "MOBILE FOOD/DESSERT" if ("mobil" in x.lower() and ("food" in x.lower() or "dessert" in x.lower()) )  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "MOVIE THEATER" if ("movie" in x.lower() or "theat" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "BANQUET" if ("banquet" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "DAYCARE" if (("day" in x.lower() and "care" in x.lower()) or ("servic" in x.lower() and ("children" in x.lower() or "childern" in x.lower())) or "1023" in x.lower() or "15 monts to 5 years old" == x.lower() )  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "ASSISTED LIVING/NURSING HOME" if (("assisted" in x.lower() or "assissted" in x.lower()) and "living" in x.lower()) or ("nursing home" in x.lower()) or "supportive living" in x.lower()  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "CHARTER SCHOOL" if ("charter" in x.lower() and "school" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "CHURCH" if ("church" in x.lower() or "religious" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "CANDY" if ("candy" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "GAS STATION/w. other services" if ("gas" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "ART GALLERY" if ("art" in x.lower() and "gallery" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "HOSPITAL" if ("hospital" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "RESTAURANT" if ("restaurant" in x.lower() or "restuarant" in x.lower() or "rstaurant" in x.lower() or "dining hall" == x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "COOKING SCHOOL" if (("cooking" in x.lower() and "school" in x.lower()) or "culinary" in x.lower() or "pastry" in x.lower() )  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "PHARMACY" if ("pharmacy" in x.lower() or "drug" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "COMMISSARY" if ("commiasary" in x.lower() or "commis" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "GROCERY" if ("grocery" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "HERBAL" if ("herbal" in x.lower() or "heraba" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "HOOKA" if ("hooka" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "BAKERY" if ("bakery" in x.lower() or "donut" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "WAREHOUSE" if ("warehouse" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "KITCHEN" if ("kitchen" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "HOT DOG" if ("hot dog" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "POPCORN" if ("popcorn" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "WHOLESALE" if ("wholesale" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "RETAIL STORE" if ("retail" in x.lower() or "grocery" in x.lower() or "convenience store" in x.lower() or "dollar" in x.lower() or "store" in x.lower() or "gift" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "TAVERN" if ("tavern" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "CAFETERIA" if ("cafeteria" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "GOLF COURSE" if ("golf" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "ROOFTOP" if ("roof" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "ICE CREAM" if ("ice cream" in x.lower() or "gelato" in x.lower() or "paleteria" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "GYM" if ("gym" in x.lower() or "exercise" in x.lower() or "fitness" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "LIQUOR" if ("liquor" in x.lower() or "liqour" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "CAFE" if ("cafeteria" not in x.lower() and ("riverwalk" in x.lower() or "cafe" in x.lower() or "coffee" in x.lower()))  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "NON-PROFIT" if ("profit" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "KIOSK" if ("kiosk" in x.lower() or "newsstand" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "BUTCHER" if ("butcher" in x.lower() or "slaughter" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "DISTRIBUTION" if ("distribut" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "SCHOOL" if ("cooking" not in x.lower() and ("school" in x.lower()))  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "PACKAGED FOOD" if ("package" in x.lower() or "pacakage" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "PRODUCE VENDOR/STAND" if ("produce" in x.lower())  else x)
df['Facility Type'] = df['Facility Type'].apply(lambda x: "BAR" if ("bar" in x.lower())  else x)

'''Filling up some places facility type. Brands like mcdonalds in some cases have some missing'''
eminemsDictionary = {}
for index, row in df.iterrows():
    if row['Facility Type'] != "NAN":
        if row['Facility Type'] not in eminemsDictionary:
            eminemsDictionary[row['DBA Name']] = row['Facility Type']
for index, row in df.iterrows():
    if row['Facility Type'] == "NAN" and row['DBA Name'] in eminemsDictionary:
        df.at[index,'Facility Type'] = eminemsDictionary[row['DBA Name']]

df['Inspection Type'] = df['Inspection Type'].apply(lambda x: str(x))
df['Inspection Type'] = df['Inspection Type'].apply(lambda x: x.upper())

df = df[~(df["Inspection Type"] == "NAN")]
df['Inspection Type'] = df['Inspection Type'].apply(lambda x: "CANVASS" if ("canvass" in x.lower() or "canvas" in x.lower() or "RECENT INSPECTION" in x)  else x)
df['Inspection Type'] = df['Inspection Type'].apply(lambda x: "OUT OF BUSINESS" if ("out" in x.lower() and "busines" in x.lower() or "o.b." in x.lower())  else x)
df['Inspection Type'] = df['Inspection Type'].apply(lambda x: "TASK FORCE LIQUOR" if ("liquor" in x.lower() or "1474" in x or "1470" in x)  else x)
df['Inspection Type'] = df['Inspection Type'].apply(lambda x: "FIRE-COMPLAINT" if ("fire" in x.lower())  else x)
df['Inspection Type'] = df['Inspection Type'].apply(lambda x: "SUSPECTED FOOD POISONING" if ("food" in x.lower() and "poisoning" in x.lower() or "two people ate and" in x.lower() )  else x)
df['Inspection Type'] = df['Inspection Type'].apply(lambda x: "COMPLAINT" if ("POISONING" in x or "COMPLAINT" in x)  else x)
df['Inspection Type'] = df['Inspection Type'].apply(lambda x: "LICENSE" if ("LICENSE RE-INSPECTION" in x or "TASK FORCE" in x or "CONSULTATION" in x)  else x)

op = df.groupby("Inspection Type").count().sort_values(by=['DBA Name'], ascending = False)
useless_inspections =[]
for index, row in op.iterrows():
    if row['DBA Name'] < 100:
        useless_inspections.append(index)

df['Inspection Type'] = df['Inspection Type'].apply(lambda x: "SHIT" if x in useless_inspections  else x)
df = df[~(df["Inspection Type"] == "SHIT")]

df = df[~(df['Facility Type'] == "NAN")]

#-------------------------------------------RUSTYS Regions------------------------------------------------
df = df.drop(columns = ['Historical Wards 2003-2015','Zip Codes', 'Community Areas', 'Census Tracts', 'Wards', 'City', 'State'])
chicago_boundaries = gpd.read_file('Boundaries_Chicago.geojson')

# Cleaning the data set: removing rows with Risk value other than 1-3
df = df[df.Risk.str.contains("[1-3]",na=False)]
# Converting Risk value to numeric
df['Risk'] = df.Risk.apply(lambda x: int(x.strip('Risk')[1]))
#Get rid of nan positions -> you might want to delete this afterwards
df = df[~df['Latitude'].isnull()]
#Adds nan column called regions
df = df.assign(Regions=np.nan)
#Creates an array holding names of all regions
all_regions = [None] * df.shape[0]

for i in range(df.shape[0]):
    j = 0
    for name in chicago_boundaries['pri_neigh']:
        x = df['Longitude'].iloc[i]
        y = df['Latitude'].iloc[i]
        polygon = chicago_boundaries['geometry'].iloc[j]
        point = Point(x,y) # create point
        #print(polygon.contains(point)) # check if polygon contains point
        if(point.within(polygon)):
            all_regions[i] = name
            break
        j = j + 1

#Add regions to the region column
df['Regions'] = all_regions

#Finds out which inspections have not been assigned to a given region
missings_all = df[df['Regions'].isnull()]

#These locations were on the borders, they had to included manually
unique_longitude_all = missings_all['Longitude'].unique()
unique_latitude_all = missings_all['Latitude'].unique()

#Include locations on borders
for index, row in missings_all.iterrows():
    if row['Longitude'] == unique_longitude_all[0] and row['Latitude'] == unique_latitude_all[0]:
        df.at[index, 'Regions'] = "O'Hare"
    if row['Longitude'] == unique_longitude_all[1] and row['Latitude'] == unique_latitude_all[1]:
        df.at[index, 'Regions'] = 'Near North'
    if row['Longitude'] == unique_longitude_all[2] and row['Latitude'] == unique_latitude_all[2]:
        df.at[index, 'Regions'] = 'Mount Greenwood'




df.to_csv('food-inspections.csv')
print("DONE")