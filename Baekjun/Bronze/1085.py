x, y, w, h = map(int, input().split())
x_min, y_min, m = 0, 0, 0
if w-x > w//2:
    x_min = x
else:
    x_min = w-x
if h-y > h//2:
    y_min = y
else:
    y_min = h-y
m = min(x_min, y_min)
print(m)