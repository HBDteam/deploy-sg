from django.http import HttpResponse
from django.shortcuts import render
from .models import ChatTrain
from django.shortcuts import render, redirect
from django.db import connection
from .sgUtils.Preprocess import Preprocess

import sys
sys.path.append('../')
import os
print(os.getcwd())

# 질문/답변 학습 디비 연결 객체 생성
db = ChatTrain.objects
db = connection.commit()   # 디비 연결


query = "피자 주문할게요"


def aiAnswer(query):
        
    # 전처리 객체 생성
    p = Preprocess(word2index_dic='aichatbot/train_tools/chatbot_dict.bin',
                   userdic='aichatbot/test/user_dic.tsv')

    # 의도 파악
    from aichatbot.intent.IntentModel import IntentModel
    intent = IntentModel(model_name='aichatbot/intent/intent_model.h5', proprocess=p)
    predict = intent.predict_class(query)
    intent_name = intent.labels[predict]

    # 개체명 인식
    from aichatbot.ner.NerModel import NerModel
    ner = NerModel(model_name='aichatbot/test/ner_model.h5', proprocess=p)
    predicts = ner.predict(query)
    ner_tags = ner.predict_tags(query)

    print("질문 : ", query)
    print("=" * 100)
    print("의도 파악 : ", intent_name)
    print("개체명 인식 : ", predicts)
    print("답변 검색에 필요한 NER 태그 : ", ner_tags)
    print("=" * 100)

    
    class FindAnswer:
        def __init__(self, db):
            self.db = db

        # 검색 쿼리 생성 ok
        def _make_query(self, intent_name, ner_tags):
            sql = "select * from chattrain"
            if intent_name != None and ner_tags == None:
                sql = sql + " where intent='{}' ".format(intent_name)
            elif intent_name != None and ner_tags != None:
                where = ' where intent="%s" ' % intent_name
                if (len(ner_tags) > 0):
                    where += 'and ('
                    for ne in ner_tags:
                        where += " ner like '%{}%' or ".format(ne)
                    where = where[:-3] + ')'
                sql = sql + where

            # 동일한 답변이 2개 이상인 경우, 랜덤으로 선택
            sql = sql + " order by rand() limit 1"

            return sql

        # 답변 검색
        def search(self, intent_name, ner_tags):
            # 의도명, 개체명으로 답변 검색
            sql = self._make_query(intent_name, ner_tags)
            answer = self.db.select_one(sql)

            # 검색되는 답변이 없으면 의도명만 검색
            if answer is None:
                sql = self._make_query(intent_name, None)
                answer = self.db.select_one(sql)

            return (answer['answer'], answer['answer_image'])

        # NER 태그를 실제 입력된 단어로 변환
        def tag_to_word(self, ner_predicts, answer):
            for word, tag in ner_predicts:

                # 변환해야하는 태그가 있는 경우 추가
                if tag == 'FOOD' or tag == 'B_DT' or tag == 'B_TI' or tag == 'EQUIP' :
                    answer = answer.replace(tag, word)

            answer = answer.replace('{', '')
            answer = answer.replace('}', '')
            return answer


    # 실제 답변 검색
    try: 
        f = FindAnswer(db)
        answer_text, answer_image = f.search(intent_name, ner_tags)
        answer = f.tag_to_word(predicts, answer_text)
    except:
        answer = "죄송해요.. 성공이는 무슨 말인지 모르겠어요ㅠㅠ"


    print("답변 : ", answer)

    
    #db = connection.close()


aiAnswer(query)
    