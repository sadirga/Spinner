def counterClockwise(yourList):
    data_mutar = [[],[],[]]                                          # buat variable list dengan 3 elemen kosong
    for i in range(len(yourList)-1,-1,-1):                           # loop i range(mulai dari panjang yourList -1,akhirnya -1,incr -1)
        for j in range(len(yourList)):                               # loop j sepanjang yourList
             data_mutar[(len(yourList)-1)-i].append(yourList[j][i])  # gunakan fungsi append pada data mutar[panjang yourList dikurang 1] dikurang i
                # sehingga setiap looping datamutar akan mulai dari elemen ke 0, lalu append j dimana j dimulai dari 0 dan i dimulai dari 2
    return data_mutar

data = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(counterClockwise(data))

# pola
#[[3, 6, 9],   [2, 5, 8],    [1, 4, 7]]
# 0,2 1,2 2,2  0,1 1,1 1,2   0,0 1,0 2,0