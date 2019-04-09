import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
os.chdir('E:\\TC\\mtwi_2018_train\\txt_train')
dir_files=os.listdir()
sub_dir_file=[]
count=0
def get_tan(x,y):
    if x[0]==y[0]:
        return 1e8
    else:
        return abs(x[1]-y[1])/abs(x[0]-y[0])
def find_direct(temp):
    a=temp[0:2]
    b=temp[2:4]
    c=temp[4:6]
    d=temp[6:8]
    a_b=get_tan(a,b)
    b_c=get_tan(b,c)
    if a_b<b_c:
        a,c=c,a
    if b[1]<a[1]:
        a,b,c,d=b,a,d,c
    if a[0]>d[0]:
        a,b,c,d=d,c,b,a
    temp=a+b+c+d
    return temp
def rotate_cut(image,position):
    height,width,channels=image.shape
    length=max(height,width)
    after=np.array([[0,0],[0,position[8]],[position[9],0]]).astype('float32')
    before=np.array([[position[0],position[1]],[position[2],position[3]],[position[6],position[7]]]).astype('float32')
    M=cv2.getAffineTransform(before,after)
    rotate_image=cv2.warpAffine(image,M,(height,width))
    #rotate_cut_image
    return rotate_image[0:int(position[8]),0:int(position[9]),:]
write=open('E:\\TC\\mtwi_2018_train\\txt_train_alter.txt','w',encoding='utf8')
for dir_file in dir_files:
    image=cv2.imread('E:\\TC\\mtwi_2018_train\\image_train\\'+dir_file[:-3]+'jpg')
    if image is None:
        sub_dir_file.append('E:\\TC\\mtwi_2018_train\\image_train\\'+dir_file[:-3]+'jpg')
        continue
    position=[]
    words=[]
    with open(dir_file,'r',encoding='utf8') as text:
        for line in text:
            temp=line.split(',')
            words.append(temp[8])
            temp=[float(temp[i]) for i in range(8)]
            temp=find_direct(temp)
            temp.append(((temp[0]-temp[2])**2+(temp[1]-temp[3])**2)**0.5)
            temp.append(((temp[0]-temp[6])**2+(temp[1]-temp[7])**2)**0.5)
            position.append(temp)
    j=0
    for i in position:
        if words[j]!='###\n':
            write.write(str(count))
            write.write(',')
            write.write(words[j])
            write.write('\n')
            cv2.imwrite('E:\\TC\\mtwi_2018_train\\image_train_alter\\'+str(count)+'.jpg',rotate_cut(image,position[j]))
            count+=1
        j+=1
write.close()
