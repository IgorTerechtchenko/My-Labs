# import init
import myawesomelab.logger


class Sample_text(myawesomelab.logger.Logger):
    def sample(self):
        print "ayy lmao m8"

    def mul(self, a, b):
        return a * b


B = Sample_text()
B.mul(2, 10)


def test_logger():
    assert str(B) == "call number: 1; method name: mul; arguments: (2, 10), {}; result: 20; \n"


def test_failed_logger():
    assert str(B) == "fail"
