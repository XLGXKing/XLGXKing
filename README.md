my name is XKing
I am a Minecraft fan
I am learning to use Python to make Minecraft particle special effects.
I am learning to use Java to make Minecraft mod effects.

我会逐步完善我写的代码，不断的上传到github，谢谢

falling_block.py前二十行不用看，此代码的主要作用为在一个区域里随机生成下落的方块（注：我指令里写的是萤石，改NBT就能换方块）
不懂schedule的看数据包和funtion教程
需要一个循环命令方块保持开启写：execute at @e[type=minecraft:falling_block] run particle minecraft:end_rod ~ ~ ~ 00.1 0.01 0.01 0.08 10 force @a
你就可以看到发光的萤石带着粒子从天而降，
