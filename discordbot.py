import discord
import random
import time
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

#디스코드 개발 토큰
token = os.getenv('TOKEN')

#msg 초기화
msg = None 
x = None

client = discord.Client()

#타자연습 영어 문장들 15개
t = ["Experience is not what happens to a man; it is what a man does with what happens to him.",
     "There is no feeling, except the extremes of fear and grief, that does not find relief in music.",
     "I hear and I forget. I see and I remember. I do and I understand.",
     "If you want to see what children can do, you must stop giving them things.",
     "The man of virtue makes the difficulty to be overcome his first business, and success only a subsequent consideration.",
     "People fail forward to success.",
     "It is wise to apply the oil of refined politeness to the mechanisms of friendship.",
     "Without friends no one would choose to live, though he had all other goods.",
     "Man's feelings are always purest and most glowing in the hour of meeting and of farewell.",
     "This bud of love, by summer's ripening breath, May prove a beauteous flower when next we meet.",
     "Running cross country is the closest man will ever get to flying.",
     "My philosophy is that not only are you responsible for your life, but doing the best at this moment puts you in the best place for the next moment.",
     "He that lives upon hope will die fasting.",
     "It has never been my object to record my dreams, just to realize them."
      ]

#타자연습 한글 문장들 15개
T = ["사랑은 언제까지나 지속되어야 하는 것인가, 아니면 이런 저런 정거장에 멈춰서는 여러 열차와 같은 것인가? 내가 그녀를 사랑한다면 어떻게 그녀를 떠날 수 있나? 그 때 내가 그렇게 느꼈다면, 지금은 왜 아무 것도 느끼지 못할까?",
     "죄를 미워하되 죄인은 사랑하라.",
     "젊은이들은 젊음이 얼마나 힘들고 무시무시할 수 있는지 안다. 그들의 젊음은 다른 모든 사람들에게 허비되는데 그야말로 끔찍한 일이다. 젊은이들에게는 권위도 존경도 없다.",
     "들은 것은 잊어버리고, 본 것은 기억하고 직접 해본 것은 이해한다",
     "아이들이 무엇을 할 수 있는지 확인해보고 싶다면 주는 것을 멈추어 보면 된다.",
     "어진 사람은 난관의 극복을 제일 중요한 일로 생각하고, 성공 여부는 부차적인 것으로 본다.",
     "실패하는 것은 곧 성공으로 한 발짝 더 나아가는 것이다.",
     "우정이라는 기계에 잘 정제된 예의라는 기름을 바르는 것은 현명하다.",
     "모든 것을 가졌다 해도 친구가 없다면, 아무도 살길 원치 않을 것이다.",
     "책은 가장 조용하고 변함 없는 벗이다. 책은 가장 쉽게 다가갈 수 있고 가장 현명한 상담자이자, 가장 인내심 있는 교사이다.",
     "그것은 죽었으면 하고 바라는 사람들이 시간을 죽이기 위해 읽는 책이었다.",
     "인간의 감정은 누군가를 만날 때와 헤어질 때 가장 순수하며 가장 빛난다.",
     "이 사랑의 꽃봉오리는 여름날 바람에 마냥 부풀었다가, 다음 만날 때엔 예쁘게 꽃필 거예요.",
     "일부 과학자들에 따르면 미래는 과거와 똑같을 것이다. 단지 훨씬 값비쌀 뿐이다.",
     "우아함이란 이제 갖 사춘기를 벗어난 이들의 특권이 아니라, 이미 스스로의 미래를 꽉 잡고 있는 이들의 것이다."]

