#The with statement itself ensures proper acquisition and release of resources
with open("abc",'w') as file:
    file.write("hello")