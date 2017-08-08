import requests
import time
import threading

url = 'http://github.com/'
letters = 'kirandm0123456789-'
candidates = []


def test_url(l, m,  o):
    r = requests.get( '{0}{1}{2}{3}'.format(url, l, m,  o))
    if r.status_code == 404:
        print "{0}:{1}".format(l+m+o, r.status_code)
        candidates.append(l+m+o)

start = time.time()
block_start = start

for l in letters:
    for m in letters:
        threads = [threading.Thread(target=test_url, args=(l, m,  o)) for o in letters]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    print l+m+"__ block completed in", time.time()-block_start, "seconds"
    block_start = time.time()

with open("output.txt", 'w') as f:
    for candidate in candidates:
        f.write(candidate + '\n')
print "search completed in", time.time()-start, "seconds"
