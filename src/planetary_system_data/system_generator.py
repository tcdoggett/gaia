#%%

print ("This is Python script to procedurally generate realistic (but fictional) star systems")
print ("using the procedures laid out in 'Arcitect of Worlds: Comprehensive Worldbuidling' by Jon F. Zeigler")
print ("published in 2024 by Ad Astra Games")
print ("")
print ("How do you wish to generate star systems today?")
print ("Option 1 - generate fictional planetary systems around real stars (make sure file system_parameters.csv is present in this directory)")
print ("Option 2 - generate fictional planetary systems around fictional stars")
validoption = {"1", "2"}
useroption = input ("Type Option Number: ")

while useroption not in validoption:
    useroption = input ("Type Option Number: ")

if useroption == 1:
    print ("okay, looking for system.parameters.csv")
    input ("Press any key to continue")

    # note - current version of system.parameters.csv contains all stars with proper names and/or Bayer Designations plus some other nearby stars
    # future use case - system.parameters.csv can be replaced with other sets of real stars of interest (e.g. every star in a sector produced by Sector_Query.py)
    # future use case - system.parameters.csv can be replaced with fictional sets of stars (e.g. every star in the New Eden Cluster in EVE Online)

    # insert code which checks for presence of system.parameters.csv and proceeds from there

if useroption == 2:
    print ("and how many star systems do you want to create today?")
    star_sys_number = input ("Enter Number of Stars: ")
    print (f"okay, generating {star_sys_number} systems today")
    input ("Press any key to continue")

    # insert code which follows procedures in Zeigler to generate stellar mass, multiplicity, age, metallicity, etc.

#%%

# will also need to develop known_exoplanet.py module to handle cases where exoplanets have been detected / real exoplanet 
# data can be ingested (pg. 176-178)
# e.g. in these cases there will be both IRL known exoplanets in the system + fair to assume that there are other undetected 
# exoplanets for which fictional but realistic stand-ins can be created here

# Step 0: Load Known System Parameters
# refer to system_parameters.csv which contains known properties of real stars (e.g. mass, age, spectral type)
# following steps will only run if parameter field is blank
# user story: need to track if a parameter is inputed / real or generated procedurally

# Step 1: Primary Star Mass

# from primary_star_mass import generate_primary_star
# Star_A = generate_primary_star()
# Mass_A = Star_A.mass
# print(f"Mass of Star A: {Star_A.mass} solar masses")

# Step 2: Stellar Multiplicity

# from stellar_multiplicity import generate_number_of_stars
# Number_of_Stars = generate_number_of_stars(Star_A.mass)
# print(f"Number of Stars in System: {Number_of_Stars}")

# Step 3: Arrange Components

# from arrange_components import Stellar_Arrangement
# print(f"Stellar Arranagement: {Stellar_Arrangement}")

# Step 4: Star System Age

# from star_system_age import Population
# from star_system_age import system_age

# print(f"Stellar Population: {Population}")
# system_age = round(system_age, 2)
# print(f"System Age: {system_age} Gyr")

# Step 5: Star System Metallicity

# from star_system_metallicity import Metallicity

# Metallicity = round(Metallicity, 2)
# print(f"Metallicity: {Metallicity}")

# Step 6: Stellar Evolution
# run stellar_evolution.py

# Step 7: Stellar Classification
# run stellar_classification.py

# Step 8: Stellar Orbital Parameters
# run stellar_orbital_parameters.py

# Step 9: Protoplanetary Disk
# run protoplanetary_disk.py here

# Step 10: Disk Instability
# run disk_instability.py here

# Step 11: Core Accretion
# run core_accretion.py here

# Step 12: Oligarchic Collision
# run oligarchic_collison.py here

# run planet_generator.py for each planet created by the steps above

# output results to test_output.txt (inputing into output_template.txt)