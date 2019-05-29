import os
pipe_name="/pipes/pipe"
def child():
    pipeout=os.open(pipe_name,os.O_WRONLY)
    while(True):
        os.write(pipeout,b"Hello Pipe\n")
def parent():
    if not os.path.exists(pipe_name):
        os.mkfifo(pipe_name)
    pid=os.fork()
    if(pid==0):
        child()
    else:
        pipein=open(pipe_name,'r')
        while True:
            test = pipein.read(1)
            #print(test,end='')
parent()
