import os
for file in os.listdir('audios'):   
    os.rename("./audios/" + file,"./audios/" + file.replace(" ", ""))
