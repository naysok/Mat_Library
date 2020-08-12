#####################
###    Python2    ###
#####################


import csv


def csv_to_memory(path):
    with open(path) as f:
        reader = csv.reader(f)
        l = [row for row in reader]
    return l


def mat_index_to_mat(mat_index):
    ### Value List Component
    if mat_index == 0:
        return "ABS"
    elif mat_index == 1:
        return "PLA"


def get_value_from_csv(path, mat_index, nozzle):
    
    l = csv_to_memory(path) 
    m = mat_index_to_mat(mat_index)
    
    for i in xrange(len(l)):
        ll = l[i]
        
        ### Check Material
        if ll[0] == m:
            
            ### Check Nozzle
            if ll[1] == str(nozzle):
                return [m, nozzle, ll[2]]
            


path = CSV
mat_index = MAT
nozzle = NZL

param = get_value_from_csv(path, mat_index, nozzle)


if param != None:
    msg = "Material : {}\nNozzle : {}\nParam : {}".format(param[0], param[1], param[2])
    DEBUG = msg
else:
    DEBUG = "N/A"
