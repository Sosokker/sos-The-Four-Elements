# DO NOT TOUCH THIS BLOCK OF CODE!
elements = ["earth", "water", "fire", "air"]
essence = 0
# DO NOT TOUCH THIS BLOCK OF CODE!

# Change 'pass' statements into your own implementation only!
# You may add new functions or lines of code but it's not recommended
# to edit the existing lines!

def weakness_of(element) -> str:
    if element == "earth" :
        return "air"
    elif element == "water" :
        return "earth"
    elif element == "fire" :
        return "water"
    elif element == "air" :
        return "fire"
    elif (element not in elements) or (type(element) is not str) :
        return "flee"

def collect_essence(amount):
    # DO NOT TOUCH THIS BLOCK OF CODE!
    global essence  # This statement is for declaring 'essence' is a global variable.
                    # This is only for the purpose of fun challenge, but it is a bad programming practice!
    # DO NOT TOUCH THIS BLOCK OF CODE!
    essence += int(amount)
    return essence

def battle(enemy): #Note {element:str , essence:int}
    if weakness_of(enemy["element"]) == "flee" :
        return
    else :
        return collect_essence(enemy["essence"])


# DO NOT TOUCH THIS BLOCK OF CODE!
if __name__ == '__main__':
    from base64 import b64decode
    eval(compile(b64decode("""CmZyb20gcmFuZG9tIGltcG9ydCBjaG9pY2VzLCByYW5kaW50CgplbmVteV9lbGVtZW50cyA9IFsiZWFydGgiLCAid2F0ZXIiLCAiYWlyIiwgImZpcmUiLCAiY2hhb3MiLCAibG92ZSJdCndlYWtuZXNzZXMgPSBbImFpciIsICJlYXJ0aCIsICJmaXJlIiwgIndhdGVyIiwgImZsZWUiLCAiZmxlZSJdCmV4cGVjdGVkX2Vzc2VuY2UgPSAwCgpkZWYgY2hlY2tfcGxheWVyX2VsZW1lbnQoZnVuYyk6CiAgICBkZWYgd3JhcHBlcihlbGVtZW50KToKICAgICAgICByZXMgPSBmdW5jKGVsZW1lbnQpCiAgICAgICAgaWYgcmVzICE9IHdlYWtuZXNzZXNbZW5lbXlfZWxlbWVudHMuaW5kZXgoZWxlbWVudCldOgogICAgICAgICAgICBwcmludCgpCiAgICAgICAgICAgIHByaW50KCJZT1UgSEFWRSBCRUVOIERFRkVBVEVEISIpCiAgICAgICAgICAgIHByaW50KCJNYXliZSB5b3UgaGF2ZSB1c2VkIGEgd3JvbmcgZWxlbWVudCBpbiBhIGZpZ2h0ISAoQ2hlY2sgY29uZGl0aW9ucykiKQogICAgICAgICAgICBwcmludCgiT3IgbWF5YmUgeW91IGRpZCBub3QgZmxlZSBmcm9tIHVua25vd24gcG93ZXIuLi4iKQogICAgICAgICAgICBwcmludCgpCiAgICAgICAgICAgIGV4aXQoMSkKICAgIHJldHVybiB3cmFwcGVyCgpkZWYgY2hlY2tfYWNjdW11bGF0aW5nX2Vzc2VuY2UoKToKICAgIGlmIGVzc2VuY2UgPCBleHBlY3RlZF9lc3NlbmNlOgogICAgICAgIHByaW50KCkKICAgICAgICBwcmludCgiWU9VIEhBVkUgQkVFTiBERUZFQVRFRCEiKQogICAgICAgIHByaW50KCJZb3UgZGlkIG5vdCBhYnNvcmIgYW4gZW5lbXkgZXNzZW5jZSEgVGhlIGVuZW15IHN0b29kIHVwIGFuZCBkZWZlYXRzIHlvdS4iKQogICAgICAgIHByaW50KCJQZXJoYXBzIHlvdSB3b3VsZCBuZWVkIHRvIGNvbGxlY3QgdGhlaXIgZXNzZW5jZT8iKQogICAgICAgIHByaW50KCkKICAgICAgICBleGl0KDEpCiAgICBpZiBlc3NlbmNlID4gZXhwZWN0ZWRfZXNzZW5jZToKICAgICAgICBwcmludCgpCiAgICAgICAgcHJpbnQoIllPVSBIQVZFIEJFRU4gREVGRUFURUQhIikKICAgICAgICBwcmludCgiWW91IHRyaWVkIHRvIGNvbGxlY3QgYW4gdW5rbm93biBwb3dlciBlc3NlbmNlIGJ1dCBpdCBiYWNrZmlyZWQuIikKICAgICAgICBwcmludCgiUGVyaGFwcyB5b3Ugd291bGQgbmVlZCB0byBjb250cm9sIHlvdXIgZ3JlZWQ/IikKICAgICAgICBwcmludCgpCiAgICAgICAgZXhpdCgxKQoKZm9yIGkgaW4gcmFuZ2UoNTApOgogICAgZW5lbXkgPSB7CiAgICAgICAgImVsZW1lbnQiOiBjaG9pY2VzKGVuZW15X2VsZW1lbnRzLCB3ZWlnaHRzPVs1LDUsNSw1LDIsMl0sIGs9MSlbMF0sCiAgICAgICAgImVzc2VuY2UiOiByYW5kaW50KDEsIDEwKQogICAgfQogICAgaWYgZW5lbXlbImVsZW1lbnQiXSBpbiBlbmVteV9lbGVtZW50c1s6NF06CiAgICAgICAgZXhwZWN0ZWRfZXNzZW5jZSArPSBlbmVteVsiZXNzZW5jZSJdCiAgICBiYXR0bGUoZW5lbXkpCiAgICBjaGVja19wbGF5ZXJfZWxlbWVudCh3ZWFrbmVzc19vZikoZW5lbXlbImVsZW1lbnQiXSkKICAgIGNoZWNrX2FjY3VtdWxhdGluZ19lc3NlbmNlKCkKCnByaW50KCkKcHJpbnQoIlZJQ1RPUklPVVMhIikKcHJpbnQoIllvdSBoYXZlIGRlZmVhdGVkIGVuZW1pZXMgYW5kIHRoZXkgYXJlIGNoYXNlZCBhd2F5IGZyb20geW91ciBob21lLiIpCnByaW50KCJZb3UgaGF2ZSB3b24gdGhpcyBiYXR0bGUhIikKcHJpbnQoKQo="""),'<string>','exec'))
# DO NOT TOUCH THIS BLOCK OF CODE!

