import re



REGEXP_EMAIL = re.compile(r"[^@]+@[^@]+\.[^@]+")
REGEXP_UPPERALPHA = re.compile(r"[A-Z]")
REGEXP_LOWERALPHA = re.compile(r"[a-z]")
REGEXP_DIGIT = re.compile(r"[0-9]")
REGEXP_RESTRICTEDSYMBOL = re.compile(r"[\;| \,| \\ | \/]+")


def missing_props(props, obj):
    return [prop for prop in props if prop not in obj]

def bad_types(prop_type_map, obj):
    bad_types = []
    for prop, prop_type in prop_type_map.iteritems():
        if prop in obj:
            try:
                prop_type(obj[prop])
            except ValueError:
                bad_types.append(prop)

    return bad_types

def bad_lengths(prop_lengths, obj):
    bad_lengths = []
    for prop, length_tuple in prop_lengths.iteritems():
        if prop in obj:
            l = len(str(obj[prop]))
            if ((length_tuple[0] is None) or (l < length_tuple[0])) and ((length_tuple[1]) is (None or l > length_tuple[1])):
                bad_lengths.append(prop)

    return bad_lengths

def valid_email(email):
    return True if re.match(REGEXP_EMAIL, email) else False

def valid_password(password):
    return (len(password) >= 6) and (re.search(REGEXP_UPPERALPHA, password)) and  (re.search(REGEXP_LOWERALPHA, password)) and (re.search(REGEXP_DIGIT, password))

def valid_username(username):
    return False if re.search(REGEXP_RESTRICTEDSYMBOL, username) else True