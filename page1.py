import os.path
from tkinter import *
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageFont, ImageDraw
from tkinter import colorchooser

color_code = '#ffffff'
extension = 'png'
x_position = 500
y_position = 150

try:
    with open('file_path.txt') as file1:
        file_name1 = file1.read()

    original_img1 = Image.open(file_name1)
except FileNotFoundError:
    pass


def choose_color():
    global color_code
    try:
        color_code = colorchooser.askcolor(title="Choose color")[1]
        add_watermark()
    except ValueError:
        pass


def down_key(*args):
    global y_position
    if original_img1.size[1] > 2000:
        y_position -= 100

    y_position -= 15
    add_watermark()


def up_key(event):
    global y_position
    if original_img1.size[1] > 2000:
        y_position += 100
    y_position += 15
    add_watermark()


def left_key(event):
    global x_position
    if original_img1.size[0] > 2000:
        x_position -= 100
    x_position -= 15
    add_watermark()


def right_key(event):
    global x_position
    if original_img1.size[0] > 2000:
        x_position += 100
    x_position += 15
    add_watermark()


def add_watermark():
    global extension, x_position, y_position
    with open('file_path.txt') as file:
        file_name = file.read()

    extension = file_name.split('/')[-1].split('.')[-1]

    # watermark
    original_img = Image.open(file_name)

    w, h = original_img.size
    x, y = int(w / 2), int(h / 2)

    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    watermark_font = ImageFont.truetype('Product Sans Regular.ttf', int(font_size / 6))
    draw = ImageDraw.Draw(original_img)

    # add watermark
    draw.text((x_position, h - y_position), text=str(watermark_entry.get()), fill=str(color_code),
              font=watermark_font,
              anchor='ms', align='left')
    original_img.save(f'saved_image.{extension}')

    base_width = 350
    image = Image.open(f'saved_image.{extension}')
    w_percent = (base_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(w_percent)))
    img1 = image.resize((base_width, hsize), Image.Resampling.LANCZOS)
    img1.save('watermark_show.png', format='PNG')

    uploaded_img.config(file='watermark_show.png')
    save_file_btn.config(state='normal')


def save_file():
    files = [('All Files', '*'),
             ('PNG File', '.png'),
             ('JPG File', '.jpg')]

    image = Image.open(f'saved_image.{extension}')
    file = asksaveasfile(defaultextension=f'.{extension}', filetypes=files)

    if file is None:
        return

    elif file:
        abs_path = os.path.abspath(file.name)
        # out = Image.alpha_composite(image)
        image.save(abs_path)


window = Tk()
window.title("Image Watermark")
window.minsize(width=775, height=485)
window.config(background='#ffffff')

window.bind('<Down>', down_key)
window.bind('<Up>', up_key)
window.bind('<Left>', left_key)
window.bind('<Right>', right_key)
# window.bind('<Ctrl> + s', save)

canvas1 = Canvas(width=775, height=122, highlightthickness=0, background='#ffffff')

title = PhotoImage(file='assets/Asset 3title.png')
canvas1.create_image(387.5, 58, image=title)

canvas1.grid(row=0, column=0, columnspan=2)
text = Label(text='Image Preview:', font=('Product Sans', 15, 'normal'), background='#ffffff')
text.grid(row=1, column=0, sticky=SW, padx=20)
canvas2 = Canvas(width=350, height=480, highlightthickness=0, background="#ffffff")

uploaded_img = PhotoImage(file='show_img.png')
canvas2.create_image(175, 240, image=uploaded_img)

canvas2.grid(row=2, rowspan=5, column=0)

watermark_label = Label(text='Watermark:', font=('Product Sans', 12, 'normal'), background="#ffffff")
watermark_label.grid(row=1, column=1, sticky=NW)

watermark_entry = Entry(width=50, background='#f2f2f2')
watermark_entry.focus()
watermark_entry.grid(row=2, column=1, sticky=NW, pady=5)

watermark_label = Label(text='Text Color:', font=('Product Sans', 12, 'normal'), background="#ffffff")
watermark_label.grid(row=4, column=1, sticky=NW)

# font_color = OptionMenu(window, color_clicked, *color_options)

font_color = Button(width=12, text="Select Color", font=('Product Sans', 11, "normal"), command=choose_color,
                    background='#ffd418', foreground='#000000', disabledforeground='#919191', relief='flat',
                    overrelief='flat', state='normal')

font_color.grid(row=5, column=1, sticky=NW, pady=10)

canvas3 = Canvas(width=300, height=280, background='#ffffff', highlightthickness=0)
canvas3.grid(row=6, column=1, sticky=NW)

add_watermark_btn = Button(width=16, text="Add Watermark", font=('Product Sans', 13, "bold"), background='#ffd418',
                           foreground='#000000', disabledforeground='#919191', relief='flat', overrelief='flat',
                           command=add_watermark, state='normal')

add_watermark_btn.grid(row=7, column=0, pady=20, sticky=N)

save_file_btn = Button(width=16, text='Save File', font=('Product Sans', 13, 'bold'), background='#ffd418',
                       foreground='#000000', disabledforeground='#919191', relief='flat', overrelief='flat',
                       command=save_file, state='disabled')

save_file_btn.grid(row=7, column=1, pady=20, sticky=N)

window.mainloop()
