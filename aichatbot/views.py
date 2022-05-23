from django.http import HttpResponse
from django.shortcuts import render
from .models import ChatTrain
from django.shortcuts import render, redirect
from .sgUtils.Preprocess import Preprocess
from django.http import JsonResponse
import logging
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

import sys
sys.path.append('../')

# 질문/답변 학습 디비 연결 객체 생성

def aichatbot(request):
    db = connection.cursor()   # 디비 연결
    result = db.execute('select * from aichatbot_chattrain;')
    datas = db.fetchall()
    connection.commit()
    connection.close()
    print('!!!!!!!!!!!!!!!!!!')
    print(datas)
    return render(request, 'aichatbot.html')

class FindAnswer:
        def __init__(self, db):
            self.db = db

        # 검색 쿼리 생성 
        def _make_query(self, intent_name, ner_tags):
            print('검색 쿼리 생성------------------------------------')
            sql = "select * from aichtbot_chattrain"
            if intent_name != None and ner_tags == None:
                sql = sql + " where intent='{}' ".format(intent_name)
                print('검색 쿼리 생성1-1------------------------------------')
            elif intent_name != None and ner_tags != None:
                where = ' where intent="%s" ' % intent_name
                print('검색 쿼리 생성1-2------------------------------------')
                if (len(ner_tags) > 0):
                    where += 'and ('
                    for ne in ner_tags:
                        where += " ner like '%{}%' or ".format(ne)
                    where = where[:-3] + ')'
                sql = sql + where
                print(sql)

            # 동일한 답변이 2개 이상인 경우, 랜덤으로 선택
            sql = sql + " order by rand() limit 1"
            return sql


        # 답변 검색
        def search(self, intent_name, ner_tags):
            # db = connection.cursor()   # 디비 연결
            # result = db.execute('select * from User;')
            # datas = db.fetchall()
            # connection.commit()
            # connection.close()
            # print('!!!!!!!!!!!!!!!!!!')
            # print(datas)
            # 의도명, 개체명으로 답변 검색
            # sql = self._make_query(intent_name, ner_tags)
            
            # answer = self.db.select_one(sql)
            # print(answer+'answer')

            # 검색되는 답변이 없으면 의도명만 검색
            if answer is None:
                sql = self._make_query(intent_name, None)
                answer = self.db.select_one(sql)

            return (answer['answer'], answer['answer_image'])



        # NER 태그를 실제 입력된 단어로 변환
        def tag_to_word(self, ner_predicts, answer):
            for word, tag in ner_predicts:
                # 변환해야하는 태그가 있는 경우 추가
                if tag == 'FOOD' or tag == 'TIME' or tag == 'NNP' or tag == 'EQUIP' or tag == '0' :
                    answer = answer.replace(tag, word)

            answer = answer.replace('{', '')
            answer = answer.replace('}', '')
            return answer



@csrf_exempt
def aiAnswer_ajax(query):
    if query.method == 'POST':
        user_txt = query.POST.get('text') # 사용자가 보낸 질문 받아옴


        # 전처리 객체 생성
        p = Preprocess(word2index_dic='aichatbot/train_tools/chatbot_dict.bin',
                    userdic='aichatbot/test/user_dic.tsv')

        # 의도 파악
        from aichatbot.intent.IntentModel import IntentModel
        intent = IntentModel(model_name='aichatbot/intent/intent_model.h5', proprocess=p)
        predict = intent.predict_class(user_txt)
        intent_name = intent.labels[predict]

        # 개체명 인식
        from aichatbot.ner.NerModel import NerModel
        ner = NerModel(model_name='aichatbot/test/ner_model.h5', proprocess=p)
        predicts = ner.predict(user_txt)
        ner_tags = ner.predict_tags(user_txt)

        print("질문 : ", user_txt)
        print("의도 파악 : ", intent_name)
        print("개체명 인식 : ", predicts)
        print("답변 검색에 필요한 NER 태그 : ", ner_tags)
        print("=" * 100)

        # 실제 답변 검색
        try: 
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(predicts, answer_text)
            #if intent_name == '욕설':
            #    answer = '저에게 욕하지 마세요 ㅠㅡㅠ'
        except:
            if intent_name == '욕설':
                answer = '저에게 욕하지 마세요 ㅠㅡㅠ'
            else : answer = "죄송해요.. 성공이는 무슨 말인지 모르겠어요ㅠㅠㅠㅠ"
      
    
    return JsonResponse({'ans_txt': answer})

      
    

    
    


   



  





    
    