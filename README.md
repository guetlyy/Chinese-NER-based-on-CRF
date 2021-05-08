<img src="nlp.png" align="right" width=30% height=30%>

# 基于条件随机场(CRF)对中文案件语料进行命名实体识别(NER)

[![Language](https://img.shields.io/badge/language-python3.6+-blue.svg)](https://www.python.org/) [![license](https://img.shields.io/badge/license-MIT-green.svg)]()


## 文件组织

 - **corpus.py** 
    语料类
    
 - **model.py**
    模型类
    
 - **utils.py**
    工具函数、映射、配置
   
 - **data**
    语料
    
 - **requirements.txt**
    依赖
    
 
## 运行
    ```
        pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
    ```
    即可


## 效果

中间结果

<img src="训练输出.png" align="center">


预测结果

<img src="正确率.png" align="center">