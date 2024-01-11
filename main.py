import LCD_1in44
import time
import socket
import math
from PIL import Image,ImageDraw,ImageFont,ImageColor
import subprocess as sp
from datetime import datetime


def get_ip_address():
    try:
        # Bir socket nesnesi oluşturun ve özel bir bağlantı noktasına bağlanın
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print("IP adresi alınamadı:", str(e))
        return None

def main():
    LCD = LCD_1in44.LCD()
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()
    a=0
    while a==0:
         image = Image.open('shark/1.bmp')
         LCD.LCD_ShowImage(image,0,0)
         time.sleep(0.2)
         image = Image.open('shark/2.bmp')
         LCD.LCD_ShowImage(image,0,0)
         time.sleep(0.2)
         image = Image.open('shark/3.bmp')
         LCD.LCD_ShowImage(image,0,0)
         time.sleep(0.2)
         image = Image.open('shark/4.bmp')
         LCD.LCD_ShowImage(image,0,0)
         time.sleep(0.2)
         image = Image.open('shark/5.bmp')
         LCD.LCD_ShowImage(image,0,0)
         time.sleep(0.2)
         image = Image.open('shark/6.bmp')
         LCD.LCD_ShowImage(image,0,0)
         time.sleep(1)
         image = Image.open('shark/6.bmp')
         LCD.LCD_ShowImage(image,0,0)
         time.sleep(1)
         a+=1
#       while (True):
def azat():

###############################################################################################################
#                                         KOMUT ALANI

    def komut():
        alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        komut = ""
        indexsayi = 0

        while True:
             print(komut)
             image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
             draw = ImageDraw.Draw(image)
             draw.rectangle([(18, 10), (110, 20)], fill="RED")
             draw.rectangle([(18, 30), (110, 40)], fill="RED")
             draw.rectangle([(18, 50), (110, 60)], fill="RED")
             draw.text((18, 10), " Komut Giriniz", fill="BLACK")
             draw.text((18, 30), komut, fill="BLACK")
             draw.text((18, 50), f'       {alfabe[indexsayi]}', fill="BLACK")  # Display the current letter

             if LCD.digital_read(LCD.GPIO_KEY_UP_PIN) == 0:  # button is released
                print("")
             else:  # button is pressed:
                print(index)
                indexsayi += 1
             if LCD.digital_read(LCD.GPIO_KEY_DOWN_PIN) == 0:  # button is released
                print("")
             else:  # button is pressed:
                 print(index)
                 indexsayi -= 1
             if LCD.digital_read(LCD.GPIO_KEY1_PIN) == 0:  # button is released
                print("a")
             else:  # button is pressed:
                if 0 <= indexsayi < len(alfabe):
                    komut = komut + alfabe[indexsayi]


             if LCD.digital_read(LCD.GPIO_KEY_PRESS_PIN) == 0: # button is released
               print("")
             else: # button is pressed:
                 break

             if LCD.digital_read(LCD.GPIO_KEY2_PIN) == 0:  # button is released
                print("")
             else:  # button is pressed:
                try:
                  result = sp.run([komut], capture_output=True, text=True, shell=True)
                  if result.returncode == 0:
                     output_text = result.stdout
                  else:
                      output_text = f"Hata: {result.stderr}"
                except Exception as e:
                  output_text = f"Hata: {str(e)}"

                draw.text((18, 70), output_text, fill="BLACK")

             if LCD.digital_read(LCD.GPIO_KEY3_PIN) == 0:  # button is released
               print("")
             else:  # button is pressed:
                komut = komut[:-1]  # Remove the last character
             LCD.LCD_ShowImage(image, 0, 0)

