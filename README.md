# STM32-DHT11-uart
基于STM32F103C8T6的温湿度传感器(HAL库版)，通过串口向电脑端反馈数据（附通过ESP8266-01s模块连接WIFI上传云平台的资料代码-固件库版本）
DHT11的DATA接STM32C8T6核心板的PA3；串口模块：PA9-RX、PA10-TX（CUBEMX指配的UART1）。
插上电脑后通过Python调用串口数据（bps:115200;COM3;数据位8，停止位1）\\附效果图+实物图：
![image](https://user-images.githubusercontent.com/83332148/118969561-c4f10300-b99f-11eb-9686-7acf813b2fc5.png)
![0592BEDB962D760CCFFDEEC9A2E5DEB4](https://user-images.githubusercontent.com/83332148/118970119-72fcad00-b9a0-11eb-84f1-360f7414ff3b.jpg)
![D15B95156AED1FDF6EEF0543F2021CA9](https://user-images.githubusercontent.com/83332148/118970271-9e7f9780-b9a0-11eb-9767-8097fd9a761a.jpg)
![04BCEF9D7C3A51E4D5766209E44320DD](https://user-images.githubusercontent.com/83332148/118970169-81e35f80-b9a0-11eb-8369-1d42a78412f1.jpg)

