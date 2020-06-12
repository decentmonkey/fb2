python early:
    import binascii
    import copy
    import base64
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS = LETTERS + LETTERS.lower() + "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"

    def getLocalCode():
        localHash = renpy.config.savedir
        md = NMD5(localHash).hexdigest()
        mdv1 = abs(binascii.crc32(md[0:5]))%64
        mdv2 = abs(binascii.crc32(md[6:10]))%64
        mdv3 = abs(binascii.crc32(md[11:16]))%64
        mdv4 = abs(binascii.crc32(md[17:22]))%64
        mdv5 = abs(binascii.crc32(md[23:28]))%64
        mdv6 = abs(binascii.crc32(md[29:36]))%64
        mdv7 = abs(binascii.crc32(md[37:42]))%64
        mdv8 = abs(binascii.crc32(md[43:49]))%64
        localKey = [mdv1, mdv2, mdv3, mdv4, mdv5, mdv6, mdv7, mdv8]
        keyStr = ""
        for numb in localKey:
            keyStr += "%02d" % (numb,)

        return keyStr

    def checkCode(remoteKey, localKey):
        makexor(remoteKey, localKey)
        return remoteKey

    def encodes(key, string):
#        string = string.encode("UTF-8")
        key = base64.urlsafe_b64encode(key).rstrip(b'=')
        encrypted = ''
        idx = 0
        for chars in string:
            key_c = key[idx % len(key)]
            if chars in LETTERS:
                num = LETTERS.find(chars)
                num += (ord(key_c) % 256)
#                num +=1
                num = num % len(LETTERS)
                encrypted += LETTERS[num]
            else:
                encrypted += chars
            idx += 1
        return base64.urlsafe_b64encode(encrypted.encode('utf-8')).decode('utf-8').rstrip(b'=')

    def decodes(key, string):
        codeList = []
        for idx1 in range(0,8):
            codeList.append(int(key[int(idx1)*2:int(idx1)*2+2]))
        print "codelist"
        print codeList
        localHash = renpy.config.savedir
        md = NMD5(localHash).hexdigest()
        mdv1 = abs(binascii.crc32(md[0:5]))%64
        mdv2 = abs(binascii.crc32(md[6:10]))%64
        mdv3 = abs(binascii.crc32(md[11:16]))%64
        mdv4 = abs(binascii.crc32(md[17:22]))%64
        mdv5 = abs(binascii.crc32(md[23:28]))%64
        mdv6 = abs(binascii.crc32(md[29:36]))%64
        mdv7 = abs(binascii.crc32(md[37:42]))%64
        mdv8 = abs(binascii.crc32(md[43:49]))%64
        localKey = [mdv1, mdv2, mdv3, mdv4, mdv5, mdv6, mdv7, mdv8]
        print localKey
        makexor(codeList, localKey)
        enckey = ""
        for num1 in codeList:
            enckey = enckey + str(num1)
        print codeList

        key = base64.urlsafe_b64encode(enckey).rstrip(b'=')
        string = base64.urlsafe_b64decode((string  + b'===').encode("UTF-8")).decode("UTF-8")
        decrypted = ''
        idx = 0
        for chars in string:
            key_c = key[idx % len(key)]
            if chars in LETTERS:
                num = LETTERS.find(chars)
                num -= ord(key_c) % 256
#                num -=1
                num = num % len(LETTERS)
                if num < 0:
                    num = len(LETTERS) + num
                decrypted +=  LETTERS[num]
            else:
                decrypted += chars
            idx += 1
        return decrypted

    def encode2(key, string):
        string = string.decode('utf8')
        encoded_chars = []
        #encoded_string = ""
        for i in range(len(string)):
            key_c = key[i % len(key)]
            encoded_c = unichr(ord(string[i]) + ord(key_c) % 256)
