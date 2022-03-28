with open("temp_Bucket_1.txt", 'r') as fp:
    x = len(fp.readlines())
    print('Total lines:', x) 