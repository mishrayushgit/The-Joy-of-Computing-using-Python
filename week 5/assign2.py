def merge_list(list1,list2):
    i,j = 0,0
    merged_list =[]
    while i<len(list1) and j < len(list2):
        if list1[i]<list2[j]:
            merged_list.append(list1[i])
            i+=1
        else :
            merged_list.append(list2[j])
            j+=1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

list1 =[1,2,3,4,5]
list2 =[1,2,3,4]
print(merge_list(list1,list2))
