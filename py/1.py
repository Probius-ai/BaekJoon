### 필요 라이브러리
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from IPython.display import clear_output

# 경로 지정
#path = '/opt/conda/proj_1/model_code/'
path = 'C:/Users/ais/Desktop/'
alcohol = pd.read_excel(path + "project/data/alcohol.xlsx")
post = pd.read_excel(path + "project/data/post.xlsx")
code = pd.read_excel(path + "project/data/code.xlsx")
store = pd.read_excel(path + "project/data/store.xlsx")
center_id = pd.read_excel(path + "project/data/center_id.xlsx")
data_center = pd.read_excel(path + "project/data/model_dataset.xlsx")
data = pd.read_excel(path + "project/raw_data/select_data.xlsx")

# GUT_DT 컬럼을 문자열로 변환
data['GUT_DT'] = data['GUT_DT'].astype(str)

# GUT_DT 값을 'YYYY-MM-DD-HH-MM-SS' 형식으로 변환하는 함수 정의
def format_datetime(dt_str):
    return f"{dt_str[:4]}-{dt_str[4:6]}-{dt_str[6:8]}-{dt_str[8:10]}-{dt_str[10:12]}-{dt_str[12:]}"

# GUT_DT 컬럼에 변환 함수 적용
data['GUT_DT'] = data['GUT_DT'].apply(format_datetime)

# GUT_DT 컬럼을 datetime 형식으로 변환
data['GUT_DT'] = pd.to_datetime(data['GUT_DT'], format='%Y-%m-%d-%H-%M-%S', errors='coerce')

# 데이터에서 연도와 월 추출하여 'Year_Month' 컬럼 추가
data['Year_Month'] = data['GUT_DT'].dt.to_period('M')

# Year_Month를 YYYYMM 형식으로 변환
data['Year_Month'] = data['Year_Month'].dt.strftime('%Y%m')

# 시간(hour)만 추출하여 'hour' 컬럼 추가
data['hour'] = data['GUT_DT'].dt.hour

# hour 열에서 NaN 값이 있는 행 삭제
data = data.dropna(subset=['hour'])

# 'hour' 컬럼을 int 형식으로 변환
data['hour'] = data['hour'].astype(int)

# RSAC_GUT_WARD_OGID 열을 문자열로 변환
data['RSAC_GUT_WARD_OGID'] = data['RSAC_GUT_WARD_OGID'].astype(str)

# '41'경기도 데이터만 필터링
data = data[data['RSAC_GUT_WARD_OGID'].str.startswith('41')]

model_data = data[['CPTC_WARD_ORGN', 'CPTC_WARD_OGID', 'RSAC_GUT_WARD_OGID', 'RSAC_GUT_WARD_ORGN',
                      'Year_Month','GUT_DT','GUT_CO', 'TRNF_CO', 'GUT_MTHV', 'GUT_YEAR', 'GUT_MTHV','GUT_DYVL', 'GUT_TMSL', 'ARHP_TMSL','hour']]

# '금오119안전센터 (4조2교대)'를 '금오119안전센터'로 변경
model_data['RSAC_GUT_WARD_ORGN'] = model_data['RSAC_GUT_WARD_ORGN'].replace('금오119안전센터 (4조2교대)', '금오119안전센터')

# 'RSAC_GUT_WARD_OGID' 열에서 4111402 값을 4111113으로 변경
model_data['RSAC_GUT_WARD_OGID'] = model_data['RSAC_GUT_WARD_OGID'].replace(4111402, 4111113)

model_set = data_center[['center_id', 'juris_station_nm', 'center_nm']]

# center_id와 RSAC_GUT_WARD_OGID를 int형으로 변환
model_set['center_id'] = model_set['center_id'].astype(int)
model_data['RSAC_GUT_WARD_OGID'] = model_data['RSAC_GUT_WARD_OGID'].astype(int)

# 두 DataFrame 병합
df = pd.merge(model_set, model_data, left_on='center_id', right_on='RSAC_GUT_WARD_OGID', how='left')
df = df.drop(columns=['RSAC_GUT_WARD_OGID','CPTC_WARD_ORGN','CPTC_WARD_OGID'])

