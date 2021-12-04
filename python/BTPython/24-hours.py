import re
def validate_time(time):
    pattern = re.compile(r'(2[0-3]|[01]?\d):[0-5]\d$')
    result = pattern.match(time)
    return result

print(validate_time("4:00"))