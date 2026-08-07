from collections import Counter

logs = [
   "ERROR: DB 연결실패" ,
   "WARNING: 메모리 부족" ,
   "ERROR: DB 서버 바이러스" ,
   "ERROR: 타임아웃 발생" ,
   "ERROR: 서버 정상 실행" ,
   "INFO: DB 유저로그인 실패" ,
   "ERROR: 인터넷 서비스 실패" ,
   "CONNECT: 배포 지연" ,
   "ERROR: 인증 무한루프" ,
   "WARNING: 보안 생체인증 불일치" ,
]

# 로그 레벨집계
levels = [log.split(':')[0]  for log in logs ]
lv_count = Counter(levels) 
print(levels) #['ERROR', 'WARNING', 'ERROR', 'ERROR', 'ERROR', 'INFO', 'ERROR', 'CONNECT', 'ERROR', 'WARNING']
print(lv_count) #Counter({'ERROR': 6, 'WARNING': 2, 'INFO': 1, 'CONNECT': 1})
print()

# # 오류 메세지 집계
errors = [log for log in logs  if log.startswith('ERROR')] #ERROR종류 추출 
err_count = Counter(errors)
print(errors)
print(err_count)
print()

print("📋 로그 레벨 분포:")
for level, count in lv_count.most_common():
    print(f"  {level:8s}: {count}건")

print("\n🔴 오류 메시지 TOP 3:")
for msg, count in err_count.most_common(3):
    print(f"  ({count}회) {msg}")




