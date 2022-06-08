# pip install ncmdump -i https://pypi.tuna.tsinghua.edu.cn/simple


from ncmdump import dump
import os
import sys
import re


SRCPATH = 'C:\\CloudMusic\\VipSongsDownload'


def Run(inputPath):

    if os.path.isfile(inputPath):
        if os.path.exists(inputPath.replace('.ncm', '.mp3')):
            print('aaaa')
            try:
                dump(inputPath, inputPath.replace('.mp3', '(1).mp3'))
            except Exception as e:
                print(e)
                return
        else:
            try:
                dump(inputPath, inputPath.replace('.ncm', '.mp3'))
            except Exception as e:
                print(e)
                return
            pass

        os.remove(inputPath)
        print("success to change format.")

    if os.path.isdir(inputPath):

        # 获取.ncm文件列表
        ncmFileList = [i for i in os.listdir(inputPath) if re.search(r'\.ncm$', i)]
        if not ncmFileList:
            print("不存在ncm文件")
            return

        for eachFile in ncmFileList:
            targetFile = os.path.join(inputPath, eachFile.replace('.ncm', '.mp3'))

            eachNcmFile = os.path.join(inputPath, eachFile)
            if os.path.exists(eachNcmFile):
                # 如果存在已转换的文件，跳过
                if os.path.exists(targetFile):
                    print("已转换：%s" % eachFile.replace('.ncm', '.mp3'))
                    continue
                try:
                    dump(eachNcmFile, targetFile)
                    # print(targetFile, targetFile)
                except Exception as e:
                    print(e)
                    continue

                # print(eachNcmFile, targetFile)
                os.remove(eachNcmFile)

        print("success to change format.")


if __name__ == '__main__':
    inputPath = sys.argv[1] if len(sys.argv) == 2 else SRCPATH
    # print(inputPath)
    Run(inputPath)
