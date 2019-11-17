import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets =  [
        ('train_rgb', 'train'), 
        ('test_rgb', 'test'),
        ]
classes = []

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(name, image_id):
    in_file = open('./%s_pascal/%s.xml'%(name, image_id))
    out_file = open('./labels/%s/%s.txt'%(name, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if int(difficult) == 1:
            continue
        print("classes: ", cls)
        if cls not in classes:
            classes.append(cls)

        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for name, image_set in sets:
    if not os.path.exists('./labels/%s'%(name)):
        os.makedirs('./labels/%s'%(name))
    image_ids = open('./%s/%s.txt'%(name, image_set)).read().strip().split()
#    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
#        list_file.write('%s/%s/%s/%s.png\n'%(wd, name, image_id))
        convert_annotation(name, image_id)
#    list_file.close()

    class_names_file = open('./obj.names', 'w')
    for class_names in classes:
        class_names_file.write(class_names+'\n')
    class_names_file.close()