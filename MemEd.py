# importing the tkinter module and PIL
# that is pillow module
from tkinter import *
from PIL import ImageTk, Image


def forward(i):
	i += 1
	#num = len(List_images)
	#if i > num - 1:
	if i > 4 - 1:
		i = 0
	Inner(i)

def back(i):
	i -= 1
	#num = len(List_images)
	if i < 0:
		#i = num - 1
		i = 4 - 1
	Inner(i)


def Inner(i):
	label = Label(image=List_images[i])
	label.grid(row=1, column=0, columnspan=3)

	#lambda i: i += 1
	button_forward = Button(root, text="Forward", command=lambda: forward(i))


	button_back = Button(root, text="Back", command=lambda: back(i))


	button_exit = Button(root, text="Exit",
					command=root.quit)

	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_forward.grid(row=5, column=2)



if __name__ == "__main__":

	i = 0
	# Calling the Tk (The intial constructor of tkinter)
	root = Tk()

	# We will make the title of our app as Image Viewer
	root.title("Image Viewer")

	# The geometry of the box which will be displayed
	root.geometry("500x538")

	# Taking images using the pillow module which has a class ImageTk
	image_no_1 = ImageTk.PhotoImage(Image.open("img/1.png"))
	image_no_2 = ImageTk.PhotoImage(Image.open("img/2.png"))
	image_no_3 = ImageTk.PhotoImage(Image.open("img/3.png"))
	image_no_4 = ImageTk.PhotoImage(Image.open("img/4.png"))

	List_images = [image_no_1, image_no_2, image_no_3, image_no_4]

	Inner(i)

	root.mainloop()




"""
def forward_1(img_no):

	# GLobal variable so that we can have
	# access and change the variable
	# whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	# This is for clearing the screen so that
	# our next image can pop up
	label = Label(image=List_images[img_no+1])

	# as the list starts from 0 so we are
	# subtracting one
	label.grid(row=1, column=0, columnspan=3)
	button_for = Button(root, text="forward",
						command=lambda: forward(img_no+1))

	# img_no+1 as we want the next image to pop up
	if img_no == 3:
		button_for = Button(root, text="Forward",
								state=DISABLED)

	# img_no-1 as we want previous image when we click
	# back button
	button_back = Button(root, text="Back",
						command=lambda: back(img_no-1))

	# Placing the button in new grid
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)



def back_1(img_no):

	# We will have global variable to access these
	# variable and change whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	# for clearing the image for new image to pop up
	label = Label(image=List_images[img_no - 1])
	label.grid(row=1, column=0, columnspan=3)
	button_forward = Button(root, text="forward",
							command=lambda: forward(img_no + 1))
	button_back = Button(root, text="Back",
						command=lambda: back(img_no - 1))
	print(img_no)

	# whenever the first image will be there we will
	# have the back button disabled
	if img_no == 1:
		button_back = Button(root, Text="Back", state=DISABLED)

	label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)
"""


