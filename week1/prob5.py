# 논리 연산자 and, or을 이용하여서 다음과 같은 결과가 나오도록 코드를 완성하세요. 
# (buttonN)과 (buttonN)의 사이를 출력 결과에 맞는 연산자로 채워주세요.
button1 = True
button2 = True
button3 = False

if (button1)  (button2) :
  print("button1과 button2가 켜졌습니다!")


if (button1)  (button2)  (button3) :
    print("모든 버튼이 켜졌습니다!")

if (button1)  (button2)  (button3)  (button3):
    print("하나 이상의 버튼이 켜졌습니다.")

# 출력 결과
#     button1과 button2가 켜졌습니다!
#     하나 이상의 버튼이 켜졌습니다.