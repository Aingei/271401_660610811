import numpy as np
import matplotlib.pyplot as plt
import random

# ==========================================
# 1. ฟังก์ชันสร้างเขาวงกต (Maze Generation)
# ==========================================
def generate_maze(width=30, height=30):
    # สร้าง Grid (1 = กำแพง, 0 = ทางเดิน)
    maze = np.ones((height + 1, width + 1))
    
    def carve_passages_from(cx, cy):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny, nx] == 1:
                # เจาะทะลุกำแพง (เปลี่ยน 1 เป็น 0)
                maze[cy + dy//2, cx + dx//2] = 0
                maze[ny, nx] = 0
                carve_passages_from(nx, ny)

    # เริ่มเจาะจากซ้ายล่าง (row=29, col=0)
    maze[height-1, 0] = 0
    carve_passages_from(0, height-1)
    
    final_maze = maze[:height, :width]
    
    # บังคับจุด Start (ซ้ายล่าง) และ End (ขวาบน) ให้เป็นทางเดิน
    final_maze[height-1, 0] = 0 
    final_maze[0, width-1] = 0
    
    # เจาะทางเชื่อมรอบๆ จุดเข้า-ออก ป้องกันการเกิดห้องปิดตาย
    final_maze[height-2, 0] = 0 
    final_maze[height-1, 1] = 0 
    final_maze[0, width-2] = 0  
    final_maze[1, width-1] = 0  
    
    return final_maze

# ==========================================
# 2. ฟังก์ชันแสดงผลสนาม (Infographic)
# ==========================================
def plot_maze(maze):
    plt.figure(figsize=(10, 10))
    # ใช้ gray_r เพื่อให้ 1(กำแพง)=สีดำ และ 0(ทางเดิน)=สีขาว
    plt.imshow(maze, cmap='gray_r', origin='upper')
    
    # วาดจุด Start (หนู) ซ้ายล่าง (x=0, y=29)
    plt.scatter(0, 29, color='green', s=200, label='Mouse (Start, 1 Cell)', zorder=5)
    
    # วาดจุด End (ชีส) ขวาบน (x=29, y=0)
    plt.scatter(29, 0, color='gold', s=200, label='Cheese (End, 1 Cell)', zorder=5)
    
    plt.title("Maze Environment (30x30, Cell = 16x16cm)", fontsize=16, fontweight='bold')
    
    # ตีเส้น Grid ขนาด 1 ช่อง เพื่อให้เห็นสัดส่วนช่องละ 16x16 cm ชัดเจน
    plt.grid(color='blue', linestyle='-', linewidth=0.5, alpha=0.3)
    plt.xticks(np.arange(-0.5, 30, 1), []) # ซ่อนตัวเลขแกน แต่ให้มีขีด Grid ทุกๆ 1 ช่อง
    plt.yticks(np.arange(-0.5, 30, 1), [])
    
    plt.legend(loc='upper right', bbox_to_anchor=(1.35, 1))
    plt.show()

# ==========================================
# 3. รันโปรแกรมเพื่อแสดงเฉพาะสนาม
# ==========================================
if __name__ == "__main__":
    print("🗺️ กำลังสร้างสนามเขาวงกตขนาด 30x30...")
    my_maze = generate_maze(30, 30)
    print("✅ สร้างเสร็จเรียบร้อย กำลังแสดงผลภาพ...")
    plot_maze(my_maze)