def rgb(r, g, b):
    def limit(num):
        if num < 0:
            return 0
        elif num > 255:
            return 255
        else:
            return num

    hex = format(limit(r),"X").zfill(2)+format(limit(g),"X").zfill(2)+format(limit(b),"X").zfill(2)
    return hex

print(rgb(-5,255,255))

# Remade after looking at suggestions

