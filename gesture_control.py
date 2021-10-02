import serial
from time import perf_counter

class GestureController:
    
    def __init__(self, port):
        self.s = serial.Serial(port)
        self.zero = self.getZero()
        
        self.prevT = perf_counter()
        self.velocity = 0

    def getSerialPort(self):
        print("Which serial port is the gesture controller connected to?")
        ports = [port.device for port in serial.tools.list_ports.comports()]
        print("0) None")
        for i in range(0, len(ports)):
            print(i+1, end=") ")
            print(ports[i])
        sel = int(input("0 - "+str(len(ports))+": "))
        if sel != 0:
            return ports[sel - 1]
        return ""

    def getZero(self):
        zerosum = 0
        for i in range(0, 50):
            try:
                zerosum += int(self.s.readline().decode())
            except:
                pass
        return zerosum // 50

    def getReading(self):
        try:
            r = int(self.s.readline().decode()) - self.zero
        except:
            r = 0
            print("Invalid value from gesture controller")
        return r

    def newPositionIncrement(self):
        nowT = perf_counter()
        reading  = -self.getReading() * 100
        t = nowT - self.prevT
        self.prevT = nowT
        distance = (self.velocity*t + 0.5*reading*(t**2)) * 100
        self.velocity = reading * t
        if abs(distance) < 3:
            return 0
        return distance
