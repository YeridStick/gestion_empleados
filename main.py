import tkinter as tk
from ui.login import LoginWindow
from data_manager import DataManager

def main():
    # Inicializar archivo de persistencia
    DataManager.inicializar_excel()
    
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
