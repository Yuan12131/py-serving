from http.server import BaseHTTPRequestHandler, HTTPServer # http.server 모듈에서 BaseHTTPRequestHandler와 HTTPServer를 가져오기

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self): #HTTP GET 요청을 처리
        if self.path == '/': # self.path : 요청의 경로 -> 요청 경로가 '/'인 경우
            self.send_response(200) # HTTP 응답의 상태 코드
            self.send_header('Content-Type', 'text/plain') # HTTP 응답 헤더
            self.end_headers() # 응답 헤더의 끝을 나타내기 위해 end_headers를 호출

            # 파일을 텍스트 모드('r')로 열어서 파일 핸들러를 file 변수에 할당
            # with 문은 파일을 열고 사용한 후 자동으로 파일을 닫음 -> 파일 핸들러를 file 변수에 할당하고 as file로 지정
            with open('index.html', 'r', encoding='utf-8') as file:
                # self.wfile.write() 메서드는 웹 브라우저에게 데이터를 보내는 역할 -> UTF-8로 인코딩된 파일 내용을 웹 브라우저에게 전달
                self.wfile.write(file.read().encode('utf-8'))
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