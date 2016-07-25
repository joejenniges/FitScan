import os
import bz2
import csv
import sys
from urllib2 import urlopen, HTTPError, URLError


def getItemSlots():
    base_url   = "https://www.fuzzwork.co.uk/dump/latest/"

    dbDir                   = os.path.join("..", "..", "resources", "db")

    dgmTypeEffects_archive   = os.path.join(dbDir, "dgmTypeEffects.csv.bz2")
    dgmTypeEffects           = os.path.join(dbDir, "dgmTypeEffects.csv")

    invTypes_archive         = os.path.join(dbDir, "invTypes.csv.bz2")
    invTypes                 = os.path.join(dbDir, "invTypes.csv")

    slotMap   = os.path.join(dbDir, "slotMap.csv")

    EFFECT_HIGHSLOT = 12
    EFFECT_MIDSLOT  = 13
    EFFECT_LOWSLOT  = 11
    EFFECT_SUBSYS   = 3772
    EFFECT_RIGSLOT  = 2663

    dogmaEffects = {}
    nameSlots = {}

    download(base_url + "dgmTypeEffects.csv.bz2", dgmTypeEffects_archive)
    download(base_url + "invTypes.csv.bz2", invTypes_archive)

    decompress(dgmTypeEffects_archive, dgmTypeEffects)
    decompress(invTypes_archive, invTypes)

    with open(dgmTypeEffects, 'rb') as file:
        print 'Reading Dogma Effects'
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for row in reader:
            typeID = row[0]
            effectID = row[1]

            if typeID in dogmaEffects.keys():
                dogmaEffects[typeID].append(effectID)
            else:
                dogmaEffects[typeID] = [effectID]
        file.close()

    with open(invTypes, 'rb') as file:
        print 'Reading Item Names'
        reader = csv.reader(file, delimiter=',', quotechar='"')
        i = 1
        for row in reader:
            s = "Reading " + str(i)
            sys.stdout.write('{0}\r'.format(s))
            sys.stdout.flush()
            i=i + 1

            typeID = row[0]
            typeName = row[2]

            if hasEffect(dogmaEffects, typeID, EFFECT_HIGHSLOT):
                nameSlots[typeName] = "H"
            if hasEffect(dogmaEffects, typeID, EFFECT_MIDSLOT):
                nameSlots[typeName] = "M"
            if hasEffect(dogmaEffects, typeID, EFFECT_LOWSLOT):
                nameSlots[typeName] = "L"
            if hasEffect(dogmaEffects, typeID, EFFECT_RIGSLOT):
                nameSlots[typeName] = "R"
            if hasEffect(dogmaEffects, typeID, EFFECT_SUBSYS):
                nameSlots[typeName] = "S"
        file.close()

    with open(slotMap, 'wb') as file:
        print 'Mapping Names to Slots'
        count = str(len(nameSlots.keys()))
        i = 1

        file.write("{},{}\n".format("typeName", "slot"))
        for typeName, slot in nameSlots.iteritems():
            s = "Reading " + str(i) + " of " + count
            sys.stdout.write('{0}\r'.format(s))
            sys.stdout.flush()
            i = i+1

            file.write("{},{}\n".format(typeName, slot))
        file.close()

def getShips():
    SHIP_CATEGORY = 6
    STRATEGIC_C   = 963

    validAttributes = {"14": "H", "13": "M", "12": "L", "1137": "R", "1367": "S", "1374": "SH", "1375": "SM", "1376": "SL"}
    ignoredShips    = ["670", "3628", "33328"]

    base_url = "https://www.fuzzwork.co.uk/dump/latest/"

    dbDir = os.path.join("..", "..", "resources", "db")

    invGroups_archive = os.path.join(dbDir, "invGroups.csv.bz2")
    invGroups         = os.path.join(dbDir, "invGroups.csv")

    invTypes          = os.path.join(dbDir, "invTypes.csv")

    dgmTypeAttributes_archive = os.path.join(dbDir, "dgmTypeAttributes.csv.bz2")
    dgmTypeAttributes         = os.path.join(dbDir, "dgmTypeAttributes.csv")

    shipMap = os.path.join(dbDir, "shipMap.csv")

    download(base_url + "invGroups.csv.bz2", invGroups_archive)
    download(base_url + "dgmTypeAttributes.csv.bz2", dgmTypeAttributes_archive)

    decompress(invGroups_archive, invGroups)
    decompress(dgmTypeAttributes_archive, dgmTypeAttributes)

    shipGroups = []
    ships      = {}
    typeAttr   = {}

    # Get all ship types based on ship category
    with open(invGroups, 'rb') as invGroups_file:
        for row in readCsv(invGroups_file):
            groupID = row[0]
            categoryID = row[1]

            if categoryID == str(SHIP_CATEGORY):
                shipGroups.append(groupID)
        invGroups_file.close()


    # Map attributes from dogma
    with open(dgmTypeAttributes, 'rb') as dgmTypeAttributes_file:
        for row in readCsv(dgmTypeAttributes_file):
            typeID = row[0]
            attributeID = row[1]
            valueInt = row[2]
            valueFloat = row[3]

            # We only care about fitting slots
            if attributeID in validAttributes.keys():

                if typeID not in typeAttr.keys():
                    typeAttr[typeID] = {}

                if valueInt != "None":
                    typeAttr[typeID][attributeID] = valueInt
                elif valueFloat != "None":
                    typeAttr[typeID][attributeID] = str(int(round(float(valueFloat))))
                else:
                    typeAttr[typeID][attributeID] = "0"

        dgmTypeAttributes_file.close()



    # Get all ships from invTypes, map into ships
    with open(invTypes, 'rb') as invTypes_file:
        for row in readCsv(invTypes_file):
            typeID = row[0]
            groupID = row[1]
            typeName = row[2]

            # Ignore stupid shit
            if typeID in ignoredShips:
                continue

            # It's a ship if its group matches
            if groupID in shipGroups:
                # Make a dict
                ships[typeName] = {}

                for key in validAttributes.keys():
                    if key in typeAttr[typeID].keys():
                        ships[typeName][validAttributes[key]] = typeAttr[typeID][key]
        invTypes_file.close()

    with open(shipMap, 'wb') as file:
        print 'Mapping Ships and Slots'
        count = str(len(ships.keys()))
        i = 1

        file.write("shipName,High,Mid,Low,Rig,Subsystems")
        for shipName, slots in ships.iteritems():
            s = "Reading " + str(i) + " of " + count
            sys.stdout.write('{0}\r'.format(s))
            sys.stdout.flush()
            i = i+1

            file.write("{},{},{},{},{},{}\n".format(
                shipName,
                psv(slots, "H"),
                psv(slots, "M"),
                psv(slots, "L"),
                psv(slots, "R"),
                psv(slots, "S")
            ))
        file.close()



