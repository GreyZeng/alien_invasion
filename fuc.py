def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# �ɱ����
print(calc(1, 3, 5, 7))
print(calc(1, 3, 5))
# Python��������list��tupleǰ���һ��*�ţ���list��tuple��Ԫ�ر�ɿɱ��������ȥ��
# number��Ϊlist����tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum