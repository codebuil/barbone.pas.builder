import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Barebone Builder")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="Build", command=self.build_kernel)
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="new file", command=self.copy_file)
        self.copy_button.pack(pady=5)

    def execute_command(self, command,shows:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if shows:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
        filename = tk.filedialog.askopenfilename(title="Select file")
        self.text_area.delete(1.0, tk.END)
        self.execute_command("mv -f kernel.bin /tmp/null",False)
        self.execute_command("mv -f /tmp/kernel.o /tmp/null",False)
        self.execute_command("mv -f /tmp/ppas.sh /tmp/null",False)
        self.execute_command("mv -f ppas.sh /tmp/null",False)
        self.execute_command("mv -f link.res /tmp/null",False)
        self.execute_command("nasm -felf32 -o /tmp/boot.o ./file/boot.s",True)
        self.execute_command("gcc -c ./file/base.c  -o lib.o -nostdlib",True)
        fff=f'fpc -Cn -CcCDECL -O2 -Xs -Xs -Xt -Pi386 -Tlinux "$1"'.replace("$1",filename)
        
        self.execute_command(fff,True)
        self.execute_command("mv -f ppas.sh /tmp",False)
        self.execute_command("mv -f link.res /tmp",False)
        self.execute_command("mv -f ./kernel.o /tmp",False)
        self.execute_command("gcc ./file/link.ld /tmp/boot.o ./lib.o /tmp/kernel.o -o /tmp/kernel.bin -nostdlib",True)
        self.execute_command("grub-file --is-x86-multiboot /tmp/kernel.bin",True)
        self.execute_command("mv -f /tmp/kernel.bin ./",True)

    def run_kernel(self):
        self.text_area.delete(1.0, tk.END)
        self.execute_command("qemu-system-i386 -kernel kernel.bin",True)

    def copy_file(self):
        self.text_area.delete(1.0, tk.END)
        filename = tk.filedialog.asksaveasfilename(title="Select file")
        if filename:
            shutil.copy( f"./file/new",filename+".pas")
            self.text_area.insert(tk.END, f"File {filename} copied \n",True)


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
