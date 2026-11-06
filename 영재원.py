import turtle
import random

screen = turtle.Screen()
screen.title("음식 추천 프로그램")
screen.bgcolor("white")
screen.setup(width=800 , height=600)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

level = 0
rice = 0
noodle= 0
spicy = 0
mild = 0
soup = 0
filling = 0 
new = 0
light = 0
food = [ ]
eat = 0

def choose (x,y):
    global eat
    pen.clear()
    for i in range(len(food)):
        width = 800 / len(food) 
        
        left = -400 + (i * width)  
        right = left + width      
    
        if x >= left and x < right:
            eat = food[i]
            pen.clear()
            pen.goto(-40,300)
            pen.write(
                f"음식이 정해졌습니다!",
                 align="center",
                font=("Noto Sans KR", 40, "bold")
            )                              
            pen.goto(-40,0)
            pen.color("blue")
            pen.write(
                f"추천 음식: {eat}",
                 align="center",
                font=("Noto Sans KR", 20, "bold")
            )   
            pen.color("black")
            screen.update()
            break                       

#사각형그리기 정의

def draw_box(x, y, width, height, color, fill_color):
    pen.goto(x - width / 2, y - height / 2)
    pen.setheading(0)

    pen.pencolor(color)
    pen.fillcolor(fill_color)

    pen.begin_fill()
    pen.pendown()

    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

    pen.pencolor("black")
    pen.penup()
    pen.end_fill()

def draw_circle(x, y, r, color, fill_color):
    pen .goto (x,y-r)
    pen.setheading(0)

    pen.pencolor(color)
    pen.fillcolor(fill_color)

    pen.begin_fill()
    pen.pendown()
    pen.circle(r)
    pen.penup()
    pen.end_fill()

#다음 화면 넘어가기

