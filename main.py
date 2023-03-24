import time
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
#
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
# 4000 x 6000
        base_width = 400
        image = Image.open(fn)
        wpercent = (base_width / float(image.size[0]))
        # 0.075
        hsize = int((float(image.size[1]) * float(wpercent)))
        #
        img1 = image.resize((base_width, hsize), Image.Resampling.LANCZOS)
        img1.save('show_img.png', format='PNG')
        # img.config(file=f'show_img.png')
        # start_button.config(text='Add watermark', command=add_watermark)
        window.destroy()
        time.sleep(1)
        import page1

#
# def add_watermark():
#     with open('file_path.txt') as file:
#         file_name = file.read()
#
#     # watermark
#     img2 = Image.open(file_name)
#     draw = ImageDraw.Draw(img2)
#
#     w, h = img2.size
#     x, y = int(w / 2), int(h / 2)
#
#     if x > y:
#         font_size = y
#     elif y > x:
#         font_size = x
#     else:
#         font_size = x
#
#     font = ImageFont.truetype('arial.ttf', int(font_size/6))
#
#     # add watermark+
#     draw.text((w, h), 'Watermark', fill=(255, 255, 255), font=font, anchor='ms')
#     img2.save(f'saved_image.{extension}')
#
#     base_width = 400
#     image = Image.open(f'saved_image.{extension}')
#     wpercent = (base_width / float(image.size[0]))
#     hsize = int((float(image.size[1]) * float(wpercent)))
#     img1 = image.resize((base_width, hsize), Image.Resampling.LANCZOS)
#     img1.save('watermark_show.png', format='PNG')
#     # img.config(file=f'watermark_show.png')
#
#     start_button.config(text='Save Image', command=save_file)
#
#     print('watermark added')
#
#
# def save_file():
#     files = [('All Files', '*'),
#              ('PNG File', '.png'),
#              ('JPG File', '.jpg')]
#
#     image = Image.open(f'saved_image.{extension}')
#     file = asksaveasfile(defaultextension=f'.{extension}', filetypes=files)
#
#     if file is None:
#         return
#
#     elif file:
#         abs_path = os.path.abspath(file.name)
#         # out = Image.alpha_composite(image)
#         image.save(abs_path)
#
#     print("file saved")


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
