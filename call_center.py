from datetime import datetime

class Call(object):
    NUM_CALLS = 0
    def __init__(self, caller, phone_num, reason):
        self.id = Call.NUM_CALLS
        self.caller = caller
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason

        Call.NUM_CALLS += 1

    def display_info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)
        
        print "#" * 20

class Callcenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)
        
    def add(self, a_call):
        self.calls.append(a_call)

    def remove(self, r_call):
        self.calls.remove(r_call)

    def info(self):
        for call in self.calls:
            call.display_info()

c = Call("Tim", "555-342-3245", 'question')
call_center = CallCenter()
call_center.add(c) #same as below
call_center.add(Call("Tim", "555-342-3245", 'question'))
print call_center.__dict__
print c.reason
print c.__dict__   