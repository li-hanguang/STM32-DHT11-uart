#通过Python代码调用serial库调试串口（简易上位机控制程序）
import serial #导入模块
import threading
STRGLO="" #读取的数据
BOOL=True  #读取标志位

#读数代码本体实现
def ReadData(ser):
    global STRGLO,BOOL
    # 循环接收数据，此为死循环，可用线程实现
    while BOOL:
        if ser.in_waiting:
            STRGLO = ser.read(ser.in_waiting).decode("gbk")
            print(STRGLO)


#打开串口
# 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
# 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
# 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
def DOpenPort(portx,bps,timeout):
    ret=False
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timeout)
        #判断是否打开成功
        if(ser.is_open):
           ret=True
           threading.Thread(target=ReadData, args=(ser,)).start()
    except Exception as e:
        print("---异常---：", e)
    return ser,ret



#关闭串口
def DColsePort(ser):
    global BOOL
    BOOL=False
    ser.close()



#写数据
def DWritePort(ser,text):
    result = ser.write(text.encode("gbk"))  # 写数据
    return result




#读数据
def DReadPort():
    global STRGLO
    str=STRGLO
    STRGLO=""#清空当次读取
    return str



if __name__=="__main__":
    ser,ret=DOpenPort("COM3",115200,None)
    if(ret==True):#判断串口是否成功打开
        # count=DWritePort(ser,"我是东小东，哈哈")
        # print("写入字节数：",count)
         DReadPort() #读串口数据
         #DColsePort(ser)  #关闭串口
