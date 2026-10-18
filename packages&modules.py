# The math module provides mathematical functions such as square root and factorial
# import math

# print(math.sqrt(25))
# print(math.factorial(5))



# The random module generates random values.
# import random

# print(random.randint(1, 10))
# print(random.choice(["Apple", "Mango", "Banana"]))



# The datetime module works with dates and times.
# import datetime

# today = datetime.date.today()
# print(today)




# NumPy is a popular third-party package used for numerical calculations and working with arrays.
# import numpy as np

# numbers = np.array([10, 20, 30, 40])

# print(numbers)
# print(np.mean(numbers))


# Pandas is a popular package for data analysis and data manipulation.
import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Marks": [80, 90, 85]
}

df = pd.DataFrame(data)
print(df)