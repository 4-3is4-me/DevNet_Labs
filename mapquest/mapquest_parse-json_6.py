import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "##############################"

while True:
    orig = input("Enter the start location: ")
    if orig == 'q' or orig == 'quit' or orig == 'exit':
        quit()
    dest = input("Enter the finish location: ")
    if dest == 'q' or dest == 'quit' or dest == 'exit':
        quit()

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("\nChecking...\n")
    json_data = requests.get(url).json()

    print("Request URL: {}".format(url))
    json_status = json_data['info']['statuscode']

    if json_status == 0:
        print("Request status is: {}".format(json_status)+ " -- Successful\n")
        print("****************************************")
        print("************* Information **************")
        print("         Start: {}".format(orig))
        print("        Finish: {}".format(dest))
        print("          Time: {}".format(json_data['route']['formattedTime']))
        print("      Distance: {}".format(json_data['route']['distance'])+" miles")
        print("     Fuel Used: {:.2f}".format((json_data['route']['fuelUsed'])*3.78) + " litres")
        print("****************************************\n")
        print("***********  Directions ****************")

        for i in json_data['route']['legs'][0]['maneuvers']:
            print((i['narrative']) + " Distance " + str("{:.2f}".format((i['distance'])) + " miles"))
        print("****************************************\n")
    elif json_status == 402:
        print("****************************************")
        print("Request status is: {}".format(json_status)+ " -- Error; One or both locations is not recognised or cannot calculate directions.\n")
        print("****************************************")
    elif json_status == 611:
        print("****************************************")
        print("Request status is: {}".format(json_status)+ " -- Error; One or both locations is missing.\n")
        print("****************************************")
    else:
        print("****************************************")
        print("Request status is: {}".format(json_status)+ " -- Error; Please refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("****************************************")