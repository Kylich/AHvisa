import twain, sys
# получаем список имеющихся источников для сканирования
sm = twain.SourceManager(1) # некий менеджер в свойствах которого будет этот источник
source_list = sm.source_list # получили список источников
print(source_list)
#sm.close()
#exit(0)
# создаём объект для работы с источником и указываем ему этот самый источник
source = sm.open_source(source_list[0].encode()) # encode() обязателен. Без него не воспринимает.
# установка параметра dpi
dpi = 150
source.set_capability(twain.ICAP_XRESOLUTION, twain.TWTY_FIX32, dpi)
source.set_capability(twain.ICAP_YRESOLUTION, twain.TWTY_FIX32, dpi)
# установка цветности
pixel_type_map = {'bw'   :twain.TWPT_BW,
                  'gray' :twain.TWPT_GRAY,
                  'color':twain.TWPT_RGB}
pixel_type = pixel_type_map['color']
source.set_capability(twain.ICAP_PIXELTYPE, twain.TWTY_UINT16, pixel_type)
# старт сканирования
source.RequestAcquire(0, 0)
print('fxfp',source.image_info)
result = source.XferImageNatively()
handle, count = result
raw_data = twain.DIBToBMFile(handle) # получаем файлв виде строки