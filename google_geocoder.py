# created by J. Clary, City of Austin Code Department, October 2014

import geocoder
import time

geocoded_data = open('geohappy.tab', 'w')
data = []

print "Initiating geocoding...."
                 
with open('addresses.txt') as inputfile: 
        for line in inputfile:
                line = line.replace("\n","")
                data.append(line)

total = len(data)
count = 0
fail = 0

# clean out the junk
scrubbers = [" EB", " SB", " NB", " WB", "SVRD", " AKA ", " aka ", "Blk", "Block of ", "\"", "UNK "]

# write header
geocoded_data.write("originalAddress" + "\t" + "foundAddress" + "\t" + "Lat" + "\t" + "Lon" + "\t" + "county" + "\t" + "accuracy" + "\n")

for entry in data:
        cleanEntry = entry
        for scrubber in scrubbers:
                 cleanEntry = cleanEntry.replace(scrubber, " ")
        lookup = cleanEntry + ", Austin, TX"
        try:
                time.sleep(.3) #  delay for .3 seconds between lookup requests...the api limit is 5 requests per second, 2500 per 24 hours
                address = geocoder.google(lookup)
                geocoded_data.write(entry + "\t")
                geocoded_data.write(address.address)
                geocoded_data.write("\t")
                geocoded_data.write(str(address.lat))
                geocoded_data.write("\t")
                geocoded_data.write(str(address.lng))
                geocoded_data.write("\t")
                geocoded_data.write(address.county)
                geocoded_data.write("\t")
                geocoded_data.write(address.accuracy)
                geocoded_data.write("\n")
                count = count + 1
        except:
                geocoded_data.write("FAILED" + "\n")
                print entry + " failed"
                fail = fail + 1  
        print str(count + fail) + " of " + str(total) + " addresses geocoded. " + str(fail) + " failed."
        
print str(count) + " successful, " + str(fail) + " failed"

geocoded_data.close()
inputfile.close()
