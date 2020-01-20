import os
import time

ren = ""
tag = ""
typ = ""
new_name = ""
split_list = ""

system = os.name
dirs = os.listdir('.')

cmd = []

for dir in dirs[:]:
    if os.path.isdir('./%s' % dir):
        continue
    if '_1_t(' in dir:
	    continue
    if 'input_sr' in dir:
        tag = 'input_sr'
    elif ('output' in dir) or ('output_sr' in dir):
        tag = 'output'
    else:
        continue
	
    if '.png' in dir:
        typ = '.png'
    elif '.yuv' in dir:
        typ = '.yuv'
    elif '.p010' in dir:
        typ = '.p010'
    else:
        continue

    split_list = dir.split('_t(')
    new_name = tag + '_t(' + split_list[1].split(typ)[0] + split_list[0].split(tag)[1] + typ

    print(new_name)
    print('dir: ', dir)

    ren = 'rename "./%s" "./%s"\n' % (dir, new_name)
    cmd.append(ren)

with open('rename.bat', 'w') as rename:
    rename.write(''.join(cmd))
    rename.close()

if "nt" == system:
    os.system("rename.bat")
    os.system('del "./rename.bat"')

if "posix" == system:
    os.rename("rename.bat", "rename.sh")
    os.system("rename.sh")
    os.remove("rename.sh")

print("程序运行时间(s)：", time.process_time())
