import numpy as np

def calculate(lst):

    if len(lst) != 9:
      raise ValueError('List must contain nine numbers.')

    # Constructing the 3x3 and flattened matrix  
    mat_flat = np.matrix(lst)
    mat = mat_flat.reshape((3,3))

    calculations = {'mean':[],
                   'variance':[],
                   'standard deviation': [],
                   'max':[],
                   'min':[],
                   'sum':[]}
  
    calculations['mean'] = [list(mat.mean(0).flat),list(mat.mean(1).flat),mat_flat.mean()]                  
    calculations['variance'] = [list(mat.var(0).flat),list(mat.var(1).flat),mat_flat.var()]
    calculations['standard deviation'] = [list(mat.std(0).flat),list(mat.std(1).flat),mat_flat.std()]
    calculations['max'] = [list(mat.max(0).flat),list(mat.max(1).flat),mat_flat.max()]
    calculations['min'] = [list(mat.min(0).flat),list(mat.min(1).flat),mat_flat.min()]
    calculations['sum'] = [list(mat.sum(0).flat),list(mat.sum(1).flat),mat_flat.sum()]


    return calculations