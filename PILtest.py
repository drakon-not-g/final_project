from PIL import Image, ImageDraw, ImageFont
image = Image.open('C://Users\\Student\\Documents\\final_project\\static\\img\\2.jpg')
print(image)
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)

(x, y) = (50, 50)
text_color = 'rgb(0, 255, 0)'

draw.text((x, y), 'Bye World!', fill=text_color, font=font)

image.save('image2_with_text.jpg')