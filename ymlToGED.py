# ---- SET UP ----
from datetime import datetime
import yaml
import os

# Date format conversion
def convert_date(date_string):
    if not date_string:
        return ""
    date_string = date_string.strip()
    date_length = len(date_string)

    # Full date (YYYY-MM-DD to DD MMM YYYY)
    if date_length == 10:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        gedcom_date = date_obj.strftime("%d %b %Y").upper()
        return gedcom_date

    # Partial date (YYYY-MM to MMM YYYY)
    elif date_length == 7:
        date_obj = datetime.strptime(date_string, "%Y-%m")
        gedcom_date = date_obj.strftime("%b %Y").upper()
        return gedcom_date

    # Partial date (YYYY)
    else:
        return date_string

usersName = input("Enter your name: ")
yamlFile = input("Enter the name of your YAML file\n(including path if not in current directory): ")
gedcomFile = os.path.splitext(yamlFile)[0] + ".gedcom"
with open(yamlFile, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
with open(gedcomFile, "w", encoding="utf-8") as file:

    file.write("0 HEAD\n")
    file.write("1 GEDC\n")
    file.write("2 VERS 5.5.1\n")
    file.write("2 FORM LINEAGE-LINKED\n")
    file.write("1 CHAR UTF-8\n")
    file.write("1 SUBM @S1@\n")
    file.write("0 @S1@ SUBM\n")
    file.write("1 NAME " + usersName + "\n")

# ---- INDIVIDUALS ----
    for i in data.get("individuals", []):

        #  ID
        id = i.get("id")
        file.write("0 @" + id + "@ INDI\n")

        #  NAME
        titl = i.get("title", "")
        npfx = i.get("prefix", "")
        givn = i.get("givenName", "")
        surn = i.get("surname", "")
        nsfx = i.get("suffix", "")
        nick = i.get("nickname", "")

        if not isinstance(givn, list):
            givn = [givn]
        if not isinstance(surn, list):

        fullName = givn[0] + " /" + surn[0] + "/"

        if npfx:
            if isinstance(npfx, list):
                fullName = npfx[0] + " " + fullName
            else: fullName = npfx + " " + fullName
        if nsfx:
            if isinstance(nsfx, list):
                fullName = fullName + " " + nsfx[0]
            else: fullName = fullName + " " + nsfx

        file.write("1 NAME " + fullName + "\n")

            #  TITLE
        if titl:
            if isinstance(titl, list):
                for t in titl:
                    file.write("2 TITL " + t + "\n")
            else: file.write("2 TITL " + titl + "\n")

            #  PREFIX
        if npfx:
            if isinstance(npfx, list):
                for n in npfx:
                    file.write("2 NPFX " + n + "\n")
            else: file.write("2 NPFX " + npfx + "\n")

            #  GIVEN NAME
        if givn:
            if isinstance(givn, list):
                for g in givn:
                    file.write("2 GIVN " + g + "\n")
            else: file.write("2 GIVN " + givn + "\n")

            #  SURNAME

        if surn:
            if isinstance(surn, list):
                for s in surn:
                    file.write("2 SURN " + s + "\n")
            else: file.write("2 SURN " + surn + "\n")

            #  SUFFIX

        if nsfx:
            if isinstance(nsfx, list):
                for n in nsfx:
                    file.write("2 NSFX " + n + "\n")
            else: file.write("2 NSFX " + nsfx + "\n")

            #  NICK NAME

        if nick:
            if isinstance(nick, list):
                for n in nick:
                    file.write("2 NICK " + n + "\n")
            else: file.write("2 NICK " + nick + "\n")

            #  ALTERNATE NAMES
        for g in givn[1:]:
            file.write("1 NAME " + g + " /" + surn[0] + "/\n")
        for s in surn[1:]:
            file.write("1 NAME " + givn[0] + " /" + s + "/\n")

        #  SEX
        sex = i.get("sex")
        if sex:
            file.write("1 SEX " + sex + "\n")

        #  BIRTH
        birth = i.get("birth", {})
        bdate = convert_date(birth.get("bdate"))
        bdateEst = birth.get("bdateEst")
        bplace = birth.get("bplace")

        if bdate or bplace:
            file.write("1 BIRT\n")
            if bdate:
                file.write("2 DATE ")
                if bdateEst:
                    file.write("EST ")
                file.write(bdate + "\n")
            if bplace:
                file.write("2 PLAC " + bplace + "\n")

        #  DEATH
        death = i.get("death", {})
        ddate = convert_date(death.get("ddate"))
        ddateEst = death.get("ddateEst")
        dplace = death.get("dplace")

        if ddate or dplace:
            file.write("1 DEAT\n")
            if ddate:
                file.write("2 DATE ")
                if ddateEst:
                    file.write("EST ")
                file.write(ddate + "\n")
            if dplace:
                file.write("2 PLAC " + dplace + "\n")

        #  RESIDENCY
        residence = i.get("residence", [])

        if residence:
            if isinstance(residence, list):
                for r in residence:
                    rdate = convert_date(r.get("rdate"))
                    rplace = r.get("rplace")
                    file.write("1 EVEN\n")
                    file.write("2 TYPE Residence\n")
                    if rdate:
                        file.write("2 DATE ")
                        if r.get("rdateEst"):
                            file.write("EST ")
                        file.write(rdate + "\n")
                    if rplace:
                        file.write("2 PLAC " + rplace + "\n")
            else:
                rdate = convert_date(residence.get("rdate"))
                rplace = residence.get("rplace")
                file.write("1 EVEN\n")
                file.write("2 TYPE Residence\n")
                if rdate:
                    file.write("2 DATE ")
                    if residence.get("rdateEst"):
                        file.write("EST ")
                    file.write(rdate + "\n")
                if rplace:
                    file.write("2 PLAC " + rplace + "\n")

# ---- FAMILIES ----
    for f in data.get("families", []):

        #  FAMID
        famID = f.get("id")
        file.write("0 @" + famID + "@ FAM\n")

        #  SPOUSE ID'S
        husband = f.get("husband")
        wife = f.get("wife")
        if husband:
            file.write("1 HUSB @" + husband + "@\n")
        if wife:
            file.write("1 WIFE @" + wife + "@\n")

        #  MARRIAGE
        marriage = f.get("marriage", [])

        if marriage:
            for m in marriage:
                mdate = convert_date(m.get("mdate"))
                mplace = m.get("mplace")

                if mdate or mplace:
                    file.write("1 MARR\n")
                    if mdate:
                        file.write("2 DATE ")
                        if m.get("mdateEst"):
                            file.write("EST ")
                        file.write(mdate + "\n")
                    if mplace:
                        file.write("2 PLAC " + mplace + "\n")

        #  CHILDREN
        children = f.get("children", [])
        if children:
            if isinstance(children, list):
                for c in children:
                    file.write("1 CHIL @" + c + "@\n")
            else:
                file.write("1 CHIL @" + children + "@\n")

# ---- DONE ----
    file.write("0 TRLR\n")
print("Created ", gedcomFile)
