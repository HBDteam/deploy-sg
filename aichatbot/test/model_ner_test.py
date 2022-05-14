import sys
sys.path.append('../')
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing
from sgModel.ner.NerModel import NerModel
from sgUtils.Preprocess import Preprocess

# import 문제로 ner폴더의 h5파일 test로 옮김
# import 문제로 ner/NerModel.py 내용 붙여넣음

p = Preprocess(word2index_dic='../train_tools/chatbot_dict.bin',
               userdic='user_dic.tsv')


ner = NerModel(model_name='ner_model.h5', proprocess=p)
query = '오늘 13시 2분에 노트북 주문 하고 싶어요'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)

