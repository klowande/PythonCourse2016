# pip install googlemaps
#https://console.developers.google.com/apis/credentials?project=_
#need maps and distance APIs enabled


# copy/paste or import gmap-auth.py here


dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
location=gmaps.geocode(whitehouse)

print location
print location[0]
print location[0]['geometry']['location']
latlng=location[0]['geometry']['location']
lat, lng=latlng.values()

destination = gmaps.reverse_geocode(latlng)
print destination 

duke = gmaps.geocode('326 Perkins Library, Durham, NC 27708')
duke=duke[0]['geometry']['location']
distance = gmaps.distance_matrix(duke, latlng)
distance['rows'][0]['elements'][0]['distance']['text']
distance['rows'][0]['elements'][0]['distance']['value']


embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
# what is its address? You will get errors - debug
# if I wanted to hold a morning meeting there, which cafe would you suggest?
# if I wanted to hold an evening meeting there, which bar would you suggest? 

wh = location[0]['geometry']['location']

def check_distance_to_wh(embassy):
	distance = gmaps.distance_matrix(wh,embassy)
	return distance['rows'][0]['elements'][0]['distance']['value']

for i in :
	latlng={'lat':embassies[i][0],'lng':embassies[i][1]}
	print check_distance_to_wh(latlng)




