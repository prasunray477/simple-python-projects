import time

print("Typing Speed Test")
print("When ready, type the following paragraph....then press enter when done! :)")
input(" Press enter to start....")

text="a quick brown fox jumps over a lazy dog.  "
start=time.time()
input(text)
finish=time.time()
count = finish - start
words=len(text.split())
wpm = words/count*60
print(f"Your Typing speed is {wpm:.2f} wpm")