import random
import string


def generate_account_number():
    return  "44" + str (random.randrange(10000000,99999999))


def generate_reference_number():
    return "ref" + str (random.shuffle([string.ascii_letters + string.digits][:31]))