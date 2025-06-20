## Intro ##
overall purpose: parsing ESA Gaia data into 3D sector maps for sci-fi purposes

## Required libraries / extensions: ##
- AstroPy
- SciPy
- NumPy
- Matplotlib
- Pandas

## File: Sector_Query.py ##

initial functions:
- loads relevant libraries
- throws out a random inspriational quote
- loads cached file with previous merged Gaia and SIMBAD data (if present) 

if no cached file is present:
- query Gaia dataset with user-defined parallax range - gets Gaia DR3 designation, gal-lon, gal-lat, parallax, G-band magnitude, bp_rp,bp_g,g_rp,teff_gspphot,mh_gspphot 
    and logg_gspphot and ingests these into a Panda dataframe
- query SIMBAD to cross-match Gaia designations with Star Names, Spectral Classifications and Object Type, add as columns to Panda data frame
- Note: this step is a bottleneck and initially produces the following warning:

```WARNING: NoResultsWarning: The request executed correctly, but there was no data corresponding to these criteria in SIMBAD [astroquery.simbad.core]```

... but the script will continue to run and get matching data for almost all of the stars pulled from Gaia (and the issue is avoided if cached file is present)
- saves a cached file with Gaia/SIMBAD query results

if cached file was already present (or has just been generated):
- calculates distance from Sol in parsecs (from Gaia-measured parallax), adds as column to Panda dataframe
- calculates adjusted mag for stars (approx. equivalent to Absolute Magnitude) from G-band for Gaia stars, adds as column to Panda dataframe
- calculates x,y,z coordinates (with Sol as the origin, X-axis as Coreward/Rimward, Y-axis as Spinward/Trailing, Z-axis as Galactic North/South) in parsecs from Gaia-measured G-lon and G-lat, adds as column to Panda dataframe
- calculates and applies a sector reference code (e.g. C1-S1-U1 is Coreward One, Spinward One, Upward One, R4-T5-D3 is Rimward 4, Trailing 5, Downward 3)
- converts SIMBAD IDs to more human-friendly text for star labels in eventual 3D plots
- adds 140+ stars from not_in_Gaia_DR3.csv (if user wants it)
- exports panda datadframe as all_results_sorted_by_sector.csv (if user wanted non-DR3 stars added)
- exports panda datadframe as DR3_sorted_by_sector.csv (if user did not want non-DR3 stars added)
- parses into separate additional .csv files for every 10pc x 10 pc x 10 pc sector within the dataframe (if user wants it)

punch list / road map for continued development:
- continue to vet the data in not_in_Gaia_DR3.csv (e.g. missing spectral types, absolute magnitudes)
- include handling of Sol (which would appear in 8 sectors under this coordinate system)
- include better handling of when no G-Mag value is present from Gaia dataset
- include better handling of when SIMBAD has cross-match but no spectral type
- check cache file for any remaining issues converting SIMBAD IDs to star labels

## File: gaia_cached.csv ##
contains results of previous runs which cross-matched Gaia and SIMBAD data
(not mirrored on github)

## File: all_results_sorted_by_sector.csv ##
primary output file from sector_query_results.csv

