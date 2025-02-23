import pandas as pd

def clean_financial_data(data):
    """재무 데이터를 정리하는 함수"""
    print(f"📊 Debug: data.columns 확인 -> {data.columns}")

    if data.empty:
        return None

    key_metrics = ["자산총계", "부채총계", "매출액", "영업이익", "당기순이익"]

    try:
        # 새로운 복사본 생성 (SettingWithCopyWarning 방지)
        filtered_data = data[data["account_nm"].isin(key_metrics)].copy()

        # 숫자 변환 (쉼표, 공백 등 제거)
        filtered_data["thstrm_amount"] = (
            filtered_data["thstrm_amount"]
            .astype(str)  # 문자열 변환
            .str.replace(r"[^\d-]", "", regex=True)  # 숫자와 "-" 제외한 문자 제거
            .replace("", "0")  # 빈 값은 0으로 대체
            .astype(float)  # float 변환
            .astype(int)  # int 변환
        )

        # "account_nm"을 인덱스로 설정
        financials = filtered_data.set_index("account_nm")[["sj_div", "thstrm_amount"]]
        return financials

    except Exception as e:
        print(f"⚠️ 데이터 정리 중 오류 발생: {e}")
        return None
