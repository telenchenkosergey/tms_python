# Декодировать в строку байтовое значение:
# b'r\xc3\xa9sum\xc3\xa9'.
# Затем результат преобразовать в байтовый вид в кодировке Latin1
# и затем результат снова декодировать в строку.

bytes = b'r\xc3\xa9sum\xc3\xa9'
string = bytes.decode('utf-8')
print(string)
latin = string.encode('Latin1')
print(latin)
latin_string = latin.decode('Latin1')
print(latin_string)
