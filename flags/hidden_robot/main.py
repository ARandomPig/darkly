import threading
import requests
import time
from bs4 import BeautifulSoup

IP = "http://10.12.248.155/"
BASE_URL = ".hidden/"

thread_pool = []
visited_count = 0
stop_thread = False

class Request(threading.Thread):
	def __init__(self, url=""):
		self.url = url
		threading.Thread.__init__(self)

	def run(self):
		global thread_pool
		global visited_count
		global stop_thread

		if (stop_thread):
			thread_pool.clear()
			exit(0)

		res = requests.get(IP + BASE_URL + self.url)
		parsed = BeautifulSoup(res.content, "html.parser")
		
		readme_value = parsed.find("pre").contents[-1].split(" ")[-1]
		if not readme_value.startswith("34"):
			stop_thread = True

			time.sleep(0.5) # processing NSA hack

			print("\n\nFound the flag on: ", IP + BASE_URL + self.url)

			flag = requests.get(IP + BASE_URL + self.url + "README")
			print(flag.content.decode(), "\n")
			
			exit(0)

		for link in parsed.find_all("a"):
			
			url = link["href"]
			if (url != "README" and url != "../"):

				if (not stop_thread):
					print("\r " + str(visited_count) + " " + self.url + url + "       ", end="", flush=True)
			
				new_thread = Request(self.url + url)
				new_thread.start()

				thread_pool.append(new_thread)
				
				visited_count += 1


def main():
	thread_pool.append(Request())
	thread_pool[0].start()

	for thread in thread_pool:
		thread.join()


if __name__ == "__main__":
	main()