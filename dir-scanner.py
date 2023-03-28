import requests , sys , threading , argparse
from threading import *

def parse_arguments():
    parser = argparse.ArgumentParser(description='A simple directory scanner')
    parser.add_argument('url', help='The target URL to scan')
    parser.add_argument('wordlist', help='The wordlist to use')
    parser.add_argument('-n', type=int, default=2, help='Number of threads to use (default: 2)')
    parser.add_argument('-l', action='store_true', help='Show less, only good results')
    parser.add_argument('-s', action='store_true', help='Stop when a file is found')
    return parser.parse_args()

args = parse_arguments()
url = args.url
wordlist = open(args.wordlist, 'r', encoding='ISO-8859-1').readlines()
n = args.n
less = args.l
stop = args.s

def check(url):     #URL Checking method check url and return status code
    try:            
        r = requests.head(url,verify=False,timeout=5) # it is faster to only request the header
        return (r.status_code)
    except:
        return 'Not Rachable'


stop_event = threading.Event()  #if stop option used we use this evet to stop all threads
found = []

def run(url,wordlist,stop_event): 
    th = str(threading.current_thread().ident)  # get thread number (I wanted to print thread id)
    for word in wordlist:
        if stop_event.is_set():     # check if stop_event is set
            return
        target = url.strip() + '/' + word.strip()   #prepare my target, URL/WORD
        result = check(target)                      #get result
        if result==404:
            if not less:                            #if result 404 print only if -l option is not used
                print("[" + th + "] " + target + ' -> ' + str(result))
        else:                                       #if not 404 print anyway
            print("[" + th + "] " + target + ' -> ' + str(result))
            found.append(target + ' -> ' + str(result))
            if stop:                                #if -s option used stop after first find
                stop_event.set()                    #send stop event

chunk_size = len(wordlist) // n     # split wordlist to number of threads
wordlist_chunks = [wordlist[i:i+chunk_size] for i in range(0, len(wordlist), chunk_size)]

threads = []
for i in range(n):                  # start n number of threads
    t = threading.Thread(target=run, args=(url, wordlist_chunks[i],stop_event))
    threads.append(t)
    t.start()

for t in threads:
    t.join()                        # wait all threads to finish
print("DONE")
for ok in found:
    print(ok)

    
    
