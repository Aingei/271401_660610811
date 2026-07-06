import numpy as np
import random

def generate_maze(width=30, height=30):
    # 1 = กำแพง, 0 = ทางเดิน
    maze = np.ones((height + 1, width + 1))
    
    def carve_passages_from(cx, cy):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny, nx] == 1:
                maze[cy + dy//2, cx + dx//2] = 0
                maze[ny, nx] = 0
                carve_passages_from(nx, ny)

    # เจาะจากมุมซ้ายล่าง
    maze[height-1, 0] = 0
    carve_passages_from(0, height-1)
    
    final_maze = maze[:height, :width]
    
    # กำหนดจุดเริ่ม (ซ้ายล่าง) และเป้าหมาย (ขวาบน) ให้เป็นทางเดินเสมอ
    final_maze[height-1, 0] = 0 
    final_maze[0, width-1] = 0
    
    # เจาะกันทางปิดตายที่จุดเข้า-ออก
    final_maze[height-2, 0] = 0 
    final_maze[height-1, 1] = 0 
    final_maze[0, width-2] = 0  
    final_maze[1, width-1] = 0  
    
    return final_maze