import time
print("Welcome to Alco-Tech! If you're looking forward to launching your business, you're in the right place.")
time.sleep(3)  # Pause execution for N seconds
print("We can help prevent you from launching your business in locations that could potentially violate the Section 27.")
time.sleep(3)
print("\n")
print("All you have to do is just enter your wishlisted location.")
time.sleep(2)
while True:
    import geopy.distance
    import time
    
    educoords_1 = (13.733219302588033, 100.53343657739191) # Put in latitude and longtitude
    educoords_2 = (13.727923232474507, 100.53500155185385) # Put in latitude and longtitude
    educoords_3 = (13.734550522216965, 100.528471789469) # Put in latitude and longtitude

    gencoords_1 = (13.735174660299437, 100.52866791196926) # Put in latitude and longtitude
    gencoords_2 = (13.734673700136422, 100.52678132524451) # Put in latitude and longtitude

    storecoords = []

    city = input("First of all, what city in Thailand would you like to launch your business in?: ")
    print("\n")
    print(city + " is such a good choice!")

    time.sleep(1)
    x = float(input("Enter the latitude: "))
    y = float(input("Enter the longtitude: "))
    storecoords.append((x,y))

    distance_to_edu1 = geopy.distance.geodesic(educoords_1, storecoords).meters
    distance_to_edu2 = geopy.distance.geodesic(educoords_2, storecoords).meters
    distance_to_edu3 = geopy.distance.geodesic(educoords_3, storecoords).meters

    distance_to_gen1 = geopy.distance.geodesic(gencoords_1, storecoords).meters
    distance_to_gen2 = geopy.distance.geodesic(gencoords_2, storecoords).meters

    print("\n")

    if distance_to_edu1 <= 300 or distance_to_edu2 <= 300 or distance_to_edu3 <= 300 or distance_to_gen1 <= 100 or distance_to_gen2 <= 100:
        print("Unfortunately, your location is too close to some of the restricted places. Here are the details:")
        print("\n")
        print(f"Your location is " + str(distance_to_edu1) + " metres away from Patumwan Demonstration School")
        print(f"Your location is " + str(distance_to_edu2) + " metres away from Chulalongkorn University Demonstration Secondary School")
        print(f"Your location is " + str(distance_to_edu3) + " metres away from Wat Hua Lamphong School")
        print("\n")
        print(f"Your location is " + str(distance_to_gen1) + " metres away from PTT Station Samyan")
        print(f"Your location is " + str(distance_to_gen2) + " metres away from Lumphini Park")
    else:
        print("Your location is perfect! :)")

    print("\n")
    time.sleep(2)
    answer = input("Would you like to check other locations? (Type Y for Yes, and N for No): ")
    if answer == "N":
        break
    else:
        print("/n")
        continue

print("\n")
print("Thank you for using our service.")
