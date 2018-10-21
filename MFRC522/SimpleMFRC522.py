# Code by Simon Monk https://github.com/simonmonk/

from MFRC522 import MFRC522
import RPi.GPIO as GPIO

class SimpleMFRC522:

    READER = None;

    KEY = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
    BLOCK_ADDRS = [8, 9, 10]

    def __init__(self):
        self.READER = MFRC522.MFRC522()

    def wait_for_tag(self):
        self.READER.Wait_For_Tag()

    def read(self):
        text = ''
        id, uid = self.read_id()
        if id != None:
            text = self.read_content(uid)
        return id, text

    def read_id(self):
        (status, TagType) = self.READER.MFRC522_Request(self.READER.PICC_REQIDL)
        if status != self.READER.MI_OK:
            return None, None
        (status, uid) = self.READER.MFRC522_Anticoll()
        if status != self.READER.MI_OK:
            return None, None
        return self.uid_to_num(uid), uid

    def read_content(self, uid):
        self.READER.MFRC522_SelectTag(uid)
        status = self.READER.MFRC522_Auth(self.READER.PICC_AUTHENT1A, 11, self.KEY, uid)
        data = []
        text_read = ''
        if status == self.READER.MI_OK:
            for block_num in self.BLOCK_ADDRS:
                block = self.READER.MFRC522_Read(block_num)
                if block:
                    data += block
            if data:
                 text_read = ''.join(chr(i) for i in data)

        self.READER.MFRC522_StopCrypto1()
        return text_read

    def write(self, uid, text):
        self.READER.MFRC522_SelectTag(uid)
        status = self.READER.MFRC522_Auth(self.READER.PICC_AUTHENT1A, 11, self.KEY, uid)
        self.READER.MFRC522_Read(11)
        if status == self.READER.MI_OK:
            data = bytearray()
            data.extend(bytearray(text.ljust(len(self.BLOCK_ADDRS) * 16).encode('ascii')))
            i = 0
            for block_num in self.BLOCK_ADDRS:
              self.READER.MFRC522_Write(block_num, data[(i*16):(i+1)*16])
              i += 1

        self.READER.MFRC522_StopCrypto1()
        return id, text[0:(len(self.BLOCK_ADDRS) * 16)]

    def uid_to_num(self, uid):
        n = 0
        for i in range(0, 5):
            n = n * 256 + uid[i]
        return n
