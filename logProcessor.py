class LogProcessor:
    def __init__(self):
        self.userData = []
    
    def process(self, filename):
        line = ''
        user = ''
        passScheme = ''
        time = ''
        # init = None
        # succ = None
        with open(filename, 'rU') as f:
            for line_terminated in f:
                line = line_terminated.rstrip('\n')

                # if self.checkTest(line): 
                #     continue
                user = self.getUser(line)
                passScheme = self.getScheme(line)
                time = self.getTime(line)
                init = self.isInit(line)
                # if init == False:
                #     succ = self.getSucc(line)
                print(user, passScheme, time )
                print(line)

    # def getSucc(self, line):
    #     temp = line.split()[3]
    #     temp = temp[0:temp.find(';')]
    #     if temp == 'textrandom':
    #         if line.split()[5] == 'good':
    #             return True
    #         else:
    #             return False
    #     elif temp == 'passtiles':
    #         if line.split()[4] == 'goodPractice':
    #             return True
    #         else:
    #             return False

    
    # def isInit(self, line):
    #     init = [ 'Create', 'Password' ]

    #     if line.split()[4] in init:
    #         return True
    #     else:
    #         return False
    
    def checkTest(self, line):
        # TODO: redo for Enter succ / fail
        entries = [ 'Create', 'pwtest', 'Password', 'goodPractice', 'badPractice' ]
        if line.split()[4] in entries:
            return True
        else:
            return False
    
    def getUser(self, line):
        return line.split()[1]

    def getTime(self, line):
        # change to flaot
        return line.split()[0]

    def getScheme(self, line):
        temp = line.split()[3]
        return temp[0:temp.find(';')]


if __name__ == '__main__':
    log = LogProcessor()
    log.process("text21.txt")
    print("done")