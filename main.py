from args import getargs
from post import postlogin
from status import whatstatus
import sys


def run():
    cfg = getargs(sys.argv[1:])
    if cfg == None:
        return
    netwkstatus = whatstatus()
    if netwkstatus == False:
        try:
            postlogin(**cfg)
            print("\033[37;42m\t登录成功！\033[0m")
        except:
            print("\033[37;41m\t发生错误。登录失败\033[0m")
    else:
        print("\033[37;41m\t网络已连通,无需重复登陆\033[0m")


run()