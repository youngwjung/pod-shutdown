import signal
import time
import sys


# 애플리케이션 종료에 필요한 시간
shutdown_time = int(sys.argv[1])


# SIGTERM이 발생할때 실행한 함수
def sigterm_handler(signum, frame):
    print("SIGTERM Received")
    print(f"Application will be shutdown in {shutdown_time}")
    for i in range(shutdown_time):
        print(i+1)
        time.sleep(1)
    print("Application is gracefully shut down")
    quit()


# 비동기 방식으로 SIGTERM 수신
signal.signal(signal.SIGTERM, sigterm_handler)

# SIGTERM이 발생할때 까지 대기
print("Application started")
print("Waiting for SIGTERM")

while True:
    time.sleep(1)
