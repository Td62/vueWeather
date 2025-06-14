import requests
import json
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


url = ""

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)
def process_weather_data(weather_data):
    """
    处理天气数据，提取当天天气和未来七天预报
    :param weather_data: 天气数据对象
    :return: 处理后的天气数据
    """
    # 天气状况映射到图标名称
    weather_icon_map = {
        # 晴天
        '晴': 'sunny.png',
        '晴间多云': 'sunny.png',
        '少云': 'sunny.png',
        '晴朗': 'sunny.png',
        
        # 多云
        '多云': 'cloudy.png',
        '阴': 'cloudy.png',
        
        # 雨天
        '雨':'rain.png',
        '小雨': 'rain.png',
        '中雨': 'rain.png',
        '大雨': 'rain.png',
        '暴雨': 'rain.png',
        '雷阵雨': 'rain.png',
        '阵雨': 'rain.png',
        '毛毛雨/细雨': 'rain.png',
        
        # 默认图标
        'default': 'sunny.png'
    }
    
    # 定义AQI等级映射字典（中英文对照）
    AQI_LEVEL_MAP = {
    1: {"name": "优", "message": "Good"},
    2: {"name": "中", "message": "Moderate"},
    3: {"name": "不健康", "message": "Unhealthy"},
    4: {"name": "非常不健康", "message": "Very Poor"},
    5: {"name": "危险", "message": "Hazardous"}
}
    # 获取当天天气信息
    current_weather = {
        'rise': weather_data['data']['rise'][0],
        'temperature': weather_data['data']['observe']['degree'],
        'humidity': weather_data['data']['observe']['humidity'],
        'precipitation': weather_data['data']['observe']['precipitation'],
        'pressure': weather_data['data']['observe']['pressure'],
        'wind_direction': weather_data['data']['observe']['wind_direction_name'],
        'weather': weather_data['data']['observe']['weather'],
        'weather_icon': weather_icon_map.get(weather_data['data']['observe']['weather']),
        'update_time': weather_data['data']['observe']['update_time'],
        'aqi':{
            'level':weather_data['data']['air']['aqi_level'],
            "message":AQI_LEVEL_MAP.get(weather_data['data']['air']['aqi_level'])
        },
        'wind_power':convert_wind_power(weather_data['data']['observe']['wind_power'])
    }
    
    # 获取未来七天预报（当天除外）
    forecast_7days = []
    forecast_data = weather_data['data']['forecast_24h']
    
    # 从第二天开始取数据，确保不包含当天
    start_index = 2  # 从索引2开始（跳过当天）
    end_index = min(start_index + 7, len(forecast_data))  # 最多取7天
    
    for i in range(start_index, end_index):
        day = forecast_data[i]
        
        # 确定天气图标（只使用白天天气）
        weather_icon = weather_icon_map.get(day['day_weather'], weather_icon_map['default'])
        
        # 提取日期（去除年份）
        date = day['time'].split('-')[1:]
        formatted_date = '-'.join(date)
        
        forecast_7days.append({
            'date': formatted_date,
            'weather': day['day_weather'],  # 只保留白天天气
            'min_temp': day['min_degree'] + '°',
            'max_temp': day['max_degree'] + '°',
            'weather_icon': weather_icon  # 只保留一个图标
        })
    
    # 返回处理后的数据
    return {
        'code':200,
        'current_weather': current_weather,
        'forecast_7days': forecast_7days
    }
# 风速取平均值
def convert_wind_power(value):
    try:
        # 直接尝试转换为浮点数
        return float(value)
    except ValueError:
        try:
            # 按分隔符拆分并取平均值
            parts = [float(x) for x in value.split('-')]
            return sum(parts) / len(parts)
        except Exception as e:
            # 双重转换失败时返回 None 并打印错误信息
            print(f"转换失败: {e}")
            return None

# 在FastAPI路由中使用
@app.get("/")
def get_weather():
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        processed_data = process_weather_data(weather_data)
        return processed_data
    else:
        return {"error": "Failed to fetch weather data"}