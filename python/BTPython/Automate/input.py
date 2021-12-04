from os import path
import pyinputplus as pyip
from pathlib import Path
"""
def main():
    age = pyip.inputNum(prompt="Enter number : ",greaterThan=5,timeout=10,default="N/A")

    response = pyip.inputNum (allowRegexes = [r'(I|V|X|L|C|D|M)+', r'zero '])

    string = pyip.inputStr(prompt="Enter str : ",limit=3,default="Hello")
    print(string)
if __name__ == "__main__":
    main()
    """

"""
p = Path("A:\BT\python\BTPython\Automate\rex.py")
c = Path.cwd().parents[1]
d = Path("A:\BT\python\BTPython\Automate")
for textFilePathObj in d.glob('*.py'):
    print(textFilePathObj)
"""
"""
file = open('test.txt')
f = file.readlines()
file.close()
print(f)
"""

print("TEST ...")
a = pyip.inputPassword(prompt="Enter PASS : ")