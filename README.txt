1、数据集描述：该数据集包括yolo和slp两种格式，数据集中根据与猪只估重和姿态跟踪相关的体表参数，确定关键点。其中yolo格式数据集中除了常规的目标框外，还多了16个关键点；而slp数据集为猪只关键点组成的骨架。
2、文件夹描述：
	labels.v001.slp为slp格式的骨架数据集，pig-30s-2k.mp4为该数据集的原视频；
	yolo.7z为yolo格式的数据集；
	json2txt.py文件为用labelme标注的原始标签（.json格式）转化为yolo格式（.txt）的代码。
	README.txt文件为描述文件。