def getSubsystems():
    SUBSYSTEM_CATEGORY = 32
    validAttributes = {"1374": "H", "1375": "M", "1376": "L"}

    dbDir = os.path.join("..", "..", "resources", "db")
    invGroups = os.path.join(dbDir, "invGroups.csv")
    invTypes = os.path.join(dbDir, "invTypes.csv")
    dgmTypeAttributes = os.path.join(dbDir, "dgmTypeAttributes.csv")
    subsystemsMap = os.path.join(dbDir, "subsystemMap.csv")

    subGroups = []
    typeAttr = {}
    subsystems = {}

    # Get all subsystem types, should be 5
    with open(invGroups, 'rb') as invGroups_file:
        for row in readCsv(invGroups_file):
            groupID = row[0]
            categoryID = row[1]

            if categoryID == str(SUBSYSTEM_CATEGORY):
                subGroups.append(groupID)
        invGroups_file.close()

    # Map attributes from dogma
    with open(dgmTypeAttributes, 'rb') as dgmTypeAttributes_file:
        for row in readCsv(dgmTypeAttributes_file):
            typeID = row[0]
            attributeID = row[1]
            valueInt = row[2]
            valueFloat = row[3]

            # We only care about fitting slots
            if attributeID in validAttributes.keys():

                if typeID not in typeAttr.keys():
                    typeAttr[typeID] = {}

                if valueInt != "None":
                    typeAttr[typeID][attributeID] = valueInt
                elif valueFloat != "None":
                    typeAttr[typeID][attributeID] = str(int(round(float(valueFloat))))
                else:
                    typeAttr[typeID][attributeID] = "0"

        dgmTypeAttributes_file.close()

    # Get all ships from invTypes, map into ships
    with open(invTypes, 'rb') as invTypes_file:
        for row in readCsv(invTypes_file):
            typeID = row[0]
            groupID = row[1]
            typeName = row[2]

            # It's a ship if its group matches
            if groupID in subGroups:
                # Make a dict
                subsystems[typeName] = {}

                for key in validAttributes.keys():
                    if key in typeAttr[typeID].keys():
                        subsystems[typeName][validAttributes[key]] = typeAttr[typeID][key]
        invTypes_file.close()
    print subsystems

    with open(subsystemsMap, 'wb') as file:
        print 'Mapping Subsystems and Slots'
        count = str(len(subsystems.keys()))
        i = 1

        file.write("subName,High,Mid,Low")
        for shipName, slots in subsystems.iteritems():
            s = "Reading " + str(i) + " of " + count
            sys.stdout.write('{0}\r'.format(s))
            sys.stdout.flush()
            i = i + 1

            file.write("{},{},{},{}\n".format(
                shipName,
                psv(slots, "H"),
                psv(slots, "M"),
                psv(slots, "L")
            ))
        file.close()

# I should be using integers
def psv(slots, slot):
    if slot in slots.keys():
        return slots[slot]
    return "0"

def readCsv(file):
    return csv.reader(file, delimiter=',', quotechar='"')

def hasEffect(dogma_effects, type_id, slot_type):
    return type_id in dogma_effects.keys() and str(slot_type) in dogma_effects[type_id]

def download(url, file):
    if os.path.isfile(file):
        os.remove(file)
    try:
        f = urlopen(url)

        print "Downloading " + url + " to " + file

        with open(file, "wb") as file:
            file.write(f.read())

    except HTTPError, e:
        print "HTTP Error: ", e.code, url
        exit()
    except URLError, e:
        print "URL Error: ", e.reason, url
        exit()

def decompress(zip, file):
    if os.path.isfile(file):
        os.remove(file)
    print "Decompressing " + zip + " to " + file
    with open(file, 'wb') as out_file, bz2.BZ2File(zip, 'rb') as in_file:
        for data in iter(lambda : in_file.read(100*1024), b''):
            out_file.write(data)

def main():
    getItemSlots()
    getShips()
    getSubsystems()

if __name__ == "__main__":
    main()