from shlex import split

name="huseyin uyan"
#print(name.capitalize())
#print(name.count("n")) içerisinde kaç tane n harfi var onu gösterir
#print(len(name)) total harf sayısı
#lengt kelimelere ayırır len ile kullanınca kelime sayısını buluruz
#kelimesayisi=len(name.split())
#print(kelimesayisi)
#                İNDEX   #
my_string="hello python"
#print(my_string[4]) #4.indexi getirecek
#print(my_string[3]) #3.indexi getirecek yani 4.sayıyı veya yazıyı verecek çünkü 0 dan başlar index

#print(len(my_string)) # len mystring -1 son indexi verecek
#my_name="huseyin uyan"
#yeniname=len(my_name)-1
#print(my_name[yeniname])
#Burada len fonk ile kaç karakter olduğunu öğrendik ve sonrasında -1 ile son indexini yeni şeyde tuttuk sonrasında
#print fonksiyonu ile son indexini yazdırdık
#print(my_name[-1])
#köşeli parantez içerisinde eksi yazmak ise son indexten başlayarak okutur
##################### ------ SLİCİNG --------
#barcode="ABCDEFGHIJKLMNOP"
#slicing işlemleri starting index , stopping index stepping index
#dilimlemek için
#barcode[starting index:stopping index: stepping index]
#starting index hangi indexten başlayacağı
#stopping index hangisinde duracağı
#stepping index kaçar kaçar gideceği // ama buraya -1 yazarsak terstern yazdırır
##print(barcode[3:6:])
print(my_string.index("o")) # o karakterinin ilk hangi indexte olduğunu bulur
print(my_string.split()) # split kelimeye böler
kelimesayisi=len(my_string.split()) # split kullanarak kelimeye böldüm sonrasında len fonksiyonu ile kaç kelime olduğunu
#bulup ekrana yazdırdım
print(kelimesayisi)