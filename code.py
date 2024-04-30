def FastestCart(t, d1, d2, d3):
    speed1 = d1 // t
    speed2 = d2 // t
    speed3 = d3 // t
    return max(speed1, speed2, speed3)

# Test the function
t = 4
d1 = 248
d2 = 124
d3 = 200
print(FastestCart(t, d1, d2, d3))