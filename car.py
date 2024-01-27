command = ""
while command.lower() != "quit":
  command = input(" > ")             #to improve quality use .lower() here
  if command.lower() == "start":
    print("Car Started....")
  elif command.lower() == "stop":
    print("Car Stopped")
  elif command.lower() == "help":
    print("""
    start - to start the car
    stop - to stop the car
    quit - to quit
    """)
  elif command.lower() == "quit":
    break
  else:
    print("sorry, I don't understand the command")