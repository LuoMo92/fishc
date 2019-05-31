import requests
import json

def get_hot_comments(res):
        comments_json = json.loads(res.text)
        hot_comments = comments_json['hotComments']
        with open('hot_comments.txt','w',encoding='utf-8') as file:
                for each in hot_comments:
                        file.write(each['user']['nickname']+':\n\n')
                        file.write(each['content']+'\n')
                        file.write("============================\n\n\n")

def get_comments(url):
    name_id = url.split('=')[1]
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "referer":url
            }
    params = "HRsxsz1i/BKzKyI/DUrGJGvsyoD/906JLk7WqMfp5u4FoGKQEKsRjo4WeOpNPWj/W71jWJyNrBJNApJs9tRFjOctBDcZzspgXyybQjo03c6DXHDvmmHicmrq+cnId+vo2H73fsLIMbIpkfdHqaqwba6wJBi5+PDEbf8ePLcP5PH2uJKkdUQ0p5Qry/YNV3Zd"        	
    encSecKey = "212cbfb8ca852165d0f16d030746a6bf18624379fc4d2933049b3e6932c14c33f31608b7364512f208e51a19a167b982963b39864cf4340699830baa06a79f9f1f9e9a294e0fb6cc54b4bf8ad44bf449c012cc57b029c860c653e809b3a7be635a96eac92c164dc62830f97e175a1a28a4fe92ed62fbb84120bb35e1b33571b0"
    
    data = {
            "params":params,
            "encSecKey":encSecKey
    }
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
    res = requests.post(target_url,headers=headers,data=data)
    return res

def main():
    url = input("请输入链接地址:\n")
    res = get_comments(url)
    get_hot_comments(res)

    with open("data.txt","w",encoding="utf-8") as file:
        file.write(res.text)

if __name__ == "__main__":
    main()