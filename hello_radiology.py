print("hello radiology")
print("I am learning python for medical imaging and AI research") 
#variable never start with number or special character, it should start with letter or underscore
#like 2nd_variable = 10 #invalid variable name
#first_variable = 10 #valid variable name
_underscore_variable = 20 #valid variable name ###
#variable name does not contain space, it should be underscore like slice thickness = 0.625 #valid variable name
#slice_thickness = 0.625 #valid variable name > snack_case naming convention is used in python for variable naming
#python keywords are reserved words in python, we cannot use them as variable name like class = 10 #invalid variable name
#variable name should be meaningful and descriptive like number_of_slices = 240 #valid variable name
#.            NAME ERROOR
# name error occurs when we try to use a variable that has not been defined or assigned a value yet. For example, if we try to print the value of a variable that has not been defined, we will get a name error.
# maswood ;= MASWOOD 
#string variable can be defined using single or double quotes like patient_name = 'John Doe' or patient_name = "John Doe"
#text should be enclosed in quotes, otherwise it will be treated as a variable name and will result in a name error if the variable is not defined. For example, if we try to print the value of a variable that has not been defined, we will get a name error.
patinet_name = 'John Doe'
modality = "CT" 
examination_date = "2023-06-01"
patient_id = 12345
print("Patient Name:", patinet_name)
print("Modality:", modality)
print("Examination Date:", examination_date)
print("Patient ID:", patient_id)
#patinet_id should be a string, not an integer, because it may contain leading zeros or other non-numeric characters. For example, if the patient ID is "0012345", it should be stored as a string to preserve the leading zeros.
messaage = "patient's CT examination is scheduled for 2023-06-01." 
print(messaage)