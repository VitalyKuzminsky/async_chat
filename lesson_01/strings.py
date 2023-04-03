# Код по методичке урок 1.
progr_1 = 'Программирование'

print(progr_1)

print(type(progr_1))

progr_2 = 'Programování'

print(progr_2)

unic_s_1 = "\N{LATIN SMALL LETTER C WITH DOT ABOVE}"

print(unic_s_1)

unic_s_2 = "\u010B"

print(unic_s_2)

progr_3 = 'Программа'

progr_4 = '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'

print(progr_4)

print(progr_3 == progr_4)

print(len(progr_4))

bytes_s_1 = b'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'

bytes_s_2 = b"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430"

bytes_s_3 = b'''\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'''

print(type(bytes_s_1))

bytes_s_4 = b'Program'

print(bytes_s_4)

print(len(bytes_s_4))

print(100 * '-')

enc_str = 'Кодировка'

enc_str_bytes = enc_str.encode('utf-8')

print(enc_str_bytes)

print(100 * '0_0')

dec_str_bytes = b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0'

dec_str = dec_str_bytes.decode('utf-8')

print(dec_str)

print(100 * '-')

str_1 = 'Программа'

str_1_enc = str.encode(str_1, encoding='utf-8')

print(str_1_enc)

print(100 * '-')

bytes_1 = b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0'

bytes_1_enc = bytes.decode(bytes_1, encoding='utf-16')

print(bytes_1_enc)

import subprocess

args = ['ping', 'google.com']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

# for line in subproc_ping.stdout:
#     print(line)

# for line in subproc_ping.stdout:
#     print(line.decode('utf-8'))

# for line in subproc_ping.stdout:
#     line = line.decode('cp866').encode('utf-8')
#     print(line.decode('utf-8'))

# import telnetlib
# import time
#
# tn_connect = telnetlib.Telnet('10.0.0.1')
#
# tn_connect.read_until(b'Username:')
# tn_connect.write(b'user\n')
#
# t.read_until(b'Password:')
# t.write(b'pass\n')
#
# time.sleep(5)

# output = tn_connect.read_very_eager().decode('cp866').encode('utf-8')
# print(output.decode('utf-8'))

import locale

def_coding = locale.getpreferredencoding()

print(def_coding)

f_n = open("test.txt", "w")

f_n.write("""test test test
test test test""")

f_n.close()

print(f_n)

with open('test.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
print()

print(100 * '-')

handl_err = 'Testování'

handl_err_bytes = handl_err.encode('ascii', 'replace')

print(handl_err_bytes)

handl_err_bytes_2 = handl_err.encode('ascii', 'namereplace')

print(handl_err_bytes_2)

handl_unicode = 'Testování'

handl_bytes = handl_unicode.encode('ascii', 'ignore')

print(handl_bytes)
print(100 * '-')

handl_str = 'Testování'

handl_str_utf8 = handl_str.encode('utf-8')

print(handl_str_utf8)

b'Testov\xc3\xa1n\xc3\xad'

handl_str_utf8_str = handl_str_utf8.decode('ascii', 'ignore')

print(handl_str_utf8_str)

handl_str = 'Testování'

handl_str_utf8 = handl_str.encode('utf-8')

handl_str_utf8_str = handl_str_utf8.decode('ascii', 'replace')

print(handl_str_utf8_str)
