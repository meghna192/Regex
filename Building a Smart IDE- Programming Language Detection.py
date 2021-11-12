import sys, re

text = sys.stdin.read()
if "#include" in text:
    print("C")
elif "import java.io." in text:
    print("Java")
else :
    print("Python")