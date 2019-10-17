import json
import urllib

nationality=[]
path='sources/'
f_n=open(path+'nationalities.txt','r')
for line in f_n:
    nationality.append(line.strip().lower())
f_n.close()

country=[]
f_c=open(path+'countries.txt','r')
for line in f_c:
    country.append(line.strip().lower())
f_c.close()

stopwords=[]
f_s=open(path+'stopwords.txt','r')
for line in f_s:
    stopwords.append(line.strip().lower())
f_s.close()

def google(str):
    api_key = 'AIzaSyApzyzMD2JgBPQxpT0n7m2aHIwMX_iasCw'
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
    'query': str,
    'limit': 1,
    'indent': True,
    'key': api_key,}
    url = service_url + '?' + urllib.parse.urlencode(params)
    try:
        type = json.loads(urllib.request.urlopen(url).read())['itemListElement'][0]['result']['@type']
    except Exception as e: 
        return False
    if 'Corporation' in type:
        return True
    else:
        return False

def iskeyword(str):
    if str.lower() in stopwords:
        return False
    elif str.lower() in country or str.lower() in nationality:
        return True
    elif 'A'<=str[0] and str[0]<='Z':
        return(google(str))
    else:
        return False

iskeyword('Bloomberg')
iskeyword('Chinese')
iskeyword('We')
iskeyword('Moreover')
