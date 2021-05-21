import ovito


# открываем файл
from ovito.io import import_file
#pipeline = import_file("short.xyz")
pipeline = import_file("../data_files/Vel_1.0/dump.flow") 
# Инициализируем вывод log файла. Необязательно
import logging
logging.basicConfig(filename="log.txt", level=logging.INFO)
# Модифицируем нашу загруженную систему
import ovito.modifiers as md

pipeline.add_to_scene()
# Меняем цвет и размер ионов и электронов по RGB. # (Создаем функцию для замены)
def modifier_color_radius(frame, data):
    color_property = data.particles_.create_property("Color") 
    pos_property = data.particles_.create_property("Position") 
    radius_property = data.particles_.create_property("Radius") 
    transparency_property = data.particles_.create_property("Transparency") 
    id_property = data.particles['Particle Identifier']
    type_property = data.particles['Particle Type']
# Можем получить кинетическую энергию частиц
    #ke_property = data.particles['c_keatom']
    for i in range(len(color_property)):
        if (type_property.array[i] == 1): #атомы
            radius_property.marray[i] = 0.4
            color_property.marray[i] = ((250)/250, 125/250, 125/250)
        else: #Электроны
            radius_property.marray[i] = 0.2
            color_property.marray[i] = (250/250, 1/250,1/250)"""
    for i in range(len(transparency_property)):
        if (frame < 2051):
            transparency_property[i] = 0
        elif (frame >= 2051 and id_property[i] == 865):
            transparency_property[i] = 0
            #if (frame == 2099):
             #   print(pos_property[i])
        else:
            transparency_property[i] = 0.95"""
                
# Указываем Ovito какую функцию modifier использовать
pipeline.modifiers.append(
        md.PythonScriptModifier(
                function = modifier_color_radius)
                )
data=pipeline.compute()
# Создаем видео
import math
import ovito.vis as vis
import math
import numpy as np
# Извлекаем размер ячейки
wall=data.cell[0][0]
# Создаем объект визуализации
vp = vis.Viewport()
vp.type = vis.Viewport.Type.Perspective
# Создаем функцию, которая бы по номеру шага выводила бы
# координаты камеры и ее направление
# В окне программы Ovito можно узнать координаты и направление камеры,
# если нажать на настройки отображения.
def get_pos_dir(frame):
    #last_pos_of=np.array([11.1564, 22.1047, 7.77449]) 
    radius=wall*4/3*(2110-frame)/110
    hight=[5,5,7.77449]
    phi = frame/2100*2*np.pi 
    direction=np.array([-1, -1, -0.5]) 
    #position = direction*radius+hight #direction = [-1,0,-1]
    position = [34.6, 5.2, 34.6]
    return tuple(position), tuple( (last_pos_of - position) )
pos, direction = get_pos_dir(2000)
# Задаем начальные данные камеры
vp.camera_pos = pos
vp.camera_dir = direction
vp.fov = math.radians(60.0)
# Создаем функцию, которая будет вызываться на каждом шаге # создания видео и будет вращать нашу камеру
def render_view(args):
    global wall
    frame=args.frame
#print (args.frame, end=" ") logging.info("frame: {:d}".format(args.frame)) #text1 = "Frame {}".format(args.frame)
    pos, direction = get_pos_dir(frame) 
    args.viewport.camera_pos = pos 
    args.viewport.camera_dir = direction 
    args.viewport.fov = math.radians(60.0)
# Добавляем эту функцию в render
vp.overlays.append(vis.PythonViewportOverlay(function = render_view)) # Мы можем создать одно изображение с разрешением 400x300


#vp.render_image(size=(400,300), filename="animation.png",
#        renderer=TachyonRenderer())
# Можем создать полную анимацию от 0 до 101 шага
# с разрешением 800x400
vp.render_anim(size=(640,480), filename="flow.mp4",
renderer=vis.TachyonRenderer(), range=(5000,5500))