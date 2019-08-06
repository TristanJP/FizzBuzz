 
def run(max):
  for i in range(1, max +1):
    print( ("" if i%3 else "Fizz") + ("" if i%5 else "Buzz") or i )

run(100)