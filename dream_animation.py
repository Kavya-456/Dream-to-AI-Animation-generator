from PIL import Image, ImageDraw
import os
import textwrap

# Create frames folder
os.makedirs("frames", exist_ok=True)

# Input
dream_text = input("Enter your dream or imagination: ")

width, height = 600, 400
frames = []

# Create animation frames
for i in range(8):
    img = Image.new("RGB", (width, height), (30, 40 + i*15, 80 + i*10))
    draw = ImageDraw.Draw(img)

    wrapped_text = textwrap.fill(dream_text, width=28)

    # Moving text effect
    draw.text(
        (40 + i*10, 160),
        wrapped_text,
        fill=(255, 255, 255)
    )

    frame_path = f"frames/frame_{i}.png"
    img.save(frame_path)
    frames.append(img)

print("✅ Frames created")

# Save as GIF
gif_path = "dream_animation.gif"
frames[0].save(
    gif_path,
    save_all=True,
    append_images=frames[1:],
    duration=400,
    loop=0
)

print("🎉 GIF animation created:", gif_path)