# NaN 값을 0으로 대체한 후 각 열을 정수형으로 변환
df['Year_Month'] = df['Year_Month'].fillna(0).astype('int64')  # Year_Month를 int64로 변환
df['GUT_CO'] = df['GUT_CO'].fillna(0).astype('int64')  # 결측값을 0으로 대체하고 int64로 변환
df['TRNF_CO'] = df['TRNF_CO'].fillna(0).astype('int64')  # 결측값을 0으로 대체하고 int64로 변환
df['GUT_YEAR'] = df['GUT_YEAR'].fillna(0).astype('int64')  # 결측값을 0으로 대체하고 int64로 변환
df['GUT_MTHV'] = df['GUT_MTHV'].fillna(0).astype('int64')  # 결측값을 0으로 대체하고 int64로 변환
df['GUT_DYVL'] = df['GUT_DYVL'].fillna(0).astype('int64')  # 결측값을 0으로 대체하고 int64로 변환
df['GUT_TMSL'] = df['GUT_TMSL'].fillna(0).astype('int64')  # 결측값을 0으로 대체하고 int64로 변환
df['ARHP_TMSL'] = df['ARHP_TMSL'].fillna(0).astype('int64')  # 결측값을 0으로 대체하고 int64로 변환
df['hour'] = df['hour'].fillna(0).astype('int64')
df['RSAC_GUT_WARD_ORGN'] = df['RSAC_GUT_WARD_ORGN'].fillna(0)

df['GUT_DT'] = df['GUT_DT'].fillna(pd.Timestamp('2024-01-01 00:00:00'))

"""### 7월 데이터"""

#데이터프레임 복사본 생성
df0 = df.copy()

# 7월 데이터 필터링 및 집계
july_data = df0[df0['Year_Month'] == 202407]  # 2024년 7월 데이터 선택
july_aggregated = july_data.groupby(['center_id', 'center_nm']).agg({
    'GUT_CO': 'sum',           # 출동건수 합산
    'TRNF_CO': 'sum'           # 이송건수 합산
}).reset_index()
july_aggregated['mon_trdi_count'] = july_aggregated['TRNF_CO'] / july_aggregated['GUT_CO']
july_aggregated = july_aggregated.rename(columns={'TRNF_CO': 'mon_tr_count'})
july_aggregated['Year_Month'] = 202407  # Year_Month 열 추가
july_aggregated = july_aggregated.drop(columns=['GUT_CO'])

# 최근 6개월(2~7월) 데이터 필터링 및 집계
recent_months = [202402, 202403, 202404, 202405, 202406, 202407]  # 2024년 2월부터 7월까지의 월
recent_data = df0[df0['Year_Month'].isin(recent_months)]  # Year_Month로 필터링
recent_aggregated = recent_data.groupby(['center_id', 'center_nm']).agg({
    'GUT_CO': 'sum',           # 출동건수 합산
    'TRNF_CO': 'sum'           # 이송건수 합산
}).reset_index()
month_count = 6  # 6개월 평균
recent_aggregated['GUT_CO'] /= month_count
recent_aggregated['TRNF_CO'] /= month_count
recent_aggregated['6mon_trdi_avg'] = recent_aggregated['TRNF_CO'] / recent_aggregated['GUT_CO']
recent_aggregated = recent_aggregated.rename(columns={'TRNF_CO': '6mon_tr_avg'})
recent_aggregated['Year_Month'] = '202402-202407'  # Year_Month 범위 표시
recent_aggregated = recent_aggregated.drop(columns=['GUT_CO'])

# 전체 센터 목록 가져오기
all_centers = df[['center_id', 'center_nm']].drop_duplicates()

# 7월 데이터와 최근 6개월 데이터를 merge하여 결합
final_result = pd.merge(all_centers, july_aggregated, on=['center_id', 'center_nm'], how='left')
final_result = pd.merge(final_result, recent_aggregated, on=['center_id', 'center_nm'], how='left', suffixes=('', '_6month'))

# 결측값을 0으로 채우기
final_result.fillna({'mon_tr_count': 0, 'mon_trdi_count': 0, '6mon_tr_avg': 0, '6mon_trdi_avg': 0}, inplace=True)

# 6시간 단위 컬럼 생성 (hour 컬럼 사용)
def get_time_slot(hour):
    if 0 <= hour < 6:
        return '0-5'
    elif 6 <= hour < 12:
        return '6-11'
    elif 12 <= hour < 18:
        return '12-17'
    else:
        return '18-23'

# 7월 데이터에서 6시간 단위 컬럼 추가
july_data['해당월6시간단위'] = july_data['hour'].apply(get_time_slot)

