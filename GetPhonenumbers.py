import phonenumbers

def get_phonenumbers(body):
    sender_phone_numbers = []
    for match in phonenumbers.PhoneNumberMatcher(body, "None"):
        if phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164) not in sender_phone_numbers:
            sender_phone_numbers.append(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
    return sender_phone_numbers

