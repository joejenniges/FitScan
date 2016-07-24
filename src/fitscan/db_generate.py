import os
import bz2
import csv
import sys
from urllib2 import urlopen, HTTPError, URLError


def getItemSlots():
    base_url   = "https://www.fuzzwork.co.uk/dump/latest/"

    db_dir                   = os.path.join("..", "..", "resources", "db")

    dgmTypeEffects_archive   = os.path.join(db_dir, "dgmTypeEffects.csv.bz2")
    dgmTypeEffects           = os.path.join(db_dir, "dgmTypeEffects.csv")

    invTypes_archive         = os.path.join(db_dir, "invTypes.csv.bz2")
    invTypes                 = os.path.join(db_dir, "invTypes.csv")

    slot_map   = os.path.join(db_dir, "slotMap.csv")

    EFFECT_HIGHSLOT = 12
    EFFECT_MIDSLOT  = 13
    EFFECT_LOWSLOT  = 11
    EFFECT_SUBSYS   = 3772
    EFFECT_RIGSLOT  = 2663

    dogma_effects = {}
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

            if typeID in dogma_effects.keys():
                dogma_effects[typeID].append(effectID)
            else:
                dogma_effects[typeID] = [effectID]
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

            if hasEffect(dogma_effects, typeID, EFFECT_HIGHSLOT):
                nameSlots[typeName] = "H"
            if hasEffect(dogma_effects, typeID, EFFECT_MIDSLOT):
                nameSlots[typeName] = "M"
            if hasEffect(dogma_effects, typeID, EFFECT_LOWSLOT):
                nameSlots[typeName] = "L"
            if hasEffect(dogma_effects, typeID, EFFECT_RIGSLOT):
                nameSlots[typeName] = "R"
            if hasEffect(dogma_effects, typeID, EFFECT_SUBSYS):
                nameSlots[typeName] = "S"
        file.close()

    with open(slot_map, 'wb') as file:
        print 'Mapping Names to Slots'
        count = str(len(nameSlots.keys()))
        i = 1
        for typeName, slot in nameSlots.iteritems():
            s = "Reading " + str(i) + " of " + count
            sys.stdout.write('{0}\r'.format(s))
            sys.stdout.flush()
            i = i+1

            file.write("{},{}\n".format(typeName, slot))
        file.close()

def getShips():
    SHIP_CATEGORY = 6
    SLOTS_HIGH    = 14
    SLOTS_MID     = 13
    SLOTS_LOW     = 12
    SLOTS_RIG     = 1137
    SLOTS_SUB     = 1367

    SLOTS_MOD_HIGH = 1374
    SLOTS_MOD_MID  = 1375
    SLOTS_MOD_LOW  = 1376

    base_url = "https://www.fuzzwork.co.uk/dump/latest/"

    db_dir = os.path.join("..", "..", "resources", "db")

    invGroups_archive = os.path.join(db_dir, "invGroups.csv.bz2")
    invGroups         = os.path.join(db_dir, "invGroups.csv")

    invTypes_archive  = os.path.join(db_dir, "invTypes.csv.bz2")
    invTypes          = os.path.join(db_dir, "invTypes.csv")

    dgmTypeAttributes_archive = os.path.join(db_dir, "dgmTypeAttributes.csv.bz2")
    dgmTypeAttributes         = os.path.join(db_dir, "dgmTypeAttributes.csv")

    download(base_url + "invGroups.csv.bz2", invGroups_archive)
    download(base_url + "invTypes.csv.bz2", invTypes_archive)
    download(base_url + "dgmTypeAttributes", dgmTypeAttributes_archive)

    decompress(invGroups_archive, invGroups)
    decompress(invTypes_archive, invTypes)
    decompress(dgmTypeAttributes_archive, dgmTypeAttributes)

    shipGroups = []
    ships      = {}

    # Get all ship types based on ship category
    for row in readCsv(invGroups):
        groupID = row[0]
        categoryID = row[1]

        if categoryID == SHIP_CATEGORY:
            shipGroups.append(groupID)


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

if __name__ == "__main__":
    main()