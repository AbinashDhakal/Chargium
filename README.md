# Chargium - Electric Charging Station Locator
Chargium is a project developed as part of the TechLabs London "Digital Shaper Program" in the Summer of 2021. The aim of this project is to provide users with a solution to identify electric charging stations during their journeys, addressing the common problem of navigating to charging stations without significantly extending travel time.
[Chargium Article](https://medium.com/@london_6354/chargium-e0d7e91aa198)

## Overview
With the increasing number of electric vehicles and charging points in the UK, Chargium offers a practical way for electric car users to find charging stations conveniently. The project utilizes data from the openchargemap website, providing a comprehensive dataset of charging station locations.

## Features
Data Collection: The project starts with the collection of charging station data from openchargemap, using tools like Parse Hub for efficient extraction of postcodes and long addresses.

Data Representation: Mapbox, a location data platform, is employed to visualize the dataset on a map, with each charging station represented by a dot. Geographical coordinates are derived from postcodes for accurate mapping.

Charging Station Distribution: The project aims to guide users to charging stations based on their specific needs. While the original mission was to enable users to navigate to specific types of chargers, limitations in available data restricted the functionality. Nevertheless, the map provides guidance to generic charging stations.

Exploratory Data Analysis: The dataset is loaded into Pandas data frame for exploratory data analysis. The analysis includes gathering insights into the number of charging points, power output per station, and other relevant information.


TechLabs London
TechLabs London is part of a non-profit learning accelerator for technology skills that aims to equip young people with the digital skills they need.

## Conclusion
Chargium contributes to the growing ecosystem of electric vehicle infrastructure by providing users with an efficient tool to locate charging stations. The project combines data science, web scraping, and visualization techniques to create a user-friendly solution for electric car enthusiasts.