# 6시간 단위로 출동 건수 집계
july_grouped = july_data.groupby(['center_id', 'center_nm', '해당월6시간단위']).agg({
    'GUT_CO': 'sum'  # 출동건수 합산
}).reset_index()

# 6시간 단위 평균 출동 건수 계산
july_average = july_grouped.groupby(['center_id', 'center_nm']).agg({
    'GUT_CO': 'mean'  # 6시간 단위 평균 출동건수
}).reset_index().rename(columns={'GUT_CO': '6시간단위_평균출동건수'})

# 최대 출동 건수 시간대 찾기
max_time_july = july_grouped.loc[july_grouped.groupby(['center_id', 'center_nm'])['GUT_CO'].idxmax()]

# 최대 출동 건수의 해당 월 평균 출동 건수 계산
max_time_july = max_time_july.rename(columns={'GUT_CO': '최대출동건수'})
max_time_july = pd.merge(max_time_july, july_average, on=['center_id', 'center_nm'], how='left')

# 비율 계산 (최대출동건수 / 6시간단위 평균 출동 건수)
max_time_july['mon_di_avg'] = max_time_july['최대출동건수'] / max_time_july['6시간단위_평균출동건수']

# 6mon_di_avg 계산 추가
max_time_july['6mon_di_avg'] = max_time_july['최대출동건수'] / max_time_july['6시간단위_평균출동건수']

# 결과에 필요한 컬럼만 선택하고 'Year_Month' 열 추가
result = max_time_july[['center_id', 'center_nm', '해당월6시간단위', 'mon_di_avg', '6mon_di_avg']]
result['Year_Month'] = 202407  # Year_Month 추가

# 전체 센터 목록에서 누락된 센터 추가
existing_centers = result['center_id'].unique()
missing_centers = set(all_centers['center_id']) - set(existing_centers)

for missing_center in missing_centers:
    center_name = df[df['center_id'] == missing_center]['center_nm'].values[0] if not df[df['center_id'] == missing_center].empty else 'Missing Center'
    new_row = {
        'center_id': missing_center,
        'center_nm': center_name,
        '해당월6시간단위': '0-5',  # 적절한 값 설정
        'mon_di_avg': 0,  # 비율을 0으로 설정
        '6mon_di_avg': 0,  # 비율을 0으로 설정
        'Year_Month': 202407  # Year_Month 설정
    }
    result = pd.concat([result, pd.DataFrame([new_row])], ignore_index=True)

# 최종 결과 생성
final_result_max = pd.merge(final_result, result, on=['center_id', 'center_nm', 'Year_Month'], how='left')

# 결측값을 0으로 채우기
final_result_max.fillna({'mon_tr_count': 0, 'mon_trdi_count': 0, '6mon_tr_avg': 0, '6mon_trdi_avg': 0, 'mon_di_avg': 0, '6mon_di_avg': 0}, inplace=True)

# 'Year_Month' 열의 NaN 값을 202407로 채우고 정수형으로 변환
final_result_max['Year_Month'] = final_result_max['Year_Month'].fillna(202407).astype(int)

# 최종 결과 출력
final_merged_result=final_result_max[['center_id', 'center_nm', 'mon_tr_count', 'mon_trdi_count', '6mon_tr_avg', '6mon_trdi_avg', '해당월6시간단위', 'mon_di_avg', '6mon_di_avg', 'Year_Month']]
final_merged_result = final_merged_result.drop(columns=['해당월6시간단위'])

"""### 8월 데이터
####  이송건수
"""

import pandas as pd

# 8월 데이터 필터링 및 집계
august_data = df[df['Year_Month'] == 202408]  # 2024년 8월 데이터 선택
august_aggregated = august_data.groupby(['center_id', 'center_nm']).agg({
    'GUT_CO': 'sum',           # 출동건수 합산
    'TRNF_CO': 'sum'           # 이송건수 합산
}).reset_index()
august_aggregated['mon_trdi_count'] = august_aggregated['TRNF_CO'] / august_aggregated['GUT_CO']
august_aggregated = august_aggregated.rename(columns={'TRNF_CO': 'mon_tr_count'})
august_aggregated['Year_Month'] = 202408  # Year_Month 열 추가
august_aggregated = august_aggregated.drop(columns=['GUT_CO'])

