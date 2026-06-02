def show(mat, n, m):
  for idx in range(n):
    for jdx in range(m):
      print(mat[idx*m+jdx], end=" ")
    print()
  print()

xs = [4,5,3,2,9,4]
show(xs, 2, 3)
# 1 2 3
# 4 5 6

show(xs, 3, 2)
# # 1 2
# # 3 4
# # 5 6