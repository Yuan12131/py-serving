from http.server import BaseHTTPRequestHandler, HTTPServer # http.server 모듈에서 BaseHTTPRequestHandler와 HTTPServer를 가져오기

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self): #HTTP GET 요청을 처리
        if self.path == '/': # self.path : 요청의 경로 -> 요청 경로가 '/'인 경우
            self.send_response(200) # HTTP 응답의 상태 코드
            self.send_header('Content-Type', 'text/plain') # HTTP 응답 헤더
            self.end_headers() # 응답 헤더의 끝을 나타내기 위해 end_headers를 호출
            self.wfile.write(bytes('hello', 'utf-8')) # self.wfile.write를 사용하여 응답 데이터 전송
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Not Found', 'utf-8'))

# 웹 서버를 실행하기 위한 run 함수 
# 서버 주소를 ('', 8080)으로 설정하고, 이 주소에서 8080 포트에서 서버를 시작 -> serve_forever 메서드를 호출하여 서버를 시작하고   계속 실행
if __name__ == '__main__':
  server_address = ('', 8080) # 서버 주소를 지정 -> 지정된 포트(8080)에서 서버를 실행
  httpd = HTTPServer(server_address, MyHandler)
  print('Starting server on port 8080')
  httpd.serve_forever() # serve_forever 메서드를 호출하여 서버를 시작하고 계속 실행