# 최근 6개월(2~7월) 데이터 필터링 및 집계
recent_months = [202402, 202403, 202404, 202405, 202406, 202407]  # 2024년 2월부터 7월까지의 월
recent_data = df[df['Year_Month'].isin(recent_months)]  # Year_Month로 필터링
recent_aggregated = recent_data.groupby(['center_id', 'center_nm']).agg({
    'GUT_CO': 'sum',           # 출동건수 합산
    'TRNF_CO': 'sum'           # 이송건수 합산
}).reset_index()
month_count = 6  # 6개월 평균
recent_aggregated['GUT_CO'] /= month_count
recent_aggregated['TRNF_CO'] /= month_count
recent_aggregated['6mon_trdi_avg'] = recent_aggregated['TRNF_CO'] / recent_aggregated['GUT_CO']
recent_aggregated = recent_aggregated.rename(columns={'TRNF_CO': '6mon_tr_avg'})
recent_aggregated['Year_Month'] = '202402-202407'  # Year_Month 범위 표시
recent_aggregated = recent_aggregated.drop(columns=['GUT_CO'])

# 모든 center_id를 포함한 데이터프레임 생성
all_centers = df[['center_id', 'center_nm']].drop_duplicates()

# 8월 데이터와 최근 6개월 데이터를 merge하여 결합
final_result1 = pd.merge(all_centers, august_aggregated, on=['center_id', 'center_nm'], how='left')
final_result1 = pd.merge(final_result1, recent_aggregated, on=['center_id', 'center_nm'], how='left', suffixes=('', '_6month'))

# 결측값을 0으로 채우기
final_result1.fillna({'mon_tr_count': 0, 'mon_trdi_count': 0, '6mon_tr_avg': 0, '6mon_trdi_avg': 0}, inplace=True)

# 컬럼 순서 변경
final_result1 = final_result1[['center_id', 'center_nm', 'Year_Month', 'mon_tr_count', 'mon_trdi_count', '6mon_tr_avg', '6mon_trdi_avg']]

# center_id 기준으로 오름차순 정렬
final_result1 = final_result1.sort_values(by='center_id').reset_index(drop=True)

"""#### (해당 월) 6시간 단위 별 최대 출동 시간대의 해당월 평균 출동 건수/ 6시간 단위 별 출동건수 평균"""

import pandas as pd

# df의 복사본 생성
df1 = df.copy()

# 8월 데이터 필터링
august_data = df1[df1['Year_Month'] == 202408]  # 2024년 8월 데이터 선택

# 6시간 단위 컬럼 생성 (hour 컬럼 사용)
def get_time_slot(hour):
    if 0 <= hour < 6:
        return '0-5'
    elif 6 <= hour < 12:
        return '6-11'
    elif 12 <= hour < 18:
        return '12-17'
    else:
        return '18-23'

# 'hour' 컬럼을 기반으로 6시간 단위 컬럼 추가
august_data['해당월6시간단위'] = august_data['hour'].apply(get_time_slot)

# 6시간 단위로 출동 건수 집계
august_grouped = august_data.groupby(['center_id', 'center_nm', '해당월6시간단위']).agg({
    'GUT_CO': 'sum'  # 출동건수 합산
}).reset_index()

# 6시간 단위 평균 출동 건수 계산
august_average = august_grouped.groupby(['center_id', 'center_nm']).agg({
    'GUT_CO': 'mean'  # 6시간 단위 평균 출동건수
}).reset_index().rename(columns={'GUT_CO': '6시간단위_평균출동건수'})

# 최대 출동 건수 시간대 찾기
max_time_august = august_grouped.loc[august_grouped.groupby(['center_id', 'center_nm'])['GUT_CO'].idxmax()]

# 최대 출동 건수의 해당 월 평균 출동 건수 계산
max_time_august = max_time_august.rename(columns={'GUT_CO': '최대출동건수'})
max_time_august = pd.merge(max_time_august, august_average, on=['center_id', 'center_nm'], how='left')

# 비율 계산 (최대출동건수 / 6시간단위 평균 출동 건수)
max_time_august['mon_di_avg'] = max_time_august['최대출동건수'] / max_time_august['6시간단위_평균출동건수']

# 필요한 컬럼만 선택하고 'Year_Month' 열 추가
result1 = max_time_august[['center_id', 'center_nm', '해당월6시간단위', 'mon_di_avg']]
result1['Year_Month'] = 202408  # Year_Month 추가

# 전체 센터 목록 가져오기
all_centers = df[['center_id', 'center_nm']].drop_duplicates()

# 고유 center_id의 개수 확인
existing_centers = result1['center_id'].unique()

