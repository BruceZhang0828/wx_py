import PIL.Image as Image
import os
import sys



# 获取文件当前所在的绝对路径
def get_dir(sys_arg):
    sys_arg = sys_arg.split("/")
    dri_str = ""
    count = 0
    for cur_dir in sys_arg:
        if count == 0:
            count = count + 1
        if count == len(sys_arg):
            break
        dri_str = dri_str+cur_dir+"/"
        count = count + 1
    
    return dri_str



def to_Photo_Wall():

    #准备生成器微信好友头像墙的尺寸

    image = Image.new("RGB",(650,650))

    # 定义初始图片的位置
    x = 0
    y = 0

    # 获取下载的头像文件

    curr_dir = get_dir(sys.argv[0])
    ls = os.listdir(curr_dir+"images")
    print("hello")
    for file_name in ls:
        try:
                # 依次打开图片
            img = Image.open(curr_dir+"images/"+file_name)
        except IOError:
            continue
        else:

            img = img.resize((50,50),Image.ANTIALIAS)
                #将图片粘贴到最终的照片墙上
            image.paste(img,(x*50,y*50))
                # 设置每一行13个图像
            x += 1
            if x == 13:
                x=0
                y=y+1
        
    img = image.save(curr_dir+"ImageWall.jpg")


if __name__=='__main__':
    to_Photo_Wall()