def square_two_nums(x, y):
    x_squared = x * x
    y_squared = y * y
    return x_squared, y_squared


oh, hey = square_two_nums(2, 4)

print(oh, hey)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

true_statement = 161 in heights

print(true_statement)

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key: value for key, value in zip(names, heights)}
# students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
