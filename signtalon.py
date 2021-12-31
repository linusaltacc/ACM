def get_signature(sender_email,body):
    import talon
    talon.init()
    from talon import signature

    text, signature = signature.extract(body, sender=sender_email)

    print("ML Signature : ", signature)


# body = """Thanks Sasha, I can't go any higher and is why I limited it to the
# homepage.

# John Doe
# via mobile
# """
#print(get_signature("john.doe@example.com",body))