import urllib.request

# This script iterates a range to download a series of MP3 files on a remote server000
# Note : the URL is now no longer valid

for x in range(1, 100):
	url = 'https://podcloud.fr/ext/les-grosses-tetes-dans-la-nuit-des-temps/publication-sans-titre-' + str(x) + '/enclosure.mp3?p=dl'  
	urllib.request.urlretrieve(url, 'C:/ps_stats/dl mp3/dl/grosses_tetes_dans_la_nuit_des_temps_' + str(x) +'.mp3')  
	print(str(x))