# 모든 센터 ID 리스트에서 누락된 센터 ID 찾기
missing_centers = set(all_centers['center_id']) - set(existing_centers)

# 누락된 센터 추가
for missing_center in missing_centers:
    # 센터 이름을 df에서 찾기
    center_name = df[df['center_id'] == missing_center]['center_nm'].values[0] if not df[df['center_id'] == missing_center].empty else 'Missing Center'

    # 데이터프레임에 추가할 딕셔너리 생성
    new_row = {
        'center_id': missing_center,
        'center_nm': center_name,
        '해당월6시간단위': '0-5',  # 적절한 값 설정
        'mon_di_avg': 0,  # 비율을 0으로 설정
        'Year_Month': 202408  # Year_Month 설정
    }

    # 새로운 행을 데이터프레임에 추가
    result1 = pd.concat([result1, pd.DataFrame([new_row])], ignore_index=True)

"""#### (최근 6개월) 6시간 단위 별 최대 출동 시간대의 월 평균 출동 건수/6시간 단위 별 출동건수 평균"""

import pandas as pd

# 데이터 복사
df2 = df.copy()

# 최근 6개월 데이터 필터링 (2024년 2월부터 7월까지)
recent_six_months = df2[df2['Year_Month'].between(202402, 202407)]

# 6시간 단위 컬럼 생성
def get_time_slot(hour):
    if 0 <= hour < 6:
        return '0-5'
    elif 6 <= hour < 12:
        return '6-11'
    elif 12 <= hour < 18:
        return '12-17'
    else:
        return '18-23'

# 'hour' 컬럼이 있다고 가정하고 6시간 단위 컬럼 추가
recent_six_months['6시간단위'] = recent_six_months['hour'].apply(get_time_slot)

# 월별 6시간 단위 출동 건수 합계 계산
monthly_grouped = recent_six_months.groupby(['center_id', 'center_nm', '6시간단위', 'Year_Month']).agg({
    'GUT_CO': 'sum'  # 출동 건수 합계
}).reset_index()

# 각 센터별로 6시간 단위에서 최대 출동 건수 시간대 찾기
max_time_grouped = monthly_grouped.loc[monthly_grouped.groupby(['center_id', 'center_nm', 'Year_Month'])['GUT_CO'].idxmax()]

# 최대 출동 시간대의 월 평균 출동 건수 계산
max_time_avg = max_time_grouped.groupby(['center_id', 'center_nm', '6시간단위']).agg({
    'GUT_CO': 'mean'  # 각 시간대별 월 평균 출동 건수
}).reset_index().rename(columns={'GUT_CO': '6시간단위_최대출동_월평균'})

# 6시간 단위 출동 건수의 전체 평균 계산 (6개월간 평균)
time_slot_avg = monthly_grouped.groupby(['center_id', 'center_nm', '6시간단위']).agg({
    'GUT_CO': 'mean'  # 6시간 단위 평균 출동 건수 (전체 평균)
}).reset_index().rename(columns={'GUT_CO': '6시간단위_평균출동건수'})

# 두 가지 계산된 데이터 병합
result = pd.merge(max_time_avg, time_slot_avg, on=['center_id', 'center_nm', '6시간단위'], how='outer')

# 전체 센터 목록 가져오기
all_centers = df[['center_id', 'center_nm']].drop_duplicates()

# 전체 센터 목록과 계산된 결과 병합 (left join)
result = pd.merge(all_centers, result, on=['center_id', 'center_nm'], how='left')

# 6시간 단위의 월 평균 출동 건수와 6시간 단위 평균 출동 건수의 비율을 계산하여 새로운 컬럼 생성
result['6mon_di_avg'] = result['6시간단위_최대출동_월평균'] / result['6시간단위_평균출동건수']

# NaN 값을 0으로 대체
result['6mon_di_avg'] = result['6mon_di_avg'].fillna(0)

# 필요한 컬럼만 선택
final_result = result[['center_id', 'center_nm', '6시간단위', '6mon_di_avg']]

# center_id별로 6mon_di_avg가 최대인 행 선택
final_result_max1 = final_result.loc[final_result.groupby('center_id')['6mon_di_avg'].idxmax()]

# Year_Month 컬럼 추가
final_result_max1['Year_Month'] = 202408

"""#### 8월 테이블 결합"""

# final_result1과 result를 먼저 병합
merged_data1 = pd.merge(final_result1, result1, on=['center_id', 'center_nm'], how='left')

