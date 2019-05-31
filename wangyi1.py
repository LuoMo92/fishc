import requests

def get_url(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}
    res = requests.get(url,headers=headers)
    return res

def main():
    url = input("请输入链接地址:\n")
    res = get_url(url)

    with open("res.txt","w",encoding="utf-8") as file:
        file.write(res.text)

if __name__ == "__main__":
    main()