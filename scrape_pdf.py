# Simple Script To Scrape PDF Files from a Given Web Page

# modules we're using (you'll need to download lxml)
import lxml.html, urllib2, urlparse, urllib

# the url of the page you want to scrape
base_url = 'https://aws.amazon.com/whitepapers/'

# fetch the page
res = urllib2.urlopen(base_url)

# parse the response into an xml tree
tree = lxml.html.fromstring(res.read())

# construct a namespace dictionary to pass to the xpath() call
# this lets us use regular expressions in the xpath
ns = {'re': 'http://exslt.org/regular-expressions'}

# iterate over all <a> tags whose href ends in ".pdf" (case-insensitive)
for node in tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns):

    # print the href, joining it to the base_url
    print urlparse.urljoin(base_url, node.attrib['href'])
    k = urlparse.urljoin(base_url, node.attrib['href'])
    data = k.split("/")
    l = len(data)-1
    c = "/Users/kiran/Desktop/Git/aws/"+data[l]
    print k
    print c
    urllib.urlretrieve(k,c)