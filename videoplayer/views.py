import re
import os
import cv2
import mimetypes
import json
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse,HttpResponse
from common.api.utils import ApiResponse
from django.conf import settings
from django.views import View
from rest_framework import status

def file_iterator(file_name, chunk_size=8192, offset=0, length=None):
    # 每次最多读取8Kb
    with open(file_name, "rb") as f:
        f.seek(offset, os.SEEK_SET)
        remaining = length  # 还有多少未读取
        while True:
            bytes_length = chunk_size if remaining is None else min(remaining, chunk_size)
            data = f.read(bytes_length)
            if not data:  # 没有数据了 退出
                break
            if remaining:
                remaining -= len(data)
            # print('1111',bytes_length)
            yield data


def stream_video(request):
    """将视频文件以流媒体的方式响应"""
    range_header = request.GET.get('Content-Range', '').strip()
    range_re = re.compile(r'bytes\s*=\s*(?P<START>\d+)\s*-\s*(?P<END>\d*)', re.I)
    range_match = range_re.match(range_header)
    path = request.GET.get('path')
    video_path = os.path.join(settings.BASE_DIR, 'static', 'video')  # 视频放在目录的static下的video文件夹中
    file_path = os.path.join(video_path, path) #path就是template ?path=后面的参数的值
    size = os.path.getsize(file_path)  # 文件总大小
    content_type, encoding = mimetypes.guess_type(file_path)
    content_type = content_type or 'application/octet-stream'
    if range_match:
        # first_byte播放到的位置
        # 下次播放的位置 
        first_byte, last_byte = range_match.group('START'), range_match.group('END')
        first_byte = int(first_byte) if first_byte else 0
        # 从播放的位置往后读取10M的数据
        last_byte = first_byte + 1024 * 1024 * 10
        if last_byte >= size:  # 如果想读取的位置大于文件大小
            last_byte = size - 1  # 最后将图片全部读完
        length = last_byte - first_byte + 1  # 此次读取的长度（字节）
        resp = StreamingHttpResponse(file_iterator(file_path, offset=first_byte, length=length), status=200, content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes = %s-%s/%s' % (first_byte, last_byte, size)
    else:
        resp = StreamingHttpResponse(FileWrapper(open(file_path, 'rb')), content_type=content_type)
        resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp

class ImageFrames(View):
    
    def __init__(self, **kwargs):
        """
        Constructor. Called in the URLconf; can contain helpful extra
        keyword arguments, and other things.
        """
        # Go through keyword arguments, and either save their values to our
        # instance, or raise an error.
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.switch = True
        self.file_path = r'D:\project\udm\static\video\test1.mp4'

    def frames(self):
        camera = cv2.VideoCapture(r'D:\project\udm\static\video\test1.mp4')
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')
        items = 0
        while True:
            # read current frame
            _, image = camera.read()
            if image is not None:
                if items % 10 == 0:
                    # encode as a jpeg image and return it
                    frame = cv2.imencode('.jpg', image)[1].tobytes()
                    yield (b'--frame\r\n'
                    b'Content-Type: text/plain;charset=utf-8\r\n\r\n' + frame + b'\r\n\r\n')
                    # yield frame

                items += 1
            else:	# 视频提取结束后，跳出
                break
    
    def get(self, request):
        data = self.frames()
        return StreamingHttpResponse(data, content_type="multipart/x-mixed-replace; boundary=frame")
    

    def post(self, request):
        res = json.loads(request.body.decode()).get('frame_num')
        self.switch = bool(res)
        print(self.switch)
        return HttpResponse(res)

def frames():
    camera = cv2.VideoCapture(r'D:\project\udm\static\video\test1.mp4')
    if not camera.isOpened():
        raise RuntimeError('Could not start camera.')
    items = 0
    while True:
        # read current frame
        _, image = camera.read()
        if image is not None:
            if items % 50 == 0:
                # encode as a jpeg image and return it
                frame = cv2.imencode('.jpg', image)[1].tobytes()
                yield (b'--frame\r\n'
                b'Content-Type: text/plain;charset=utf-8\r\n\r\n' + frame + b'\r\n\r\n')
                # yield frame

            items += 1
        else:	# 视频提取结束后，跳出
            break


def video_list(request):
    data = frames()
    # print(type(data))
    return StreamingHttpResponse(data, content_type="multipart/x-mixed-replace; boundary=frame")
    # return StreamingHttpResponse(data, content_type="video/mp4")