#디스코드 봇 실행시 터미널로 보여주기
class Typewriterbot(discord.Client):
    chatTest = "False"
    channel = "NULL"
    q = "NULL"
    print("debug ready")
    async def on_ready(self):
        game = discord.Game("!문제를 해결")

        await client.change_presence(status=discord.Status.online, activity=game)
        print("Ready to Action...")

    async def on_message(self, message):
       
        if message.author.bot:
            return None


        #기본적인 명령어
        if message.content == '!안녕':
            channel = message.channel
            msg = "안녕"
            await channel.send(msg)
            return None

        if message.content == '!잘가':
            channel = message.channel
            msg = "잘가 ㅠㅠ"
            await channel.send(msg)
            return None
            
        ``
        #명령어 보여주기        
        if message.content == '!명령어':                                    
            channel = message.channel
            msg = "```\n!안녕 - 안녕\n"
            msg += "!잘가 - 잘가 ㅠㅠ\n"
            msg += "!타자연습 - 타자 연습 시작합니다.\n"
            msg += "!타자연습 영어 - 타자 연습 영어 시작합니다.\n"
            msg += "!타자연습 한글 - 타자 연습 한글 시작합니다.\n"
            msg += "!c언어 - 필요한 문법 책 링크를 보여줍니다.\n"
            msg += "!c언어 OO - OO 보여줌\n  예시:!c언어 for\n```"
            await channel.send(msg)
            return None

        
        #c언어 명령어
        if message.content == '!c언어':
            channel = message.channel
            msg = "```\nC언어\n"
            msg += "비쥬얼 스튜디오 설치하기\n https://visualstudio.microsoft.com/ko/downloads/\n"
            msg += "DEV C++ 설치하기\n https://gabii.tistory.com/entry/Dev-C-Dev-C-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-%EB%B0%8F-%EC%84%A4%EC%B9%98\n"
            msg += "변수\n https://thebook.io/006989/ch02/01/\n"
            msg += "함수\n https://thebook.io/006989/ch03/\n"
            msg += "연산자\n https://thebook.io/006989/ch04/\n"
            msg += "조건문\n https://thebook.io/006989/ch05/\n"
            msg += "반복문\n https://thebook.io/006989/ch06/\n"
            msg += "배열\n https://thebook.io/006989/ch07/\n"
            msg += "포인터\n https://thebook.io/006989/ch08/\n\n"
            msg += "링크는 복사 붙여넣기로 사용하실 수 있습니다\n```"
            await channel.send(msg)
            return None

        if message.content == '!c언어 변수':
            channel = message.channel
            msg = "변수\n https://thebook.io/006989/ch02/01/\n"
            await channel.send(msg)
            return None

        if message.content == '!c언어 함수':
            channel = message.channel
            msg = "함수\n https://thebook.io/006989/ch03/\n"
            await channel.send(msg)
            return None

        if message.content == '!c언어 연산자':
            channel = message.channel
            msg = "연산자\n https://thebook.io/006989/ch04/\n"
            await channel.send(msg)
            return None    

        if message.content == '!c언어 조건문':
            channel = message.channel
            msg = "조건문\n https://thebook.io/006989/ch05/\n"
            await channel.send(msg)
            return None            
       
        if message.content == '!c언어 반복문':
            channel = message.channel
            msg = "반복문\n https://thebook.io/006989/ch06/\n"
            await channel.send(msg)
            return None            

        if message.content == '!c언어 배열':
            channel = message.channel
            msg = "배열\n https://thebook.io/006989/ch07/\n"
            await channel.send(msg)
            return None  
            
        if message.content == '!c언어 포인터':
            channel = message.channel
            msg = "포인터\n https://thebook.io/006989/ch08/\n"
            await channel.send(msg)
            return None       
        
        #타자 연습 
        
        if message.content == '!타자연습 영어':                              #타자연습 영어 시작
            channel = message.channel
            msg = "시작\n"
            msg += "<문장>"
            self.chatTest = "True"
            await channel.send(msg)
                                                                  
            self.q = random.choice(t)
            await channel.send("============= 문제 ============\n!정답 입력후 정답을 입력해주세요 예(!정답 Hello world)")
            await channel.send(self.q)
            return None

        if self.chatTest == "True": 
            print(self.chatTest)
            channel = message.channel
            msg = message.content
            
            print(self.q)
            print(message.content)
    
            if '!정답 ' + self.q == message.content:
                await channel.send("정답")
                print("정답")
            else:
                await channel.send("땡")
                print("땡")

            self.chatTest = "False"
            return None
        #타자 시간 재기
            #end = time.time()                                                   #종료시간을 기록
            #et = end - start                                                    #실제시간을 기록
            #~et = format(et, ".2f")                                              #소수점 둘째자리까지만 표시되도록 포멧팅

if __name__ == "__main__":
    client = Typewriterbot()
    client.run(token)    