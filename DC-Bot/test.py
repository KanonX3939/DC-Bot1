import os
for filename in os.listdir('./cmds'):
    print(filename)


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
