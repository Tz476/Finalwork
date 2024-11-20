import math
from dorothy import Dorothy

# 初始化画布
canvas_width = 800
canvas_height = 800
dot = Dot.dorothy  
# 函数：设置原点并绘制网格
def draw_grid(dot, origin_x, origin_y, square_size=50, grid_size=5):
    dot.clear()
    dot.set_origin(origin_x, origin_y)
    for row in range(-grid_size, grid_size + 1):
        for col in range(-grid_size, grid_size + 1):
            x = col * square_size
            y = row * square_size
            dot.draw_rect(x, y, square_size, square_size)

# 函数：应用旋转和缩放
def apply_transformations(dot, scale=1.0, rotate=0.0):
    # 构建变换矩阵
    scale_matrix = [[scale, 0, 0],
                    [0, scale, 0],
                    [0, 0, 1]]
    rotate_matrix = [[math.cos(math.radians(rotate)), -math.sin(math.radians(rotate)), 0],
                     [math.sin(math.radians(rotate)), math.cos(math.radians(rotate)), 0],
                     [0, 0, 1]]
    # 组合变换矩阵 (R × S)
    combined_matrix = matrix_multiply(rotate_matrix, scale_matrix)
    dot.transform(matrix=combined_matrix)

# 矩阵相乘工具函数
def matrix_multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def task1(dot):
    draw_grid(dot, canvas_width // 2, canvas_height // 2)
    apply_transformations(dot, scale=1.5, rotate=45)
    dot.show()

# # 任务 2：网格的旋转演示
# def rotate_grid(dot):
#     dot.clear()
#     square_size = 50
#     grid_size = 5
#     for row in range(-grid_size, grid_size + 1):
#         for col in range(-grid_size, grid_size + 1):
#             dot.push()  # 保存状态
#             x = col * square_size
#             y = row * square_size
#             dot.translate(x, y)  # 移动到每个方块中心
#             dot.rotate(15 * (row + grid_size) + 15 * (col + grid_size))  # 旋转
#             dot.draw_rect(-square_size // 2, -square_size // 2, square_size, square_size)
#             dot.pop()  # 恢复状态
#     dot.show()

# # 任务 3：径向绘制
# def radial_faces(dot):
#     dot.clear()
#     num_faces = 12
#     for i in range(num_faces):
#         dot.push()
#         angle = 360 / num_faces * i
#         dot.translate(canvas_width // 2, canvas_height // 2)
#         dot.rotate(angle)
#         dot.translate(200, 0)  # 径向偏移
#         dot.draw_circle(0, 0, 20)  # 在当前原点绘制一个圆
#         dot.pop()
#     dot.show()

# # 动态交互：响应鼠标
# def interactive(dot, mouse_x, mouse_y):
#     dot.clear()
#     dot.set_origin(canvas_width // 2, canvas_height // 2)
#     rotation = mouse_x % 360
#     scale = 1 + mouse_y / canvas_height
#     apply_transformations(dot, scale=scale, rotate=rotation)
#     dot.draw_circle(0, 0, 100)
#     dot.show()

# # 主函数
# def main():
#     # 运行任务 1：基础旋转与缩放
#     task1(dot)
    
#     # 运行任务 2：网格旋转
#     rotate_grid(dot)
    
#     # 运行任务 3：径向绘制
#     radial_faces(dot)
    
#     # 动态交互：可以替换为事件驱动代码
#     # 模拟鼠标输入
#     for mouse_x, mouse_y in [(100, 200), (300, 500), (600, 700)]:
#         interactive(dot, mouse_x, mouse_y)

# # 调用主函数
# if __name__ == "__main__":
#     main()
