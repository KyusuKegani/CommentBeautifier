import sys

args = sys.argv
filePath = args[1]
offset = 4
sourceCode = []
try:
    with open(filePath) as lines:
        for line in lines:
            sourceCode.append(line.rstrip())
except OSError:
    print("ファイルを開くことができません")
if sourceCode[0].startswith("//"):
    index = 0
    maxLength = len(sourceCode[0])
    for sourceLine in sourceCode:
        if sourceLine.startswith("//"):
            index += 1
            maxLength = max(maxLength, len(sourceLine))
            continue
        else:
            index += 1
            break

    headerComment = "/" * (maxLength + offset)
    sourceCode.insert(0, headerComment)
    sourceCode.insert(index, headerComment)

else:
    print("No Header Comment")

print(sourceCode)

try:
    with open(filePath + "2", "w") as newLine:
        newLine.write("\n".join(sourceCode))
except OSError:
    print("ファイルを開くことができません")
