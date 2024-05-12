from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

def hide_message():
    global secret_message

    global file
    if not file:
        messagebox.showerror("Error", "Silakan pilih gambar terlebih dahulu sebelum menyembunyikan pesan")
        return

    secret_message = lsb.hide(str(file), message)
    text.delete(1.0, END)
    messagebox.showinfo("Pesan", "Pesan tersembunyi")
    
    # Hapus tampilan gambar setelah pesan disembunyikan
    frame_1_label.configure(image=None)

def open_image():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Masukkan Gambar", filetype=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All file", "*.*")))
    if file:
        img = Image.open(file)
        img = ImageTk.PhotoImage(img.resize((350, 350)))
        frame_1_label.configure(image=img, width=350, height=350)
        frame_1_label.image = img

      
def hide_message():
    global secret_message  # Tambahkan baris ini untuk mendeklarasikan variabel sebagai global

    global file
    if not file:
        messagebox.showerror("Error", "Silakan pilih gambar terlebih dahulu sebelum menyembunyikan pesan")
        return

    message = text.get(1.0, END)
    if not message.strip():
        messagebox.showerror("Error", "Tidak ada pesan yang akan disembunyikan")
        return

    secret_message = lsb.hide(str(file), message)
    text.delete(1.0, END)
    messagebox.showinfo("Pesan", "Pesan tersembunyi")


def show_message():
    global file
    if not file:
        messagebox.showerror("Error", "Silakan pilih gambar terlebih dahulu sebelum menampilkan pesan")
        return

    try:
        clear_message = lsb.reveal(file)
    except IndexError:
        messagebox.showerror("Error", "Tidak ada pesan tersembunyi dalam gambar ini")
        return

    text.delete(1.0, END)
    text.insert(END, clear_message)


def save_image():
    global file
    if not file:
        messagebox.showerror("Error", "Silakan pilih gambar terlebih dahulu sebelum menyimpan gambar")
        return

    try:
        secret_message
    except NameError:
        messagebox.showerror("Error", "Masukkan Gambar dan sembunyikan pesan")
        return

    secret_message.save("Gambar_Pesan_Tersembunyi.png")
    messagebox.showinfo("Pesan", "Gambar tersebut disimpan dengan nama 'Gambar_Pesan_Tersembunyi.png'")

def main():
    root = Tk()
    root.title("Penyembunyian pesan didalam gambar")
    root.geometry("1200x624")
    root.resizable(False, False)

    bg_img = Image.open("26.gembok_l.png")
    bg_img = bg_img.resize((1200, 624))
    bg = ImageTk.PhotoImage(bg_img)

    canvas1 = Canvas(root, width=1200, height=624)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")

    Label(text="Penyembunyian pesan didalam gambar", background="white", fg="black", font="arial 20").place(x=450, y=20)

    frame_1 = Frame(root, highlightbackground="#1900ff", highlightthickness="5", width="350", height="350")
    frame_1.place(x=100, y=100)  # image
    frame_2 = Frame(root, width="350", height="350")
    frame_2.place(x=750, y=100)  # text

    global frame_1_label
    frame_1_label = Label(frame_1, bg="black")
    frame_1_label.place(x=0, y=0)

    global text
    text = Text(frame_2, highlightbackground="#1900ff", highlightthickness="5", font="Roboto 20", bg="white", fg="black", wrap=WORD)
    text.place(x=0, y=0, width=350, height=350)

    Button(text="Buka Gambar", activebackground="#1900ff", width=15, height=2, command=open_image).place(x=480, y=100)
    Button(text="Simpan Gambar", activebackground="#1900ff", width=15, height=2, command=save_image).place(x=480, y=150)
    Button(text="Sembunyikan Pesan", activebackground="#1900ff", width=15, height=2, command=hide_message).place(x=480, y=300)
    Button(text="Tampilkan Pesan", activebackground="#1900ff", width=15, height=2, command=show_message).place(x=480, y=350)

    root.mainloop()

if __name__ == "__main__":
    main()
