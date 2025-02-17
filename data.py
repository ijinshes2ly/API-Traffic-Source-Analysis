```python
import pandas as pd

# 하드코딩된 트래픽 소스 데이터 (30일)
data = {
    "Date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "Traffic_Source": [
        "Organic Search", "Direct", "Referral", "Social", "Paid Search"] * 6,
    "Visitors": [
        3200, 2100, 1500, 1800, 1200,
        3300, 2200, 1600, 1900, 1300,
        3400, 2300, 1700, 2000, 1400,
        3500, 2400, 1800, 2100, 1500,
        3600, 2500, 1900, 2200, 1600,
        3700, 2600, 2000, 2300, 1700
    ],
    "Conversion_Rate": [
        3.8, 2.9, 1.5, 2.1, 4.5,
        3.9, 3.0, 1.6, 2.2, 4.6,
        4.0, 3.1, 1.7, 2.3, 4.7,
        4.1, 3.2, 1.8, 2.4, 4.8,
        4.2, 3.3, 1.9, 2.5, 4.9,
        4.3, 3.4, 2.0, 2.6, 5.0
    ]
}

# 데이터프레임 생성 및 CSV 저장
csv_filename = "traffic_source_data.csv"
traffic_data = pd.DataFrame(data)
traffic_data.to_csv(csv_filename, index=False)

print(f"CSV 파일 '{csv_filename}' 저장 완료!")
```
