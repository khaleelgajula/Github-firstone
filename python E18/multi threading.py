# """import threading
# def rev(str):
#     for i in str:
#         print(f"reverse of string {str}:{str[::-1]}")
    

# t1=threading.Thread(target=str, args=['python'])
# t2=threading.Thread(target=str, args=['sql'])
# t3=threading.Thread(target=str, args=['java'])

# t1.start()
# t1.join()

# t2.start()
# t2.join()

# t3.start()
# t3.join()"""


# #without using threading

# # import time
# # def task (seconds):
# #     print(f'Task return for {seconds} seconds')
# #     time.sleep(seconds)
# # start = time.perf_counter()
# # task(10)
# # task(8)
# # task(5)
# # task(3)
# # end = time.perf_counter
# # print(f'Time taken is : {end-start}')

# #With using multi threading

# """import threading
# import time
# def task (seconds):
#     print(f'Task running for{seconds} seconds')
#     time.sleep(seconds)
# start=time.perf_counter()
# t1=threading.Thread(target=task , args=[5])
# t2=threading.Thread(target=task , args=[4])
# t3=threading.Thread(target=task , args=[3])
# t4=threading.Thread(target=task , args=[1])

# t1.start()
# t2.start()
# t3.start()
# t4.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()

# end =time.perf_counter()
# print(f'time taken is : {end-start}')"""


# #for even or odd numbers from 0to11

# import threading
# def even():
#     for i in range(0,11,2):
#         print(f'even number is : {i}')
# def odd():
#     for i in range(1,11,2):
#         print(f'odd number is : {i}')
# t1=threading.Thread(target=even)
# t2=threading.Thread(target=odd)

# t1.start()
# t1.join()

# t2.start()
# t2.join()


import threading
def task (nums):
    res=nums*nums
    print(f'square of {nums} is {res}')
object1=threading.Thread(target=task,args=[2])
object2=threading.Thread(target=task,args=[3])
object3=threading.Thread(target=task,args=[4])
object4=threading.Thread(target=task,args=[5])

object1.start()
object1.join()


object2.start()
object2.join()

object3.start()
object3.join()

object4.start()
object4.join()





