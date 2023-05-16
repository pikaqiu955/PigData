import os
import json
import traceback
import cv2

root_path = r'C:\Users\pikaqiu\Desktop\BISHE\convert\yolov5-face'
json_labels_path = os.path.join(root_path,'labels')
txt_labels_path = os.path.join(root_path,'txt')

box = {}
leftear = {}
rightear= {}
neck = {}
arc1 = {}
arc2 = {}
shoulder1 = {}
shoulder2 = {}
bumppoint1 = {}
bumppoint2 = {}
trunk1 = {}
trunk2 = {}
bumppoint3 = {}
bumppoint4 = {}
ham1 = {}
ham2 = {}
tail = {}

def read_json_file(json_file_name):
    with open(json_file_name, 'r', encoding='utf8') as f:
        data = json.load(f)
        w, h = data['imageWidth'], data['imageHeight']
        shapes = data['shapes']
        for dic in shapes:
            group_id = dic['group_id']
            if dic['label'] == 'pig':
                box.update({group_id:dic['points']})
            elif dic['label'] == 'leftear':
                leftear.update({group_id:dic['points']})
            elif dic['label'] == 'rightear':
                rightear.update({group_id:dic['points']})
            elif dic['label'] == 'neck':
                neck.update({group_id:dic['points']})
            elif dic['label'] == 'arc1':
                arc1.update({group_id:dic['points']})
            elif dic['label'] == 'arc2':
                arc2.update({group_id:dic['points']})
            elif dic['label'] == 'shoulder1':
                shoulder1.update({group_id:dic['points']})
            elif dic['label'] == 'shoulder2':
                shoulder2.update({group_id:dic['points']})
            elif dic['label'] == 'bumppoint1':
                bumppoint1.update({group_id:dic['points']})
            elif dic['label'] == 'bumppoint2':
                bumppoint2.update({group_id:dic['points']})
            elif dic['label'] == 'trunk1':
                trunk1.update({group_id:dic['points']})
            elif dic['label'] == 'trunk2':
                trunk2.update({group_id:dic['points']})
            elif dic['label'] == 'bumppoint3':
                bumppoint3.update({group_id:dic['points']})
            elif dic['label'] == 'bumppoint4':
                bumppoint4.update({group_id:dic['points']})
            elif dic['label'] == 'ham1':
                ham1.update({group_id:dic['points']})
            elif dic['label'] == 'ham2':
                ham2.update({group_id:dic['points']})
            elif dic['label'] == 'tail':
                tail.update({group_id:dic['points']})
            # print('当前读取文件为：', )
        print(leftear)
        f.close()
    return w, h

def calculate_and_write2txt(size, txt_filename):
    print('正在处理：', txt_filename)
    txt_path = os.path.join(txt_labels_path, txt_filename)
    f = open(txt_path,'w', encoding='utf8')
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    id = '0'
    # i = True
    try:
        for group_id in box:
            box_points = box[group_id]
            x0,y0,x1,y1 = box_points[0][0],box_points[0][1],box_points[1][0],box_points[1][1]
            x = (x0 + x1) / 2.0 - 1
            y = (y0 + y1) / 2.0 - 1
            w = float(abs(x1 - x0))
            h = float(abs(y1 - y0))
            center_x = round(x * dw, 6)
            center_y = round(y * dh, 6)
            w = round(w * dw, 6)
            h = round(h * dh, 6)
            leftear_x, leftear_y = round(leftear[group_id][0][0] * dw, 6), round(leftear[group_id][0][1] * dh, 6)
            rightear_x, rightear_y = round(rightear[group_id][0][0] * dw, 6), round(rightear[group_id][0][1] * dh, 6)
            neck_x, neck_y = round(neck[group_id][0][0] * dw, 6), round(neck[group_id][0][1]* dh, 6)
            arc1_x, arc1_y = round(arc1[group_id][0][0] * dw, 6), round(arc1[group_id][0][1] * dh, 6)
            arc2_x, arc2_y = round(arc2[group_id][0][0] * dw, 6), round(arc2[group_id][0][1] * dh, 6)
            shoulder1_x, shoulder1_y = round(shoulder1[group_id][0][0] * dw, 6), round(shoulder1[group_id][0][1] * dh, 6)
            shoulder2_x, shoulder2_y = round(shoulder2[group_id][0][0] * dw, 6), round(shoulder2[group_id][0][1] * dh, 6)
            bumppoint1_x, bumppoint1_y =  round(bumppoint1[group_id][0][0] * dw, 6), round(bumppoint1[group_id][0][1] * dh, 6)
            bumppoint2_x, bumppoint2_y = round(bumppoint2[group_id][0][0] * dw, 6), round(bumppoint2[group_id][0][1] * dh, 6)
            trunk1_x, trunk1_y = round(trunk1[group_id][0][0] * dw, 6), round(trunk1[group_id][0][1] * dh, 6)
            trunk2_x, trunk2_y = round(trunk2[group_id][0][0] * dw, 6), round(trunk2[group_id][0][1] * dh)
            bumppoint3_x, bumppoint3_y = round(bumppoint3[group_id][0][0] * dw, 6), round(bumppoint3[group_id][0][1] * dh, 6)
            bumppoint4_x, bumppoint4_y = round(bumppoint4[group_id][0][0] * dw, 6), round(bumppoint4[group_id][0][1] * dh, 6)
            ham1_x, ham1_y = round(ham1[group_id][0][0] * dw, 6), round(ham1[group_id][0][1] * dh, 6)
            ham2_x, ham2_y = round(ham2[group_id][0][0] * dw, 6), round(ham2[group_id][0][1] * dh, 6)
            tail_x, tail_y = round(tail[group_id][0][0] * dw, 6) , round(tail[group_id][0][1] * dh, 6)
          
            
            f.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" %
                    ('0', str(center_x), str(center_y), str(w), str(h), str(leftear_x), str(leftear_y), str(rightear_x), str(rightear_y),
                    str(neck_x), (neck_y), str(arc1_x), str(arc1_y), str(arc2_x), str(arc2_y), str(shoulder1_x), str(shoulder1_y),
                    str(shoulder2_x), str(shoulder2_y), str(bumppoint1_x), str(bumppoint1_y), str(bumppoint2_x), str(bumppoint2_y),
                    str(trunk1_x), str(trunk1_y), str(trunk2_x), str(trunk2_y), str(bumppoint3_x), str(bumppoint3_y), str(bumppoint4_x), str(bumppoint4_y),
                    str(ham1_x), str(ham1_y), str(ham2_x), str(ham2_y), str(tail_x), str(tail_y)))
            
            # i = False
        print(txt_filename,'写入成功！')
    except Exception as e:
        traceback.print_exc()
        print('出现错误!group_id=',group_id)
    finally:
        f.close()
    
if __name__ == '__main__':
    json_file_list = os.listdir(json_labels_path)
    for file in json_file_list:
        json_file_name = os.path.join(json_labels_path, file)
        size = read_json_file(json_file_name)
        txt_filename = file.replace(file[-5:],'.txt')
        calculate_and_write2txt(size,txt_filename)