#            encoded_chars.append(encoded_c.decode("ISO-8859-1"))
            encoded_chars.append(encoded_c)
            #encoded_string += encoded_c.decode("ISO-8859-1")
        encoded_string = ''.join(encoded_chars)
        encoded_string = encoded_string.encode('UTF-8')
        return base64.b64encode(encoded_string).rstrip(b'=')

    def decode2(key, string):
        string = base64.b64decode(string + b'===')
        string = string.decode('UTF-8')
        encoded_chars = []
        for i in range(len(string)):
            key_c = key[i % len(key)]
#            char = string[i].encode("ISO-8859-1")
            char = string[i]
            encoded_c = unichr((ord(char) - ord(key_c) + 256) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = ''.join(encoded_chars)
        return encoded_string

    class NMD5:
        def __init__(self, arg=None):
            self.__A = 0x67452301
            self.__B = 0xEFCDAB89
            self.__C = 0x98BADCFE
            self.__D = 0x10325476
            self.__list = LinkedList(None)
            if arg:
                self.__list.add(Node(arg, None))
            self.__hash(self.__list.toString())
            self.digest_size = 16
        def update(self, arg):
            self.__A, self.__B, self.__C, self.__D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
            self.__list.add(Node(arg, None))
            self.__hash(self.__list.toString())
        def copy(self):
            return copy.deepcopy(self)
        def hexdigest(self):
            return ''.join(["{:02x}".format(byte) for byte in bytearray(self.digest())])
        def digest(self):
            res = b''
            buffers = [self.__A, self.__B, self.__C, self.__D]
            for buffer in buffers:
                bufferbytes = []
                b = bin(buffer).replace('b', '0')
                b = "0"*(34-len(b)) + b
                bufferbytes.append(int(b[ 2:10],2))
                bufferbytes.append(int(b[10:18],2))
                bufferbytes.append(int(b[18:26],2))
                bufferbytes.append(int(b[26:34],2))

                res += bytes([bufferbytes[3]])
                res += bytes([bufferbytes[2]])
                res += bytes([bufferbytes[1]])
                res += bytes([bufferbytes[0]])

            return res


        # Main hashing function
        def __hash(self, message):
            messageLength = len(message.encode('utf-8'))
            chunks = self.__splitToBlocks(self.__pad(self.__toBinaryString(message)), 512)

            R11, R12, R13, R14 = 7, 12, 17, 22
            R21, R22, R23, R24 = 5, 9, 14, 20
            R31, R32, R33, R34 = 4, 11, 16, 23
            R41, R42, R43, R44 = 6, 10, 15, 21

            F, G, H, I, R, = self.__F, self.__G, self.__H, self.__I, self.__R

            for chunk in chunks:
                words = self.__createWordArray(chunk, messageLength, chunks.index(chunk)==len(chunks)-1)
                a, b, c, d = A, B, C, D = self.__A, self.__B, self.__C, self.__D
                a = R(F, a, b, c, d, words[ 0], R11, 0xD76AA478)
                d = R(F, d, a, b, c, words[ 1], R12, 0xE8C7B756)
                c = R(F, c, d, a, b, words[ 2], R13, 0x242070DB)
                b = R(F, b, c, d, a, words[ 3], R14, 0xC1BDCEEE)
                a = R(F, a, b, c, d, words[ 4], R11, 0xF57C0FAF)
                d = R(F, d, a, b, c, words[ 5], R12, 0x4787C62A)
                c = R(F, c, d, a, b, words[ 6], R13, 0xA8304613)
                b = R(F, b, c, d, a, words[ 7], R14, 0xFD469501)
                a = R(F, a, b, c, d, words[ 8], R11, 0x698098D8)
                d = R(F, d, a, b, c, words[ 9], R12, 0x8B44F7AF)
                c = R(F, c, d, a, b, words[10], R13, 0xFFFF5BB1)
                b = R(F, b, c, d, a, words[11], R14, 0x895CD7BE)
                a = R(F, a, b, c, d, words[12], R11, 0x6B901122)
                d = R(F, d, a, b, c, words[13], R12, 0xFD987193)
                c = R(F, c, d, a, b, words[14], R13, 0xA679438E)
                b = R(F, b, c, d, a, words[15], R14, 0x49B40821)
                a = R(G, a, b, c, d, words[ 1], R21, 0xF61E2562)
                d = R(G, d, a, b, c, words[ 6], R22, 0xC040B340)
                c = R(G, c, d, a, b, words[11], R23, 0x265E5A51)
                b = R(G, b, c, d, a, words[ 0], R24, 0xE9B6C7AA)
                a = R(G, a, b, c, d, words[ 5], R21, 0xD62F105D)
                d = R(G, d, a, b, c, words[10], R22, 0x02441453)
                c = R(G, c, d, a, b, words[15], R23, 0xD8A1E681)
                b = R(G, b, c, d, a, words[ 4], R24, 0xE7D3FBC8)
                a = R(G, a, b, c, d, words[ 9], R21, 0x21E1CDE6)
                d = R(G, d, a, b, c, words[14], R22, 0xC33707D6)
                c = R(G, c, d, a, b, words[ 3], R23, 0xF4D50D87)
                b = R(G, b, c, d, a, words[ 8], R24, 0x455A14ED)
                a = R(G, a, b, c, d, words[13], R21, 0xA9E3E905)
                d = R(G, d, a, b, c, words[ 2], R22, 0xFCEFA3F8)
                c = R(G, c, d, a, b, words[ 7], R23, 0x676F02D9)
                b = R(G, b, c, d, a, words[12], R24, 0x8D2A4C8A)
                a = R(H, a, b, c, d, words[ 5], R31, 0xFFFA3942)
                d = R(H, d, a, b, c, words[ 8], R32, 0x8771F681)
                c = R(H, c, d, a, b, words[11], R33, 0x6D9D6122)
                b = R(H, b, c, d, a, words[14], R34, 0xFDE5380C)
                a = R(H, a, b, c, d, words[ 1], R31, 0xA4BEEA44)
                d = R(H, d, a, b, c, words[ 4], R32, 0x4BDECFA9)
                c = R(H, c, d, a, b, words[ 7], R33, 0xF6BB4B60)
                b = R(H, b, c, d, a, words[10], R34, 0xBEBFBC70)
                a = R(H, a, b, c, d, words[13], R31, 0x289B7EC6)
                d = R(H, d, a, b, c, words[ 0], R32, 0xEAA127FA)
                c = R(H, c, d, a, b, words[ 3], R33, 0xD4EF3085)
                b = R(H, b, c, d, a, words[ 6], R34, 0x04881D05)
                a = R(H, a, b, c, d, words[ 9], R31, 0xD9D4D039)
                d = R(H, d, a, b, c, words[12], R32, 0xE6DB99E5)
                c = R(H, c, d, a, b, words[15], R33, 0x1FA27CF8)
                b = R(H, b, c, d, a, words[ 2], R34, 0xC4AC5665)
                a = R(I, a, b, c, d, words[ 0], R41, 0xF4292244)
                d = R(I, d, a, b, c, words[ 7], R42, 0x432AFF97)
                c = R(I, c, d, a, b, words[14], R43, 0xAB9423A7)
                b = R(I, b, c, d, a, words[ 5], R44, 0xFC93A039)
                a = R(I, a, b, c, d, words[12], R41, 0x655B59C3)
                d = R(I, d, a, b, c, words[ 3], R42, 0x8F0CCC92)
                c = R(I, c, d, a, b, words[10], R43, 0xFFEFF47D)
                b = R(I, b, c, d, a, words[ 1], R44, 0x85845DD1)
                a = R(I, a, b, c, d, words[ 8], R41, 0x6FA87E4F)
                d = R(I, d, a, b, c, words[15], R42, 0xFE2CE6E0)
                c = R(I, c, d, a, b, words[ 6], R43, 0xA3014314)
                b = R(I, b, c, d, a, words[13], R44, 0x4E0811A1)
                a = R(I, a, b, c, d, words[ 4], R41, 0xF7537E82)
                d = R(I, d, a, b, c, words[11], R42, 0xBD3AF235)
                c = R(I, c, d, a, b, words[ 2], R43, 0x2AD7D2BB)
                b = R(I, b, c, d, a, words[ 9], R44, 0xEB86D391)

                A = (a + A) & 0xffffffff
                B = (b + B) & 0xffffffff
                C = (c + C) & 0xffffffff
                D = (d + D) & 0xffffffff

                self.__A = A
                self.__B = B
                self.__C = C
                self.__D = D


        def __toBinaryString(self, string):
            return ''.join("{:08b}".format(byte) for byte in bytearray(string.encode('utf-8')))

        def __pad(self, bstring):
            padded = ''
            messageLength = len(bstring)

            bstring+="1"

            while (len(bstring) % 512) != 448:
                bstring+="0"

            padded += bstring + self.__pad64B(messageLength)

            return padded

        def __pad64B(self, length):
            s = bin(length).replace('b', '0')

            # If we reach 64-bit overflow
            if len(s) > 64:
                return '0' + '1'*63

            padded = ''

            padded = "0" * (64 - len(s))
            padded += s[::-1] # reverse length byte first to preserve correct order
            return padded[::-1]


        def __splitToBlocks(self, message, n):
            return [message[i:i+n] for i in range(0, len(message), n)]

        def __createWordArray(self, message, messageLength, finalBlock):
            message = self.__splitToBlocks(message, 32)
            wordArray = [0] * 16

            wordIndex = 0
            for word in message:
                bytes = self.__splitToBlocks(word, 8)
                tempByte = 0
                powers = 0

                for byte in bytes:
                    tempByte = wordArray[wordIndex]
                    tempByte = tempByte | int(byte, 2) << powers
                    powers += 8
                    wordArray[wordIndex] = tempByte
                wordIndex += 1
                powers = 0
            if finalBlock:
                wordArray[-2] = messageLength << 3
                wordArray[-1] = messageLength >> 29
            return wordArray

        def __F(self, x, y, z):
            return (x & y) | ((~x) & z)

        def __G(self, x, y, z):
            return (x & z) | (y & (~z))

        def __H(self, x, y, z):
            return x ^ y ^ z

        def __I(self, x, y, z):
            return y ^ (x | (~z))

        def __rotateLeft(self, x, n):
            return (x << n) | (x >> (32-n))

        def __R(self, function,a,b,c,d,x,s,ac):
            r = a + function(b,c,d)
            r = r + x
            r = r + ac
            r = r & 0xffffffff
            r = self.__rotateLeft(r, s)
            r = r & 0xffffffff
            r = r + b

            return r & 0xffffffff
    def new(arg=None):
        return NMD5(arg)

    def md5(arg=None):
        return NMD5(arg)


    class LinkedList:
        def __init__(self, root):
            self.root = root
            self.tail = root

        def toString(self):
            s = ""
            root = self.root

            if root == None:
                return s

            while (root != None):
                s += root.value
                root = root.next
            return s


        def add(self, node):
            if self.root == None:
                self.root = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node


    class Node:
        """A simple node for the list"""
        def __init__(self, value, next):
            self.value = value
            self.next = next










    # IMPORTANT: The block size MUST be less than or equal to the key size!
    # (Note: The block size is in bytes, the key size is in bits. There
    # are 8 bits in 1 byte.)
    DEFAULT_BLOCK_SIZE = 128 # 128 bytes
    BYTE_SIZE = 256 # One byte has 256 different values.

    def main():
        # Runs a test that encrypts a message to a file or decrypts a message
        # from a file.
        filename = 'encrypted_file.txt' # the file to write to/read from
        mode = 'encrypt' # set to 'encrypt' or 'decrypt'

        if mode == 'encrypt':
            message = '''"Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets." -Gerald Priestland "The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
            pubKeyFilename = 'al_sweigart_pubkey.txt'
            print('Encrypting and writing to %s...' % (filename))
            encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)

            print('Encrypted text:')
            print(encryptedText)

        elif mode == 'decrypt':
            privKeyFilename = 'al_sweigart_privkey.txt'
            print('Reading from %s and decrypting...' % (filename))
            decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)

            print('Decrypted text:')
            print(decryptedText)


    def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
        # Converts a string message to a list of block integers. Each integer
        # represents 128 (or whatever blockSize is set to) string characters.

        messageBytes = message.encode('ascii') # convert the string to bytes

        blockInts = []
        for blockStart in range(0, len(messageBytes), blockSize):
            # Calculate the block integer for this block of text
            blockInt = 0
            for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
                blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
            blockInts.append(blockInt)
        return blockInts


    def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
        # Converts a list of block integers to the original message string.
        # The original message length is needed to properly convert the last
        # block integer.
        message = []
        for blockInt in blockInts:
            blockMessage = []
            for i in range(blockSize - 1, -1, -1):
                if len(message) + i < messageLength:
                    # Decode the message string for the 128 (or whatever
                    # blockSize is set to) characters from this block integer.
                    asciiNumber = blockInt // (BYTE_SIZE ** i)
                    blockInt = blockInt % (BYTE_SIZE ** i)
                    blockMessage.insert(0, chr(asciiNumber))
            message.extend(blockMessage)
        return ''.join(message)


    def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
        # Converts the message string into a list of block integers, and then
        # encrypts each block integer. Pass the PUBLIC key to encrypt.
        encryptedBlocks = []
        n, e = key

        for block in getBlocksFromText(message, blockSize):
            # ciphertext = plaintext ^ e mod n
            encryptedBlocks.append(pow(block, e, n))
        return encryptedBlocks


    def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
        # Decrypts a list of encrypted block ints into the original message
        # string. The original message length is required to properly decrypt
        # the last block. Be sure to pass the PRIVATE key to decrypt.
        decryptedBlocks = []
        n, d = key
        for block in encryptedBlocks:
            # plaintext = ciphertext ^ d mod n
            decryptedBlocks.append(pow(block, d, n))
        return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


    def readKeyFile(keyFilename):
        # Given the filename of a file that contains a public or private key,
        # return the key as a (n,e) or (n,d) tuple value.
        fo = open(keyFilename)
        content = fo.read()
        fo.close()
        keySize, n, EorD = content.split(',')
        return (int(keySize), int(n), int(EorD))


    def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
        # Using a key from a key file, encrypt the message and save it to a
        # file. Returns the encrypted message string.
        keySize, n, e = readKeyFile(keyFilename)

        # Check that key size is greater than block size.
        if keySize < blockSize * 8: # * 8 to convert bytes to bits
            sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Either decrease the block size or use different keys.' % (blockSize * 8, keySize))


        # Encrypt the message
        encryptedBlocks = encryptMessage(message, (n, e), blockSize)

        # Convert the large int values to one string value.
        for i in range(len(encryptedBlocks)):
            encryptedBlocks[i] = str(encryptedBlocks[i])
        encryptedContent = ','.join(encryptedBlocks)

        # Write out the encrypted string to the output file.
        encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
        fo = open(messageFilename, 'w')
        fo.write(encryptedContent)
        fo.close()
        # Also return the encrypted string.
        return encryptedContent


    def readFromFileAndDecrypt(messageFilename, keyFilename):
        # Using a key from a key file, read an encrypted message from a file
        # and then decrypt it. Returns the decrypted message string.
        keySize, n, d = readKeyFile(keyFilename)


        # Read in the message length and the encrypted message from the file.
        fo = open(messageFilename)
        content = fo.read()
        messageLength, blockSize, encryptedMessage = content.split('_')
        messageLength = int(messageLength)
        blockSize = int(blockSize)

        # Check that key size is greater than block size.
        if keySize < blockSize * 8: # * 8 to convert bytes to bits
            sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))

        # Convert the encrypted message into large int values.
        encryptedBlocks = []
        for block in encryptedMessage.split(','):
            encryptedBlocks.append(int(block))

        # Decrypt the large int values.
        return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)

    def makexor(list1, list2):
        result = []
        l1l = len(list1)
        j1l = len(list2)
        for l1 in range(0, l1l):
            for j1 in range(0, j1l):
                    list1[l1] = list1[l1] ^ list2[j1]
        return list1
