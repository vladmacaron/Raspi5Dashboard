import sys
import os
import logging
import time
assets = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
from PIL import Image, ImageDraw, ImageFont, ImageOps
from lib import epd2in7_V2

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

logging.basicConfig(level=logging.DEBUG)

try:
    def transparent_to_white(path):
        orig = Image.open(path).convert("RGBA")
        copy = Image.new("RGB", orig.size, "WHITE")
        copy.paste(orig, (0, 0), mask=orig) 
        return(copy)

    def draw_weather(icon_name, temperature, feels_like, forecast):
        epd = epd2in7_V2.EPD()
        epd.init()
        epd.Clear()
        
        font_normal = ImageFont.truetype(os.path.join(assets, 'Roboto-Regular.ttf'), 19)
        font_small = ImageFont.truetype(os.path.join(assets, 'Roboto-Regular.ttf'), 15)
        
        weather_image = Image.new('1', (epd.height, epd.width), 255)
        draw = ImageDraw.Draw(weather_image)
        
        icon = transparent_to_white(os.path.join(assets, icon_name))
        weather_image.paste(icon, (0,0))

        draw.text((0,50), str(temperature)+'°C (FL: '+str(feels_like)+'°C)', font=font_normal, fill=0)
        draw.text((55,0), 'Next 3 hours:', font=font_small, fill=0) 
        draw.text((55,20), forecast, font=font_normal, fill=0) 
        
        weather_image = weather_image.rotate(180)
        epd.display(epd.getbuffer(weather_image))
    
    #def draw_weather_info(temperature):
        


except IOError as e:
    logging.info(e)