import sys

args = sys.argv
filePath = args[1]

sourceCode = []
try:
    with open(filePath) as lines:
        for line in lines:
            sourceCode.append(line.rstrip())
except OSError:
    print("ファイルを開くことができません")
if sourceCode[0].startswith("//"):
    index = 0
    sourceCode.insert(index, "//////////////////////////")
    for sourceLine in sourceCode:
        if sourceLine.startswith("//"):
            index += 1
            continue
        else:
            break
    print(index)
    sourceCode.insert(index, "//////////////////////////")

else:
    print("No Header Comment")

print(sourceCode)

try:
    with open(filePath+"2", "w") as newLine:
        newLine.write("\n".join(sourceCode))
except OSError:
    print("ファイルを開くことができません")
