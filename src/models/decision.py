import pandas as pd

def generate_investment_opinion(financials):
    """재무 데이터를 바탕으로 투자 의견을 자동 생성하는 함수"""
    print("📊 Debug: financials DataFrame")
    print(financials)

    if financials is None or financials.empty:
        return "데이터 오류"

    # "당기순이익"과 "매출액"이 데이터에 있는지 확인
    if "당기순이익" in financials.index and "매출액" in financials.index:
        try:
            # 데이터 추출
            net_profit = financials.loc["당기순이익", "thstrm_amount"]
            sales = financials.loc["매출액", "thstrm_amount"]

            # Series일 경우 첫 번째 값만 가져오기
            if isinstance(net_profit, pd.Series):
                net_profit = net_profit.iloc[0] if not net_profit.empty else 0
            if isinstance(sales, pd.Series):
                sales = sales.iloc[0] if not sales.empty else 0

            # NaN 값 처리
            net_profit = 0 if pd.isna(net_profit) else net_profit
            sales = 0 if pd.isna(sales) else sales

        except Exception as e:
            print(f"⚠️ 변환 오류 발생: {e}")
            return "데이터 오류"

        # 🔥 비교 연산 오류 해결: 단일 값으로 비교
        if net_profit > 0 and sales > 1_000_000_000:
            return "매수 (Strong Buy)"
        elif net_profit > 0:
            return "중립 (Hold)"

    return "매도 (Sell)"
