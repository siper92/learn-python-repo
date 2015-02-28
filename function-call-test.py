__author__ = 'todormitev'


def inception(*args, **kwargs):
    print('-------------')
    print(args)
    print(kwargs)


# def test_caller(*args, **kwargs):
#     print('-----')
#     print(args)
#     print(kwargs)
#     inception(kwargs)


def test_caller_two(*args, **kwargs):
    print('++++++')
    print(args)
    print(kwargs)
    inception(*args, **kwargs)

# test_caller(name='todor', test='none', test_two=None, objectDb=1)
test_caller_two('tetete', name='todor', test='none', test_two=None, objectDb=1)