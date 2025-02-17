```pyton
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로드
csv_filename = "traffic_source_data.csv"
traffic_data = pd.read_csv(csv_filename)

# 주요 지표 계산
total_visitors = traffic_data["Visitors"].sum()
avg_conversion_rate = round(traffic_data["Conversion_Rate"].mean(), 2)

# 트래픽 소스별 방문자 수 집계
traffic_source_summary = traffic_data.groupby("Traffic_Source")["Visitors"].sum().reset_index()

# 데이터 시각화: 트래픽 소스별 방문자 수
plt.figure(figsize=(8, 5))
plt.bar(traffic_source_summary["Traffic_Source"], traffic_source_summary["Visitors"], color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Traffic Source")
plt.ylabel("Total Visitors")
plt.title("Total Visitors by Traffic Source")
plt.grid(axis='y')
plt.show()

# 트래픽 소스별 평균 전환율 집계
traffic_conversion_summary = traffic_data.groupby("Traffic_Source")["Conversion_Rate"].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(traffic_conversion_summary["Traffic_Source"], traffic_conversion_summary["Conversion_Rate"], color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Traffic Source")
plt.ylabel("Average Conversion Rate (%)")
plt.title("Average Conversion Rate by Traffic Source")
plt.grid(axis='y')
plt.show()

# 주요 지표 출력
summary_metrics = {
    "Total Visitors": total_visitors,
    "Average Conversion Rate (%)": avg_conversion_rate
}

# 데이터프레임 생성 및 출력
summary_df = pd.DataFrame(summary_metrics, index=[0])
print(summary_df)
```
