import threading
from queue import Queue
from spider import Spider
from domain import *
from main import *


PROJECT_NAME = 'medium'
HOMEPAGE = 'https://medium.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)



# create worker threads(will die when general exits
#def create_worker():
   # for _ in range(NUMBER_OF_THREADS):
     #   t = threading.Thread(target=work)
     #   t.daemon = True
      #  t.start()


# do the next job in the queue
#def work():
  #  while True:
      #  url = queue.get()
      #  Spider.crawl_page(threading.current_thread().name, url)
      #  queue.task_done()


# each queued link is a job
#def create_jobs():
    #for link in file_to_set(QUEUE_FILE):
     #   queue.put(link)
#    crawl()


# check for items in the queue
#def crawl():
   # queued_links = file_to_set(QUEUE_FILE)
  #  if len(queued_links) > 0:
    #    print(str(len(queued_links)) + 'links in the queue')
   #     create_jobs()


#create_worker()
#crawl()