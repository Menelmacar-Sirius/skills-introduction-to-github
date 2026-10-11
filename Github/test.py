from splinter import Browser

# 告诉 Splinter Edge 驱动在哪里
executable_path = {"executable_path": r"D:\msedgedriver\msedgedriver.exe"}

# 启动 Edge 浏览器
browser = Browser("edge", **executable_path)

# 试试打开百度
browser.visit("https://www.baidu.com")

# 停几秒看看效果（可选）
import time
time.sleep(5)

# 关闭浏览器
browser.quit()

self.weather_data_dict = {}
for line in raw_lines:
    parts = line.split(',', 6)  # 最多切6次，确保天气描述中的逗号不被切
    if len(parts) == 7:
        c, t, tmp, p, wd, ws, desc = parts
        self.weather_data_dict[c] = {
            'time': t,
            'temperature': float(tmp),
            'pressure': float(p),
            'wind_direction': int(wd),
            'wind_speed': int(ws),
            'weather_description': desc
        }


def weather_checking(self):
    print("正在查询", self.city, "的天气……")
    if self.city in self.weather_data_dict:
        data = self.weather_data_dict[self.city]
        print(f"✅ {self.city} 今天 {data['weather_description']}")
        print(f"   时间: {data['time']}")
        print(f"   温度: {data['temperature']}°C")
        print(f"   气压: {data['pressure']} hPa")
        print(f"   风向: {data['wind_direction']}°")
        print(f"   风速: {data['wind_speed']} km/h")
    else:
        print(f"❌ 抱歉，暂时不支持 {self.city} 的天气查询。")