# 위에서 병합된 데이터에 final_result_max를 추가로 병합
final_merged_result1 = pd.merge(merged_data1, final_result_max1, on=['center_id', 'center_nm'], how='left')

# '6시간단위', 'Year_Month_x', 'Year_Month_y' 컬럼 삭제
final_merged_result1 = final_merged_result1.drop(columns=['6시간단위', 'Year_Month_x', 'Year_Month_y','해당월6시간단위'])

"""### 7,8월 데이터 결합 결합"""

# final_result와 final_result1을 수직으로 결합
final_combined = pd.concat([final_merged_result, final_merged_result1], ignore_index=True)

"""# 외부데이터

### 음주율

#### 시군구명 컬럼 결합
"""

# 시군구명 컬럼 생성 (구가 없으면 시군명만, 구가 있으면 시군명 + 구명)
alcohol['시군구명'] = alcohol.apply(
    lambda row: row['sigun_nm'] if pd.isna(row['gu_nm']) else f"{row['sigun_nm']} {row['gu_nm']}",
    axis=1
)

# '년도' 컬럼 삭제 후, 시군구별로 나머지 컬럼들의 평균 계산
alcohol = alcohol.drop(columns=['year'])

# 시군구별로 평균 계산
alcohol = alcohol.groupby('시군구명').mean(numeric_only=True).reset_index()

"""#### 행정동_법정동코드 결합"""

# 두 테이블 간의 조인
merged_alcohol = pd.merge(alcohol, code[['시군구명', '행정동코드', '법정동코드']], on='시군구명', how='left')

"""### 음식점 데이터

#### 음식점(술집)수집데이터_전처리
"""

# 영업상태가 '폐업'인 행 삭제
store = store[store['영업상태명'] != '폐업']

"""##### NA 전처리"""

# 폐업일자, 다중이용업소여부, 총시설규모(㎡), 위생업종명 컬럼 제거
store = store.drop(columns=['폐업일자', '다중이용업소여부', '총시설규모(㎡)', '위생업종명'])

"""##### 중복값 처리"""

# 사업장명과 소재지우편번호가 같은 경우 중복된 행 제거
df_deduplicated = store.drop_duplicates(subset=['사업장명', '우편번호'])

"""## 우편번호"""

post_selected = post[['시군구','우편번호', '법정동코드', '법정동명', '행정동명']]

"""### 데이터 결합"""

# 데이터 결합
post_merged_data = pd.merge(df_deduplicated, post_selected[['시군구', '우편번호', '법정동코드', '법정동명', '행정동명']], on='우편번호', how='left')

# 시군구와 시군명에서 '시'까지만 비교하여 다른 경우 제거
post_merged_data = post_merged_data[post_merged_data['시군구'].str[:2] == post_merged_data['시군명'].str[:2]]

# '우편번호'가 같고 '사업장명'이 같은 경우만 중복으로 간주하고 제거
merge_data_post = post_merged_data.drop_duplicates(subset=['우편번호', '사업장명'], keep='first')

"""### 우편번호 결합 데이터 결측값"""

# 법정동코드가 null인 행 제거
merge_data_post = merge_data_post.dropna(subset=['법정동코드'])

"""## 행정동코드

### 경기도 데이터 가공
"""

# 지역에 따른 필터링

kyoungi_code = code[code['시도명'].str[0:3] == '경기도']

# 필요없는 컬럼 삭제

kyoungi_code.drop(columns = ['생성일자' , '말소일자'] , inplace = True)

# 읍면동명 컬럼을 행정동명으로 이름 변경
kyoungi_code.rename(columns={'읍면동명': '행정동명'}, inplace=True)
kyoungi_code.rename(columns={'동리명': '법정동명'}, inplace=True)

"""### 경기도 행정동코드 데이터 저장

### 우편데이터 결측값처리과정
"""

# 필요한 컬럼만 추출
kyoungi_subset = kyoungi_code[['법정동코드', '법정동명', '행정동명']]

# merge_data_post와 kyoungi_subset 데이터를 법정동코드를 기준으로 병합
merge_data_post = merge_data_post.merge(kyoungi_subset, on='법정동코드', how='left', suffixes=('', '_from_kyoungi'))

# 법정동명과 행정동명의 결측값을 kyoungi_subset에서 가져온 값으로 채움|
merge_data_post['법정동명'].fillna(merge_data_post['법정동명_from_kyoungi'], inplace=True)
merge_data_post['행정동명'].fillna(merge_data_post['행정동명_from_kyoungi'], inplace=True)

