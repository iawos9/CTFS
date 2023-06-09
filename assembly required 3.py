# add \x before every charectar
# org d_1024 => \9dn\93\c8\b2\b9A\8b\c2\90\8bd\c7\9e\c9\88b\95\91\90\dac\c5\95\95\d82\c4\c5\92\8ee\92\96\97\8ca\c4\93\92\90\00\00
# org d_1067 => \f1\a7\f0\07\ed
# REFERENCE => https://youtu.be/A8F9wfZB_78
d_1024 = b"\x9dn\x93\xc8\xb2\xb9A\x8b\xc2\x90\x8bd\xc7\x9e\xc9\x88b\x95\x91\x90\xdac\xc5\x95\x95\xd82\xc4\xc5\x92\x8ee\x92\x96\x97\x8ca\xc4\x93\x92\x90\x00\x00"
d_1067 = b"\xf1\xa7\xf0\x07\xed"
out = bytearray()
for i, c in enumerate(d_1024):
    char = d_1067[4 - (i % 5)]
    out.append(c ^ char)
print(out)
