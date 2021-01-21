import os 
import time
import subprocess
st = ''
old_list = []
cur_list   = []

delay = 3





try:
    f = open('logger.txt','a',encoding = 'utf-8')
except:
    print(' making log file... ')
    f = open('logger.txt','w',encoding = 'utf-8')
    


f.write("""\n\n\n\n\n\n\n\n\n
============================================================================================================================================================================================

     ----------------------------------------------
    |                                              |
    |        .....logger  launched......           |
    |                                              |
     ----------------------------------------------

        """)
f.close()
        

while(True):
    
    tm = """\n\n\n\n\n\n\n\n============================================================================================================================================================================================\n""" + time.asctime(time.localtime())+'\n'

    #get the tasklist
    try:
        st = str(subprocess.check_output('tasklist',shell = True).decode('utf-8'))  #shell = True keeps the command shell from being launched
        print('------\nlogged\n------')

    except:
        st = '\n err \n'
        print('an error occurred')

    f = open('logger.txt','a',encoding = 'utf-8')

    
    

    #find new processes and terminated/killed ones
    if st != 'err' :
        #heading = (st).split('\n')[0] + (st).split('\n')[1] + (st).split('\n')[2] + (st).split('\n')[3]
        #heading =
        heading  = '\n-----------'

        cur_list = []
        temp = (st).split('\n')[3:]
        j= 0
        for i in temp:
            try:
                cur_list.append((i.split()[0]))
            except:
                print('')
            j+=1
            
        

        new_list = []
        killed   = []
        for i in cur_list:
            if i not in old_list:
                new_list.append('\n'+i)
        for i in old_list:
            if i not in cur_list:
                killed.append('\n'+i)

                
        if (new_list)== [] and killed == []:  #exception handling
            f.close()
            old_list = cur_list
            time.sleep(delay)
            continue
            

        f.write(tm)
        f.write('\n\nNEW TASKS \n'+heading)
        for i in new_list:
            f.write(i)

        
        f.write('\n\n\n\nKILLED TASKS \n'+heading)
        for i in killed:
            f.write(i)
        
        

    else :
        f.write(tm)
        f.write('\n'+st)
    

    f.close()

    time.sleep(delay)
    old_list = cur_list
    


