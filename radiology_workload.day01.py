# Day 1: Analysis of a hypothetical radiology  dataset
# integer which represents the number of slices in a CT scan and no decimal values are allowed
#float which represents the slice thickness in millimeters and decimal values are allowed
#string(str) represents the quotation marks around the modality name
#boolean which represents the presence of contrast in the scan and can only be True or False
modality = "CT"
number_of_slices = 240
rows = 512
columns = 512
slice_thickness_mm = 0.625
pixels_per_slice = rows * columns
total_pixels = pixels_per_slice * number_of_slices
print("Modality:", modality)
print("Number of Slices:", number_of_slices)
print("Rows:", rows)
print("Columns:", columns)
print("Slice Thickness (mm):", slice_thickness_mm)
print("Pixels per Slice:", pixels_per_slice)
print("Total pixels across slices:", total_pixels)