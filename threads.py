# V1 (sync task no threading) - usually takes something like 1.5e-5 seconds
import time

def compute(x):
    a = x ** 2
    b = a * 14
    c = b - 3
    d = 9 * 19 - 4 + c
    print(d)

start_time = time.time()

compute(10)
compute(10)

end_time = time.time()

print(f'time taken: {end_time - start_time}')

# V2 (sync task w/ threading) - usually takes something like 2.0e-4 seconds
import time
import threading

def compute(x):
    a = x ** 2
    b = a * 14
    c = b - 3
    d = 9 * 19 - 4 + c
    print(d)

start_time = time.time()

t1 = threading.Thread(target=compute, args=(10,))
t2 = threading.Thread(target=compute, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()

print(f'time taken: {end_time - start_time}')

# V3 (async task no threading) - usually takes 0.3 to 0.4 seconds
import time
import requests

def fetch(url):
    response = requests.get(url=url)
    print(response.text[:100])

start_time = time.time()

fetch('https://google.com')
fetch('https://microsoft.com')

end_time = time.time()

print(f'time taken: {end_time - start_time}')

# V4 (async task w/ threading) - usually takes 0.17 seconds
import time
import requests
import threading

def fetch(url):
    response = requests.get(url=url)
    print(response.text[:100])

start_time = time.time()

t1 = threading.Thread(target=fetch, args=('https://google.com', ))
t2 = threading.Thread(target=fetch, args=('https://microsoft.com', ))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()

print(f'time taken: {end_time - start_time}')

