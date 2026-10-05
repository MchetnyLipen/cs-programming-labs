sec = int(input())

HH = sec//3600
rem_sec = sec % 3600
MM = rem_sec // 60
SS = rem_sec % 60

print(f"{HH:02}:{MM:02}:{SS:02}")