#type conversion and arithmetic operations
#Type conversion - converting one data type to another
number_of_slices = "240" # str
number_of_slices = int(number_of_slices) # converting str to int
print(number_of_slices)
print(type(number_of_slices)) # <class 'int'>
#int() to float conversion,float() to int conversion, str() to int conversion, int() to str conversion

#Arithmetic operations - addition, subtraction, multiplication, division, modulus, exponentiation
#Floor division = // example: 5 // 2 = 2, 7 // 3 = 2 kam se kam kitna bar mutiplication kre ke uske najdik phuch jaye
#modulus(remainder) = % example: 5 % 2 = 1, 7 % 3 = 1
#exponentiation = ** example: 2 ** 3 = 8, 3 ** 2 = 9
rows = 512
columns = 512
pixels_per_slice = rows * columns
print(pixels_per_slice)
#suppose we have 240 slices in a CT scan,and divide the slices into 4 equal parts, how many slices will be in each part? 
slices = 240
groups = 4
result = slices / groups
print(result) # 60.0
# suppose we have Ct dataset 
#number of reconstructed slices  = 240
# slice interval/thickness   = 0.625 mm
#what is the total distsance btw first and last slice?
#formula = (number_of_slices - 1) * slice_thickness_mm
number_of_slices = 240
slice_thickness_mm = 0.625
total_distance_mm = (number_of_slices - 1) * slice_thickness_mm
print(total_distance_mm) # 149.375
print("distance:", total_distance_mm, "mm")
# CT Dataset calculation
modality = "CT"
rows = 512
columns = 512
slice = 240
slice_interval_mm = 0.625 
#Pixel calculation
pixels_per_slice = rows * columns
total_pixels = pixels_per_slice * slice
#slice position calculation
distance = (slice - 1) * slice_interval_mm
#Display the results
print("Modality:", modality)
print("pixels per Slice:", pixels_per_slice)
print("Total pixels :", total_pixels)
print("centre-to-centre distance between first and last slice:", distance, "mm")