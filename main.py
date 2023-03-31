import time
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image


extension = 'png'


def open_file(event):
    global extension
    fn = askopenfilename(filetypes=[("Image files", ".png .jpg .jpeg")])

    if fn is None:
        return

    elif fn:
        extension = fn.split('/')[-1].split('.')[-1]
        # label4.config(text=fn.split('/')[-1])

        with open("file_path.txt", mode="w") as file:
            file.write(fn)
        base_width = 350
        image = Image.open(fn)
        w_percent = (base_width / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(w_percent)))
        img1 = image.resize((base_width, hsize), Image.Resampling.LANCZOS)
        img1.save('show_img.png', format='PNG')
        window.destroy()
        time.sleep(1)
        import page1


window = Tk()
window.title("Image Watermark")
window.minsize(width=775, height=485)
window.config(background='#ffffff')

title = PhotoImage(file='assets/Asset 3title.png')
canvas1 = Canvas(width=500, height=122, highlightthickness=0, background='#ffffff')
canvas1.create_image(250, 58, image=title, state='normal')
canvas1.pack()


canvas2 = Canvas(width=443, height=235, highlightthickness=0, background="#f2f2f2")

label1 = canvas2.create_text(221.5, 65, text='Upload File', font=('Myriad Pro', 20, 'normal'))
label2 = canvas2.create_text(221.5, 107, text='(.png/.jpg/.jpeg etc.)', fill='#898989', font=('Myriad Pro', 12, 'bold'))
label3 = canvas2.create_text(221.5, 143.6, text='Open File Explorer', fill='#256fff',
                             font=('Myriad Pro', 12, 'bold', 'underline'))

canvas2.tag_bind(label3, '<Button-1>', open_file)

canvas2.pack()

start_button = Button(width=16, text="Add Watermark", font=('Product Sans', 13, "bold"), background='#ffd418',
                      foreground='#000000', disabledforeground='#919191', relief='flat', overrelief='flat',
                      state='disabled')

start_button.pack(pady=25)

window.mainloop()
