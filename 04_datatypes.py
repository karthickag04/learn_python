
float_value= 10.5
int_value= 20
str_value= "Hello, World! lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."



str_value01 = """ Hello, World! lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

Ut




 enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat." 


Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 


sunt in culpa qui officia deserunt mollit anim id est laborum."""



bool_value= True
list_value= [1, 2, 3, 4, 5]
print(list_value)
print(list_value[0])
print(list_value[1])
print(list_value[2])
print(list_value[3])
print(list_value[4])
print(list_value[0:2])
print(list_value[0:4])
print("****************")
list_value[0]=10
print(list_value)
print("****************")
print("****************")
print("****************")

tuple_value= (1, 2, 3)
print(tuple_value)
print(tuple_value[0])
print(tuple_value[1])
# cannot change the value of tuple
# tuple_value[0]=100 # TypeError: 'tuple' object does not support item assignment
# for that we need to convert tuple to list
# and then change the value and convert it back to tuple
temp_list= list(tuple_value)
temp_list[0]=100
tuple_value= tuple(temp_list)

print(tuple_value)
print("****************")
print("****************")
print("****************")
# dict_value= {"key1": "value1", "key2": "value2"}  # this is syntax for creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False
    }

print(person)

print(person["name"])
print(person["age"])
print(person["city"])
print(person["is_student"])
print("****************") 
print("****************")
person["name"]= "Jane" 
person["location"]= "USA"
print(person)

set_value= {1, 2, 3, 4, 5}
print(set_value)
# print(set_value[0]) # TypeError: 'set' object is not subscriptable
# set_value[0]=100 # TypeError: 'set' object does not support item assignment

# # None value
none_value= None

print("******************")
print("******************")
print("******************")
print("******************")
print("******************")
# # type of variable
type_value= type(float_value)
print("variable float_value is ..", type(float_value) , "Data Type")
print("variable int_value is ..", type(int_value) , "Data Type")
print("variable str_value is ..", type(str_value) , "Data Type")
print(type(int_value))
print(type(str_value))
print(type(bool_value))
print(type(list_value))
print(type(tuple_value))
print(type(person))
# print(type(set_value))
# print(type(none_value))
# print(type(complex_value))
# print(type(bytes_value))
# print(type(bytearray_value))
# print(type(memoryview_value))
# print(type(frozenset_value))
# print(type(range_value))
# print(type(object_value))
# print(type(type_value))