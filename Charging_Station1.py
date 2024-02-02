import re

text = """
MFG MILE CROSS LANE 
Mile Cross Lane
Mile Cross
England
NR6 6RQ
United Kingdom
View
Public
Operational
EPPING FOREST CORNMILL 
Cornmill
Waltham Abbey
England
EN9 1RD
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
TESLA SUPERCHARGER, NORWICH EAST 
Northern Distributor Road
Postwick with Witton
England
NR13 5GE
United Kingdom
View
Public - Membership Required
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
CROMPTON CLOSE 
Crompton Close
Basildon
England
SS14 3AL
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
TOLVADDON ROAD 
1 Tolvaddon Road
Carn Brea
Camborne
TR14 0BJ
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
RIVERMEAD LEISURE CENTRE 
Richfield Avenue
Reading
RG1 8BY
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
COLUMBUS WAY 
Columbus Way
Andover
SP10 5NP
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
JET REFINERY FILLING STATION 
Eastfield Road
South Killingholme
England
DN40 3DJ
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
THE BAY TREE PUB 
Westbrook
Wantage
England
OX12 0AN
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
LEVERSTOCK GREEN SHOPPING PARADE 
Leverstock Green Road
Hemel Hempstead
HP3 8QG
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
OLD FORGE GARAGE 
Menefreda Way
St Minver
Wadebridge
PL27 6QJ
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
PRINCESS STREET CAR PARK 
Princess Street
Congleton
CW12 1DF
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 Type 2 (Tethered Connector)
HICKS ROAD 
Hicks Road
1 Hicks Road
Markyate
AL3 8LJ
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
SKIPTON HIGH STREET CAR PARK 
Jerry Croft
Skipton
BD23 1ED
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
WHITE LION 
White Lion
Dunstable
Houghton Regis
LU6 1RS
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
AUBREY ARMS 
Aubrey Arms
Swansea Road
Cardiff
CF5 6TQ
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
PLOUGH 
Plough
Newark Road
Lincoln
LN6 8RJ
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
HOWARD'S LANE CAR PARK 
Howard's Lane
Wareham Town
Wareham
England
BH20 4HU
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
CATTLE MARKET CAR PARK 
14 Bridge Street
Frome
Somerset
BA11 3HY
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
CLARKS INTERNATIONAL 
40 High St
Street
BA16 0EQ
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
WBC SOUTH CAR PARK 
Oglethorpe Court
Godalming
England
GU7 1AJ
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
TESLA - GRIDSERVE ELECTRIC FORECOURT 
Ring Road South
Crawley
England
RH6 0NT
United Kingdom
View
Private - Restricted Access
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
THE MERLIN 
Drove Road
New Town
Swindon
England
SN1 3AF
United Kingdom
View
Public - Pay At Location
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
30 THE STABLES 
Bowleaze Coveway
Weymouth
Dorset
DT3 6PP
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
TESLA ROMFORD SUPERCHARGER 
The Liberty Shopping Centre
Romford
RM1 3JT
United Kingdom
View
Public - Membership Required
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
SWAN 
Swan
Stourbridge Road
Fairfield
B61 9NG
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BLACKSMITHS ARMS 
1 Downs Barn Boulevard
Milton Keynes
Bedfordshire
MK14 7QG
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
CARR GATE GARDEN CENTRE 
Carr Gate Garden Centre
Bradford Road
Wakefield
WF2 0SY
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CHAdeMO
THE KINGS HEAD 
Southam Road
Napton on the Hill
Stratford-on-Avon
Warwickshire
CV47 8NG
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
ORTONGATE SHOPPING CENTRE 
Ortongate Shopping Centre
Orton Goldhay
Peterborough
PE2 5TD
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
SALT ASH PLACE 
Salt Ash Place
Great Cranford St
Poundbury
DT1 3HS
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
TESLA LUTON GIPSY LANE RETAIL PARK 
Gipsy Lane
Park Town
Luton
England
LU1 3JH
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
OSPREY RAPID CHARGING 1  
Colchester Retail Park
Sheepen Road
Colchester
CO3 3LL
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
FISHERGATE CENTRE CAR PARK 
Butler Street
Avenham
England
PR1 8HJ
United Kingdom
View
Public
Not Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
GREAT HOLLANDS SHOPS 
Great Hollands Square
Hanworth
Bracknell
England
RG12 8UX
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
APPLEGREEN ELECTRIC CHARNOCK RICHARD NORTHBOUND   2
Charnock Richard Northbound
PR7 5LR
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BOURNE LEISURE-LITTLECOTE HOUSE 
Littlecote House
Hungerford
RG17 0SU
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
HOCHTIEF MURPHY JOINT VENTURE 
Old Kent Road
Southwark
London
SE15 1JZ
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
LOVAT PARKS-PENMARLAM LODGE RETREAT 
Bodinnick
Fowey
Cornwall
PL23 1LZ
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
STANTON ST JOHN VILLAGE HALL 
Middle Road
Stanton St John
OX33 1HD
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
BASEPOINT BUSINESS CENTRE 
Chairborough Road
Castlefield
High Wycombe
England
HP12 3UL
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
ETHORPE HOTEL 
Ethorpe Crescent
Gerrards Cross
Gerrards Cross
England
SL9 8QR
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BERKELEY HOMES-FARMSTEAD 
Horseshoe Lane
Cranbrook
TN17 3FB
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
HUNTINGDON CREMATORIUM 
Mayfield Heath Farm
Sapley Road
Huntington
England
PE28 2NX
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
ROCK MILL HOLIDAY APARTMENTS 
Rock Mill
The Dale
Stoney Middleton
S32 4TF
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
THE OLD LIBRARY 
14 Park Square
Masham
HG4 4HF
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
NEW INN 
New Inn
Ounsdale Road
Wombourne
WV5 9EY
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
FLY LINE 
Fly Line
Aberford Road
Garforth
LS25 2EB
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
THE BELL INN 
The Bell Inn
Newport Road
Shifnal
TF11 8PS
United Kingdom
View
Public - Pay At Location
Partly Operational (Mixed)
 Level 3: High (Over 40kW)
 CCS (Type 2)
ADMIRAL HOUSE 
78 St Leonard's Road
Windsor
SL4 3BL
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
THE HADCROFT 
The Hadcroft
Grange Lane
Stourbridge
DY9 7DX
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
FFORDD ANGOR / ANCHOR DRIVE 
Ffordd Angor / Anchor Drive
St. David's and the Cathedral Close
Cymru / Wales
SA62 6BW
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
KILLEAVY CASTLE ESTATE 
Ballintemple Road
BT35 8LQ
United Kingdom
View
Public - Membership Required
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
ARNHALL BUSINESS PARK 
Venture Way
Westhill
Aberdeen
Aberdeenshire
AB32 6BQ
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
CAIRN LODGE SERVICES 
Cairn Lodge Services
Alba / Scotland
ML11 0RJ
United Kingdom
View
Public - Membership Required
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
SHELL FOSSETTS WAY 
Fossetts Way
Southend-on-Sea
England
SS2 4DQ
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CHAdeMO
WALTON COURT 
Station Avenue
Walton-on-Thames
KT12 1FJ
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
EV POINT, BAYNARDS GREEN 
B4100
Stoke Lyne
England
OX27 7SG
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BILLINGHAM GOLF CLUB 
Sandy Lane
Stockton-on-Tees
Billingham
England
TS22 5NA
United Kingdom
View
Public
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
BILLINGBEAR PARK GOLF CLUB 
The Straight Mile
Wokingham
England
RG40 5SJ
United Kingdom
View
Public
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
RIPON CITY GOLF CLUB 
Palace Road
Ripon
England
HG4 3HH
United Kingdom
View
Public
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
ROYAL WOOTTON RUGBY CLUB 
Malmesbury Road
Royal Wootton Bassett
Swindon
England
SN4 8DS
United Kingdom
View
Public
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
MICK APPLEBY RACING & BREADING 
The Homestead
Langham
Oakham
England
LE15 7EJ
United Kingdom
View
Public
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
BP 
Park Street
Thame
England
OX9 3HS
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BOUNDARY HOUSE 
Oxford Road
Northcourt
Abingdon
England
OX14 2ED
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BLOOR HOMES 
5 Bellenger Drive
Carterton
England
OX18 1PQ
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BP 
Newnham Avenue
Castle
Bedford
England
MK40 3UQ
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
MCDONALDS 
Fairhill
Harpur
Bedford
England
MK41 7FY
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
WEETABIX, BURTON LATIMER 
Station Road
Burton Latimer
NN15 5JR
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
WOLDS EDGE HOLIDAY LODGES 
Main Street
Bishop Wilton
York
YO42 1RX
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
UCKFIELD RETAIL PARK CAR PARK 
Uckfield Retail Park
off A272
Uckfield
TN22 2DU
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
3 THE STABLES 
Bowleaze Coveway
Weymouth
Dorset
DT3 6PP
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
PORT OF BOSTON 
St John's Road
Skirbeck
Boston
PE21 6BN
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
STARBUCKS INTOWN ROAD 
Starbucks Intown Road
Intown Road
Aberdeen
AB23 8EE
United Kingdom
View
Public - Pay At Location
Partly Operational (Mixed)
 Level 3: High (Over 40kW)
 CCS (Type 2)
FOLLY FARM LEISURE LTD 
Folly Farm Leisure LTD
Begelly
SA68 0XA
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
BOAT HOUSE 
Boat House
London Road
Daventry
NN11 7HB
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
COTTIS LANE CAR PARK 
199 Cottis Lane
Epping
CM16 4BL
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
HOLIDAY INN GATWICK-WORTH HOTEL 
Crabbet Park
Turners Hill Rd
Worth
RH10 4SS
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
TESCO EXTRA-NEWCASTLE UPON TYNE (75KW) 
Brunton Lane
Kingston Park
Newcastle Upon Tyne
NE3 2FP
United Kingdom
View
Public - Membership Required
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BENSON HILL ROAD 
Flats 1-7
1 Benson Hill Road
Pease Pottage
RH11 9SF
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
DODDINGTON COMMUNITY HOSPITAL 
Benwick Road
Doddington
PE15 0UG
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
THE ACADEMY 
The Liverpool Way
Kirkby
L33 7ED
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
EALING BROADWAY 
The Broadway
London
W5 5JY
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
THE WATERLOO HOTEL 
Holyhead Road
Betws-Y-Coed
LL24 0AR
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
RYECROFT 
Ryecroft Mill
Smith Street
Ashton-under-Lyne
OL7 0DB
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
WATERSIDE HOLIDAY PARK & SPA-BOWLEAZE COVEWAY 
Bowleaze Coveway
Weymouth
Dorset
DT3 6PP
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
THE APHRODITES GROUP-WINDERMERE TRANQUIL RETREAT 
Windermere Tranquil Retreat
Crook Road
Windermere
LA23 3NE
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
HURST GRID SUBSTATION SITE 
Haul Road
Bexley
DA5 3ND
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
UNIVERSITY OF ESSEX-ESSEX BUSINESS SCHOOL (FOR STUDENTS & EMPLOYEES USE ONLY) 
Wivenhoe Park
Colchester
CO4 3SQ
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
NORCO GROUP LTD 
Pitmedden Road
Dyce
Aberdeen
AB21 0DT
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
SAINSBURY'S APSLEY MILLS 
London Road
Apsley
England
HP3 9SP
United Kingdom
View
Public
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
HU-ROADCHEF STRENSHAM SOUTHBOUND 
Junction 8 M5
Worcester
WR8 0BZ
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
BAKEWELL BRIDGE CAR PARK COOMBS ROAD-DE45 1AQ 
Coombs Road
Bakewell
DE45 1AQ
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
EUROSPAR MOY 
Charlemont Street
Dungannon
BT71 7TG
United Kingdom
View
Public - Membership Required
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
EUROSPAR 
36 Rathfriland Road
Dromara
BT25 2JG
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CCS (Type 2)
ALLISON COURT 
Allison Court
Marconi Way
Durham
NE11 9YS
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 CHAdeMO
DOGS TRUST NEWBURY 
Plumb Farm
Hamstead Marshall
Newbury
RG20 0HR
United Kingdom
View
Public - Membership Required
Operational
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
FRASERBURGH 
22 Seaforth Street
Fraserburgh
AB43 9BB
United Kingdom
View
Public
Unknown
 Level 3: High (Over 40kW)
 CHAdeMO
EG GROUP MONTROSE 
122 N Esk Rd
Montrose
DD10 9AY
United Kingdom
View
Public - Pay At Location
Operational
 Level 3: High (Over 40kW)
 Type 2 (Tethered Connector)
TESCO SUPERSTORE - DUNDEE MONIFIETH 
High Street
Dundee
DD5 4TP
United Kingdom
View
Public
Unknown
 Level 2 : Medium (Over 2kW)
 Type 2 (Socket Only)
"""

# Define regular expressions
address_pattern = re.compile(r"(.*?)\n(.*?)\n(.*?)\n(.*?)\n.*?Level (\d+).*?(\w+ \(\w+ \d+kW\)).*?(\w+ \(Type \d\))", re.DOTALL | re.MULTILINE)

# Find matches
matches = re.findall(address_pattern, text)

# List to store charging stations
charging_stations_list = []

# Process matches and append to the list
for match in matches:
    title = match[0].strip().title()  # Convert to title case
    address = f"{match[1]}, {match[2]}, {match[3]}"
    
    # Search for postcode within the specific match
    postcode_match = re.search(r"\b([A-Z0-9]+ \d[A-Z0-9]*)\b", match[4])
    postcode = postcode_match.group() if postcode_match else None
    
    level = match[5]
    connection_type = match[6]
    
    # Create a dictionary for each charging station
    charging_station_dict = {
        "Title": title,
        "Address": address,
        "Postcode": postcode,
        "Level": level,
        "Connection Type": connection_type
    }
    
    # Append the dictionary to the list
    charging_stations_list.append(charging_station_dict)

# Display the list
for station in charging_stations_list:
    print(station)
    print("\n")