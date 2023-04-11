import os
import tkinter as tk
import tkinter.colorchooser as colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
from config import FONT, IMAGE_FONT, IMAGE_BLUR_FONT, IMAGE_FONT_COLOR, IMAGE_FONT_SIZE, POSITION_X, POSITION_Y, DEFAULT_FILE_NAME, BG_COLOR


class ImageUploader(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("1400x800")
        self.master.minsize(1400, 800)
        self.master.maxsize(1400, 800)
        self.master.title("Image Watermarking Desktop App")
        self.master.iconbitmap('assets/icon.ico')
        self.pack_propagate(0)
        self.grid(pady=50, padx=50)
        self.master.configure(background=BG_COLOR)
        self.settings()
        self.create_widgets()
        

    def create_widgets(self):
        # -------------- LOADING ASSETS -------------- #
        
        self.blue_btn = tk.PhotoImage(file="assets/bluebtn.png")
        self.greenbtn_save_as = tk.PhotoImage(file="assets/greenbtn_save_as.png")
        self.greenbtn_save = tk.PhotoImage(file="assets/greenbtn_save.png")
        self.grey_btn = tk.PhotoImage(file="assets/greybtn.png")
        self.light_greenbtn = tk.PhotoImage(file="assets/light_greenbtn.png")
        self.orange_btn = tk.PhotoImage(file="assets/orangebtn.png")
        self.red_btn = tk.PhotoImage(file="assets/redbtn.png")
        self.purple_btn = tk.PhotoImage(file="assets/purplebtn.png")
        
        
        # -------------- STYLING -------------- #
        
        self.configure(bg=BG_COLOR)
        
        settings_for_1st_col = {
            "width": 0,
            "bg": BG_COLOR,
            "foreground": "white",
            "font": (FONT, 20)
        }
        
        settings_for_photo_btn = {
            "borderwidth": 0,
            "bg": BG_COLOR,
            "activebackground": BG_COLOR
        }
        
        paddings = {
            "padx": 5,
            "pady": 5,
        }
        
        
        # -------------- LEFT SITE -------------- #
        
        self.x_axis_label = tk.Label(self, text="X-AXIS: ", **settings_for_1st_col)
        self.x_axis_label.grid(column=0, row=1, **paddings)
        self.x_axis_entry = tk.Entry(self, textvariable=self.position_x, **settings_for_1st_col, state="disabled")
        self.x_axis_entry.grid(column=1, row=1, **paddings)
        
        self.y_axis_label = tk.Label(self, text="Y-AXIS: ", **settings_for_1st_col)
        self.y_axis_label.grid(column=0, row=2, **paddings)
        self.y_axis_entry = tk.Entry(self, textvariable=self.position_y, **settings_for_1st_col, state="disabled")
        self.y_axis_entry.grid(column=1, row=2, **paddings)
        
        self.blur_font_label = tk.Label(self, text="Font Blur: ", **settings_for_1st_col)
        self.blur_font_label.grid(column=0, row=3, **paddings)
        self.blur_font_scale = tk.Scale(self, variable=self.image_blur_font, from_=0, to=255, orient=tk.HORIZONTAL, resolution=1, font=(FONT, 20), bg=BG_COLOR, foreground="white", state="disabled")       
        self.blur_font_scale.grid(column=1, row=3, **paddings)
        
        self.font_size_label = tk.Label(self, text="Font Size: ", **settings_for_1st_col)
        self.font_size_label.grid(column=0, row=4, **paddings)
        self.font_size_entry = tk.Entry(self, textvariable=self.image_font_size, **settings_for_1st_col, state="disabled")
        self.font_size_entry.grid(column=1, row=4, **paddings)
        
        self.color_button = tk.Button(self, image=self.grey_btn, state="disabled", command=self.choose_font_color, **settings_for_photo_btn)
        self.color_button.grid(column=0, row=5, columnspan=2, **paddings)
        
        
        # -------------- RIGHT SITE -------------- #
        
        self.select_button = tk.Button(self, image=self.blue_btn, command=self.select_image, **settings_for_photo_btn)
        self.select_button.grid(column=3, row=0, **paddings)

        self.watermark_button_default = tk.Button(self, image=self.grey_btn, state="disabled", command=self.watermarking_image_default_save, **settings_for_photo_btn)
        self.watermark_button_default .grid(column=3, row=1, **paddings)

        self.watermark_button_save_as = tk.Button(self, image=self.grey_btn, state="disabled", command=self.save_as_dialog, **settings_for_photo_btn)
        self.watermark_button_save_as .grid(column=3, row=2, **paddings)
        
        self.try_watermark_button = tk.Button(self, image=self.grey_btn, state="disabled", command=self.try_watermark, **settings_for_photo_btn)
        self.try_watermark_button .grid(column=3, row=3, **paddings)
        
        self.clear_button = tk.Button(self, image=self.grey_btn, state="disabled", command=self.clear_image, **settings_for_photo_btn)
        self.clear_button .grid(column=3, row=4, **paddings)

        self.name_label = tk.Label(self, text="Enter your signature:", font=(FONT, 18, 'normal'), bg=BG_COLOR)
        self.name_label.grid(column=3, row=5)
        self.name_entry = tk.Entry(self, width=20, font=(FONT, 18, 'normal'))
        self.name_entry.grid(column=3, row=6, **paddings)
        self.name_entry.focus()
       
        self.quit_button = tk.Button(self, image=self.red_btn, borderwidth=0, bg=BG_COLOR, activebackground=BG_COLOR, command=self.master.destroy)
        self.quit_button.grid(column=3, row=7, **paddings)
        
        
        
        # -------------- CANVAS -------------- #
        
        self.canvas = tk.Canvas(self, width=640, height=640, bg="white", bd=0, highlightthickness=0)
        self.canvas.create_rectangle(2, 2, 638, 638, dash=(4, 2))    
        self.canvas.create_text(319, 319, text="Select image to start.", font=(FONT, 30), anchor='center')   
        self.canvas.grid(column=2, rowspan=8, row=0, padx=20, pady=20)
 
       
    def choose_font_color(self):
        new_color = colorchooser.askcolor(title="Choose font color", color=self.image_font_color)
        if new_color:
            self.image_font_color = new_color[0]    

        
    def settings(self):
        self.position_x = tk.IntVar()
        self.position_x.set(POSITION_X)
        self.position_y = tk.IntVar()
        self.position_y.set(POSITION_Y)       
        self.image_blur_font = tk.IntVar()
        self.image_blur_font.set(IMAGE_BLUR_FONT)        
        self.image_font_color = IMAGE_FONT_COLOR
        self.image_font_size = tk.IntVar()
        self.image_font_size.set(IMAGE_FONT_SIZE)
        

    def select_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.watermark_button_default.configure(state="normal", image=self.greenbtn_save)
            self.watermark_button_save_as.configure(state="normal", image=self.greenbtn_save_as)
            self.try_watermark_button.configure(state="normal", image=self.light_greenbtn)
            self.clear_button.configure(state="normal", image=self.orange_btn)
            self.color_button.configure(state="normal", image=self.purple_btn)
            
            self.x_axis_entry.configure(state="normal")
            self.y_axis_entry.configure(state="normal")
            self.blur_font_scale.configure(state="normal")
            self.font_size_entry.configure(state="normal")
            
            self.image_file = open(file_path, 'rb')
            self.image = Image.open(self.image_file)
            self.image = self.image.resize((640, 640), Image.LANCZOS)
            
            # ----- Set default canvas ----- #
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas_bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.canvas.image = self.photo
    
        
    def try_watermark(self):
        # -------------- COPY OF IMAGE -------------- #
        # ----- Load variables ----- #
        x_axis = int(self.x_axis_entry.get())
        y_axis = int(self.y_axis_entry.get())
        font_blur = int(self.blur_font_scale.get())
        font_color = self.image_font_color + (font_blur,)
        font_size =int(self.image_font_size.get())
        
        # ----- Resized copy of the image ----- #
        image_copy = self.image
        watermark = Image.new("RGBA", image_copy.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark)
        watermark_text = self.name_entry.get()
        font = ImageFont.truetype(IMAGE_FONT, int(font_size / 2))
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        x = image_copy.width - text_width - x_axis
        y = image_copy.height - text_height - y_axis
        
        draw.text((x, y), watermark_text, font=font, fill=font_color)
        
        watermarked_image = Image.alpha_composite(image_copy.convert("RGBA"), watermark)
        
        # ----- Image to canvas ----- #
        photo_watermarked = ImageTk.PhotoImage(watermarked_image)
        self.canvas.itemconfig(self.canvas_bg, image=photo_watermarked)
        self.canvas.image = photo_watermarked
        
        
    def clear_image(self):
        self.canvas.itemconfig(self.canvas_bg, image=self.photo)
        self.canvas.image = self.photo


    def watermarking_image(self, file_path=None):
        # ----- Load variables ----- #
        x_axis = int(self.x_axis_entry.get())
        y_axis = int(self.y_axis_entry.get())
        font_blur = int(self.blur_font_scale.get())
        font_color = self.image_font_color + (font_blur,)
        font_size =int(self.image_font_size.get())
        
        # ----- Watermarking original photo ----- #
        image = Image.open(self.image_file)
        watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark)
        watermark_text = self.name_entry.get()

        font = ImageFont.truetype(IMAGE_FONT, font_size)
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        x = image.width - text_width - x_axis
        y = image.height - text_height - y_axis

        draw.text((x, y), watermark_text, font=font, fill=font_color)

        self.watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark)
        self.watermarked_image = self.watermarked_image.convert('RGB')

        # ----- Save in to file ----- #
        if file_path:
            self.watermarked_image.save(file_path)
        else:
            if not os.path.exists('photos'):
                os.makedirs('photos')
            counter = 0
            filename = DEFAULT_FILE_NAME
            while os.path.exists(filename):
                counter += 1
                filename = f"photos/watermarked_image_{counter}.jpg"
            self.watermarked_image.save(filename)

        tk.messagebox.showinfo("Watermarking successful",
                               "Image watermarked successfully!")


    def save_as_dialog(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[
                                                 ('JPEG', '*.jpg'), ('PNG', '*.png')])
        if file_path:
            self.watermarking_image(file_path)


    def watermarking_image_default_save(self):
        self.watermarking_image()


root = tk.Tk()
app = ImageUploader(master=root)
if __name__ == '__main__':
    app.mainloop()
