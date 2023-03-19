import requests , sys , threading
from threading import *

def printUsage():   #When entered wrong args show usage and exit
    print("USAGE: dir-scanner.py [URL] [WORDLIST] [NUM OF THREAD] <OPTIONS>")
    print("-l	show less, only good results")
    print("-s	stop when found")
    sys.exit()


def check(url):     #URL Checking method check url and return status code
                    #https://www.pemavor.com/url-status-code-checker-with-python/
    try:            
        r = requests.head(url,verify=False,timeout=5) # it is faster to only request the header
        return (r.status_code)
    except:
        return 'Not Rachable'

# ----------------------------------------ARGUMENTS---------------------------------------

wordlist = ''
less = False    # is -l option ticked in args
stop = False    # is -s option ticked in args
n = 2           # Number of threads by default 2

if len(sys.argv) < 4:   # if less args
    printUsage()
else:
    try:
        url = sys.argv[1]
        wordlist = open(sys.argv[2], 'r', encoding='ISO-8859-1').readlines()
    except:
        print("Error in WORDLIST")
        printUsage()
    if sys.argv[3].isnumeric():
        n = int(sys.argv[3])    #Number of threads 
    else:
        printUsage()



     
        
if len(sys.argv) == 5:  # if there is 5 args mean options is used check if used -l or -s
    if sys.argv[4].lower() == '-l':
        less = True
    elif sys.argv[4].lower() == '-s':
        stop = True
    else:
        printUsage()
        
if len(sys.argv) == 6:  # if there is 6 args mean both options is used but still wanted to be sure
    if sys.argv[4].lower() == '-l':
        less = True
    elif sys.argv[4].lower() == '-s':
        stop = True
    else:
        printUsage()
    if sys.argv[5].lower() == '-l':
        less = True
    elif sys.argv[5].lower() == '-s':
        stop = True
    else:
        printUsage()
# -------------------------------------ARGUMENTS SECTION END------------------------------------


# ------------------------------------actual code starts here-----------------------------------

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

    
    
