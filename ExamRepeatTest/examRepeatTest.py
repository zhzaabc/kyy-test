import requests

isRepeat = 0
questionArray = []
examIdArray = ['121972',
               '121973',
               '121974',
               '121975',
               '121976',
               '121977',
               '121978',
               '121979',
               '121980',
               '121981']

header = {
    'Cookie' : 'token=6CBA078470D2CC69E59D70FE90EA323F'
}

url = 'http://www.kuaixuezaixian.com/admin/api/question/examMock/preview?id='

for examId in examIdArray:
    examUrl = url + examId

    examResult = requests.get(examUrl, headers=header)
    examJson = examResult.json()
    print('===========================================')
    print('试卷名称：【' + examJson['result']['examInfo']['name'] + '】')
    partList = examJson['result']['part']
    # print(examJson)
    # print(examJson['result']['part'])
    for partDict in partList:
        print('当前正在检测试卷的' + partDict['partInfo']['name'])
        partQuestionList = partDict['question']

        for questionDict in partQuestionList:
            if len(questionArray) != 0:

                for questionId in questionArray:
                    if questionDict['id'] == questionId:
                        isRepeat = 1

            questionArray.append(questionDict['id'])

print('===========================================')
print('合计总共检测' +str(len(questionArray)) + '道题目')
if isRepeat == 1:
    print('该组试卷中存在重复题目')
else:
    print('该组试卷中没有重复题目')