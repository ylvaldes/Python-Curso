import  urllib.request,json
def main():
    data=urllib.request.urlopen("https://github.com/hussien89aa").read()
    jsonr=json.loads(data.decode("utf-8"))
    #print(jsonr,type(jsonr))
    for row in jsonr['ToolData']:
        print(row['ToolTypeName'])



if __name__ == '__main__':main()