import qrcode as qr
a=input(" Enter the thing for which u want to make qr : ")
b=input("Enter the 'Name of file' and ' Image Type' of file  here")
img= qr.make(a)
img.save(b)