# 불필요한 보조 컬럼 삭제
merge_data_post.drop(columns=['법정동명_from_kyoungi', '행정동명_from_kyoungi'], inplace=True)

"""### 행정동코드 결합"""

# merge_data_post 데이터프레임에 kyoungi_code의 행정동코드를 left join으로 병합
merged_data = pd.merge(
    merge_data_post,
    kyoungi_code[['행정동코드', '행정동명','법정동코드','법정동명']],
    on='법정동코드',
how='left'
)

# '우편번호'가 같고 '사업장명'이 같은 경우만 중복으로 간주하고 제거
merged_data_code = merged_data.drop_duplicates(subset=['우편번호', '사업장명'], keep='first')

# `_x`가 포함된 컬럼 삭제
drop_merge_data2 = merged_data.drop(columns=[col for col in merged_data.columns if '_x' in col])

# `_y`가 포함된 컬럼을 찾아 접미사를 제거하고, 컬럼명이 중복되지 않도록 처리
drop_merge_data2.columns = [
    col.replace('_y', '') if '_y' in col else col for col in drop_merge_data2.columns
]

"""#### 결측값처리"""

# 김포2동에 해당하는 행정동코드 수동으로 입력 (4157056000)
drop_merge_data2.loc[(drop_merge_data2['행정동명'] == '김포2동') & (drop_merge_data2['행정동코드'].isnull()), '행정동코드'] = '4157056000'

# '우편번호'가 같고 '사업장명'이 같은 경우만 중복으로 간주하고 제거
post_merge_data = drop_merge_data2.drop_duplicates(subset=['우편번호', '사업장명'], keep='first')

"""## 센터와 결합"""

# 센터 아이디 데이터를 행정동 , 법정동으로 분리한다.

center_id_han = center_id.drop(columns = ['법정동코드']).drop_duplicates(subset = ['행정동코드'])
center_id_bob = center_id.drop(columns = ['행정동코드']).drop_duplicates(subset = ['법정동코드'])

# 메인 데이터를 행정동 법정동으로 분리한다.

# 행정동 코드가 있는 데이터
main_data_han = post_merge_data[post_merge_data['행정동코드'].notna()]
main_data_bob = post_merge_data[post_merge_data['법정동코드'].notna()]

# 각 행정동 , 법정동 대로 합병

cols_han = ['juris_station_nm' , 'center_nm' , 'location' , '행정동코드']
cols_bob = ['juris_station_nm' , 'center_nm' , 'location' , '법정동코드']

merged_main_data_han = pd.merge(left = main_data_han , right = center_id_han[cols_han] , on = '행정동코드' , how = 'left')
merged_main_data_bob = pd.merge(left = main_data_bob , right = center_id_bob[cols_bob] , on = '법정동코드' , how = 'left')

# 합병

merged_main_data = pd.concat([merged_main_data_han , merged_main_data_bob] , axis = 0)

"""### 결합후 중복값 처리"""

# 1. 행정동코드와 사업장명 컬럼에서 중복된 행을 찾아 필터링
duplicated_rows = merged_main_data[merged_main_data.duplicated(subset=['행정동코드', '사업장명'], keep=False)]

# 2. 중복된 행 중 center_nm이 null인 행은 삭제하고, null이 아닌 경우는 남기기
# 먼저 null이 아닌 값들을 우선으로 남기고, null 값인 것들은 제거
duplicated_resolved = duplicated_rows.sort_values(by='center_nm', na_position='last').drop_duplicates(subset=['행정동코드', '사업장명'], keep='first')

# 데이터프레임 병합을 통해 center_id 추가
duplicated_resolved = duplicated_resolved.merge(
    data_center[['center_id', 'juris_station_nm', 'center_nm']],
    on=['juris_station_nm', 'center_nm'],
    how='left'
)

"""## 음주율과 결합"""

merged_df = pd.merge(duplicated_resolved, merged_alcohol, on=['행정동코드', '법정동코드'], how='outer')

"""### 음식점 가공"""

# center_id로 그룹화하고 사업장명을 기준으로 개수 세기
business_count_per_center = merged_df.groupby('center_id')['사업장명'].count().reset_index()

# 컬럼 이름 변경 (가독성을 위해)
business_count_per_center.columns = ['center_id', '음식점수']

