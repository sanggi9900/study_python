# Module : 부품/부속품/파츠
# - 다른 파일로 분리시켜 보관한 함수/변수/기타 코드의 묶음

# 1) 외장모듈 : 내가 직접 만들었거나, 인터넷상에서 다운받은 것
# - 불러올 소스파일의 소스파일명만 적으면 된다. 확장자는 제외.
# - 소스파일은 같은 폴더에 있어야 함
# 방법1. import 모듈명(파일명)
import myModule
# - 모듈명.필요한기능으로 지정하여 사용한다.
myModule.function1()
# - 중복을 예방하기 위한 목적으로 사용. 기본 사용방식.
myModule.function2(3)
# - 모듈명으로 변수나 함수 만들면 절대로 안됨
print()

# 방법2. from 모듈명(파일명) import 대상1 (, 대상2, ....)
from myModule1 import function3, function4
# - 대상명으로만 기능 사용이 가능하다.
print(function3())
# - 필요한 것만 정확하게 불러오기 때문에, 모듈명을 적을 필요가 없음
print(function4(2))
# - 대상명이 중복되면 안됨