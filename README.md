# YAML to GEDCOM Converter

**A Python tool for converting genealogy data from YAML format to GEDCOM 5.5.1 format.**

**Work in Progress:** This is a personal genealogy project that currently supports basic individual and family records, with more being added. Any suggestions are welcome.

## Features

### Currently supported
- Individual and family records
- Partial and estimated dates
- Birth, death, and residence events
- Multiple names, titles, prefixes, suffixes, nicknames

### Planned features
- Source citations
- Additional event and date types
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
individuals:                    # REQUIRED: List of individual records
  - id: I1                      # REQUIRED: Unique identifier
    title: Esquire              # optional: Can be string or list
    prefix: Sir                 # optional: Can be string or list
    givenName: John             # optional: Can be string or list
    surname: [Smith, Smyth]     # optional: Can be string or list
    suffix: Jr.                 # optional: Can be string or list
    nickname: Johnny            # optional: Can be string or list
    sex: M                      # optional: M, F, or U (Unknown)
    birth:                      # optional: Birth information
      bdate: 1430-09-14         # optional: YYYY-MM-DD, YYYY-MM, or YYYY
      bdateEst: true            # optional: Mark date as estimated
      bplace: London, England   # optional: Birth place
    death:                      # optional: Death information
      ddate: 1510-11            # optional: YYYY-MM-DD, YYYY-MM, or YYYY
      ddateEst: false           # optional: Mark date as estimated
      dplace: England           # optional: Death place
    residence:                  # optional: List of residences
      - rdate: 1480             # optional: YYYY-MM-DD, YYYY-MM, or YYYY
        rdateEst: true          # optional: Mark date as estimated
        rplace: Bristol         # optional: Can be list or single residence
```
### Family Records
```yaml
families:                       # REQUIRED: List of family records
  - id: F1                      # REQUIRED: Unique family identifier
    husband: I1                 # optional: Reference to individual ID
    wife: I2                    # optional: Reference to individual ID
    marriage:                   # optional: List of marriage events
      - mdate: 1481-05-04       # optional: YYYY-MM-DD, YYYY-MM, or YYYY
        ddateEst: false         # optional: Mark date as estimated
        mplace: London          # optional: Marriage location
    children: [I3, I4, I5]      # optional: List of child IDs
```
