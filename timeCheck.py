#!/usr/bin/env python
#coding:utf-8

def IsValidTimes(times):
    if times is None or times.isdigit() is False:
        return False
    return True

def time():
    while True:
        print '0時～23時の間で時刻を入力してください！'
        input_times = raw_input()
        if IsValidTimes(input_times) is False:
            continue
        print '開始時刻を入力してください！'
        start_times = raw_input()
        if IsValidTimes(start_times) is False:
            continue
        print '終了時刻を入力してください!'
        end_times = raw_input()
        if IsValidTimes(end_times) is False:
            continue
        if start_times < end_times
            if input_times >= start_times and input_times < end_times:
                print '%s時は%s時から%s時の間に含まれています。'%(input_times,start_times,end_times)
                break
            else:
                print '%s時は%s時から%s時の間に含まれていません。'%(input_times,start_times,end_times)
                break
        elif start_times > end_times:
            input_times = int(input_times)
            end_times = int(end_times)
            input_times += 24
            end_tiems += 24
            
            if input_times >= start_times and input_times < end_times:
                input_times -= 24
                end_times -= 24
                print "%s時は%s時から%s時の間に含まれています！"%(input_times, start_times,end_times)
                break
            else:
                input_times -= 24
                end_times -= 24
                print "%s時は%s時から%s時の間に含まれています！"%(input_times, start_times,end_times)
                break
        elif start_times == end_times and input_times == end_times:
                print "%s時は%s時から%s時の間に含まれています！"%(input_times, start_times,end_times)
                break
if __name__ == "__main__":
    time()

