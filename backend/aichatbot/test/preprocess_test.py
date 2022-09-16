import sys
sys.path.append("/Users/jenny/success_gilyeon/aichatbot/uutils")
from uutils.Preprocess import Preprocess

sent = "내일 오후 1시에 노트북 대여할래"

# 전처리 객체 생성
p = Preprocess(userdic='user_dic.tsv')

# 형태소 분석기 실행
pos = p.pos(sent)

# 품사 태그와 같이 키워드 출력
ret = p.get_keywords(pos, without_tag=False)
print(ret)

# 품사 태그 없이 키워드 출력
ret = p.get_keywords(pos, without_tag=True)
print(ret)