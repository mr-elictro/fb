import os,time
os.system('cls')
for i in range(1000):
    def oko():
        time.sleep(1)
        os.system('cls')
        make = input('Target : ')

        num1 = '07511018729'
        num2 = '07503947463'
        num3 = '100015310471473'
        num4 = ':'


        list_inject = str(num1)+str(num4)+str(make)
        list_inject2 = str(num2)+str(num4)+str(make)
        list_inject3 = str(num3)+str(num4)+str(make)
        print('\033[91mXinject >> \033[92mseccessful\033[97m')

        with open('List.txt','a') as slaw:
            slaw.write(list_inject+'\n'+list_inject2+'\n'+list_inject3+'\n')
            slaw.close()

    oko()


