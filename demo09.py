from os.path import isdir, join, splitext
from os import remove, listdir, stat, getcwd

# 指定要删除的文件类型
filetypes = ['.tmp', '.log', '.obj', '.txt']
def delCertainFiles(directory):
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            # 递归调用
            delCertainFiles(temp)
        elif splitext(temp)[1] in filetypes or stat(temp).st_size==0:
            #删除文件
            remove(temp)
            print(temp, ' deleted....')

if __name__ == '__main__':
    path = getcwd()
    if isdir(path):
        delCertainFiles(path)