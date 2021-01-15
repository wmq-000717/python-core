a, b, c, d = map(int,(input()))
if a > b: t = a;a = b;b = t;
if b > c: t = b;a = b;c = t;
if c > d: t = c;c = d;d = t;
if a > b: t = a;a = b;b = t;
if b > c: t = b;a = b;c = t;
if c > d: t = c;c = d;d = t;