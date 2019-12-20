# Possible reason why establishments go out of business in Chicago

# Abstract
This project aims at analyzing the Food inspections dataset of the city of Chicago and gaining insight on reasons why businesses might be ceasing their operations. Different analysis is done based on the lifetime of the businesses, their violation types and their location. We further our investigation by utilizing other complementary datasets. We were able to conclude that the position of an establishment, the high number of restaurants clustered together as well as its lifetime are indicating factors of its possible failure. Furthermore, we observed that violations contrary to our belief do not represent a decisive factor.

# Research questions
* Is there any correlation between facilities going out of business and their location?
* Are the violations present related to facilities going out of business?
* Is there a correlation between a business’s age and it going out of business?

# Data set
We will use the provided data set called Chicago Food Inspections (https://www.kaggle.com/chicago/chicago-food-inspections). It is in a csv format and provides information such as violations, type of facility, and location. We try to gain more insight by augmenting our datset with other datasets provided by the city of Chicago. Those datasets are:
* Census Data - Selected socioeconomic indicators in Chicago (https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2) - provides us socioeconomic information about each region separately.
* Boundaries (https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6) - provides detailed latitude and longitude of each reason. We use this to know in which region each of our establishments is by using latitude and longitude.

# Note
We have separated the cleaning part of our work with the analysis one, for the sake of keeping our notebook a bit cleaner. Hence our repository has two files. The dba_name_cleanup.py is a python script which cleans the database entries and saves the result as a file. The Analysis.ipynb represents our complete analysis into one notebook.

Everyone from the team provided an equal amount of contribution to this project.
