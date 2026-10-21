#adding element 
mri_scans = [
    "mri brain ",
    "mri spine",
    "mri knee",
]
# print original list 
print("original list:",mri_scans)
#add a new examination 
mri_scans.append("mri shoulder") # if we want to add anaother elements so we need this command 
# print updated list
print("updated list:",mri_scans)
# count total examination 
#print ("total examination:",len(mri_scans))

                    # inserting elements using insert()
ct_scan = [
    "ct brain",
    "ct chest",
    "ct abdomen",
    "ct angiography"
]
print("original list:",ct_scan)
#ct_scan.insert(1,"ct angiography") which place you want to add insert(numbering but start from 0 always )
#print("updated list:",ct_scan)
#print("total examination",len(ct_scan))
#append() = adding in list in last position 
#insert() = specific position in list for elements 
#remove() = on the bases of value remove element
#len  (). = total elements 
ct_scan.remove("ct chest")
print("updated list",ct_scan)
print("total examination",len(ct_scan))