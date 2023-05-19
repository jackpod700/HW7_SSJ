import numpy as np

def q1():
    arr=np.arange(1,5).reshape(2,2)
    vec1=np.array([1,2,3])
    vec2=np.array([4,5,6])

    eig_val,eig_vec=np.linalg.eig(arr)
    determinant = np.linalg.det(arr)
    crossproduct=np.cross(vec1, vec2)
    a = np.array([[1, 2, -2], [2, 1, -5], [1, -4, 1]])
    b = np.array([-15, -21, 18])
    solution = np.linalg.solve(a, b)

    print("Eigenvalues: ",eig_val)
    print("Eigenvectors: {0}, {1}".format(eig_vec[0],eig_vec[1]))
    print("Determinant: ", int(determinant))
    print("Cross product: ",crossproduct)
    print("Solution: ",solution)

if __name__=="__main__":
    q1()