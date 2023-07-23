import time

def pomodoro_timer(focus_time=25, break_time=5):
    while True:
        print('开始专注...')
        for i in range(focus_time * 60, -1, -1):
            mins, secs = divmod(i, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)

        print('\n专注时间结束，休息一下.')

        for i in range(break_time * 60, -1, -1):
            mins, secs = divmod(i, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)

        print('\n休息结束，开始新的专注时间.')

if __name__ == "__main__":
    pomodoro_timer()
