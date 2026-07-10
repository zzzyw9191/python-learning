

name = input("请输入商品名称：")
price = float(input("请输入商品价格："))
amount = int(input("请输入购买数量："))

total_price = price * amount
print("商品:",name)
print("原价:",total_price)

if(total_price >= 200):
    discount = total_price * 0.8
    print(f"实付金额: {discount:.2f}")
elif(total_price >= 100):
    discount = total_price * 0.9
    print(f"实付金额: {discount:.2f}")
else:
    print(f"实付金额: {total_price:.2f}")