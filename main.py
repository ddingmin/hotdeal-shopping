import slack
import time

last_item = 0
while 1:
    last_item = slack.notice_messages(last_item)
    print("sleeping...")
    time.sleep(60 * 60)