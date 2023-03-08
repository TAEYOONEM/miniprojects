# NaverApi 클래스 - Open Api : 인터넷을 통해서 데이터를 전달 받음
from urllib.request import Request, urlopen
from urllib.parse import quote
import datetime # 현재시간 사용
import json # 결과는 json으로 return

class NaverApi :
    def __init__(self) -> None:
        print(f"[{datetime.datetime.now()}] Create Naver Api")

    # Naver Api를 호출 함수
    def get_request_url(self,url) :
        req = Request(url)
        # Naver Api 개인별 인증
        req.add_header("X-Naver-Client-Id","ubDfiaP_89JdUJDx2TDx")
        req.add_header("X-Naver-Client-Secret","lH8wLKpSSr")

        try :
            res = urlopen(req) # 요청 결과가 바로 돌아옴
            if res.getcode() == 200 : # respose Ok
                print(f"[{datetime.datetime.now()}] Url Request Succeed")
                return res.read().decode("utf-8")
            else :
                print(f"[{datetime.datetime.now()}] Url Request fail")
                return None                
        except Exception as e:
            print(f"[{datetime.datetime.now()}] 예외발생 : {e}")
            return None
            
    # 호출함수        
    def get_naver_search(self, node, search, start, display) :
        base_url = "https://openapi.naver.com/v1/search"
        node_url = f"/{node}.json" 
        params = f"?query={quote(search)}&start={start}&display={display}"

        url = base_url + node_url + params
        retData = self.get_request_url(url)

        if retData == None :
            return None
        else :
            return json.loads(retData)
                

