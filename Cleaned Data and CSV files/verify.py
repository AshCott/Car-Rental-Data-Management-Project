import csv
import pprint

#-----------------------------------------------------------------
#               Functions
#-----------------------------------------------------------------
#Imports CSV file column as list
def importCSV(file, column):
    with open(file) as car:
        data_list = []
        reader = csv.DictReader(car)
        for row in reader:
            data_list.append(row[column])
    return data_list

#Finds missing values in another list
def find_missing(store_data, central_data, name):
    print("==============================")
    count = 0
    for key in store_data:
        if key not in central_data:
            print("Missing",name + ":", key)
            count += 1
    if count == 0:
        print("none")
    print("------------------------------")
    print("Total missing", name + "'s:", count)
    print("==============================\n")

#-----------------------------------------------------------------
#                      Find Missing Entry's
#-----------------------------------------------------------------

cd_order_id = importCSV('central_database.csv', 'Order_ID')
sd_order_id = importCSV('data_in_store.csv', 'Order_ID')
find_missing(sd_order_id,cd_order_id,"Order ID")

cd_car_id = importCSV('central_database.csv', 'Car_ID')
sd_car_id = importCSV('data_in_store.csv', 'Car_ID')
find_missing(sd_car_id,cd_car_id,"Car ID")

cd_customer_id = importCSV('central_database.csv', 'Customer_ID')
sd_customer_id = importCSV('data_in_store.csv', 'Customer_ID')
find_missing(sd_customer_id,cd_customer_id,"Customer_ID")

#-----------------------------------------------------------------
#                    Find Cars still rented out
#-----------------------------------------------------------------

#Open and read data from store csv
with open('data_in_store.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    dict = {}
    carid_store = []
    count = 0
    for row in reader:
        #print(row['Car_ID'], row['Pickup_Or_Return'])
        #print (count)
        #count += 1
        dict[row['Car_ID']] = row['Pickup_Or_Return']
        carid_store.append(row['Car_ID'])

#pprint.pprint(dict)
#print (len(dict))
unavailable = {}
for key in dict:
    if (dict[key] == "Pickup"):
        unavailable[key] = dict[key]
#pprint.pprint(unavailable)  
print("Cars not returned: ",len(unavailable))  