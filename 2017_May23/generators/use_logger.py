from logger import log

testlog = log("test.log", "test program")

for l in testlog:
    testlog.send("this is a test message...")
    print "sent one log message..."

    testlog.send("this is another log message..")
    print "Sent another log message..."

    testlog.send(None)

