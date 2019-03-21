import csv
from datetime import datetime
# from operator import add
# use python csv module
class LogProcessor:
    def __init__(self):
        # csv
        # user, scheme, logins, successes, failures, *Times
        # data
        # user, scheme, succesVses, failures, lastLogin, *Times
        self.userData = []
    
    # ['ast134', 'Text21', 15, 0, '2017-07-18 18:20:47', '0:00:16', '0:00:05', '0:00:05']
    def toCSV(self, data):
        for i in data:
            del i[4]
            i.insert(2, i[2]+i[3])

    
    def process(self, filename):
        user = ''
        passScheme = ''
        checkType = ''
        time = ''
        with open(filename, 'r') as f:
            csvReader = csv.reader(f)
            for lineList in csvReader:
                if self.check(lineList) == False:
                    continue

                user = lineList[1]
                passScheme = self.getScheme(lineList)
                checkType = lineList[6]
                time = lineList[0]
                self.record(user,passScheme,checkType,time)
        self.toCSV(self.userData)
        with open("output.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerows(self.userData)

    # TODO: calculate total logins after parse remove lasttime
    def record(self, user, scheme, checkType, time):
        index = self.recordSearch(user, scheme)
        if index == -1:
            self.userData.append([user,scheme,0,0,0])
        index = len(self.userData)-1
        if checkType == "success":
            self.userData[index][2] += 1
        if checkType == "failure":
            self.userData[index][3] += 1
        if checkType == "start":
            self.userData[index][4] = time

        diffWords = ["goodLogin", "badLogin", "passwordSubmitted"]
        if checkType in diffWords:
            diff = self.timeDiff(self.userData[index][4], time)
            self.userData[index].append(diff)

    def timeDiff(self, t1, t2):
        start = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
        return str(end - start)

    def recordSearch(self, user, scheme):
        count = -1
        for i in self.userData:
            count += 1
            if i[0] == user and i[1] == scheme:
                return count
        return -1

    def check(self,line):
        checkList = ["success", "failure", "passwordSubmitted", "goodLogin", "badLogin", "start"]
        if line[6] in checkList:
            return True
        else:
            return False

    def getScheme(self, line):
        if line[3] == "testtextrandom":
            return "Text21"
        elif line[3] == "testpasstiles":
            return "Image21"
        else:
            return ""

if __name__ == '__main__':
    log = LogProcessor()
    print("Please enter your text21 CSV: ")
    x1 = input()
    print("Please enter your image21 CSV: ")
    x2 = input()
    log.process(x1)
    log.process(x2)
    print("output.csv create.")