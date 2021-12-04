import re
import re
def validate_pin(pin):
    pattern = re.compile(r'[^0-9]')
    result = pattern.findall(pin)
    if result:
        return False
    else:
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False


print(validate_pin("098765"))
    