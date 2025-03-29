def wavg(image_matrix):
    a = len(image_matrix)
    b = image_matrix.size/a/3
    print(b)
    print(a)
    xsum=0
    xisum=0
    yjsum=0
    for i in range(a):
        for j in range(int(b)):#calculatint the mean of som histogram
            xsum+=image_matrix[i][j][0]*1.0
            xisum += (image_matrix[i][j][0]*1.0*i)
            yjsum += (image_matrix[i][j][0]*1.0*j)
    xavg=xisum/xsum
    yavg=yjsum/xsum
    pos = [xavg,yavg]
    return pos