## API호출 관련 모듈(OpenDART API와 통신하여 데이터를 가져옴)
# 기존 requests.get() 방식 → OpenDartReader 라이브러리 사용하여 코드 간소화
# 종목코드(예: 005930)로 바로 조회 가능
import OpenDartReader
from src.utils.config import dart  # OpenDartReader 객체 가져오기

def get_financial_statements(company_name, year=2023):
    """
    특정 기업의 재무제표 데이터를 OpenDartReader를 이용해 가져오는 함수
    """
    try:
        data = dart.finstate(company_name, year)
        return data
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return None

# 삼성전자 2023년 재무제표 조회 예제
if __name__ == "__main__":
    data = get_financial_statements("삼성전자", 2023)
    print(data.head())  # DataFrame 형태로 반환됨
