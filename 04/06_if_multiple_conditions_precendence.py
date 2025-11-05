temprature = 50
humidity = 70
rain = True

if temprature > 30 or humidity > 70 and not rain:
    print('Dry wheather')

# not rain          False
# humidity < 70     False
#                   False and False = False
# temprature > 30   True
#                   True or False = True

if temprature > 30 or humidity < 70 and not rain:
    print('Dry wheather')

# temprature > 30   True
#humidity < 70      False
#                   True or False = True

