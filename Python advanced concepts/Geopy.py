
from geopy.distance import geodesic as GD
New_York = (40.7128, 74.0060)
Texas = (31.9686, 99.9018)

print ("The distance between New York and Texas is: ", GD(New_York, Texas).km)


#Distance between Two Points Using Great Circle Distance
from geopy.distance import great_circle as GC
New_York = (40.7128, 74.0060)
Texas = (31.9686, 99.9018)
print ("The distance between New York and Texas is: ", GC(New_York, Texas).km)

# Distance between Two Points using Haversine Formula


# For calculating the distance in Kilometres
from math import radians, cos, sin, asin, sqrt
def distance_1(La1, La2, Lo1, Lo2):
    # The math module contains the function name "radians" which is used for converting the degrees value into radians.
    Lo1 = radians(Lo1)
    Lo2 = radians(Lo2)
    La1 = radians(La1)
    La2 = radians(La2)

    # Using the "Haversine formula"
    D_Lo = Lo2 - Lo1
    D_La = La2 - La1
    P = sin(D_La / 2) ** 2 + cos(La1) * cos(La2) * sin(D_Lo / 2) ** 2

    Q = 2 * asin(sqrt(P))

    # The radius of earth in kilometres.
    R_km = 6371

    # Then, we will calculate the result
    return (Q * R_km)


# driver code
La1 = 40.7128
La2 = 31.9686
Lo1 = -74.0060
Lo2 = -99.9018
print("The distance between New York and Texas is: ", distance_1(La1, La2, Lo1, Lo2), "K.M")


# For calculating the distance in Miles
def distance_2(La1, La2, Lo1, Lo2):
    # The math module contains the function name "radians" which is used for converting the degrees value into radians.
    Lo1 = radians(Lo1)
    Lo2 = radians(Lo2)
    La1 = radians(La1)
    La2 = radians(La2)

    # Using the "Haversine formula"
    D_Lo = Lo2 - Lo1
    D_La = La2 - La1
    P = sin(D_La / 2) ** 2 + cos(La1) * cos(La2) * sin(D_Lo / 2) ** 2

    Q = 2 * asin(sqrt(P))
    # The radius of earth in Miles.
    R_Mi = 3963

    # Then, we will calculate the result
    return (Q * R_Mi)


print("The distance between New York and Texas is: ", distance_2(La1, La2, Lo1, Lo2), "Miles")