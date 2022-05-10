
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import json
import sys
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from PIL import ImageTk, Image



def scapedData(target):
    with open(f'{target}/Details.json') as f:
      data_j = json.load(f)
    line_1 = ''
    line_2 = ''
    line_3 = ''
    final_list= lambda test_list, x: [test_list[i:i+x] for i in range(0, len(test_list), x)]
    output=final_list(data_j[4]['bio'], 3)
    for item in output[0]:
      line_1 = line_1 + ' ' + item + ' '
    for item in output[1]:
      line_2 = line_2 + ' ' + item + ' '
    for item in output[2]:
      line_3 = line_3 + ' ' + item + ' '
    Details = [data_j[0]['Name'],data_j[1]['following'],data_j[2]['posts'],data_j[3]['followers'],line_1,line_2,line_3]
    return Details

def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    return ASSETS_PATH / Path(path)


def relative_to_assets_profile(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/profile")
    return ASSETS_PATH / Path(path)

def relative_to_target_pictures(target,path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(f"./{target}")
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x600")
window.configure(bg = "#FFFFFF")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
window.wm_iconphoto(False, image_image_2)
window.title('Golden Bird')

canvas = Canvas(
    window,
    bg = "#111645",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)



target = sys.argv[1]

image_image_1_profile = PhotoImage(file=relative_to_assets_profile("image_1.png"))
image_image_2_profile = PhotoImage(file=relative_to_assets_profile("image_2.png"))
button_image_1_profile = PhotoImage(file=relative_to_assets_profile("button_1.png"))
path_logo = target+ "\\" + target + "0.jpg"
path_pic_1 = target+ "\\" + target + "3.jpg"
path_pic_2 = target+ "\\" + target + "4.jpg"
path_pic_3 = target+ "\\" + target + "5.jpg"

print(path_logo)


img = ImageTk.PhotoImage(Image.open(path_logo))
img_1 = Image.open(path_pic_1)
img_2 = Image.open(path_pic_2)
img_3 = Image.open(path_pic_3)

img_1 = img_1.resize((198, 191))
img_1 = ImageTk.PhotoImage(img_1)
img_2 = img_2.resize((198, 191))
img_2 = ImageTk.PhotoImage(img_2)
img_3 = img_3.resize((198, 191))
img_3 = ImageTk.PhotoImage(img_3)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    823.0,
    600.0,
    fill="#111645",
    outline="")


image_1 = canvas.create_image(
    400.0,
    300.0,
    image=image_image_1_profile
)

canvas.create_text(
    298.0,
    135.0,
    anchor="nw",
    text="Bio",
    fill="#C4C4C4",
    font=("InriaSans Regular", 20 * -1)
)


image_2 = canvas.create_image(
    744.0,
    59.0,
    image=image_image_2_profile
)
    # picture_1


image_n_1 = canvas.create_image(
    170.0,
    437.0,
    image=img_1)




# picture_2


image_n_2 = canvas.create_image(
    380.0,
    437.0,
    image=img_2)

# picture_3


image_n_3 = canvas.create_image(
    590.0,
    437.0,
    image=img_3)



# profile pic
image_propic = canvas.create_image(
    163.0,
    127.0,
    image=img
)


canvas.create_text(
    162.0,
    250.0,
    anchor="nw",
    text="Followers",
    fill="#C4C4C4",
    font=("InriaSans Regular", 20 * -1)
)
# Target name
name = canvas.create_text(
    279.0,
    95.0,
    anchor="nw",
    text="Target name : " ,
    fill="#C4C4C4",
    font=("InriaSans Regular", 20 * -1)
)

# Numbers of Followers
followers = canvas.create_text(
    190.0,
    286.0,
    anchor="nw",
    text="",
    fill="#C4C4C4",
    font=("InriaSans Regular", 20 * -1)
)

# Number of Following
following = canvas.create_text(
    353.0,
    286.0,
    anchor="nw",
    text="",
    fill="#C4C4C4",
    font=("InriaSans Regular", 20 * -1)
)

# Number of posts
posts =canvas.create_text(
    500.0,
    286.0,
    anchor="nw",
    text="",
    fill="#C4C4C4",
    font=("InriaSans Regular", 20 * -1)
)

# Bio lines
line_1 = canvas.create_text(
    324.0,
    151.0,
    anchor="nw",
    text="Line 1",
    fill="#C4C4C4",
    font=("InriaSans Regular", 15 * -1)
)


line_2 = canvas.create_text(
    324.0,
    173.0,
    anchor="nw",
    text="Line 2",
    fill="#C4C4C4",
    font=("InriaSans Regular", 15 * -1)
)


line_3 = canvas.create_text(
    324.0,
    197.0,
    anchor="nw",
    text="Line 3",
    fill="#C4C4C4",
    font=("InriaSans Regular", 15 * -1)
)


data = scapedData(target)


#blankDetailFiller(canvas,data[0],data[3],data[1],data[2])
canvas.itemconfig(name, text=data[0])
canvas.itemconfig(followers, text=data[3])
canvas.itemconfig(following, text=data[1])
canvas.itemconfig(posts, text=data[2])
canvas.itemconfig(line_1, text=data[4])
canvas.itemconfig(line_2, text=data[5])
canvas.itemconfig(line_3, text=data[6])


canvas.create_text(
    324.0,
    249.0,
    anchor="nw",
    text="Following",
    fill="#C4C4C4",
    font=("InriaSans Regular", 20 * -1)
)

canvas.create_text(
    494.0,
    249.0,
    anchor="nw",
    text="Post",
    fill="#C4C4C4",
    font=("InriaSans Regular", 20 * -1)
)







button_1 = Button(
    image=button_image_1_profile,
    bg="#111645",
    activebackground = '#111645',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=629.0,
    y=551.0,
    width=78.0,
    height=29.0
)

window.resizable(False, False)
window.mainloop()
'''canvas.create_text(
                322.0,
                400.0,
                anchor="nw",
                text="If nothing there",
                fill="#000000",
                font=("InriaSans Regular", 24 * -1)
            )
        '''
window.resizable(False, False)
window.mainloop()

