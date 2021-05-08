# -*- coding: utf-8 -*-
"""
@version: 
@time: 2018/11/24
@software: PyCharm
@file: main
"""
import json
from sklearn_crfsuite import metrics
from singleton import get_model
from utils import test_config, document, entity, section_map, is_train
import codecs
from model import LoadModelPredict

if __name__ == '__main__':
    if is_train.get("train"):
        model = get_model()
        y_fix, y_predict, sorted_labels = model.train()
        with open(test_config.get("test_path").format("testset"), encoding='utf-8') as f:
            content = f.read()
        testset = json.loads(content)
        entity_list = []
        for obj in testset:
            sentence_0 = obj.get(document, {}).get(section_map["party_info"])
            if len(list(sentence_0.keys())) == 0:
                sentence_0 = ""
            elif len(list(sentence_0.keys())) == 1:
                sentence_0 = obj.get(document, {}).get(section_map["party_info"])["0"]
            else:
                sentence_0 = obj.get(document, {}).get(section_map["party_info"])["1"]
            sentence_1 = obj.get(document, {}).get(section_map["case_info"])
            if len(list(sentence_1.keys())) == 0:
                sentence_1 = ""
            else:
                sentence_1 = obj.get(document, {}).get(section_map["case_info"])["0"]
            entity_0, original_sentence_0, label_seq_0 = model.predict(sentence_0, 0)
            entity_1, original_sentence_1, label_seq_1 = model.predict(sentence_1, 1)
            entity_obj = entity_0.copy()
            entity_obj.update(entity_1)
            print("--> ", entity_obj)
            print("-->", original_sentence_0)
            print("-->", label_seq_0)
            entity_list.append({entity: entity_obj})
        print(metrics.flat_classification_report(y_fix, y_predict, labels=sorted_labels, digits=3))
        with codecs.open(test_config.get("output_path").format("output"), 'w', encoding='utf-8') as f:
            content = json.dumps(entity_list, indent=4, ensure_ascii=False)
            f.write(content)
    else:
        model = LoadModelPredict()
        """
        完成代码，调用model.predict（）函数，输入要识别的文字，并打印预测结果
        参考如下：
        识别结果, 原始语句, BIO标注结果 = model.predict(“你的文字”, 0)
        print(要打印的变量)
        """


