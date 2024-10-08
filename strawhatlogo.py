import machine
from ssd1306 import SSD1306_I2C
import framebuf

bitmap = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xc0, 0xc0, 0xe0, 0xe0, 0xe0, 0xe0, 0xe0, 0xc0, 
	0xc0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x80, 0xc0, 0xc0, 0xe0, 0xe0, 0xe0, 0xc0, 0xc0, 0x80, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x78, 0x7c, 0xfc, 0xfc, 0xfc, 0xfc, 0xff, 0xff, 0x7f, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xf3, 0xf1, 0xe0, 0xe0, 0xc0, 0x80, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xc0, 0xc0, 0xe0, 
	0x70, 0x70, 0xb8, 0x98, 0xd8, 0x7c, 0x7c, 0xbc, 0xfe, 0xfe, 0x7e, 0x7e, 0xfe, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0xfe, 0xfe, 0xfe, 0xfe, 0x7c, 0x7c, 0xfc, 
	0xf8, 0xf8, 0xb8, 0x30, 0x70, 0xe0, 0xc0, 0xc0, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 
	0xc0, 0xe0, 0xe0, 0xf3, 0xf7, 0xff, 0xff, 0xff, 0xff, 0xff, 0x7f, 0x7f, 0xff, 0xff, 0xfc, 0xfc, 
	0xfc, 0xfc, 0x78, 0x78, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x03, 
	0x07, 0x07, 0x0f, 0x0f, 0x1f, 0x1f, 0x0f, 0x03, 0x00, 0x00, 0x00, 0x03, 0x03, 0x03, 0x03, 0x03, 
	0x02, 0x03, 0x03, 0x03, 0x03, 0x00, 0x03, 0x03, 0x03, 0x03, 0x02, 0x03, 0x03, 0x03, 0x03, 0x03, 
	0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x00, 0x03, 
	0x03, 0x03, 0x03, 0x03, 0x00, 0x00, 0x03, 0x03, 0x03, 0x03, 0x00, 0x00, 0x00, 0x03, 0x07, 0x1f, 
	0x1f, 0x0f, 0x0f, 0x07, 0x07, 0x03, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 
	0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x3b, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 
	0x7b, 0x3b, 0x1b, 0x1b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x1b, 0x1b, 0x3b, 0x7b, 0xfb, 
	0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0x7b, 0x3b, 0x1b, 0x1b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 
	0x0b, 0x1b, 0x1b, 0x3b, 0x7b, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0x3b, 0x0b, 0x03, 0x03, 
	0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x07, 0x0f, 0x1f, 0x1f, 
	0x3e, 0x38, 0x70, 0x70, 0xe0, 0xe0, 0xe0, 0xe0, 0xe0, 0xe0, 0xe0, 0xe0, 0xf0, 0xf0, 0xf8, 0xff, 
	0xbf, 0x1f, 0x1f, 0x1f, 0x1f, 0xff, 0xfc, 0xf8, 0xf0, 0xe0, 0xe0, 0xe0, 0xe0, 0xe0, 0xe0, 0xe0, 
	0xe0, 0x60, 0x70, 0x38, 0x3c, 0x1f, 0x1f, 0x0f, 0x07, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xc0, 0xc0, 0xe0, 0xe0, 0xf0, 0xf0, 0xf8, 0xfc, 
	0x0c, 0x00, 0x70, 0xec, 0xee, 0xee, 0xde, 0xdc, 0x1d, 0x05, 0x81, 0xbd, 0xbd, 0xb9, 0xb9, 0xbb, 
	0xbb, 0xbb, 0x03, 0xbb, 0xbb, 0xb9, 0xb9, 0xb9, 0xb9, 0x91, 0x01, 0x1d, 0xdd, 0xdc, 0xde, 0xee, 
	0xee, 0xe8, 0x60, 0x04, 0x3c, 0xf8, 0xf8, 0xf0, 0xf0, 0xe0, 0xc0, 0xc0, 0x80, 0x80, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x1c, 0x3e, 0x3e, 0x7f, 0x7f, 0x7f, 
	0xff, 0xfe, 0xfe, 0xfe, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xdf, 0x0f, 0x0f, 0x07, 0x03, 0x03, 0x01, 
	0x00, 0x02, 0x1e, 0x3e, 0x7e, 0xfc, 0xfd, 0xfd, 0xfc, 0xf8, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 
	0xfb, 0xfb, 0xf8, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xfb, 0xf9, 0xf8, 0xfd, 0xfd, 0xfd, 0xfd, 
	0x7e, 0x3e, 0x0e, 0x00, 0x00, 0x03, 0x03, 0x07, 0x07, 0x0f, 0x9f, 0xff, 0xff, 0xff, 0xff, 0xfe, 
	0xfe, 0xfc, 0xfe, 0xfe, 0x7f, 0x7f, 0x7f, 0x7f, 0x3e, 0x3e, 0x1c, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x01, 0x03, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x03, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x03, 0x03, 0x03, 0x03, 0x03, 0x07, 0x07, 
	0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x03, 0x03, 0x03, 0x03, 0x03, 0x01, 0x01, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x07, 0x07, 0x07, 0x07, 
	0x07, 0x07, 0x07, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])


i2c = machine.I2C(sda=machine.Pin(21), scl=machine.Pin(22))
i2c.scan()
oled = SSD1306_I2C(128, 64, i2c)
fb = framebuf.FrameBuffer(bitmap,128,64, framebuf.MVLSB)
oled.fill(0)
oled.blit(fb,0,0)
oled.show()


