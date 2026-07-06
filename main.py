import numpy as np
import matplotlib.pyplot as plt
from maze_map import generate_maze

def show_map_with_mouse():
    # 1. สร้างแผนที่ 30x30
    my_maze = generate_maze(30, 30)
    
    # กำหนดพิกัด (แกน Y, แกน X)
    start_pos = (29, 0) # ซ้ายล่าง (หนู)
    end_pos = (0, 29)   # ขวาบน (เป้าหมาย)
    
    # 2. วาดกราฟิก
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(my_maze, cmap='gray_r', origin='upper')
    
    # วางอีโมจิหนู (🐭) และ เปลี่ยนชีสเป็นดาว (⭐) เพื่อแก้ปัญหาฟอนต์ไม่รองรับ
    ax.text(start_pos[1], start_pos[0], '🐭', fontsize=24, ha='center', va='center', zorder=5)
    ax.text(end_pos[1], end_pos[0], '⭐', fontsize=24, ha='center', va='center', zorder=5, color='orange')
    
    ax.set_title("Maze Map with Mouse (30x30, Cell = 16x16cm)", fontsize=16, fontweight='bold')
    
    # สร้างเส้นตาราง (Grid) ให้เห็นช่องชัดเจน
    ax.grid(color='blue', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.set_xticks(np.arange(-0.5, 30, 1)) 
    ax.set_yticks(np.arange(-0.5, 30, 1))
    ax.set_xticklabels([]) # ซ่อนตัวเลข
    ax.set_yticklabels([]) # ซ่อนตัวเลข
    
    # คำอธิบาย (Legend) - ย้ายมาด้านขวานอกกรอบ (bbox_to_anchor=(1.05, 1))
    ax.plot([], [], ' ', label='🐭 = Mouse (Start)')
    ax.plot([], [], ' ', label='⭐ = Goal (Target)')
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=12)
    
    # บังคับให้โปรแกรมจัดหน้าจอให้พอดี ไม่ให้ Legend โดนตัดหรือไปทับกราฟ
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("🗺️ กำลังสร้างแผนที่และวางหนู...")
    show_map_with_mouse()