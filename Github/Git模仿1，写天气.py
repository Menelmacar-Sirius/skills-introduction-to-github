class CheckingWeather(object):
    def __init__(self,city,time,temperature,pressure,wind_direction,wind_speed,weather_description):
        self.city = city
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed
        self.weather_description = weather_description

        raw_lines = ["北京,2025-04-05 14:30,18.2,1012.5,45,12,晴",
                "上海,2025-04-05 15:00,20.5,1010.8,135,18,多云",
                "广州,2025-04-05 14:45,26.7,1008.3,180,22,阵雨",
                "成都,2025-04-05 13:20,22.1,956.4,225,8,阴",
                "西安,2025-04-05 16:10,24.3,985.7,300,15,晴",
                "哈尔滨,2025-04-05 12:00,8.9,1020.1,10,20,多云",
                "乌鲁木齐,2025-04-05 17:30,15.6,920.5,60,25,晴，有扬沙",
                "昆明,2025-04-05 14:00,21.4,812.3,200,10,晴",
                "杭州,2025-04-05 15:20,19.8,1009.6,150,14,小雨",
                "武汉,2025-04-05 14:50,23.0,1007.2,170,16,雷阵雨",
                "青岛,2025-04-05 16:00,16.5,1013.0,90,28,多云，海风大",
                "拉萨,2025-04-05 13:40,12.3,650.8,320,12,晴，高海拔",

                "纽约 (New York),2025-04-05 02:30,9.5,1015.2,315,24,Partly cloudy",
                "伦敦 (London),2025-04-05 07:00,11.2,1008.7,225,18,Light rain",
                "东京 (Tokyo),2025-04-05 15:30,17.8,1011.4,135,15,Sunny",
                "巴黎 (Paris),2025-04-05 08:20,13.6,1010.3,200,12,Overcast",
                "悉尼 (Sydney),2025-04-05 16:45,22.4,1016.8,120,20,Clear sky",
                "莫斯科 (Moscow),2025-04-05 05:10,2.1,1022.5,10,30,Snow showers",
                "迪拜 (Dubai),2025-04-05 14:00,34.7,1005.0,180,22,Hot and clear",
                "多伦多 (Toronto),2025-04-05 02:15,6.3,1018.9,270,26,Cloudy with gusts",
                "里约热内卢 (Rio de Janeiro),2025-04-05 11:30,28.9,1009.1,90,14,Scattered thunderstorms",
                "柏林 (Berlin),2025-04-05 08:50,10.8,1007.6,250,19,Drizzle",
                "新加坡 (Singapore),2025-04-05 14:20,31.2,1008.5,160,10,Heavy rain",
                "开罗 (Cairo),2025-04-05 13:00,29.5,1006.2,180,16,Sunny, dusty"]
        self.weather_data_dict = {}
        for line in raw_lines:
            city_name = line.split(',', 1)[0]  # 只切一次，取第一个逗号前的部分（就是城市名）
            self.weather_data_dict[city_name] = line

    def weather_checking(self):
        print("正在查询", self.city, "的天气……")

        if self.city in self.weather_data_dict:
            weather = self.weather_data_dict[self.city]
            print(f"✅ {self.city} 今天 {weather['weather_description']}")
            print(f"   时间: {weather['time']}")
            print(f"   温度: {weather['temperature']}°C")
            print(f"   气压: {weather['pressure']} hPa")
            print(f"   风向: {weather['wind_direction']}°")
            print(f"   风速: {weather['wind_speed']} km/h")
        else:
            print(f"❌ 抱歉，暂时不支持 {self.city} 的天气查询。")
    def start_check(self):
        print("正在监控",self.city,"的天气变化.....")
        count=0
        while True:
            count +=1
            print(f"第{count}次查询")






























