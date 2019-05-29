import os
def child(pipeout):
    while(True):
        os.write(pipeout,b"Hello Pipe\n")
def parent():
    pipein,pipeout=os.pipe()
    pipein=os.fdopen(pipein)
    if(os.fork()==0):
        child(pipeout)
    else:
        while True:
            test = pipein.read(1)
            print(test,end='')
parent()
