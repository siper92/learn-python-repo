__author__ = 'todormitev'
print(bin(len('test')*8))
print(bin(32))
messages = ['todor', 'todor mitev', 'dsfs dfsdfsdjfsd kfsdfkjsdh fksjf sdhfksjdfh sdkfhs dkfshd kfhsdksd jfhsdkfshk fhdj sdhfksdhfskd fhsdkfhsdkfjh sdkfhsdkfjshdkfjshdf ksdfhk sdjfhsk djfhskd fhskdfhsdkfhs dkjfhsdkjfhs dkfshdfkjsdfh ksdh dkfhsdf kshdf sdkjfh s']
for message in messages:
    length_of_string_by_8 = len(message) * 8
    print("len({1}) * 8) == {0}".format(length_of_string_by_8, message))
    bin_of_length = bin(length_of_string_by_8)
    print("bin(length_of_string_by_8) == {0}".format(bin_of_length))
    remove_0b_from_bin = bin_of_length[2:]
    print("bin_of_length[2:] == {0}".format(remove_0b_from_bin))
    length = remove_0b_from_bin.rjust(64, "0")
    print("Final -> remove_0b_from_bin.rjust(64, \"0\") == {0}".format(length))
