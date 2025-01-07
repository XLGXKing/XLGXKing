'''
import math
import random
import os


a = 0
b = 0
c = 0
d = random.randint(1, 100)
e = random.randint(1, 100)
f = random.randint(1, 100)
while a <= d:
    a += 0.1
    if b <= e:
        b += 0.1
    if c <= f:
        c += 0.1
    print(f"particle {a} {b} {c} 0 0 0 0 0 force")
'''

import os
import math
import random

x = 5468
y = 230
z = 6827
w = 0
count = 0

folder_name = "falling_block"
folder_path = os.path.join(os.getcwd(), folder_name)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

while x < 5723:
    file_name = f"{count}.mcfunction"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as fp:

        d = random.randint(5, 10)
        x += d

        z = 6827
        d = random.randint(-20, 20)
        z += d

        w += 1

        fp.write(f"summon minecraft:falling_block {x} {y} {z} {{Time:1, BlockState:{{Name:'glowstone'}}, Tags:['xking']}}\n")
        fp.write(f"schedule function k:falling_block/{w} 1s\n")

    count += 1

print(f"Commands have been written to {count - 1} files in the '{folder_name}' folder.")



