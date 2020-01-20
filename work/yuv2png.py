#!/usr/bin/env python

# encoding: utf-8
import os
import re
import numpy as np
import skimage.io
import threadpool
import time

starttime = time.time()

def yuv2png(index, total, filename):

    if os.path.exists(os.path.splitext(filename)[0] + '.png'):
        return

    is_p010 = 0
    if '.p010' in filename:
        is_p010 = 1

    fsize = os.path.getsize(filename)
    if is_p010 > 0:
        fsize = fsize // 2

    regex = re.compile('[0-9]+x[0-9]+')

    sizes = regex.findall(filename)
    assert len(sizes) == 2
    fstsize = sizes[0].split('x')
    sndsize = sizes[1].split('x')
    fstw = int(fstsize[0])
    fsth = int(fstsize[1])
    sndw = int(sndsize[0])
    sndh = int(sndsize[1])
    w = 0
    h = 0
    if fstw * fsth * 3 // 2 == fsize:
        w = fstw
        h = fsth
    if fstw * sndh * 3 // 2 == fsize:
        w = fstw
        h = sndh
    if sndw * fsth * 3 // 2 == fsize:
        w = sndw
        h = fsth
    if sndw * sndh * 3 // 2 == fsize:
        w = sndw
        h = sndh

    assert w != 0 and h != 0

    # h = 3024
    # w = 4032
    # if 'input_sr' in filename:
    #     w = 4032
    #     h = 3072
    if is_p010 > 0:
        data = np.fromfile(filename, dtype=np.uint16, count=int(w*h*1.5))
    else:
        data = np.fromfile(filename, dtype=np.uint8, count=int(w*h*1.5))

    img = np.reshape(data, (int(h*1.5), w))
    YUV = np.zeros([h, w, 3],dtype=np.float32)
    YUV[:, :, 0] = img[0:h,:]# np.transpose(img[:,0:h], axes=[1, 0])

    YUV[:,:,1] = YUV[:,:,0]
    YUV[:,:,2] = YUV[:,:,0]
    UV = img[h:,:]

    U = UV[:,0::2]# np.transpose(UV[0::2,:], axes=[1, 0])
    V = UV[:,1::2]# np.transpose(UV[1::2,:], axes=[1, 0])
    YUV[0::2,0::2,1] = U
    YUV[1::2,0::2,1] = U
    YUV[0::2,1::2,1] = U
    YUV[1::2,1::2,1] = U
    YUV[0::2,0::2,2] = V
    YUV[1::2,0::2,2] = V
    YUV[0::2,1::2,2] = V
    YUV[1::2,1::2,2] = V

    if is_p010 > 0:
        YUV = YUV / 256

    RGB = np.zeros([h, w, 3],dtype=np.float32)
    RGB[:,:,0] = YUV[:,:,0] + 1.402   * (YUV[:,:,2]-128);
    RGB[:,:,1] = YUV[:,:,0] - 0.34414 * (YUV[:,:,1]-128) - 0.71414*(YUV[:,:,2]-128);
    RGB[:,:,2] = YUV[:,:,0] + 1.772   * (YUV[:,:,1]-128);

    RGB[RGB>255] = 255;
    RGB[RGB<0] = 0;

    # cropped_RGB = RGB
    # if 'input_sr' in filename:
    cropped_RGB = RGB[0:sndh, 0:sndw, :]

    cropped_RGB = cropped_RGB + 0.5
    cropped_RGB = cropped_RGB.astype(np.uint8)
    skimage.io.imsave(os.path.splitext(filename)[0] + '.png', cropped_RGB)

    nowtime = time.time()
    remaintime = (nowtime - starttime) / (index + 1) * (total - index) / 60
    tip = 'now:%d | total:%d | remain: %f min     '%(index + 1, total, remaintime)
    print(tip, filename)


if __name__ == '__main__':
    poolsize = 6
    pool = threadpool.ThreadPool(poolsize)
    files = os.listdir('.')
    files = list(filter(lambda x: ('.yuv' in x) or ('.p010' in x), files))
    nfile = len(files)
    filewithindex = []
    for i in range(nfile):
        filewithindex.append(([i, nfile, files[i]], None))
    # print(files)
    requests = threadpool.makeRequests(yuv2png, filewithindex)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    # for f in files:
    #     yuv2png(f)
