import os
import subprocess
import time
Parameters = {'--output-spaces MNI152NLin6Asym:res-2 MNI152NLin2009cAsym','--me-output-echos','--random-seed 666'}
Parameters0 = {'--fs-no-reconall','--me-output-echos'}
Parameters1 = {'--slice-time-ref 0.5'}
Parameters2 = {'--me-output-echos','--slice-time-ref 0.5','--write-graph'}
#cmd = 'fmriprep-docker C:\\Users\\sdzcgaoxiang\\Desktop\\Data\\TestBids_funcitonal C:\\Users\\sdzcgaoxiang\\Desktop\\Data\\Test_preprocessed --participant-label {}  --fs-license-file C:\\Users\\sdzcgaoxiang\\Desktop\\Data\\license.txt --fs-no-reconall '.format('02')
startNumber = 8
endNumber = 8
licensePath = r'C:\Users\sdzcgaoxiang\Desktop\Data\license.txt'
inputPath = r'C:\Users\sdzcgaoxiang\Desktop\Data\TestBids_funcitonal'
outputPath = r'C:\Users\sdzcgaoxiang\Desktop\Data\Test_preprocessed1'
otherPara = ''

thisParameters = Parameters1
for para in thisParameters:
    otherPara = otherPara + ' ' + para

while 1:
    thisNumber = str(startNumber)
    if startNumber < 10:
        thisNumber = '0' + thisNumber

    cmd = r'docker run --rm -e DOCKER_VERSION_8395080871=20.10.17  -v {}:/opt/freesurfer/license.txt:ro -v {}:/data:ro -v {}:/out nipreps/fmriprep:22.0.0 /data /out participant --participant-label {} {}'.format(licensePath,inputPath,outputPath,thisNumber,otherPara)

    p = subprocess.Popen(cmd, shell=True, encoding='utf8',stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    # p.stdin.write('y\n')
    # p.stdin.close()
    # 当前时间格式化
    # 循环显示输出
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        localtime = time.localtime(time.time())
        curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        if line:
            print('{} Subprogram output: {}'.format(curtime, line))
        if p.returncode == 0:
            print('Subprogram success')

    if startNumber == endNumber:
        print('全部处理完成')
        break
    startNumber += 1

# docker run --rm -e DOCKER_VERSION_8395080871=20.10.17 -it -v C:\Users\sdzcgaoxiang\Desktop\Data\license.txt:/opt/freesurfer/license.txt:ro -v C:\Users\sdzcgaoxiang\Desktop\Data\TestBids_funcitonal:/data:ro -v C:\Users\sdzcgaoxiang\Desktop\Data\Test_preprocessed:/out nipreps/fmriprep:22.0.0 /data /out participant --participant-label 02 --fs-no-reconall