def question_start(a):
    global level
    pen.clear()
    pen.pencolor("black")
    if a == 1:
        level = 1
        pen.goto(0, 165)
        pen.write(
            "밥을 얼마나 좋아하시나요?",
            align="center",
            font=("Noto Sans KR", 22,"bold")
        )
        pen.up()
        draw_box(0, -230, 220, 70 , "blue" , "blue")
        pen.goto(0, -250)
        pen.write(
            "선택" ,
            align="center",
            font=("Noto Sans KR", 30, "bold")
        )
        for i in range(5):
            draw_circle(-180 + i * 72 ,0,10,"black","white")
            pen.goto(-180 + i * 72 ,-10)
            pen.write(
                i + 1,
                align="center",
                font=("Noto Sans KR", 12, "bold")
            )
            
            
    elif a == 2:
        level = 2
        pen.goto(0, 165)
        pen.write(
             "면을 얼마나 좋아하시나요?",
             align="center",
               font=("Noto Sans KR", 22,"bold")
        )
        pen.up()
        draw_box(0, -230, 220, 70 , "blue" , "blue")
        pen.goto(0, -250)
        pen.write(
            "선택" ,
            align="center",
            font=("Noto Sans KR", 30, "bold")
        )
        for i in range(5):
              draw_circle(-180 + i * 72 ,0,10,"black","white")
              pen.goto(-180 + i * 72 ,-10)
              pen.write(
                   i + 1,
                  align="center",
                  font=("Noto Sans KR", 12, "bold")
              )
    elif a == 3:
        level = 3
        pen.goto(0, 165)
        pen.write(
             "매운음식을 얼마나 좋아하시나요?",
             align="center",
             font=("Noto Sans KR", 22,"bold")
        )
        pen.up()
        draw_box(0, -230, 220, 70 , "blue" , "blue")
        pen.goto(0, -250)
        pen.write(
            "선택" ,
            align="center",
            font=("Noto Sans KR", 30, "bold")
        )
        for i in range(5):
              draw_circle(-180 + i * 72 ,0,10,"black","white")
              pen.goto(-180 + i * 72 ,-10)
              pen.write(
                   i + 1,
                  align="center",
                  font=("Noto Sans KR", 12, "bold")
              )      
    elif a == 4:
        level = 4
        pen.goto(0, 165)
        pen.write(
             "담백함을 얼마나 좋아하시나요?",
             align="center",
               font=("Noto Sans KR", 22,"bold")
        )
        pen.up()
        draw_box(0, -230, 220, 70 , "blue" , "blue")
        pen.goto(0, -250)
        pen.write(
            "선택" ,
            align="center",
            font=("Noto Sans KR", 30, "bold")
        )
        for i in range(5):
              draw_circle(-180 + i * 72 ,0,10,"black","white")
              pen.goto(-180 + i * 72 ,-10)
              pen.write(
                   i + 1,
                  align="center",
                  font=("Noto Sans KR", 12, "bold")
              )          
    elif a == 5 :
        level = 5
        pen.goto(0, 165)
        pen.write(
             "국물을 얼마나 좋아하시나요?",
             align="center",
               font=("Noto Sans KR", 22,"bold")
        )
        pen.up()
        draw_box(0, -230, 220, 70 , "blue" , "blue")
        pen.goto(0, -250)
        pen.write(
            "선택" ,
            align="center",
            font=("Noto Sans KR", 30, "bold")
        )
        for i in range(5):
              draw_circle(-180 + i * 72 ,0,10,"black","white")
              pen.goto(-180 + i * 72 ,-10)
              pen.write(
                   i + 1,
                  align="center",
                  font=("Noto Sans KR", 12, "bold")
              )    
    elif a == 6:
        level = 6
        pen.goto(0, 165)
        pen.write(
             "든든함을 얼마나 좋아하시나요?",
             align="center",
               font=("Noto Sans KR", 22,"bold")
        )
        pen.up()
        draw_box(0, -230, 220, 70 , "blue" , "blue")
        pen.goto(0, -250)
        pen.write(
            "선택" ,
            align="center",
            font=("Noto Sans KR", 30, "bold")
        )
        for i in range(5):
              draw_circle(-180 + i * 72 ,0,10,"black","white")
              pen.goto(-180 + i * 72 ,-10)
              pen.write(
                   i + 1,
                  align="center",
                  font=("Noto Sans KR", 12, "bold")
              )                       
    elif a == 7:
        level = 7
        pen.goto(0, 165)
        pen.write(
             "새로운 맛을 얼마나 좋아하시나요?",
             align="center",
               font=("Noto Sans KR", 22,"bold")
        )
        pen.up()
        draw_box(0, -230, 220, 70 , "blue" , "blue")
        pen.goto(0, -250)
        pen.write(
            "선택" ,
            align="center",
            font=("Noto Sans KR", 30, "bold")
        )
        for i in range(5):
              draw_circle(-180 + i * 72 ,0,10,"black","white")
              pen.goto(-180 + i * 72 ,-10)
              pen.write(
                   i + 1,
                  align="center",
                  font=("Noto Sans KR", 12, "bold")
              )     
    elif a == 8:
        level = 8
        pen.goto(0, 165)
        pen.write(
             "간편함을 얼마나 좋아하시나요?",
             align="center",
               font=("Noto Sans KR", 22,"bold")
        )
        pen.up()
        draw_box(0, -230, 220, 70 , "blue" , "blue")
        pen.goto(0, -250)
        pen.write(
            "선택" ,
            align="center",
            font=("Noto Sans KR", 30, "bold")
        )
        for i in range(5):
              draw_circle(-180 + i * 72 ,0,10,"black","white")
              pen.goto(-180 + i * 72 ,-10)
              pen.write(
                   i + 1,
                  align="center",
                  font=("Noto Sans KR", 12, "bold")
              )                       
    elif a == 9:
        level = 9
        korea = 100 - (rice - 5) ** 2 * 5 + 100 - (4 - noodle) ** 2 * 5 + 100 - (4 - spicy) ** 2 * 5 + 100 - (3.5 - mild) ** 2 * 5 + 100 - (4 - soup) ** 2 * 5 + 100 - (4 - filling) ** 2 * 5 + 100 - (2.3 - new) ** 2 * 5 + 100 - (3 - light) ** 2 * 5
        japan = 100 - (rice - 4) ** 2 * 5 + 100 - (4 - noodle) ** 2 * 5 + 100 - (0 - spicy) ** 2 * 5 + 100 - (3 - mild) ** 2 * 5 + 100 - (3.5 - soup) ** 2 * 5 + 100 - (9 - filling) ** 2 * 5 + 100 - (3.6 - new) ** 2 * 5 + 100 - (3 - light) ** 2 * 5
        china = 100 - (3.4 - rice) ** 2 * 5 + 100 - (4.5 - noodle) ** 2 * 5 + 100 - (4.7 - spicy) ** 2 * 5 + 100 - (3.1 - mild) ** 2 * 5 + 100 - (3.5 - soup) ** 2 * 5 + 100 - (4.5 - filling) ** 2 * 5
        western = 100 - (2 - rice) ** 2 * 5 + 100 - (4.7 - noodle) ** 2 * 5 + 100 - (0 - spicy) ** 2 * 5 + 100 - (2.5 - mild) ** 2 * 5 + 100 - (3 - soup) ** 2 * 5 + 100 - (4 - filling) ** 2 * 5 + 100 - (4.1 - new) ** 2 * 5 + 100 - (3.1 - light) ** 2 * 5
        if korea >= japan and korea >= china and korea >= western :
            if rice >= noodle and rice >= spicy and rice >= mild and rice >= soup and rice >= filling and rice >= new and rice >= light:
                food.append("비빔밥")
            if noodle >= rice and noodle >= spicy and noodle >= mild and noodle >= soup and noodle >= filling and noodle >= new and noodle >= light:
                food.append("칼국수")
            if spicy >= rice and spicy >= noodle and spicy >= mild and spicy >= soup and spicy >= filling and spicy >= new and spicy >= light:
                food.append("김치찌개")
            if mild >= rice and mild >= noodle and mild >= spicy and mild >= soup and mild >= filling and mild >= new and mild >= light:
                food.append("곰탕")
            if soup >= rice and soup >= noodle and soup >= spicy and soup >= mild and soup >= filling and soup >= new and soup >= light:
                food.append("떡국")
            if filling >= rice and filling >= noodle and filling >= spicy and filling >= mild and filling >= soup and filling >= new and filling >= light:
                food.append("국밥")
            if new >= rice and new >= noodle and new >= spicy and new >= mild and new >= soup and new >= filling and new >= light:
                food.append("로제떡볶이")
            if light >= rice and light >= noodle and light >= spicy and light >= mild and light >= soup and light >= filling and light >= new:
                food.append("냉면")
        if japan >= korea and japan >= china and japan >= western :
            if rice >= noodle and rice >= spicy and rice >= mild and rice >= soup and rice >= filling and rice >= new and rice >= light:
                food.append("오니기리")
            if noodle >= rice and noodle >= spicy and noodle >= mild and noodle >= soup and noodle >= filling and noodle >= new and noodle >= light:
                food.append("우동")
            if spicy >= rice and spicy >= noodle and spicy >= mild and spicy >= soup and spicy >= filling and spicy >= new and spicy >= light:
                food.append("매운 미소라멘")
            if mild >= rice and mild >= noodle and mild >= spicy and mild >= soup and mild >= filling and mild >= new and mild >= light:
                food.append("스시")
            if soup >= rice and soup >= noodle and soup >= spicy and soup >= mild and soup >= filling and soup >= new and soup >= light:
                food.append("전골")
            if filling >= rice and filling >= noodle and filling >= spicy and filling >= mild and filling >= soup and filling >= new and filling >= light:
                food.append("규동")
            if new >= rice and new >= noodle and new >= spicy and new >= mild and new >= soup and new >= filling and new >= light:
                food.append("타코야키")
            if light >= rice and light >= noodle and light >= spicy and light >= mild and light >= soup and light >= filling and light >= new:
                food.append("유부초밥")
        if china >= korea and china >= japan and china >= western :
            if rice >= noodle and rice >= spicy and rice >= mild and rice >= soup and rice >= filling and rice >= new and rice >= light:
                food.append("마파두부 덮밥")
            if noodle >= rice and noodle >= spicy and noodle >= mild and noodle >= soup and noodle >= filling and noodle >= new and noodle >= light:
                food.append("우육면")
            if spicy >= rice and spicy >= noodle and spicy >= mild and spicy >= soup and spicy >= filling and spicy >= new and spicy >= light:
                food.append("짬뽕")
            if mild >= rice and mild >= noodle and mild >= spicy and mild >= soup and mild >= filling and mild >= new and mild >= light:
                food.append("찐만두")
            if soup >= rice and soup >= noodle and soup >= spicy and soup >= mild and soup >= filling and soup >= new and soup >= light:
                food.append("마라탕")
            if filling >= rice and filling >= noodle and filling >= spicy and filling >= mild and filling >= soup and filling >= new and filling >= light:
                food.append("짜장면")
            if new >= rice and new >= noodle and new >= spicy and new >= mild and new >= soup and new >= filling and new >= light:
                food.append("훠궈")
            if light >= rice and light >= noodle and light >= spicy and light >= mild and light >= soup and light >= filling and light >= new:
                food.append("계란탕")
        if western >= korea and western >= japan and western >= china :
            if rice >= noodle and rice >= spicy and rice >= mild and rice >= soup and rice >= filling and rice >= new and rice >= light:
                food.append("리소토")
            if noodle >= rice and noodle >= spicy and noodle >= mild and noodle >= soup and noodle >= filling and noodle >= new and noodle >= light:
                food.append("파스타")
            if spicy >= rice and spicy >= noodle and spicy >= mild and spicy >= soup and spicy >= filling and spicy >= new and spicy >= light:
                food.append("매운 스테이크")
            if mild >= rice and mild >= noodle and mild >= spicy and mild >= soup and mild >= filling and mild >= new and mild >= light:
                food.append("양송이 수프")
            if soup >= rice and soup >= noodle and soup >= spicy and soup >= mild and soup >= filling and soup >= new and soup >= light:
                food.append("부야베스")
            if filling >= rice and filling >= noodle and filling >= spicy and filling >= mild and filling >= soup and filling >= new and filling >= light:
                food.append("라자냐")
            if new >= rice and new >= noodle and new >= spicy and new >= mild and new >= soup and new >= filling and new >= light:
                food.append("뇨끼")
            if light >= rice and light >= noodle and light >= spicy and light >= mild and light >= soup and light >= filling and light >= new:
                food.append("잠봉뵈르")

            pen.goto(0,0)  
            pen.write(
                "화면을 눌러 주세요"
            )
   
            

        