#=============================================================================================
#                                     KEY CONTROL ALANI

    def keycontrol():
         image = Image.new('RGB', (LCD.width, LCD.height))
         draw = ImageDraw.Draw(image)
         draw.rectangle((0,0,LCD.width,LCD.height), outline=0, fill=0)
         LCD.LCD_ShowImage(image,0,0)
         while True:
               if LCD.digital_read(LCD.GPIO_KEY_UP_PIN ) == 0: # button is released
                  draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0xff00)  #Up
               else: # button is pressed:
                  draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  #Up filled
                  print ("Up" )
               if LCD.digital_read(LCD.GPIO_KEY_LEFT_PIN) == 0: # button is released
                  draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0xff00)  #left
               else: # button is pressed:
                  draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  #left filled
                  print ("left")
               if LCD.digital_read(LCD.GPIO_KEY_RIGHT_PIN) == 0: # button is released
                  draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0xff00) #right
               else: # button is pressed:
                  draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0) #right filled
                  print ("right")
               if LCD.digital_read(LCD.GPIO_KEY_DOWN_PIN) == 0: # button is released
                  draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0xff00) #down
               else: # button is pressed:
                  draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0) #down filled
                  print ("down")
               if LCD.digital_read(LCD.GPIO_KEY_PRESS_PIN) == 0: # button is released
                  draw.rectangle((20, 22,40,40), outline=255, fill=0xff00) #center
               else: # button is pressed:
                  draw.rectangle((20, 22,40,40), outline=255, fill=0) #center filled
                  break
               if LCD.digital_read(LCD.GPIO_KEY1_PIN) == 0: # button is released
                  draw.ellipse((70,0,90,20), outline=255, fill=0xff00) #A button
               else: # button is pressed:
                  draw.ellipse((70,0,90,20), outline=255, fill=0) #A button filled
                  print ("KEY1")
               if LCD.digital_read(LCD.GPIO_KEY2_PIN) == 0: # button is released
                  draw.ellipse((100,20,120,40), outline=255, fill=0xff00) #B button]
               else: # button is pressed:
                  draw.ellipse((100,20,120,40), outline=255, fill=0) #B button filled
                  print ("KEY2")
               if LCD.digital_read(LCD.GPIO_KEY3_PIN) == 0: # button is released
                  draw.ellipse((70,40,90,60), outline=255, fill=0xff00) #A button
               else: # button is pressed:
                  draw.ellipse((70,40,90,60), outline=255, fill=0) #A button filled
                  print ("KEY3")

               LCD.LCD_ShowImage(image,0,0)