# 기존 데이터에 음식점수 컬럼 추가 (center_id 기준으로 병합)
data4 = pd.merge(merged_df, business_count_per_center, on='center_id', how='left')

# '음식점수' 컬럼의 널값을 0으로 대체
data4['음식점수'] = data4['음식점수'].fillna(0)

# '음식점수' 컬럼을 int64로 변환
data4['음식점수'] = data4['음식점수'].astype(int)

# '음식점수' 컬럼명을 'store_cn'으로 변경
data4.rename(columns={'음식점수': 'store_cn'}, inplace=True)

"""### 음주율 널값 처리"""

# 1. 행정동코드를 문자열로 변환하고, 앞의 5자리만 추출
data4['행정동코드'] = data4['행정동코드'].astype(str)
data4['행정동코드_5자리'] = data4['행정동코드'].str[:5]

# 2. 널값을 가진 행 추출
null_rows = data4[data4[['rept_cnt', 'adjst_rate', 'std_err', 'std_rate', 'std_std_err', '시군구명']].isnull().any(axis=1)]

# 3. 널값이 없는 데이터 중 동일한 행정동코드의 앞 5자리로 채우기
for idx, row in null_rows.iterrows():
    # 동일한 행정동코드 5자리에서 가장 유사한 행 찾기
    similar_rows = data4[(data4['행정동코드_5자리'] == row['행정동코드_5자리']) &
                          data4[['rept_cnt', 'adjst_rate', 'std_err', 'std_rate', 'std_std_err']].notnull().all(axis=1)]

    if not similar_rows.empty:
        closest_row = similar_rows.iloc[0]  # 가장 가까운 행 선택
        # Fill missing values
        data4.loc[idx, ['rept_cnt', 'adjst_rate', 'std_err', 'std_rate', 'std_std_err']] = closest_row[['rept_cnt', 'adjst_rate', 'std_err', 'std_rate', 'std_std_err']]
        # Fill the 시군구명
        data4.loc[idx, '시군구명'] = closest_row['시군구명']

# adjst_rate 컬럼에서 null 값이 있는 행을 제거
outer_data = data4.dropna(subset=['center_id'])

"""# 모델용 데이터셋 결합"""

final_combined.rename(columns={'Year_Month': 'date'}, inplace=True)

"""#### 내부데이터와 결합"""

# 'store_cn' 컬럼이 있는 data3 데이터프레임을 center_id를 기준으로 data2와 병합
final_merged_data = pd.merge(final_combined, outer_data[['center_id', 'store_cn', 'adjst_rate', 'juris_station_nm']], on='center_id', how='left')

# 'date' 컬럼 옆에 'store_cn'을 위치시키기 위해 컬럼 순서 재정렬
cols = list(final_merged_data.columns)
store_cn_index = cols.index('date') + 1  # 'date' 컬럼 바로 뒤에 추가
cols.insert(store_cn_index, cols.pop(cols.index('store_cn')))

# 컬럼 순서를 재정렬한 데이터프레임
final_data = final_merged_data[cols]

# 중복된 값 중 날짜별로 1개씩 남기기 (center_id와 date 기준으로 중복 제거)
final_data_unique = final_data.drop_duplicates(subset=['center_id', 'date'], keep='first')

"""### 결측값 처리"""

# center_id에서 중복 제거 및 필요한 컬럼 선택
center_code_unique = data_center[['center_id', 'juris_station_nm']].drop_duplicates()

# 중복을 제거한 center_id 데이터를 'center_id' 기준으로 병합
final_data_unique = final_data_unique.merge(
    center_code_unique,
    on='center_id',
    how='left',
    suffixes=('', '_code')
)

# 'jurist_station_nm'의 결측값을 'jurist_station_nm_code' 컬럼의 값으로 채우기
final_data_unique['juris_station_nm'] = final_data_unique['juris_station_nm'].combine_first(final_data_unique['juris_station_nm_code'])

# 임시로 생성된 'jurist_station_nm_code' 컬럼 삭제
final_data_unique.drop(columns=['juris_station_nm_code'], inplace=True)

# adjst_rate널값처리
final_data_unique['adjst_rate'] = final_data_unique.groupby('juris_station_nm')['adjst_rate'].transform(lambda x: x.fillna(method='ffill').fillna(method='bfill'))

final_data = final_data_unique.fillna(0)

# 로컬 경로에 파일 저장
final_data.to_excel(r'C:/Users/ais/Desktop/project/modeldatav1.xlsx', index=False)