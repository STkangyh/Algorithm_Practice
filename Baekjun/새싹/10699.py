from datetime import datetime as dt
#from pytz import timezone
#T = datetime.now(timezone('Asia/Seoul')) 원하는 도시의 시간대로 설정
#print(f"{T.year}-{T.month}-{T.day}") 문자열로 print하는 format
print(str(dt.now())[:10]) #10글자만 출력하도록 설정
#d=datetime.date.today()  오늘 날짜의 date 객체 생성
#print(d.isoformat())  date 객체의 정보를 'YYYY-MM-DD'형태의 문자열로 반환하는 메서드