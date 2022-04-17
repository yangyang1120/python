import re #導入正規表示法
condition = '[A-Za-z][A-Za-z-]+[A-Za-z]' #搜索條件
#導入US08438662-US08438671的XML檔
for i in range(62,72): 
    XML = 'US084386%i-20130514.XML' %i 
    XML = open (XML) #開啟檔案
    data = XML.read() #讀取檔案
    data_str = re.sub("<.*?>"," ",data) #找出tag並用空白取代
    #'w'打開一個文件只用於寫入，如果該文件已存在則打開文件，並從開頭編輯，即原有內容會被刪除；若該文件不存在，創建新文件
    file = open('final_hw.txt','w')
    file.write(data_str)
    #從data_str尋找符合條件的結果
    data_list = re.findall(condition,data_str) 
    #從檔案62-71裡找出common words
    if i == 62:
        compare_list = data_list
    else:
        compare_list = list(set(compare_list) & set(data_list)) #檔案62-71取交集
#把common words取代成空白     
for common in compare_list:
    data_str = re.sub(' '+common+' '," ",data_str) #把data依據條件取代成空白
#
for times in range(0,2):
    if times == 0: #如果times=1，跑關鍵字及數量
        data_list = re.findall(condition,data_str) #從data_str尋找符合條件的結果
        print("關鍵字:數量")
    else: #如果times=2，跑組合關鍵字及數量
        data_list = re.findall(condition+' '+condition,data_str) #從data_str尋找符合條件的結果
        print("組合關鍵字:數量")
    #計數單字量
    counter_dict = dict() 
    for counter in data_list:    
        counter_dict.setdefault(counter,0)
        counter_dict[counter] = counter_dict[counter] + 1
    #把單字量由大排到小/reverse反向
    counter_list = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True) 
    
    for i in range (1,21):
        print("%2d"%i,counter_list[i-1][0],":",counter_list[i-1][1]) #顯示前20個關鍵字        