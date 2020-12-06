# Julian Saldana
# ID: 018462169
# using numpy, recommended to use as found online
import numpy as np

ID = 18462169
birthMonth = 7

print("1) remainder is:", ID % 3, ", so a 4 x 4 matrix is used.\n")  # test out remainder beforehand so I knew the result

four_b_four = np.array([[12, 5, 3, 74],
                        [23, 41, 12, 41],
                        [17, 36, 9, 8],
                        [19, 23, 14, 9]])

birthday_matrix = np.array([[birthMonth + 2],
                            [birthMonth + 23],
                            [birthMonth + 17],
                            [birthMonth + 8]])

#1A
print("1A) 12 * A =")
print(12 * four_b_four, "\n")

# 1B
print("1B) det(A) =", np.linalg.det(four_b_four), "\n")

# 1C
inverse = np.linalg.inv(four_b_four)
print("1C) inverse of matrix is: ")
print(inverse, "\n")

# 1D
print("1D) transpose of matrix is: ")
print(four_b_four.transpose(), "\n")

# 1E
print("1E) the trace of matrix is: ", four_b_four.trace(), "\n")

# 1F
print("1F) A*(A^-1) (inverse) =")
print(np.matmul(inverse, four_b_four), "\n")

# 1G
print("1G) A * A = ")
print(np.matmul(four_b_four, four_b_four), "\n")

# 1H
print("1H) A - (A^-1) =")
print(np.subtract(four_b_four, inverse), "\n")

# 1I
result = np.linalg.eig(four_b_four)
eigen_val = result[0]
eigen_vector = result[1]
print("1I) Eigen value =", eigen_val)
print("Eigen vector =")
print(eigen_vector, "\n")

# 1J
print("1J) Second row multiplied by my birth month =", four_b_four[1] * birthMonth, "\n")

# 1K
print("1K) Third column multiplied by my birth month =", four_b_four[:, 2] * birthMonth, "\n")

# 1L
second = 2 * four_b_four[1]
first_second = np.add(four_b_four[0], second)
print("1L) 1 * firstRow + 2 * secondRow", first_second, "\n")

# 1M
print("1M) Ax = B, where B is by birth month matrix modified matrix with 4 rows")
print(np.matmul(inverse, birthday_matrix))


#FIXME: RESULTS HERE

# C:\Users\Julian\Desktop\PycharmProjects\cecs229\venv\Scripts\python.exe C:/Users/Julian/Desktop/PycharmProjects/cecs229/exercise2.py

# 1) remainder is: 1 , so a 4 x 4 matrix is used.
#
# 1A) 12 * A =
# [[144  60  36 888]
#  [276 492 144 492]
#  [204 432 108  96]
#  [228 276 168 108]]
#
# 1B) det(A) = 32067.999999999993
#
# 1C) inverse of matrix is:
# [[ 0.28770114 -0.66742547  0.668704    0.08054759]
#  [-0.06305351  0.14291506 -0.0960459  -0.04724336]
#  [-0.27547711  0.62389298 -0.70250717  0.04730573]
#  [-0.01771236  0.07328178 -0.07346888 -0.01178745]]
#
# 1D) transpose of matrix is:
# [[12 23 17 19]
#  [ 5 41 36 23]
#  [ 3 12  9 14]
#  [74 41  8  9]]
#
# 1E) the trace of matrix is:  71
#
# 1F) A*(A^-1) (inverse) =
# [[ 1.00000000e+00 -2.66453526e-15  8.88178420e-16 -8.88178420e-16]
#  [-4.44089210e-16  1.00000000e+00 -2.22044605e-16 -5.55111512e-17]
#  [-2.22044605e-15  1.77635684e-15  1.00000000e+00 -1.60982339e-15]
#  [-5.55111512e-17  2.22044605e-16  0.00000000e+00  1.00000000e+00]]
#
# 1G) A * A =
# [[1716 2075 1159 1783]
#  [2202 3171 1243 3848]
#  [1337 2069  676 2878]
#  [1166 1749  585 2542]]
#
# 1H) A - (A^-1) =
# [[11.71229886  5.66742547  2.331296   73.91945241]
#  [23.06305351 40.85708494 12.0960459  41.04724336]
#  [17.27547711 35.37610702  9.70250717  7.95269427]
#  [19.01771236 22.92671822 14.07346888  9.01178745]]
#
# 1I) Eigen value = [ 87.30584874 -20.68765003   6.94010171  -2.55830041]
# Eigen vector =
# [[-0.44152705 -0.8494737  -0.78984518  0.67233077]
#  [-0.67628524  0.0027127   0.34155615 -0.0608548 ]
#  [-0.44615465  0.38629793  0.50929192 -0.73113768]
#  [-0.3855362   0.35938975  0.01028216 -0.09851765]]
#
# 1J) Second row multiplied by my birth month = [161 287  84 287]
#
# 1K) Third column multiplied by my birth month = [21 84 63 98]
#
# 1L) 1 * firstRow + 2 * secondRow [ 58  87  27 156]
#
# 1M) Ax = B, where B is by birth month matrix modified matrix with 4 rows
# [[-0.17634402]
#  [ 0.70621804]
#  [ 0.08690907]
#  [ 0.09897717]]
#
# Process finished with exit code 0
