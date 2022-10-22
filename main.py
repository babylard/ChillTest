import multiprocessing
from time import time

print("-" * 50)
print("This application is intended to put your CPU under a heavy load, this application can be used to test Cooling effeciency, and testing your CPU durability. If you dont know what your doing then you should probably not run this Application as you could damage your System.")
print("-" * 50)
print(" ")
answer = input("Are you sure you want to run the application? (y/n): ")


if answer == 'y':

    print("Application will start in 10 seconds, close this Window if you have changed your mind!")
    time.sleep(10)
    def worker():
        """worker function"""
        print ('Worker')
        k = []

        # of course in an infinite loop
        while True:
            # lets use the cpu mathematical power, to increse its temp
            l = (2*33) >> 3 
            # it is also possible to consume memory..
            # but it will crash windows 8.1 after a while
            # k.append(l)
            pass
        return

    if __name__ == '__main__':
        jobs = []

        cpu = multiprocessing.cpu_count()
        print("CPU count=" + str(cpu))
        for i in range(cpu):
            p = multiprocessing.Process(target=worker)
            jobs.append(p)
            p.start()

else:
    print("Job canceled. Closing window in 5 seconds...")
    time.sleep(5)