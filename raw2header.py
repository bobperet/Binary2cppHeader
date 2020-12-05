#80974 40487
import struct
import sys
class R2h():
    def readFile(self, filename):
        buf = open(filename, "rb").read()              # read file into buf
        cnt = sys.getsizeof(buf)                       # get count of bytes
       # cnt = cnt >> 1                                 # get count of shorts
        cnt = cnt & 0xFFFFFE                                 # get count of shorts
        vals = struct.iter_unpack('=H', buf[:cnt])
        print("#define SoundDataSize %d" %(cnt/2))
        print("uint16_t sndData[SoundDataSize] = {", end='')
        lineCount = 0
        for x in vals:
            print("%d, " %(x), end='', sep='')
            lineCount = lineCount + 1
            if lineCount >= 16:
                print()
                print("                                  ",end='')
                lineCount = 0
        print("};")

#
# MAIN
#
if __name__ == '__main__':
    r2h = R2h()
    r2h.readFile("pop.raw")
    print("[Application done]")   # application has exited