- column 1 - designation from Gaia DR3 (or from DR2 or DR1 if not in DR3), empty if not in any Gaia DR
- column 2 - l - galactic longitude - in degrees (as measured by Gaia in most cases, otherwise from SIMBAD)
- column 3 - b - galactic latitude - in degrees (as measured by Gaia in most cases, otherwise from SIMBAD)
- column 4 - parallax - in milliarcseconds (mas) (as measured by Gaia in most cases, otherwise from SIMBAD)
- column 5 - phot_g_mean_mag - mean magnitude in the G-band from Gaia
- column 6 - bp_rp - BP-RP color from Gaia
- column 7 - bp_g - BP-G color from Gaia
- column 8 - g_rp - G-RP color from Gaia 
- column 9 - teff_gspphot - effective temperature from GSP-Phot (Generalized Stellar Parameterizer from Photometry) Aeneas best library using BP/RP spectra
- column 10 - mh_gspphot - iron abundance from GSP-Phot Aeneas best library using BP/RP spectra
- column 11 - logg_gspphot  - surface gravity from GSP-Phot Aeneas best library using BP/RP spectra
- column 12 - SIMBAD ID - main id in SIMBAD (if a match existed between Gaia and SIMBAD)
- column 13 - Spectral Type - spectral classification in SIMBAD (if any)
- column 14 - Obect Type - object type in SIMBAD (if any)
- column 15 - distance - in parsecs from Sol
- column 16 - adjusted_mag - value after the equivalent of the conversion from Apparent Magnitude to Absolute Magnitude has been done to the G_band magnitude from Gaia (or the Absolute Magnitude value of non-Gaia stars from the csv)
- column 17 - X - cartesian coordinates in units of parsecs where positive X is coreward from Sol and negative X is rimward
- column 18 - Y - cartesian coordinates in units of parsecs where positive Y is spinward from Sol and negative Y is trailing (in context of the direction of galactic disk rotation)
- column 19 - Z - cartesian coordinates in units of parsecs where positive Z is "galactic north" and negative Z is "galactic south
- column 20 - sector reference code (e.g. C1-S1-U1 is Coreward One, Spinward One, Upward One, R4-T5-D3 is Rimward 4, Trailing 5, Downward 3)
- column 21 - label_name - readable star names to use for labelling in 3D sector maps

## File: not_in_Gaia_DR3.csv ##

contains 141 stars formatted for ingest into panda dataframe by Gaia_Query.py

specifically: stars with Bayer and/or Flamsteed Designations but no matching entries in DR3 (based on queries made in SIMBAD and cross-checking to remove cases where binary systems had separate entries in Gaia DR3 and/or DR2)

mostly these are stars which are too bright for Gaia / saturated the detector, while some (~40) appear in DR1 and/or DR2 but not DR3

exception: currently does not include Sol (a G2V star at X=0, Y=0, Z=0 which would be split between 8 sectors in this coordinate system)

exception: includes Procyon B - dim white dwarf which was not in any Gaia dataset (presumably due to proximity to the bright star Procyon A)

includes parallax, gal-lon, gal-lat, parallax and spectral type from SIMBAD

minor exception: Beta Phoenicis - used parallax value of 17.63 mas instead of 0.12 mas (which is the value in SIMBAD)

per wikipedia: "The distance to Beta Phoenicis is poorly known. The original reduction of the Hipparcos satellite's data yielded a parallax value of 16 milliarcseconds, yet its standard error was larger than the parallax value itself. An individual note in the Hipparcos catalogue provided a more likely parallax of 17.63±2.09 mas, corresponding to a distance of 185±22 light-years, consistent with the expected distance implied by the absolute visual magnitude of a G8 giant. The new reduction of the Hipparcos data gave 0.12 ± 14.62 milliarcseconds, still unusable. The General Catalogue of Trigonometric Parallaxes, an older catalogue of ground-based parallaxes, lists the parallax as 20 ± 16 milliarcseconds, corresponding to about 200 light-years (61 pc)"

(n.b. a parallax of 0.12 mas would be equivalent to a distance of 27,180 light years, which seems unreasonable for a star bright enough to saturate Gaia's detectors)

## Separate script to be written ##

- ingests individual sector files produced by Sector_Query.py
- creates 3D plots as sector maps (Iota_Pegasi_Sector.py being a prototype)
- color of markers to be keyed to spectral type (OBAFGKM) of star
- size of markers to be keyed to the brightness of the star
- markers to be labeled by star name
- output: labeled 3D sector maps, labeled 2D sector maps, gazetteer table of stars in the sector (formated in Textile)

## File: Iota_Pegasi_Sector.py ##

current functionality:
- prototype of sector maps that will be mass-generated by this project