# import tkinter as tk

# from PIL import Image, ImageSequence, ImageTk


# class AssistanGui:
#     def __init__(self, root):
#         self.root = root

#     def setup(
#         self,
#         title: str,
#         width: str,
#         height: str,
#         bg_color: str,
#         borderless: bool = False,
#         on_top: bool = False,
#     ):
#         self.root.title(title)
#         self.root.geometry(width + "x" + height)
#         self.root.overrideredirect(borderless)
#         self.root.configure(bg=bg_color)
#         self.root.wm_attributes("-topmost", on_top)

#         self.canvas = tk.Canvas(
#             self.root, width=width, height=height, highlightthickness=0
#         )
#         self.canvas.pack(expand=True, fill="both")

#         self.gif = Image.open("example.gif")
#         self.size_frame = (int(width), int(height))
#         self.frames = [
#             ImageTk.PhotoImage(
#                 img.resize(self.size_frame, Image.LANCZOS).convert("RGBA")
#             )
#             for img in ImageSequence.Iterator(self.gif)
#         ]
#         self.gif_index = 0
#         self.image = self.canvas.create_image(0, 0, image=self.frames[0], anchor="nw")
#         self.animate()

#         self.chat = tk.Text(
#             self.root,

#         )

#     def animate(self):
#         self.canvas.itemconfig(self.image, image=self.frames[self.gif_index])
#         self.gif_index = (self.gif_index + 1) % len(self.frames)
#         self.root.after(100, self.animate)
