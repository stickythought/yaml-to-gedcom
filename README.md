# YAML to GEDCOM Converter

**A Python tool for converting genealogy data from YAML format to GEDCOM 5.5.1 format.**

**Work in Progress:** This is a personal genealogy project that currently supports basic individual and family records, with more being added. Any suggestions are welcome.

## Features

### Currently supported
- Individual records with basic biographical data
- Family records with marriage and children data
- Multiple names, titles, and suffixes per individual
- Birth, death, and residence events
- Partial and estimated dates

### Planned features
- Source citations
- Additional event types
- Family cross-references (FAMC/FAMS)
- More error handling and output validation

## Requirements

- Python 3.6+
- PyYAML
  
## Instructions

1. Install pyyaml:

   `pip install pyyaml`
   
   `pip3 install pyyaml` — for macOS/Linux running python3
  
2. Create genealogy data in YAML format (see specifications below)
3. Run the converter:

   `python ymlToGED.py`
   
   `python3 ymlToGED.py` — for macOS/Linux running python3
   
5. Enter your name when prompted (for the GEDCOM header)
6. Enter the name of your YAML file (including its path if not in same directory)
7. A GEDCOM file by the same name as your YAML file will be generated within in the same directory.

## YAML Format Specifications

### Individual Records
```yaml
individuals:                    # Required: List of individual records
  - id: I1                      # Required: Uniquire identifier
    title:                      # Optional: Can be string or list
    givenName: John             # Optional: Can be string or list
    surname: [Smith, Smyth]     # Optional: Can be string or list
    suffix: Jr.                 # Optional: Can be string or list
    sex: M                      # Optional: M, F, or U (Unknown)
    birth:                      # Optional: Birth information
      bdate: 1430-09-14         # Optional: YYYY-MM-DD, YYYY-MM, or YYYY
      bdateEst: true            # Optional: Mark date as estimated
      bplace: London, England   # Optional: Birth place
    death:                      # Optional: Death information
      ddate: 1510-11            # Optional: YYYY-MM-DD, YYYY-MM, or YYYY
      ddateEst: false           # Optional: Mark date as estimated
      dplace: England           # Optional: Death place
    residence:                  # Optional: List of residences
      - rdate: 1480             # Optional: YYYY-MM-DD, YYYY-MM, or YYYY
        rdateEst: true          # Optional: Mark date as estimated
        rplace: 1495            # Optional: Residence location
      - rdate: 1495
        rplace: Bristol
```
### Family Records
```yaml
families:                       # Required: List of family records
  - id: F1                      # Required: Uniquire family identifier
    husband: I1                 # Optional: Reference to individual ID
    wife: I2                    # Optional: Reference to individual ID
    marriage:                   # Optional: List of marriage events
      - mdate: 1481-05-04       # Optional: YYYY-MM-DD, YYYY-MM, or YYYY
        ddateEst: false         # Optional: Mark date as estimated
        mplace: London          # Optional: Marriage location
    children: [I3, I4, I5]      # Optional: List of child IDs
```
