# 协程包
import asyncio
# 网路请求包
import requests


async def download(url):
    print('%s 下载中' % url)
    await asyncio.sleep(1)
    resp = requests.get(url)
    return resp.content, resp.status_code


@asyncio.coroutine
def write_file(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)
    print(filename, 'Write OK')


@asyncio.coroutine
def save(url, filename):
    # print('%s 下载中' % url)
    content, code = yield from download(url)
    print(url, code)
    yield from write_file(filename, content)
    print(url, filename, '保存成功')


if __name__ == '__main__':
    # 获取事件循环器对象
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait([
        save('https://www.baidu.com', 'baidu.html'),
        save('https://jd.com', 'jd.html'),
        save('https://mail.qq.com', 'qq_mail.html'),
    ]))



