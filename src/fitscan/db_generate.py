import os
import bz2
import csv
import sys
from urllib2 import urlopen, HTTPError, URLError


def main():
    base_url   = "https://www.fuzzwork.co.uk/dump/latest/"

    db_dir     = os.path.join("..", "..", "resources", "db")
    dgm_file   = os.path.join(db_dir, "typeEffects.csv.bz2")
    types_file = os.path.join(db_dir, "invTypes.csv.bz2")
    dgm_db     = os.path.join(db_dir, "typeEffects.csv")
    types_db   = os.path.join(db_dir, "invTypes.csv")

    slot_map   = os.path.join(db_dir, "slotMap.csv")

    EFFECT_HIGHSLOT = 12
    EFFECT_MIDSLOT  = 13
    EFFECT_LOWSLOT  = 11
    EFFECT_SUBSYS   = 3772
    EFFECT_RIGSLOT  = 2663

    dogma_effects = {}
    types   = {}
    nameSlots = {}

    # download(base_url + "dgmTypeEffects.csv.bz2", dgm_file)
    # download(base_url + "invTypes.csv.bz2", types_file)
    #
    # decompress(dgm_file, dgm_db)
    # decompress(types_file, types_db)

    with open(dgm_db, 'rb') as file:
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

    with open(types_db, 'rb') as file:
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


if __name__ == "__main__":
    main()