#클릭 확인
            

def next (x, y):
    global level, rice, noodle, spicy, mild, soup, filling, new, light
    if -110 <= x <= 110 and -265 <= y <= -195:
        if level != 0:
            if rice != 0:
                if noodle !=0:
                    if spicy != 0:
                        if mild != 0:
                            if soup != 0:
                                if filling != 0:
                                    if new != 0:
                                        if light != 0: 
                                            question_start(9)
                                        elif light == 0:
                                            question_start(8)    
                                    elif new == 0:
                                        question_start(7)
                                elif filling ==0:
                                    question_start(6)
                            elif soup == 0:
                                question_start(5)    
                        elif mild == 0:
                            question_start(4)    
                    elif spicy == 0:
                        question_start(3)    
                elif noodle == 0:
                    question_start(2)
    elif -110 <= x <= 110 and -35 <= y <= 35 and level == 0:
        question_start(1)
       
        
#선택항목 표시
def score(x,y):
    global level, rice, noodle, spicy, mild, soup, filling, new, light
    for i in range(5):
        left = -190 + i * 72
        right = -170 + i * 72

        if left <= x <= right and -10 <= y <= 10:

            answer = i + 1

            if level == 1:
                rice = answer
                draw_circle(-180 + i * 72 ,0,10,"red","white")
                pen.goto(-180 + i * 72 ,-10)
                pen.pencolor("red")
                pen.write(
                    i + 1,
                    align="center",
                    font=("Noto Sans KR", 12, "bold")
                )
                if i == 0:
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    
                elif i == 1:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                         align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 2:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )     
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )             
                elif i == 3:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                        1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                         align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 4:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )

            elif level == 2:
                noodle = answer
                draw_circle(-180 + i * 72 ,0,10,"red","white")
                pen.goto(-180 + i * 72 ,-10)
                pen.pencolor("red")
                pen.write(
                    i + 1,
                    align="center",
                    font=("Noto Sans KR", 12, "bold")
                )
                if i == 0:
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                elif i == 1:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                         align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 2:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )     
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )             
                elif i == 3:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                        1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                         align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 4:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    ) 
            elif level == 3 :     
                spicy = answer
                draw_circle(-180 + i * 72 ,0,10,"red","white")
                pen.goto(-180 + i * 72 ,-10)
                pen.pencolor("red")
                pen.write(
                    i + 1,
                    align="center",
                    font=("Noto Sans KR", 12, "bold")
                )                    
                if i == 0:
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                elif i == 1:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                         align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 2:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )     
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )             
                elif i == 3:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                        1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                         align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 4:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
            elif level == 4:
                mild = answer
                draw_circle(-180 + i * 72 ,0,10,"red","white")
                pen.goto(-180 + i * 72 ,-10)
                pen.pencolor("red")
                pen.write(
                    i + 1,
                    align="center",
                    font=("Noto Sans KR", 12, "bold")
                )                    
                if i == 0:
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                elif i == 1:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                         align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 2:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )     
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )             
                elif i == 3:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                        1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                         align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 4:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    ) 
            elif level == 5:
                soup = answer
                draw_circle(-180 + i * 72 ,0,10,"red","white")
                pen.goto(-180 + i * 72 ,-10)
                pen.pencolor("red")
                pen.write(
                    i + 1,
                    align="center",
                    font=("Noto Sans KR", 12, "bold")
                )                    
                if i == 0:
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                elif i == 1:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                         align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 2:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )     
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )             
                elif i == 3:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                        1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                         align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 4:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    ) 
            elif level == 6:
                filling = answer
                draw_circle(-180 + i * 72 ,0,10,"red","white")
                pen.goto(-180 + i * 72 ,-10)
                pen.pencolor("red")
                pen.write(
                    i + 1,
                    align="center",
                    font=("Noto Sans KR", 12, "bold")
                )                    
                if i == 0:
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                elif i == 1:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                         align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 2:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )     
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )             
                elif i == 3:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                        1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                         align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 4:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    ) 
            elif level == 7:
                new = answer
                draw_circle(-180 + i * 72 ,0,10,"red","white")
                pen.goto(-180 + i * 72 ,-10)
                pen.pencolor("red")
                pen.write(
                    i + 1,
                    align="center",
                    font=("Noto Sans KR", 12, "bold")
                )                    
                if i == 0:
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                elif i == 1:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                         align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 2:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )     
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )             
                elif i == 3:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                        1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                         align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 4:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )  
            elif level == 8:
                light = answer
                draw_circle(-180 + i * 72 ,0,10,"red","white")
                pen.goto(-180 + i * 72 ,-10)
                pen.pencolor("red")
                pen.write(
                    i + 1,
                    align="center",
                    font=("Noto Sans KR", 12, "bold")
                )                    
                if i == 0:
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                elif i == 1:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                         3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                         align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 2:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )     
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                         2,
                        align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )             
                elif i == 3:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                        1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                         align="center",
                         font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 4 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 4 * 72 ,-10)
                    pen.write(
                        5,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )
                elif i == 4:
                    draw_circle(-180 + 0 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 0 * 72 ,-10)
                    pen.write(
                         1,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 1 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 1 * 72 ,-10)
                    pen.write(
                        2,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                    )
                    draw_circle(-180 + 2 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 2 * 72 ,-10)
                    pen.write(
                        3,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")
                     )
                    draw_circle(-180 + 3 * 72 ,0,10,"black","white")
                    pen.goto(-180 + 3 * 72 ,-10)
                    pen.write(
                        4,
                        align="center",
                        font=("Noto Sans KR", 12, "bold")  
                    )                                                                                                
                        

def click(x , y):
    global level 
    global eat
    score(x, y)
    next (x, y)
    if level == 9:
        if eat == 0:
            choose(x, y)
 
 
    
        


#================================================================================================================================================================

#제목
    
draw_box(0, 180, 300, 80, "black", "white")

pen.goto(0, 165)
pen.write(
    "음식 추천 프로그램",
    align="center",
    font=("Noto Sans KR", 22, "bold")
)

#시작버튼

draw_box(0, 0, 220, 70 , "blue" , "blue")

pen.goto(0, -15)
pen.pencolor("white")
pen.write(
    "시작하기",
    align="center",
    font=("Noto Sans KR", 20, "bold")
)
pen.pencolor("black")

#다음 화면 넘어가기

screen.onclick(click)


turtle.mainloop()