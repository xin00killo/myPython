#coding=utf-8
# __autor__='wyxces'

'''给定一个非负整数，你可以最多交换两个数字一次来获得最大值的数字。 返回您可以获得的最大值。'''

def maximumSwap(num):
    num_list = list(str(num))
    result_list = []
    while(True and len(num_list)>0):
        if num_list[0] == max(num_list):
            result_list.append(num_list[0])
            num_list.remove(num_list[0])
            # print("ssss",num_list)
            continue
        else:
            if num_list.count(max(num_list))>1:
                print("elif",num_list)
                # max_index = max([i for i, x in enumerate(num_list) if x == max(num_list)])
                max_count = 0
                for i in range(0,len(num_list)):
                    if num_list[i] == max(num_list):
                        max_count +=1
                    if  max_count == num_list.count(max(num_list)):
                        max_index = i
                        break
            else:
                max_index = num_list.index(max(num_list))
            temp = num_list[0]
            num_list[0] = num_list[max_index]
            num_list[max_index] = temp
            break
    result_list.extend(num_list)
    result = int("".join(list(result_list)))
    return result



if __name__ =="__main__":
    num = 9915464455641349
    print(num,maximumSwap(num))