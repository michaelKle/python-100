states = ["Alabama", "New York", "Kansas"]

print(states[0])
print(states[-1])

states[0] = "Alaska"
print(states[0])

states.append("Ohia")
print(states[-1])

states.extend(["Idaho", "Texas"])
print(states)
