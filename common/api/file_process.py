import cv2
import os

def getFilePath(file_name):
    all_flie_name = os.listdir(file_name)
    all_file_path = []
    for video_file in all_flie_name:
        all_file_path.append(os.path.join(file_name, video_file))
    return all_file_path


def saveToImg(video_file, fps):
    items = 0
    savename = 0
    save_file_name = video_file.split('\\')[-1]
    index = save_file_name.index('.mp4')	# 以mp4文件为例，生成保存文件夹名
    file_name = save_file_name[:index]
    save_file_name = os.path.join(r'D:\project\test\fitvideo\result', file_name)
    if not os.path.exists(save_file_name):
        os.makedirs(save_file_name)         # 创建保存文件夹，命名以视频文件名为依据    
    camera = cv2.VideoCapture(video_file)	# 读取视频对象
    fps_one_second = camera.get(cv2.CAP_PROP_FPS)
    print(fps_one_second)
    print('Pls waiting···')
    while camera.isOpened():        
        _, image = camera.read()	
        if image is not None:
            if items % fps == 0:	# 按间隔帧保存为图片
                img_file_name = os.path.join(save_file_name, file_name + '_' + str(savename) + '.jpg')
                # print(img_file_name)
                cv2.imwrite(img_file_name, image) 
                done_name = img_file_name.split('\\')[-1]
                # print(f'{done_name} Done')     
                savename += 1
            # print(image.shape)
            items += 1
        else:	# 视频提取结束后，跳出
            break
    print('{} Done'.format(video_file.split('\\')[-1]))

def showImg(img_path):	# 查看图片
    img = cv2.imread(img_path)
    print(img.shape)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    file_name = r'D:\project\test\fitvideo\video'	# 视频文件夹路径
    all_file_path = getFilePath(file_name=file_name)
    for file in all_file_path:
        saveToImg(file, fps=1)


if __name__=='__main__':
    main()
