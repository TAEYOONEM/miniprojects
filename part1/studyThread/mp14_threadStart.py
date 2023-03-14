# 기본 프레서스 하나, 서브스레드 다섯개 동시에 진행
import threading
import time

# Thread를 상속받은 백그라운드 작업 클래스
class BackgroundWorker(threading.Thread) :
    def __init__(self, names: str) -> None:
        super().__init__()
        self._name =f'{threading.current_thread().name} : {names}'
    
    def run(self) -> None :
        print(f'BackgroundWorked Start : {self._name}')
        # time.sleep(2)
        print(f'BackgroundWorked End : {self._name}')

if __name__ == '__main__' :
    print('Main Thread Start') # 기본 프레세스 == 메인 스레드
    for i in range(5) :
        name = f'Sub Thread {i}'
        th = BackgroundWorker(name)
        th.start() # run()
    
    print('Main Thread End')