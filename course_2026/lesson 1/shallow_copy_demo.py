a = [[1, 2], [3, 4]]

b = a[:]   # 浅复制：外层列表独立，内层列表仍共享
c = a      # 赋值：c 和 a 指向同一个列表

b[0].append(9)     # 修改共享的内部列表
b[1] = [30, 40]    # b[1] 改为指向一个新列表
a.append([5, 6])   # 修改 a 的外层列表，c 也会看到变化

print(a)
print(b)
print(c)

print(a is b)
print(a is c)
print(a[0] is b[0])
print(a[1] is b[1])