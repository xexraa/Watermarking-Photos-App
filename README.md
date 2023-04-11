# Watermarking Photos App

## The application has two possibilities of use

The exe file is a ready-to-use product, just download and install it on your computer to enjoy the program, or alternatively, you can download the classic Python scripts and use them in your interpreter.
More information below.

## Brief description of the program:

If you often need to sign your work or photos and would like to do it quickly without using professional programs, try my app! It allows you to sign an image anywhere you want and also has more options that I will describe below.

# Installation options

## First "exe"

- Download the file "WatermarkingPhotosApp_WINDOWS_1.5_setup.exe"
- During installation, you will be prompted for standard options like creating a shortcut and selecting a save path.
- And that's all to enjoy the app.

## Second "scripts"

To use the Python scripts, simply download them. The "requirements.txt" file contains all the necessary libraries. You can adjust the parameters in the "config.ini" file.

# Full program description

During the first use, the program looks like this: 
![start](https://user-images.githubusercontent.com/121942715/231084276-11bb58a7-18b1-46df-869a-102f404281df.png)

After launching the program, all options are locked. We need to load the image first by clicking the Select Image button and choosing it from the disk.

## After launch

![opis](https://user-images.githubusercontent.com/121942715/231084910-fb24b2a1-b0fb-4775-a86b-668fa6157be3.png)

After loading the image, we have many options on the right side:

Default Save: saves with a standard name.
Save As: allows us to choose the name and location of the saved file.
Try it out: shows us how our current settings will look on the image.
Clear photo: restores the original state of the image.
Enter your signature: the place where we input our signature.
Quit: closes the program.

On the left side, we have:

X-AXIS: horizontal axis.
Y-AXIS: vertical axis.
Font Blur: blurs our signature (min 0, max 255).
Font Size: the size of our signature.
Choose font color: a menu where we can choose the color of our signature.

![podpis](https://user-images.githubusercontent.com/121942715/231087395-0e7ab6c9-6856-46d4-9ccf-b6b8e7046de1.png)

In the center, we have a preview of our loaded image. It is resized to 640x640, so please note that there may be a small difference in the position and appearance of the signature, especially with large images.

## Color option

![kolor](https://user-images.githubusercontent.com/121942715/231087588-af331469-fe3f-4dc1-91a9-4d67d774f321.png)

After clicking Choose font color, the entire color selection menu will open, and we can choose a color according to our needs and preferences. It should be remembered that after restarting the program, the color will return to default values (125, 125, 125), but it can be changed, as I will explain in the next section.

## Default settings

![settings](https://user-images.githubusercontent.com/121942715/231088829-a7ff4474-4ddf-47a7-ad5f-9343704ef2e9.png)

In the config.ini file, we have the ability to set several default settings:

FONT: the default font of the program.
IMAGE_FONT: the font that the signature will use. It is important to use fonts that are currently installed on our system.
IMAGE_BLUR_FONT: the blur of the signature.
IMAGE_FONT_COLOR: the color of the signature.
IMAGE_FONT_SIZE: the size of the signature.
POSITION_X: the position of the signature on the X-axis.
POSITION_Y: the position of the signature on the Y-axis.
DEFAULT_FILE_NAME: the default file name. It is important not to change the folder in which the file is to be saved ("photos/"), as this may cause problems with saving.
BG_COLOR: the background color of our program. We can set it to our liking.

## In addition

The program does not modify the original photo in any way. When saving, it creates a new file.

## What sources did I use?

**Python:**

- Pillow
- tkinter

**Programs:**

- GIT
- VSC
