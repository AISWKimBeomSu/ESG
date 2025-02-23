from src.api.opendart import get_financial_statements
from src.utils.helper import clean_financial_data
from src.models.decision import generate_investment_opinion

# 분석할 기업 리스트 (기업명 + 종목코드)
companies = [
    {"name": "삼성전자", "code": "005930"},
    {"name": "엔씨소프트", "code": "036570"},
    {"name": "넥슨", "code": "225570"},
    {"name": "카카오게임즈", "code": "293490"},
]

def format_number(num):
    """긴 숫자를 '조', '억', '만' 단위로 변환"""
    try:
        num = int(num)
        if num >= 1_0000_0000_0000:
            return f"{num // 1_0000_0000_0000}조 {num % 1_0000_0000_0000 // 1_0000_0000}억"
        elif num >= 1_0000_0000:
            return f"{num // 1_0000_0000}억 {num % 1_0000_0000 // 1_0000}만"
        elif num >= 1_0000:
            return f"{num // 1_0000}만 {num % 1_0000}"
        return str(num)
    except ValueError:
        return "N/A"

for company in companies:
    print(f"\n🔎 {company['name']} 재무 분석 중...")

    # OpenDART API에서 데이터 가져오기
    data = get_financial_statements(company["code"])

    if data is None or data.empty:
        print(f"❌ {company['name']}의 재무 데이터를 찾을 수 없습니다.\n")
        continue

    # 데이터 정리
    clean_data = clean_financial_data(data)
    if clean_data is None or clean_data.empty:
        print(f"❌ {company['name']}의 재무 데이터 정리에 실패했습니다.\n")
        continue

    # 투자 의견 도출
    opinion = generate_investment_opinion(clean_data)

    # 보기 좋게 숫자 변환
    clean_data["thstrm_amount"] = clean_data["thstrm_amount"].apply(format_number)

    # 결과 출력
    print("📊 기업 재무 데이터:")
    print(clean_data.to_string(index=True))  # 표가 잘리면 전체 출력하도록 설정
    print(f"💡 투자 의견: {opinion}\n")
