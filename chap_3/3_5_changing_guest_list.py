guests = ["scarlet johansson", "charlie chaplin", "charlize teron", "megan fox"]
changed_guest = guests.pop()
guests.append("jennifer lawrence")

print(f"Hello {guests[0].title()}, \nI would like to invite you for a nice dinner with friends at my place tomorrow evening.\nPlease confirm as soon as possible.\nCiao,\nCarlo")
print()
print(f"Hello {guests[1].title()}, \nI would like to invite you for a nice dinner with friends at my place tomorrow evening.\nPlease confirm as soon as possible.\nCiao,\nCarlo")
print()
print(f"Hello {guests[2].title()}, \nI would like to invite you for a nice dinner with friends at my place tomorrow evening.\nPlease confirm as soon as possible.\nCiao,\nCarlo")
print()
print(f"Hello {guests[3].title()}, \nI would like to invite you for a nice dinner with friends at my place tomorrow evening.\nPlease confirm as soon as possible.\nCiao,\nCarlo")

print()
print(f"{changed_guest.title()} will not able to join us")
