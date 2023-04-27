from PIL import Image

# 读取 R.txt、G.txt、B.txt
with open('C:/Users/10858/Desktop/output_R.txt') as f:
    r_data = [int(x) for x in f.read().split()]

with open('C:/Users/10858/Desktop/output_G.txt') as f:
    g_data = [int(x) for x in f.read().split()]

with open('C:/Users/10858/Desktop/output_B.txt') as f:
    b_data = [int(x) for x in f.read().split()]

# 设置图片的宽度和高度
width = 1600
height = 1200

# 创建空白的图片
img = Image.new('RGB', (width, height))

# 填充图片
for y in range(height):
    for x in range(width):
        r = r_data[y * width + x]
        g = g_data[y * width + x]
        b = b_data[y * width + x]
        img.putpixel((x, y), (r, g, b))

# 保存图片
img.show()