#########################################################################################
#                                   SAAT ALANI

    def draw_clock(draw, center_x, center_y, radius):
          draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), outline="WHITE")

          for i in range(12):
             angle = math.radians(i * 30)
             x1 = center_x + int(radius * 0.9 * math.cos(angle))
             y1 = center_y + int(radius * 0.9 * math.sin(angle))
             x2 = center_x + int(radius * math.cos(angle))
             y2 = center_y + int(radius * math.sin(angle))
             draw.line((x1, y1, x2, y2), fill="WHITE")

    def draw_clock_hands(draw, center_x, center_y, radius, hour, minute, second):
           hour_angle = math.radians((hour % 12) * 30 + minute / 60 * 30)
           minute_angle = math.radians(minute * 6 + second / 60 * 6)
           second_angle = math.radians(second * 6)

           draw.line((center_x, center_y, center_x + int(radius * 0.6 * math.cos(hour_angle)),
           center_y + int(radius * 0.6 * math.sin(hour_angle))), fill="WHITE", width=3)

           draw.line((center_x, center_y, center_x + int(radius * 0.8 * math.cos(minute_angle)),
           center_y + int(radius * 0.8 * math.sin(minute_angle))), fill="WHITE", width=2)

           draw.line((center_x, center_y, center_x + int(radius * 0.9 * math.cos(second_angle)),
           center_y + int(radius * 0.9 * math.sin(second_angle))), fill="RED", width=1)

    def display_analog_clock():

          while True:
               if LCD.digital_read(LCD.GPIO_KEY_PRESS_PIN) == 0: # button is released
                  print("")
               else: # button is pressed:
                  index=0
                  break
               image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
               draw = ImageDraw.Draw(image)

               current_time = datetime.now()
               hour = current_time.hour
               minute = current_time.minute
               second = current_time.second

               draw_clock(draw, LCD.width // 2, LCD.height // 2, min(LCD.width, LCD.height) // 2 - 5)
               draw_clock_hands(draw, LCD.width // 2, LCD.height // 2, min(LCD.width, LCD.height) // 2 - 5, hour, minute, second)

               LCD.LCD_ShowImage(image, 0, 0)
               time.sleep(1)  # Her saniyede bir güncelle























    LCD = LCD_1in44.LCD()
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    index = 0
    secenek = ["Komut","Key_Control","Saat",""]


    while True:
        ip_address = get_ip_address()
        if ip_address:
            image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
            print ("***draw line")
            #draw.line([(0,0),(127,0)], fill = "BLUE",width = 5)
            #draw.line([(127,0),(127,127)], fill = "BLUE",width = 5)
            #draw.line([(127,127),(0,127)], fill = "BLUE",width = 5)
            #draw.line([(0,127),(0,0)], fill = "BLUE",width = 5)
            print ("***draw rectangle")
            draw.rectangle([(18,10),(110,20)],fill = "RED")
            draw.rectangle([(18, 30), (110, 40)], fill="RED")
            draw.rectangle([(18, 50), (110, 60)], fill="RED")
            draw.rectangle([(18, 70), (110, 80)], fill="GREEN")
            #draw.rectangle([(28,21),(210,50)],fill = "BLUE")
            #I1 = ImageDraw.Draw(image)
            #I1.text((28, 36), "nice Car", fill=(255, 0, 0))
            draw.text((18,10) ," " +ip_address ,fill= "BLACK")
            draw.text((18,30),"   AZAT DICLE",fill="BLACK")
            draw.text((18,50),"      BETA",fill="BLACK")
            draw.text((18,70),secenek[index],fill="BLACK")
            # SAAT OLAYI
            #current_time = datetime.now().strftime("%H:%M:%S")
            #font = ImageFont.load_default()
            #text_color = "black"
            #draw.text((18, 70), f"Saat: {current_time}", font=font, fill=text_color)

            draw.text((18,90),"  MEGALODON-PI",fill="RED")

            print("IP Adresi:", ip_address)
            if index==3:
               index=0
            else:
               print("devam")

            #SAĞ SOL SECENEK KONTROLERİ
            if LCD.digital_read(LCD.GPIO_KEY_LEFT_PIN) == 0: # button is released
                print(index)
            else: # button is pressed:
                index-=1
                print(index)
            if LCD.digital_read(LCD.GPIO_KEY_RIGHT_PIN) == 0: # button is released
               print(index)
            else: # button is pressed:
                print(index)
                index+=1






            if LCD.digital_read(LCD.GPIO_KEY2_PIN) == 0: # button is released
                print("")
            else: # button is pressed: print ("KEY2")
               if index==0:
                  index=0
                  komut()
                  #display_analog_clock()
               elif index==1:
                  index=0
                  keycontrol()
               elif index==2:
                  index=0
                  display_analog_clock()
               else:
                  print("dd")

            if LCD.digital_read(LCD.GPIO_KEY_UP_PIN) == 0:
               print("Up")
            else:
                keyup()
            if LCD.digital_read(LCD.GPIO_KEY_DOWN_PIN) == 0:
               print("Down")
            else:
               keydown()
            LCD.LCD_ShowImage(image,0,0)
            def keyup():
              if LCD.digital_read(LCD.GPIO_KEY_UP_PIN) == 0:  # button is released
                 print("Up")
              else:
                  LCD.LCD_Clear()
                  image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
                  draw = ImageDraw.Draw(image)
                  font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
                  draw.line([(0, 0), (127, 0)], fill="BLUE", width=5)
                  draw.line([(127, 0), (127, 127)], fill="BLUE", width=5)
                  draw.line([(127, 127), (0, 127)], fill="BLUE", width=5)
                  draw.line([(0, 127), (0, 0)], fill="BLUE", width=5)
                  draw.rectangle([(18, 10), (110, 20)], fill="RED")
                  azat = ImageDraw.Draw(image)
                  azat.rectangle([(19, 20), (110, 50)], fill="BLUE")
                  draw.text((18, 10), 'AZAT DICLE', fill="BLACK")
                  LCD.LCD_ShowImage(image, 0, 0)
                  draw.rectangle([(10, 30), (80, 60)], fill="GREEN")
                  draw.text((10, 30), 'Merhaba', fill="WHITE")
                  LCD.LCD_ShowImage(image, 0, 0)
                  draw.rectangle([(20, 40), (90, 70)], fill="YELLOW")
                  draw.text((20, 40), 'Merhaba', fill="BLACK")
                  LCD.LCD_ShowImage(image, 0, 0)
                  draw.rectangle([(30, 50), (100, 80)], fill="ORANGE")
                  draw.text((30, 50), 'Merhaba', fill="WHITE")
                  LCD.LCD_ShowImage(image, 0, 0)
                  draw.rectangle([(40, 60), (110, 90)], fill="PURPLE")
                  draw.text((40, 60), 'Merhaba', fill="BLACK")
                  LCD.LCD_ShowImage(image, 0, 0)

              if LCD.digital_read(LCD.GPIO_KEY1_PIN) == 0:
                  print("d")
              else:
                 return
            def keydown():
               while True:
                    if LCD.digital_read(LCD.GPIO_KEY_DOWN_PIN) == 0:
                        image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
                        draw = ImageDraw.Draw(image)
                        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
                        print ("***draw line")
                        draw.rectangle([(18,10),(110,20)],fill = "RED")
                        draw.rectangle([(18, 30), (110, 40)], fill="RED")
                        draw.text((18,10), ip_address ,fill= "BLACK")
                        draw.text((18,30),"  SISTEM SAATI",fill="BLACK")

                        # SAAT OLAYI
                        current_time = datetime.now().strftime("%H:%M:%S")
                        font = ImageFont.load_default()
                        text_color = "black"
                        draw.text((18, 50), f"Saat: {current_time}", font=font, fill=text_color)
                        LCD.LCD_ShowImage(image,0,0)

                        #if LCD.digital_read(LCD.GPIO_KEY1_PIN) == 0:
                        #    break
                        #else:
                        #    print("")
                    else:
                        print("")
            def keyuc():
                 print("")
        else:
            print("IP adresi alınamadı.")
            time.sleep(5)

if __name__ == "__main__":
    main()
    azat()
