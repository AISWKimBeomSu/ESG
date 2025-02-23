import os
from dotenv import load_dotenv
import OpenDartReader

load_dotenv()

API_KEY = os.getenv("DART_API_KEY")  # .env 파일에서 API 키 로드
dart = OpenDartReader(API_KEY)  # OpenDartReader 객체 생성
