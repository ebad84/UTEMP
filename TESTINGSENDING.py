import requests

# اطلاعات سنسور
SENSOR_UUID = "5a1e4bed-9bc8-4c13-ae1a-a7caa26dcc93"
API_KEY = "9210d017b80ee04a553fc681fded63868983b8fe7f0ec95dec51797523caa5a4"

# مقدار دما برای آپلود
temperature = 22.33

# URL API (مثال لوکال)
url = "http://127.0.0.1:5000/api/upload"

# داده‌ها
headers = {
    "X-API-KEY": API_KEY,
}
data = {
    "temperature": temperature
}

# درخواست POST
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("دما با موفقیت آپلود شد:", response.json())
else:
    print("خطا در آپلود:", response.status_code, response.text)
