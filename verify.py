import hmac, hashlib
def check(p, s, sec): return hmac.new(sec.encode(), p, hashlib.sha256).hexdigest() == s