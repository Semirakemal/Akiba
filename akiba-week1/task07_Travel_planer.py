#travel planner
destination = input("where do you want to travel? ")
distance = float(input("please enter its distance: "))
A_speed = float(input("can you input its speed? "))

Time = distance / A_speed

Minute = Time * 60

print(f"Distination: {destination}")
print(f"Distance: {distance} km")
print(f"Speed: {A_speed} m/s")
print(f"Estimated Time Travel: {Time} hours")
print(f"Minute: {Minute} Min")