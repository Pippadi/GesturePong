import serial
from time import perf_counter

class GestureController:
    
    def __init__(self, port):
        self.s = serial.Serial(port)
        self.s.readline(); self.s.readline();
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
            zerosum += int(self.s.readline().decode())
        return zerosum // 50

    def getReading(self):
        r = int(self.s.readline().decode) - self.zero
        if abs(r) < 2:
            return 0
        return r

    def newPositionIncrement(self):
        nowT = perf_counter()
        reading  = -self.getReading() * 100
        t = nowT - self.prevT
        self.prevT = nowT
        distance = self.velocity*t + 0.5*reading*(t**2)
        self.velocity = reading * t
        return distance
