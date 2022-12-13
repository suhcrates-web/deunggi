import pythoncom

context = pythoncom.CreateBindCtx(0)  # 인수는 0 이어야 함


#get running object Table
# help(pythoncom)
running_coms = pythoncom.GetRunningObjectTable()


# Creates an enumerator that can list all the monikiers in our tables
    # help(running_coms)  # 안에 들은걸 볼수있음
monikiers = running_coms.EnumRunning()

# Loop Through all the monikiers
    #monikiers : kind of 'link'.
for monikier in monikiers:
    print('-'*50)

    #print display name
    print(monikier.GetDisplayName(context, monikier))
        # => 지금 열려있는 파일들 다 출력됨  (난 안되긴 함)

    #print hash
    print(monikier.Hash())

    #Is system monikier
    print(monikier.IsSystemMoniker())



